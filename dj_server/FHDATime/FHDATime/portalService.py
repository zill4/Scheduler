try:
    from .dataFetch import portal, portalClassData
    from .Firebase import FHDATimeFireBase
except ModuleNotFoundError:
    from dataFetch import portal, portalClassData 
    from Firebase import FHDATimeFireBase


class Platform():

    def __init__(self, *args, **kwargs):
        ''' initializes the frames in the window'''
        self.db = FHDATimeFireBase()
        
     
class LoginForm():
    ''' 
    Login Form is a frame class where users can enter their
    myPortal login credentials to log in to the system
    '''
    def __init__(self,parent, controller):
        '''Initializes widgets and the slide show'''
        self.sid = ''
        self.password = ''


    def validate_login(self, name, passw):
        ''' Callback function that checks for correct user input
        Can be invoked in 2 ways - either by enter key or the Log In button'''
        
        uname = name
        pword = passw # call portal object @ dataFetch.py
        try:
            myPortal = portal(uname, pword)
            myPortal.login()
               
            #myPortal.timeoutExec(15,myPortal.logout)            
        except RuntimeError:
            print("Oops!", "The username or password you entered is incorrect!")
            