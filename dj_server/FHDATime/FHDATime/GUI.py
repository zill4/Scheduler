# CIS41B Final Project
# Author: Mega Putra, William Chen
try:  
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3+
    import tkinter as tk
    import tkinter.font as tkfont
    import tkinter.ttk as ttk
#import database
from glob import glob
import platform
import os
import sys
import tkinter.messagebox as tkmb
import threading
try:
    from .dataFetch import portal
    from .Firebase import FHDATimeFireBase
except ModuleNotFoundError:
    from dataFetch import portal
    from Firebase import FHDATimeFireBase

class FHDATime(tk.Tk):
    '''Main TK class window that contains multiple frames'''
    
    def __init__(self, *args, **kwargs):
        ''' initializes the frames in the window'''
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(950, 0)
        self.title_font = tkfont.Font(family='Times New Roman', size = 18, weight = "bold") # set 
        # container holds multiple frames that stacks on top of each other so only one is visible at a time
        container = tk.Frame(self, bg = 'yellow')
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.windowFrames = {}
        self.db = FHDATimeFireBase()
        for f in (LoginForm, QuarterSelect, SearchForm):
            page_name = f.__name__
            frame = f(parent=container, controller=self)
            self.windowFrames[page_name] = frame
            #put page in the location for individual visibility
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginForm") #Make the login form to show up first
        self.windowFrames["LoginForm"].idBox.focus() # Make focus to login StuID
            
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.windowFrames[page_name]
        frame.tkraise()
        
class LoginForm(tk.Frame):
    ''' 
    Login Form is a frame class where users can enter their
    myPortal login credentials to log in to the system
    '''
    def __init__(self,parent, controller):
        '''Initializes widgets and the slide show'''
        self.isClick = False
        tk.Frame.__init__(self, parent)
        self.controller = controller  
        self.sid = tk.StringVar()
        self.password = tk.StringVar()
        self.init_widgets()   
        
        self.images = glob("*.gif")
        self.cur = 0
        # label showing the image
        self.f1 = tk.Frame(self, width = 400,height = 500)
        self.image = tk.PhotoImage()
        imagelabel = tk.Label(self.f1, image=self.image)
        imagelabel.grid(row=5, column = 0, columnspan=2)
        
        # layout and show first image
        self.f1.pack_propagate(0)
        self.f1.grid(row=5, column = 0, columnspan=2)
        self.f1.grid_propagate(0)
        self.after(500, self.show_next)
        
    def show_next(self):
        '''Shows the next image in your folder for the slide show'''
        if(len(self.images)):
            self.cur = (self.cur + 1) % len(self.images)
            self.image.configure(file= self.images[self.cur] ) 
            self.id = self.after(800, self.show_next)
        
    def init_widgets(self):
        ''' initialize widgets '''
        
        labelPrompt = tk.Label(self, text= "Please enter your MyPortal login credentials")
        idLabel = tk.Label(self, text = "Student ID:")
        self.idBox = tk.Entry(self, textvariable = self.sid,width = 130)
        passLabel = tk.Label(self, text = "Password:")
        self.passBox = tk.Entry(self, textvariable = self.password,show = "*", width = 130)
        loginButton = tk.Button(self, text = "Log in", command = self.validate_login) #, command = openSearch)
        quitButton = tk.Button(self, text = "Quit") # command = quit)
        # place the widgets 
        labelPrompt.grid(columnspan = 3)
        idLabel.grid(row = 2, column = 0, sticky = 'w')
        self.idBox.grid(row = 2, column = 1,columnspan = 2, sticky = 'w')
        passLabel.grid(row = 3, column = 0, sticky = 'w')
        self.passBox.grid(row = 3, column = 1, columnspan = 2, sticky = 'w')
        loginButton.grid(row = 4, column = 0, sticky = 'e')
        quitButton.grid(row = 4, column = 1, sticky = 'w')
        self.grid_columnconfigure(1, weight = 1) # stretchy

        self.passBox.bind('<Return>', self.validate_login)  
        quitButton.bind('<Button-1>', self.close)
    
    def close(self,event):
        '''A callback function for the 'Quit' button to end the program'''
        sys.exit() #quit program

    def validate_login(self, *args):
        ''' Callback function that checks for correct user input
        Can be invoked in 2 ways - either by enter key or the Log In button'''
        
        uname = self.sid.get()
        pword = self.password.get() # call portal object @ dataFetch.py
        try:
            if(self.isClick):
                tkmb.showwarning("Oops!", "You just clicked submit. Please wait!", parent = self)
                return 
            self.isClick = True
            myPortal = portal(uname, pword)
            myPortal.login()
            if(self.id):
                self.after_cancel(self.id)
            self.controller.show_frame("QuarterSelect")
            myPortal.timeoutExec(15,myPortal.logout)            
        except RuntimeError:
            tkmb.showwarning("Oops!", "The username or password you entered is incorrect!", parent = self)
            self.isClick = False

