# CIS41B Final Project
# Author: Mega Putra, William Chen
import os
import requests
import time
import bs4
import json
import threading
import atexit
class portal:
    '''
    This class is major connector to connect fhda portal
    It can login with FHDA stduent id, password.
    '''
    def __init__(self,studentID=None,password=None):
        '''
        default construtor, if no student ID or password.
        It will just be object created
        Args:
            studentID: This is the student id 
            password: This is the password 
        Returns:
            None
        Raises:
            None
        '''
        self._studentID = studentID
        self._password = password
        self._lastReqTime = 0
        self._reqInterval = 10
        self._maxTryTime = 3
        self._loginStatus = False
        self._loginTime = None
        self._session = None
        self._timoutThreadList = []
        self._delObj = threading.Event()
        self._delObj.clear()
        if(self._studentID and self._password):
            self.login()
        atexit.register(self._exit)
    
    def setstudentID(self,studentID):
        '''
        Student ID setter, and the student ID only digits
        Args:
            studentID: This is student ID field
        Return:
            None
        Raises:
            RuntimeError: Error student ID
        '''
        try:
            studentID=str(studentID)
            if(not studentID.isdigit()):
                print("Error student ID")
                raise RuntimeError("Error student ID")
            self._studentID = studentID
        except Exception:
            raise RuntimeError("Error student ID")

    def getStudentID(self):
        '''
        Get student ID
        Args:
            None
        Return:
            studentID: This is a student ID
        Raises:
            None
        '''
        return self._studentID
    
    def setPassword(self,passowrd):
        '''
        Set up the password
        Args:
            password: This is a password for login
        Return:
            None
        Raises:
            None
        '''
        self._password=passowrd

    def login(self):
        '''
        Make user login
        Args:
            None
        Return:
            None
        Raises:
            RuntimeError: Login error message
        '''
        if(not self._loginTime):
            self._requestsSession()

    def logout(self):
        '''
        Make user logout
        Args:
            None
        Return:
            None
        Raises:
            None
        '''
        self.requestPageGet("https://banssb.fhda.edu/PROD/twbkwbis.P_Logout")
        self.__init__()

    def checkStatus(self):
        '''
        Check login status
        Args:
            None
        Return:
            loginStatus: True for login, False for logout
        Raises:
            RuntimeError: Login error message(Should never raises if server is alive)
        '''
        timeOut = 3600 #s
        if(self._loginTime and 
             (time.time()-self._loginTime) > timeOut and 
             self._loginStatus):
            self._requestsSession()
        return self._loginStatus
    
    def requestPageGet(self,requestLink:str):
        '''
        Request from website only login
        sleep for wait time(sec) per request 
        It will try to request by max try time(default is 3)
        Args:
            requestLink: a link for any login page
        Return:
            page: return the request get page
        Raises:
            RuntimeError: Open website fail or not login
        '''
        if(not self.checkStatus()):
            raise RuntimeError("Not login yet")
        tryTime = 0
        while(tryTime == 0 or page.status_code != requests.codes.ok):
            tryTime += 1
            if(time.time() - self._lastReqTime < self._reqInterval):
                time.sleep(self._reqInterval- (time.time() - self._lastReqTime))
            self._lastReqTime = time.time()
            try:
                page = self._session.get(requestLink)
            except requests.exceptions.HTTPError as e: 
                print ("HTTP Error:", e) 
            except requests.exceptions.ConnectionError as e: 
                print ("Error Connecting:", e) 
            except requests.exceptions.Timeout as e: 
                print ("Timeout Error:", e) 
            except requests.exceptions.RequestException as e:     # any other Requests error
                print ("Request exception:", e)
            if (page.status_code != requests.codes.ok and tryTime >= self._maxTryTime ):
                raise RuntimeError("Open page error, and tried",tryTime,"times")
        page.encoding ="utf8"
        page.decoding = "utf8"
        return page

    def _requestsSession(self):
        '''
        Request from website for login
        Args:
            None
        Return:
            None
        Raises:
            RuntimeError: No student ID,password or open website fail 
        '''
        if(not self._studentID or not self._password):
            raise RuntimeError("No student ID or password")
        LOGIN_PAGE = "https://banssb.fhda.edu/PROD/twbkwbis.P_WWWLogin"
        LOGIN_URL = "https://banssb.fhda.edu/PROD/twbkwbis.P_ValLogin"
        session_requests = requests.session()
        try:
            session_requests.get(LOGIN_PAGE)
            # Perform login
            post = session_requests.post(LOGIN_URL, 
                data = {
                    "sid": self._studentID, 
                    "PIN": self._password
                    },
                headers = {
                    'User-Agent':'Mozilla/5.0'
                })
            checkStatus = post.text.split('\n')
            if (post.status_code != requests.codes.ok or 
                 "<TITLE>User Login</TITLE>" in checkStatus or 
                 "Invalid login information. Please try again." in checkStatus):
                    self._loginStatus = False
                    self._session = None
                    raise RuntimeError("Login Error! password or student id not correct")
            self._loginStatus = True
            self._session = session_requests
            self._loginTime = time.time()
            self._lastReqTime = time.time()
        except requests.exceptions.HTTPError as e: 
            raise RuntimeError("HTTP Error:", e)
        except requests.exceptions.ConnectionError as e: 
            raise RuntimeError ("Error Connecting:", e) 
        except requests.exceptions.Timeout as e: 
            raise RuntimeError ("Timeout Error:", e) 
        except requests.exceptions.RequestException as e:     # any other Requests error
            raise RuntimeError ("Request exception:", e)
    def timeoutExec(self,sec,f,*args):
        def _timeoutThreadFn(sec,f,*args):
            i = 0
            while i < sec and self._delObj.isSet():
                time.sleep(1)
                i+=1
            f(*args)
        self._delObj.set()
        t = threading.Thread(target=_timeoutThreadFn,args=(sec,f,*args))
        self._timoutThreadList.append(t)
        t.start()

    def _exit(self):
        self._delObj.clear()
        for t in self._timoutThreadList:
            t.join()
            
