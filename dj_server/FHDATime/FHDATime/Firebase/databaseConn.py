# CIS41B Final Project
# Author: Mega Putra, William Chen
import pyrebase  # REF: https://github.com/thisbejim/Pyrebase
import os
import json
import threading
import re
class FHDATimeFireBase():
    '''
    This class read data from protalClassData class output file(Json)
    convert that to Firebase, and read from Firebase
    
    It maybe slow when fetch different quarter
    
    Fetch quarter course data is handle by thread
    

    NOTE: Have to have services account docuement to upload the data to Firebase
    '''

    def __init__(self,defaultFetching = True):
        '''
        default construtor
        It will just be object created and basic setup
        And read from latest quarter to buffer

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        config = {
            #"serviceAccount": os.path.join(os.getcwd(), "fhdatime-firebase-adminsdk.json"),
            "apiKey": "AIzaSyBdDxwKn1dMYQdzjkM-zFdiBuldgNSj81E",
            "authDomain": "fhdatime.firebaseapp.com",
            "databaseURL": "https://fhdatime.firebaseio.com",
            "storageBucket": "fhdatime.appspot.com"
        }
        self._firebase = pyrebase.initialize_app(config)
        self._db = self._firebase.database()
        self._buffer = {"currentCampus" : "DA",
                        "currentQuarter":None,
                        "quartersName": None,
                        "courseInitial": None,
                        "courses":None                         
                       }
        if(defaultFetching):
            self._buffer["quartersName"]=self._FBgetQuarterName(self._buffer["currentCampus"])
            self._buffer["currentQuarter"] = self._buffer["quartersName"][-1]
            self._buffer["courseInitial"] = self._FBgetCourseInitial(self._buffer["currentCampus"])
        
            self._courseUpdateThread = threading.Thread(target = self._courseDataThreadFetch)
            self._courseUpdateThread.start()
     
    def _courseDataThreadFetch(self):
        '''
        A thread function to fetch data for a quarter

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        self._buffer["courses"]=self._FBgetCourseData(self._buffer["currentCampus"], self._buffer["currentQuarter"])

    def _FBgetCourseInitial(self,campus):
        '''
        Fetch course match data from Firebase for a campus

        Args:
            campus: campus name "DA" or "FH"
        Returns:
            CourseInitialInitial: a dict of course match EX: ACCT:Accounting-DA
        Raises:
            None
        '''
        return dict(self._db.child("CourseInitial").child(campus).get().val())

    def _FBgetQuarterName(self,campus):
        '''
        Fetch quarter name data from Firebase for a campus

        Args:
            campus: campus name "DA" or "FH"
        Returns:
            quarterName: a sorted list  by year + quarter order 
        Raises:
            None
        '''
        return sorted(self._db.child("CourseData").child(campus).shallow().get().val(), key=lambda quarter: (quarter.split()[0], quarter.split()[1] == "Fall", quarter.split()[1] == "Summer", quarter.split()[1] == "Spring", quarter.split()[1] == "Winter"))

    def _FBgetCourseData(self, campus, quarterName):
        '''
        Fetch course data from Firebase for a campus and a quarter

        Args:
            campus: campus name "DA" or "FH"
            quarterName: a quarter name select from quarter name EX:"2018 Spring De Anza"
        Returns:
            courseData: a many level dict course data for a quarter
        Raises:
            None
        '''
        return self._db.child("CourseData").child(campus).child(quarterName).order_by_key().limit_to_last(1).get().val()[0]["Courses"]

    def courseDataToFirebase(self,courseData):
        '''
        push course data to Firebase by protalClassData output file

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        for quarterName,data in courseData.items():
            print("Processing:",quarterName)
            if("De Anza" in quarterName):
                campus = "DA"
            elif("Foothill" in quarterName):
                campus = "FH"
            pathList = self._db.child("CourseData").child(campus).child(quarterName).shallow().get().val()
            if(not pathList):
                index = 0
            else:
                index = len(pathList)
            self._db.child("CourseData").child(campus).child(quarterName).child(index).child("FetchTime").set(data["FetchTime"])
            for subj,courseList in data["CourseData"].items():
                for course in courseList:
                    self._db.child("CourseData").child(campus).child(quarterName).child(index).child("Courses").child(
                        subj.replace("/","-")).child(course["Crse"].replace(".", "")).child(course["CRN"]).set(course)
            print("Done:", quarterName)
    
    def courseInitialToFirebase(self,campus,CourseInitial):
        '''
        push course match initial to Firebase by protalClassData output file

        Args:
            campus: campus name "DA" or "FH"
            CourseInitial: a dict of course(dept.) initial by protalClassData output file
        Returns:
            None
        Raises:
            None
        '''
        for key in CourseInitial:
            self._db.child("CourseInitial").child(
                campus).child(key).set(CourseInitial[key])
    
    def getCourseInitialDict(self,campus=None):
        '''
        Get course match from buffer, fetch again if different campus

        Args:
            campus: campus name "DA" or "FH"
        Returns:
            CourseInitialInitial: a dict of course match EX: ACCT:Accounting-DA
        Raises:
            None
        '''
        if(not campus):
            campus = self._buffer["currentCampus"]
        if(campus != self._buffer["currentCampus"]):
            self._updateBuffer(campus)
        return self._buffer["courseInitial"]
    
    def getCourseData(self,campus=None,quarterName=None):
        '''
        Get course data from buffer, fetch again if different campus or quarter name

        Args:
            campus: campus name "DA" or "FH"
            quarterName: a quarter name select from quarter name EX:"2018 Spring De Anza"
        Returns:
            courseData: a many level dict course data for a quarter
        Raises:
            None
        '''
        if(not campus):
            campus = self._buffer["currentCampus"]
            quarterName = self._buffer["currentCampus"]
        elif(not quarterName):
            quarterName = self._buffer["currentCampus"]

        if(campus != self._buffer["currentCampus"] or self._buffer["currentQuarter"] != quarterName):
            self._updateBuffer(campus, quarterName)
        self._courseUpdateThread.join()        
        return self._buffer["courses"]
    
    def getQuartersName(self, campus=None):
        '''
        Get quarter name list from buffer, fetch again if different campus

        Args:
            campus: campus name "DA" or "FH"
        Returns:
            quarterName: a sorted list  by year + quarter order 
        Raises:
            None
        '''
        if(not campus):
            campus = self._buffer["currentCampus"]
            
        if (campus != self._buffer["currentCampus"]):
            self._updateBuffer(campus)
        return self._buffer["quartersName"]
    
    def _updateBuffer(self, campus, quarterName=None):
        '''
        update buffer data for campus or quarter name different than the buffer
        default quarter is lastest quarter for selected campus

        Args:
            campus: campus name "DA" or "FH"
            quarterName: a quarter name select from quarter name EX:"2018 Spring De Anza"
        Returns:
            None
        Raises:
            None
        '''
        if(campus != self._buffer["currentCampus"]):
            self._buffer["currentCampus"] = campus
            self._buffer["quartersName"] = self._FBgetQuarterName(self._buffer["currentCampus"])
            self._buffer["courseInitial"] = self._FBgetCourseInitial(self._buffer["currentCampus"])   
            if(not quarterName or not quarterName in self._buffer["quartersName"]):
                quarterName  = self._buffer["quartersName"][-1]
        if(quarterName != self._buffer["currentQuarter"] and quarterName in self._buffer["quartersName"]):
            self._buffer["currentQuarter"] = quarterName
            self._courseUpdateThread.join()
            self._courseUpdateThread = threading.Thread(target = self._courseDataThreadFetch)
            self._courseUpdateThread.start()

    def courseSearch(self, courseName, courseNumber=None, campus=None, quarterName=None):
        '''
        Get a list of list for a user course search data

        Args:
            campus: campus name "DA" or "FH"
            quarterName: a quarter name select from quarter name EX:"2018 Spring De Anza"
            courseName: the courseName that user want to search EX:CIS
            courseNumber(optional): the course Number that user want to search EX:21JA
        Returns:
            List: a list of list for a user course search data. return None if not found
        Raises:
            None
        '''
        if (not campus):
            campus = self._buffer["currentCampus"]
            quarterName = self._buffer["quartersName"]
        elif (not quarterName):
            quarterName = self._buffer["quartersName"]

        if(campus != self._buffer["currentCampus"] or self._buffer["currentQuarter"] != quarterName):
            self._updateBuffer(campus, quarterName)
        self._courseUpdateThread.join()
        
        if(courseNumber and courseNumber != ""):
            regexGroup = re.search(r'(\d+)(.*)', courseNumber)
            if(len(regexGroup.group(2))==2):
                buff = self._buffer["currentCampus"][0] + "0" * (
                    2-len(regexGroup.group(1))) + regexGroup.group(1) + regexGroup.group(2).upper()
            else:
                buff = self._buffer["currentCampus"][0] + "0" * (
                    3-len(regexGroup.group(1))) + regexGroup.group(1) + regexGroup.group(2).upper()
            try:
                return [[data["CRN"], courseName, data["Crse"], data["Title"], data["Days"], data["Time"], data["Instructor"], data["Location"]] for data in self._buffer["courses"][courseName][buff].values()]
            except KeyError:
                return None
        #else
        try:
            return [[data["CRN"], courseName, data["Crse"], data["Title"], data["Days"], data["Time"], data["Instructor"], data["Location"]] for courseNumber in self._buffer["courses"][courseName].values() for data in courseNumber.values()]
        except KeyError:
            return None


def _uploadGroupfileTOFB():
    '''
    A function for upload all file in tmp folder
    '''
    import time
    FHDATimeFB = FHDATimeFireBase(False)
    for root, dirs, files in os.walk(os.path.join("../tmp/"), topdown=False):
        for fileName in files:
            if(fileName.endswith(".json")):
                status = True
                while(status):
                    try:
                        print(fileName," START")
                        with open(os.path.join(root, fileName), 'r') as f:
                            data = json.load(f)
                        if("DeAnza_coursesInitial" in fileName):
                            FHDATimeFB.courseInitialToFirebase("DA",data)
                        elif("Foothill_coursesInitial" in fileName):
                            FHDATimeFB.courseInitialToFirebase("FH",data)
                        else:
                            FHDATimeFB.courseDataToFirebase(data)
                        print(fileName, " DONE")
                        os.rename(os.path.join(root, fileName),
                                  os.path.join(root, fileName+"_UPLOADED"))
                        status = False
                    except Exception as e:
                        print("Process file: ",fileName,"ERROR: ",e)
                        quarterName = fileName.split("_courseData.json")[0].replace("_"," ")
                        if("courseData" in fileName):
                            if("De_Anza" in fileName):
                                campus = "DA"
                            elif("Foothill" in fileName):
                                campus = "FH"
                            time.sleep(10)
                            pathList = FHDATimeFB._db.child("CourseData").child(campus).child(quarterName).shallow().get().val()
                            if(not pathList):
                                index = 0
                            else:
                                index = len(pathList) - 1
                            FHDATimeFB._db.child("CourseData").child(campus).child(quarterName).child(index).remove()
                        FHDATimeFB = FHDATimeFireBase(False)
            else:
                print(fileName)

if __name__ == '__main__':
    FHDATimeFB = FHDATimeFireBase()
    campus = "DA"
    quarterName = "2018 Spring De Anza"
'''
# Example for GUI
    
    # Use for courseName and courseNumber (return List of lists)
    FHDATimeFB.courseSearch("CIS", "22A",campus, quarterName)
    
    # Use for courseName only (return List of lists)
    FHDATimeFB.courseSearch("GEO",campus, quarterName)

    # Use for same campus search
    FHDATimeFB.courseSearch("GEO")
    FHDATimeFB.courseSearch("CIS","22A")
