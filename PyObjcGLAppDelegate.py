#
#  PyObjcGLAppDelegate.py
#  PyObjcGL
#
#  Created by Christopher Denter on 1/7/11.
#  Copyright none 2011. All rights reserved.
#

from Foundation import *
from AppKit import *

class PyObjcGLAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
