# CIS41B Final Project
# Author: Mega Putra, William Chen
import platform
import os
from FHDATime import FHDATime

if __name__ == "__main__":
    fhdaTime = FHDATime()
    fhdaTime.title("FHDA Time")
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is %d to true'
        os.system("/usr/bin/osascript -e '%s'" % (tmpl % os.getpid()))
    fhdaTime.mainloop()