class QuarterSelect(tk.Frame):
    '''Form that lets user choose a quarter period selection'''
    def __init__(self, parent, controller):
        self.db = controller.db
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        ''' initialize widgets '''
        self.campus = "DA"
        self.TKcampus = tk.StringVar()
        self.TKcampus.set("De Anza College")
        selectLabel = tk.Label(self, text ="Select a Quarter and campus:")
        campusMenu = tk.Menubutton(self, textvariable=self.TKcampus)
        campusMenu.menu = tk.Menu(campusMenu, tearoff=0)
        campusMenu['menu'] = campusMenu.menu
        def callbackCampus(n):
            qtrMenu.menu.delete(0, len(self.db.getQuartersName(self.campus)))
            self.campus = n
            if(self.campus == "FH"):
                self.TKcampus.set("Foothill College")
            else:
                self.TKcampus.set("De Anza College")
            for quarterName in self.db.getQuartersName(self.campus): # add the quarter and years to the menu button    
                qtrMenu.menu.add_command(label=quarterName, command=lambda quarterName=quarterName: callbackChoice(quarterName)) 
        campusMenu.menu.add_command(label="De Anza College", command=lambda campus="DA": callbackCampus(campus)) 
        campusMenu.menu.add_command(label="Foothill College", command=lambda campus="FH": callbackCampus(campus)) 
        qtrMenu = tk.Menubutton(self, text = "Choose a period")
        qtrMenu.menu = tk.Menu(qtrMenu, tearoff = 0) # qtrMenu is master of menu
        qtrMenu['menu'] = qtrMenu.menu
        def callbackChoice(n) :      
            self.db.getCourseData(self.campus, n)
            self.controller.show_frame("SearchForm")
            self.controller.windowFrames["SearchForm"].subjBox.focus()
        for quarterName in self.db.getQuartersName(self.campus): # add the quarter and years to the menu button    
            qtrMenu.menu.add_command(label=quarterName, command=lambda quarterName=quarterName: callbackChoice(quarterName)) 
        selectLabel.grid(row=0, column=1)
        campusMenu.grid(row=1,column=0)
        qtrMenu.grid(row=1, column=1)     
        