class portalClassData(portal):
    '''
    This class fetch data from portal
    Since you have to login, we should have student id, and password
    
    Parent class: portal
    '''
    def __init__(self, studentID=None, password=None):
        '''
        default construtor, if no student ID or password.
        It will just be object created
        Args:
            studentID: This is the student id 
            password: This is the password 
        Returns:
            None
        Raises:
            None
        '''
        self._courseData = {}
        self._courseInitial = {}
        self._quarterOptions = {}
        self._selectQuarter = 1  # 1 the lastest quarter in De Anza College
        self._fetchDataThread = None
        super().__init__(studentID, password)

    def login(self):
        '''
        Make user login and 
        fetch same default data and create thread to fetch default quarter class data
        Args:
            None
        Return:
            None
        Raises:
            RuntimeError: Login error message
        '''
        if(not self._loginTime):
            self._requestsSession()
        if(not self._loginTime):
            super(portalClassData, self).login()
            if(self.checkStatus()):
                self._grabQuarters()
                self._fetchDataThread = threading.Thread(target = self._fetchData)
                self._fetchDataThread.start()
            
    def logout(self):
        '''
        Logout function, and stop thread if still running
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        self._fetchDataThread.join()
        super(portalClassData, self).logout()

    def printQuarterOption(self):
        '''
        Print out what option we have for quaters option
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        if (not len(self._quarterOptions)):
            self._grabQuarters()
        for key in self._quarterOptions:
            print(key, ":", self._quarterOptions[key][0])

    def selectQuarter(self,select):
        '''
        select what quarter data you want to have
        And grap all data
        Args:
            option: a integer of quater menu
        Returns:
            None
        Raises:
            RuntimeError: Error selection
        '''
        if (not len(self._quarterOptions)):
            self._grabQuarters()
        if(select < 1 or select > len(self._quarterOptions)):
            raise RuntimeError("Error selection for quarter")
        if(self._fetchDataThread):
            self._fetchDataThread.join()
        self._selectQuarter = select
        self._courseData = {}
        self._fetchDataThread = threading.Thread(target=self._fetchData)
        self._fetchDataThread.start()

    def _grabQuarters(self):
        '''
        Fetch quater name from portal 

        Args:
            None
        Returns:
            None
        Raises:
            RuntimeError: No login or fetch data fail
        '''
        if(not self.checkStatus()):
            raise RuntimeError("Please login!")
        self._quarterOptions = {}
        CLASS_SEARCH_URL = "https://banssb.fhda.edu/PROD/bwskfcls.p_sel_crse_search"
        soup = bs4.BeautifulSoup(self.requestPageGet(CLASS_SEARCH_URL).text, "lxml")
        for i,data in enumerate(soup.find(id="term_input_id").find_all("option")):
            if(i != 0):
                self._quarterOptions[i] = (data.get_text(), data['value'])
    
    def getCourseData(self):
        '''
        Return course data

        Args:
            None
        Returns:
            None
        Raises:
            RuntimeError: No login or fetch data fail
        '''
        self._fetchDataThread.join()
        if(not len(self._courseData)):
            self._fetchDataThread = threading.Thread(target=self._fetchData)
            self._fetchDataThread.start()
        self._fetchDataThread.join()
        return self._courseData

    def getCourseInitial(self):
        '''
        Return course match initial 
        
        Example:
            ACCT : Accouting-DA
        Args:
            None
        Returns:
            None
        Raises:
            RuntimeError: No login or fetch data fail
        '''
        self._fetchDataThread.join()
        if(not len(self._courseData)):
            self._fetchDataThread = threading.Thread(target=self._fetchData)
            self._fetchDataThread.start()
        self._fetchDataThread.join()
        return self._courseInitial

    def getQuarter(self):
        '''
        Return quarters as a dict

        Args:
            None
        Returns:
            None
        Raises:
            RuntimeError: No login or fetch data fail
        '''
        if (not len(self._quarterOptions)):
            self._grabQuarters()
        return self._quarterOptions

    def _processLine(self,line,department_short,course):
        '''
        Process a line save to private course match initial dict and course data dict

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        features = [elem for elem in line.split('\n') if elem != ""]
        if(line.endswith("-DA\n") or line.endswith("-FD\n") or line.endswith("-FH\n") or line == "\nEnglish/Second Language Learnr\n" or len(features) == 1):
            department_short = line.strip()
        elif(not line.startswith("\nSelect")):
            try:
                if(not features[1].isdigit()): # LAB
                    labTime = {}
                    labTime["Days"] = features[8].replace("\u00a0", "")
                    labTime["Time"] = features[9]
                    labTime["Instructor"] = features[16].strip().replace(" (P)", "").replace(
                        "   ", "  ").replace("  ", " ").replace(" ", ",")
                    labTime["Date"] = features[17]
                    labTime["Location"] = features[18]
                    course["Lab Time"].append(labTime)
                else: # Regular Class
                    department = features[2].replace("/","-")
                    course = {}
                    course["CRN"] = features[1]
                    course["Crse"] = features[3].replace(".","")
                    course["Sec"] = features[4]
                    course["Cmp"] = features[5]
                    course["Cred"] = features[6]
                    course["Title"] = features[7].replace("\r", "")
                    course["Days"] = features[8].replace("\u00a0", "")
                    course["Time"] = features[9]
                    course["Cap"] = features[10]
                    course["Act"] = features[11]
                    course["WL Cap"] = features[13]
                    course["WL Act"] = features[14]
                    course["Instructor"] = features[16].strip().replace(" (P)", "").replace(
                        "   ", "  ").replace("  ", " ").replace(" ", ",")

                    course["Date"] = features[17]
                    course["Location"] = features[18]
                    course["Attribute"] = features[19].replace("\u00a0", "")
                    course["Lab Time"] = []
                    #course["Zero Textbook Cost"]=features[20]
                    if department not in self._courseData:
                        self._courseData[department] = []
                    self._courseData[department].append(course)
                    if department not in self._courseInitial:
                        self._courseInitial[department] = department_short
            except Exception:
                print(line,features)
        return department_short,course        

    def _fetchData(self):
        '''
        Fetch data from portal and process in all data

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        if(not self.checkStatus()):
            raise RuntimeError("Please login!")
        # print("Fetch Data:",self._quarterOptions[self._selectQuarter][0], " FetchTime:", time.ctime())
        dataLink = self.requestPageGet("https://banssb.fhda.edu/PROD/bwskfcls.P_GetCrse_Advanced?rsts=dummy&crn=dummy&term_in=" +
        self._quarterOptions[self._selectQuarter][1] +
        "&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&" +
        "sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&" +
        "sel_subj=%25&sel_crse=&sel_title=&sel_schd=%25&sel_from_cred=&sel_to_cred=&" +
        "sel_camp=%25&sel_levl=%25&sel_ptrm=%25&sel_instr=%25&sel_sess=%25&sel_attr=%25&" +
        "begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&SUB_BTN=Section+Search&path=1")

        course={}
        department_short=""
        for line in bs4.BeautifulSoup(dataLink.text, "lxml").find('table', class_="datadisplaytable").find_all('tr'):
            department_short, course = self._processLine(str(line.get_text()), department_short, course)

    def outputToCourseDataJson(self):
        '''
        output course data to Json
        File Name will be:
            quarterName_courseData.json

        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        quarterName = self._quarterOptions[self._selectQuarter][0].replace(" (View only)","").replace(" ", "_")
        self._fetchDataThread.join()
        os.makedirs("../tmp/", exist_ok=True)
        with open(os.path.join(os.path.join("../tmp/"), quarterName+'_courseData.json'), 'w') as f:
            json.dump({self._quarterOptions[self._selectQuarter][0].replace(" (View only)", ""):
                        { 
                          "FetchTime": time.ctime(),
                          "CourseData": self._courseData
                        }
                      }, f, indent=3)
    
    def outputCourseInitialToJson(self):
        '''
        output couuse initial to Json
        File Name will be:
            campusName_coursesInitial.json
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        self._fetchDataThread.join()
        fileName = "DeAnza_coursesInitial.json"
        if(not "De Anza" in self._quarterOptions[self._selectQuarter][0]):
            fileName = "Foothill_coursesInitial.json"
        os.makedirs("../tmp/", exist_ok=True)
        with open(os.path.join(os.path.join("../tmp/"), fileName), 'w') as f:
            json.dump(self._courseInitial, f, indent=3)
        

