#
#  main.py
#  PyObjcGL
#
#  Created by Christopher Denter on 1/7/11.
#  Copyright none 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import PyObjcGLAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
