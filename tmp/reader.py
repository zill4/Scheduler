import json
import requests
import pprint
url = 'http://localhost:8080/subjects/'

jsonFile = open("2018_Winter_De_Anza_courseData.json","r")
#jsonFile = open("DeAnza_coursesInitial.json", 'r')

jsonData = json.loads(jsonFile.read())
pp = pprint.PrettyPrinter(indent=4)
#print(jsonData)

for j in jsonData:
	#print(j)
	#k = input("wait")
	moData = jsonData[j] 

courseData = moData["CourseData"]

for c in courseData:
	print(c)
	#k = input("wait")
	obj = courseData[c]
	proper_up = {}
	proper_up['initials'] = c
	p_list = []
	for o in obj:
		proper = {}
		#print(o['CRN'])
		#
		proper['crn'] = o['CRN']
		#
		#print(o['Crse'])
		proper['crse'] = o['Crse']
		#
		#print(o['Sec'])
		proper['sec'] = o['Sec']
		#
		#print(o['Cmp'])
		proper['cmp'] = o['Cmp']
		#
		#print(o['Cred'])
		proper['cred'] = o['Cred']
		#
		#print(o['Title'])
		proper['title'] = o['Title']
		#
		#print(o['Days'])
		proper['days'] = o['Days']
		#
		#print(o['Time'])
		proper['time'] = o['Time']
		#
		#print(o['Cap'])
		proper['cap'] = o['Cap']
		#
		#print(o['Act'])
		proper['act'] = o['Act']
		#
		#print(o['WL Cap'])
		proper['wl_cap'] = o['WL Cap']
		#
		#print(o['WL Act'])
		proper['wl_act'] = o['WL Act']
		#
		#print(o['Instructor'])
		proper['instructor'] = o['Instructor']
		#
		#print(o['Date'])
		proper['date'] = o['Date']
		#
		#print(o['Location'])
		proper['location'] = o['Location']
		#
		#print(o['Attribute'])
		proper['attribute'] = o['Attribute']
		#
		#print(o['Lab Time'])
		if(len(o['Lab Time']) > 0):
			for l in o['Lab Time']:
				proper['lab_days'] = l['Days']
				proper['lab_time'] = l['Time']
				proper['lab_instructor'] = l['Instructor']
				proper['lab_date'] = l['Date']
				proper['lab_location'] = l['Location']
		#p = input("wait")
		p_list.append(proper)
	proper_up['courses'] = p_list
	#pp.pprint(proper_up)
	#pl = input("wait")
	response = requests.post(url,json=proper_up)

		#print(o['Lab Tim'])
'''
for j in jsonData:
	#print(j)
	#print("\n")
	#print(jsonData[j])
	#print("\n")
	post = {}
	post['name'] = jsonData[j];
	post['initials'] = j
	jsonD = json.dumps(post)
	print(jsonD)
	wait = input("wait...")
	response = requests.post(url,json=post)
	print(response.content)
'''

''' /*
    COURSE MATH1A
    CRN": "30202",
    "Crse": "F001A",
    "Sec": "07",
    "Cmp": "FH",
    "Cred": "5.000",
    "Title": "CALCULUS",
               "Days": "TR",
               "Time": "06:00 pm-08:15 pm",
               "Cap": "40",
               "Act": "38",
               "WL Cap": "10",
               "WL Act": "0",
               "Instructor": "Yuh,Ni",
               "Date": "01/08-03/30",
               "Location": "FH 4606",
               "Attribute": "Comm and Analytical Thinking",
               "Lab Time": []
               "Lab Time": [
                  {
                     "Days": "F",
                     "Time": "10:00 am-10:50 am",
                     "Instructor": "Young,Hee,Park,Lee",
                     "Date": "01/08-03/30",
                     "Location": "FH 4603"
                  }
               ]



               {
        "name": "Business",
        "initials": "BUSII",
        "courses": [
            {
                "crn": "777",
                "crse": "BUSII",
                "sec": "03",
                "cmp": "FF",
                "cred": "7.0",
                "title": "BUSINESS 101",
                "days": "TR",
                "time": "6pm-8pm",
                "cap": "5.0",
                "act": "10",
                "wl_cap": "20",
                "wl_act": "30",
                "instructor": "Doc",
                "date": "1/9 - 03/20",
                "location": "cupertion",
                "attribute": "forever me",
                "lab_days": "30",
				"lab_time": "10",
				"lab_instructor":"bob",
				"lab_date" : "340231",
				"lab_ocation" : "fifty"
                
            }
        ]
    }
     */
'''