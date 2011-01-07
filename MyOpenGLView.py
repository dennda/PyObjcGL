#
#  MyOpenGLView.py
#  PyObjcGL
#
#  Created by Christopher Denter on 1/7/11.
#  Copyright (c) 2011 none. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *
from OpenGL.GL import *

class MyOpenGLView(NSOpenGLView):
    def initWithFrame_(self, frame):
        self = super(MyOpenGLView, self).initWithFrame_(frame)
        if self:
            # initialization code here
            pass
        return self

    def drawRect_(self, rect):
        # drawing code here
        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.85, 0.35)
        glBegin(GL_TRIANGLES)
        glVertex3f( 0.0, 0.6, 0.0)
        glVertex3f( -0.2, -0.3, 0.0)
        glVertex3f( 0.2, -0.3 ,0.0)
        glEnd()
        glFlush()