'''


"""
# Example:
    # get quarter name list
    print(FHDATimeFB.getQuartersName(campus))
    # ['2010 Fall De Anza', '2010 Summer De Anza', '2011 Fall De Anza', '2011 Spring De Anza', '2011 Summer De Anza', '2011 Winter De Anza',
    # '2012 Fall De Anza', '2012 Spring De Anza', '2012 Summer De Anza', '2012 Winter De Anza', '2013 Fall De Anza', '2013 Spring De Anza',
    # '2013 Summer De Anza', '2013 Winter De Anza', '2014 Fall De Anza', '2014 Spring De Anza', '2014 Summer De Anza', '2014 Winter De Anza',
    # '2015 Fall De Anza', '2015 Spring De Anza', '2015 Summer De Anza', '2015 Winter De Anza', '2016 Fall De Anza', '2016 Spring De Anza',
    # '2016 Summer De Anza', '2016 Winter De Anza', '2017 Fall De Anza', '2017 Spring De Anza', '2017 Summer De Anza', '2017 Winter De Anza',
    # '2018 Spring De Anza', '2018 Winter De Anza']

    # get course matct dict
    CourseInitialDictList = FHDATimeFB.getCourseInitialDict(campus)
    print(CourseInitialDictList)

    
    # get course data dict
    courseData = FHDATimeFB.getCourseData(campus, quarterName)
    print(courseData)
    #               {"ACCT":
    #                   {"D001A":
    #                       {"00002":
    #                           {
    #                               'Act': '40',
    #                               'Attribute': '',
    #                               'CRN': '00002',
    #                               'Cap': '40', 
    #                               'Cmp': 'DA',
    #                               'Cred': '5.000', 
    #                               'Crse': 'D001A',
    #                               'Date': '04/09-06/29',
    #                               'Days': 'MW',
    #                               'Instructor': 'Keith,Lawrence,Mello',
    #                               'Location': 'DA L74',
    #                               'Sec': '01', 
    #                               'Time': '08:30 am-10:45 am',
    #                               'Title': 'Financial Accounting I',
    #                               'WL Act': '5',
    #                               'WL Cap': '5'
    #                           }
    #                       }
    #                   }
    #               }

    for CRN, course in courseData["ACCT"]["D001A"].items():
         # print(course) # a course session dict one session each 
                        # {'Act': '40', 'Attribute': '', 'CRN': '00002', 'Cap': '40', 'Cmp': 'DA', 'Cred': '5.000', 'Crse': 'D001A', 'Date': 
                        # '04/09-06/29', 'Days': 'MW', 'Instructor': 'Keith,Lawrence,Mello', 'Location': 'DA L74', 'Sec': '01', 'Time': '08:30 
                        # am-10:45 am', 'Title': 'Financial Accounting I', 'WL Act': '5', 'WL Cap': '5'}
        for itemName, data in course.items(): 
           print(itemName, data) # ACT 40
"""
'''
## NOTE:
# ## Remove a folder
# FHDATimeFB._db.child("CourseData").child("DA").child("2018 Spring De Anza").child("1").remove()
# FHDATimeFB._db.child("CourseData").remove()
# ## Upload all json in tmp folder
# _uploadGroupfileTOFB()
'''