class SearchForm(tk.Frame):
    '''
    Main frame where the user interacts
    Searches for classes within a choosen quarter, displays in a MultiLevelListBox and lets user add classes to another listbox
    '''
    def __init__(self, parent, controller):
        self.db = controller.db
        self.lb = None
        self.addClassList = []
        self.parent=parent
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.courseSubj = tk.StringVar()
        self.courseNum = tk.StringVar()
        self.init_widgets()
    
    def init_widgets(self):
        ''' initialize widgets '''
        labelPrompt = tk.Label(self, text= "Enter a class information")
        idLabel = tk.Label(self, text = "Subject: ")
        self.subjBox = tk.Entry(self, textvariable = self.courseSubj, width = 50) ###
        numLabel = tk.Label(self, text = "Course Number:")
        self.numBox = tk.Entry(self, textvariable = self.courseNum, width = 50)  ###
        ex1 = tk.Label(self, text = "Ex: 'CIS'")
        ex2 = tk.Label(self, text = "Ex: '22A'")
        calTitle = tk.Label(self,text="My classes:")
        searchButton = tk.Button(self, text = "Search", command = self._search)
        #advSearchButton = tk.Button(self, text = "Advanced Search")  
        self.removeClass = tk.Button(self,text = "Remove Class", command = self._removeClass)
        self.f1 = tk.Frame(self)
        self.f1.grid(row=8, column=0, sticky='nsew', columnspan=8)
        self.exportCalButton = tk.Button(self,text = "Export Calendar", command = self.exportList)
        self.quitButton = tk.Button(self,text = "Quit")
        self.s = tk.Scrollbar(self, orient = "vertical")             
        self.lbox = tk.Listbox(self, height = 10, width = 40, yscrollcommand = self.s.set)     # connects list box with scrollbar
        # place the widgets
        labelPrompt.grid(row = 1, columnspan = 2, sticky = 'w')
        idLabel.grid(row = 2, column = 0, sticky = 'w')
        self.subjBox.grid(row = 2, column = 1,  sticky = 'we')
        ex1.grid(row = 2, column = 2, sticky = 'we')
        numLabel.grid(row = 3, column = 0, sticky = 'w')
        self.numBox.grid(row = 3, column = 1, sticky = 'we')
        ex2.grid(row = 3, column = 2, sticky = 'we')
        calTitle.grid(row=4,column =0, sticky = 'nw')
        searchButton.grid(row = 2, column = 3, sticky = 'w')
        #advSearchButton.grid(row = 4, column = 1, sticky = 'e')
        self.lbox.grid(row = 5, column = 0, columnspan = 5, sticky='wnse')
        self.s.config(command = self.lbox.yview) # "command = " is the callback because the scrollbar needs to know where it is/how much to show
        self.s.grid(row = 5, column = 5, sticky= 'nsw')   
        self.removeClass.grid(row = 6, column = 4)
        self.exportCalButton.grid(row = 6, column = 0)
        self.quitButton.grid(row = 6, column =2)  
        self.numBox.bind('<Return>', self._search) # enter to search
        self.subjBox.bind('<Return>', self._search)
        self.quitButton.bind('<Button-1>', self.close)
        self.grid_columnconfigure(1, weight=1) 
        self.update()
        self.lb = None
        
    def close(self,event):
        '''callback function to quit the program'''
        
        sys.exit() #quit program     
        
    def _removeClass(self):
        '''Removes class from a listbox of classes added to calendar'''
        
        if self.lbox.size() != 0:
            selection = self.lbox.curselection()
            self.addClassList.pop(selection[0])
            self.lbox.delete(selection[0])
        else:
            tkmb.showwarning("Warning!", "Nothing to remove", parent = self)    
   
    def _search(self, event = None):
        ''' Looks for the class and subject name, finds whether user input is valid, if valid, calls the constructData function '''
        if self.lb != None: # if multicolumn listbox already exists, kill it
            self.lb.killframe()
        tk.Label(self,text = \
                 """
                 Click on header to sort by that column
                 Drag column to change boundary
                 Double Click selection to Add to Calendar
                 """).grid(row = 6, column = 1, sticky = 'ew')  
        # based on user input
        try:
            subjInit = self.courseSubj.get().upper().strip()
            subj = self.db.getCourseInitialDict()[subjInit]
            tk.Label(self, text = "Results for " +subj + ' ' + self.courseNum.get().upper()). \
                     grid(row = 7,column = 1, sticky = 'ew')    
            self.constructData(subjInit) # choose which dictionary to search on
        except KeyError as e:
            tkmb.showwarning("Oops!", "Please fill out/enter a correct subject", parent = self)     
            tk.Label(self, text = "").grid(row = 7,column = 1, sticky = 'ew')
            print(str(e))
        
    def constructData(self,subjInit):
        '''Populates a multicolumn listbox based on what the user enters
        Display buttons where user can perform operations based on the search result
        '''
        
        courseNum = self.courseNum.get().upper().strip()
        if courseNum == "":
            courseNum = None
        finalCon = self.db.courseSearch(subjInit, courseNum)
        if not finalCon: 
            tkmb.showwarning("Warning!", "No result found!", parent = self) 
        else:
            self.lb = MultiColumnListbox(["CRN","Subj","Crse","Title","Days","Time","Instructor","Location"],finalCon, self)

    def exportList(self):
        '''Callback function to let user export the list of classes into a csv format'''
        
        import csv
        if len(self.addClassList) == 0:
            tkmb.showwarning("Oops!","Schedule is empty. No class data to export!" , parent = self)
        else:
            with open('myCourseData.csv', 'w', newline='') as fh :
                writer = csv.writer(fh) 
                for item in self.addClassList:
                    writer.writerow(item)
            tkmb.showinfo("Good!","Your class schedule has been exported!" , parent = self)
        
