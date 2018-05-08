# FHDA Time

This is a final project for CIS41B - Advanced Python Programming class instructed by Professor Clare Nguyen  
This application allows Foothill and De Anza College students to add their own class schedule :school:  
Private Github: https://github.com/kis87988/FHDATime

## Overview

Since most of the students in the Foothill/De Anza College aim to transfer to a 4-year university,
we try to make their transition smoother and better by supporting them in terms of time management.
In this case, allowing users to plan, schedule, and modify classes that they are going to take.

## Functionality

The program mimics a scheduler or a class planner.
Users will log in using their myPortal student ID and Password.
User will select a campus and a period to search the class on.
User can enjoy the Functionality of the scheduller by utilizing the search feature.

- Main file : driver.py  
  Please run this file to execute the program.
- GUI module : FHDATime/GUI.py  
  Contains the Graphical User Interface (GUI) for the program
- DataFetching module: FHDATime/datafetch  
  Data fetching from my portal with login functionality.
- Firebase modlue(Database): FHDA/Firebase  
  Database connector
- Temporary files: FHDATime/tmp  
  All temporary file store include datafetch output file
- GIF file: ./*.gif  
  Contains slideshow pictures

## Related modules

- OS
- Tkinter
- tkFont
- ttk
- messagebox
- glob
- os
- sys
- platform
- threading
- json
- re
- pyrebase: please do python3 -m pip install pyrebase

## Plan

We aim to make a program and website that can perform the following:

- [x] Fetch data fromFHDA myportal system
- [x] Student ID login requared
- [x] Add a class in to schedule
- [x] Basic User interface
- [x] Export schedule to csv file
- [ ] Export schedule to cal file (may include google calander)
- [ ] Website interface
- [ ] Find overlap schedule of class that student selected class
- [ ] Import data from assist.org
- [ ] Have a plan 2-3 years plan for majors class schedule
- [ ] Analytics previous quarters enrollment stats
- [ ] Rate professor and classes

More features coming soon...

## Team

- William Chen
- Mega Putra

If you are interested about this project, please contact us at william@williamusa.me