if __name__ == '__main__':
    import getpass,sys
    try:
        print("------------This is testing programming for FHDA portal Data Fetching------------")
        studentID = input("studentID: ")
        password = getpass.getpass(prompt='Password: ',stream=sys.stderr)
        myPortal = portalClassData('20256942','P1ezill4P1e!')
        # myPortal.setstudentID(studentID)
        # myPortal.setPassword(password)
        # myPortal.login()
        for i in range(2,65,2):
            myPortal.selectQuarter(i)
            print(myPortal.getQuarter()[i][0])
            myPortal.outputToCourseDataJson()
        myPortal.outputCourseInitialToJson()
        '''
        myPortal.printQuarterOption()
        
        myPortal.selectQuarter(int(input("Please Select:")))
        #print(myPortal.getCourseData())
        myPortal.outputCourseInitialToJson()
        myPortal.outputToCourseDataJson()
        myPortal.logout()
        print("------------Thank you for testing------------")
        '''
        '''
        # get groups of quarter datas
        #index = 1  #DeAnza
        index = 2 #Foothill
        for i in range(index,65,2):
            myPortal.selectQuarter(i)
            print(myPortal.getQuarter()[i][0])
            myPortal.outputToCourseDataJson()
        myPortal.outputCourseInitialToJson()
        myPortal.logout()
        print("------------Thank you for testing------------")
        '''
    except Exception as e:
        print(e)
