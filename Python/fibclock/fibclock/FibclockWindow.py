# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE


import getFibTime
import sched, time
from threading import Thread

import gettext
from gettext import gettext as _
gettext.textdomain('fibclock')

from gi.repository import Gtk, Gdk
import gobject # pylint: disable=E0611
import logging
logger = logging.getLogger('fibclock')

from fibclock_lib import Window
from fibclock.AboutFibclockDialog import AboutFibclockDialog
from fibclock.PreferencesFibclockDialog import PreferencesFibclockDialog

colors = {}
colors['White'] = {"Red":255, "Green":255,"Blue":255}
colors['Red'] = {"Red":255, "Green":0,"Blue":0}
colors['Blue'] = {"Red":0, "Green":0,"Blue":255}
colors['Green'] = {"Red":0, "Green":255,"Blue":0}

# See fibclock_lib.Window.py for more details about how this class works
class FibclockWindow(Window):
    __gtype_name__ = "FibclockWindow"
        
    def setRGBA(self,color):
        red = colors[color]['Red']
        green = colors[color]['Green']
        blue = colors[color]['Blue']
               
        colorRGBA = Gdk.RGBA(red, green, blue)
        
        return colorRGBA
    
    def updateUI(self):
    
        curTimeColors = getFibTime.currentFibonacciTime()
        draw5RGBA = self.setRGBA(curTimeColors[5])        
        draw3RGBA = self.setRGBA(curTimeColors[3])        
        draw2RGBA = self.setRGBA(curTimeColors[2])        
        draw1aRGBA = self.setRGBA(curTimeColors[1][0])        
        draw1bRGBA = self.setRGBA(curTimeColors[1][1])
        
        self.draw5.override_background_color(Gtk.StateFlags.NORMAL,draw5RGBA)
        self.draw3.override_background_color(Gtk.StateFlags.NORMAL,draw3RGBA)
        self.draw2.override_background_color(Gtk.StateFlags.NORMAL,draw2RGBA)
        self.draw1a.override_background_color(Gtk.StateFlags.NORMAL,draw1aRGBA)
        self.draw1b.override_background_color(Gtk.StateFlags.NORMAL,draw1bRGBA)
        return True
        
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(FibclockWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutFibclockDialog
        self.PreferencesDialog = PreferencesFibclockDialog

        # Code for other initialization actions should be added here.
        self.draw5 = self.builder.get_object("drawAreaFor5")
        self.draw3 = self.builder.get_object("drawAreaFor3")
        self.draw2 = self.builder.get_object("drawAreaFor2")
        self.draw1a = self.builder.get_object("drawAreaFor1a")
        self.draw1b = self.builder.get_object("drawAreaFor1b")
        
        self.updateUI()