class MultiColumnListbox():
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self,c,l, parent):
        self.tree = None
        self.parent = parent
        self.className = ""
        self._setup_widgets(c)
        self._build_tree(c,l)
        
    def _setup_widgets(self,c):
        '''initialize widgets'''
        self.container = ttk.Frame(self.parent.f1)
        #self.container.pack(fill='both')#, expand = True)
        self.container.grid(row=0, column=0, sticky='nsew',columnspan=9)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=c, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=0, column=0, sticky='nsew', in_=self.container)
        
        self.tree.bind("<Double-1>", self.OnDoubleClick) #when use double clicks the list
        vsb.grid(row=0, column=10, sticky='ns', in_=self.container)
        hsb.grid(row=1, column=0, sticky='ew', in_=self.container)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
    def OnDoubleClick(self, event):
        '''call back function that lets user add a highlighted class to another listbox of classes'''
        
        selectData = self.tree.item(self.tree.selection())['values']
        if selectData[1]+selectData[2] not in [item[1]+item[2] for item in self.parent.addClassList]:
            self.parent.addClassList.append(selectData)
            tkmb.showinfo("Good!",selectData[1]+ " class is added!", parent = self.tree)
            temp = selectData[1]+selectData[2] + " with " + selectData[-2] + " @ " + selectData[5]
            if(selectData[4]!=""):
                temp += " on "+selectData[4]
            self.parent.lbox.insert(tk.END, temp)
            #self.parent.lbox.insert(tk.END,selectData)
        else:
            tkmb.showwarning("Oops","You cannot add the same class! " + selectData[1], parent = self.tree)
    
    def _build_tree(self,c,l):
        '''builds the multi column listbox based on headers and contents'''
        
        for col in c:
            self.tree.heading(col, text=col.title(), command = lambda c=col: self.sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkfont.Font().measure(col.title()))

        for item in l:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val) + 10
                if self.tree.column(c[ix], width=None) < col_w:
                    if platform.system() == 'Darwin': 
                        self.tree.column(c[ix], width = col_w)
                    elif col_w > 480:
                        self.tree.column(c[ix], width=480)
                    else:
                        self.tree.column(c[ix], width=col_w)
                    
                    
    def killframe(self):
        '''deletes the multicolumn listbox to clear the screen before adding a new one'''
        self.container.pack_forget()
        self.container.destroy()    

    def sortby(self,tree, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
        # if the data to be sorted is numeric change to float
        # data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: self.sortby(tree, col, \
            int(not descending)))   
            
if __name__ == "__main__":
    fhdaTime = FHDATime()
    fhdaTime.title("FHDA Time")
    if platform.system() == 'Darwin': 
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))           
    fhdaTime.mainloop()
