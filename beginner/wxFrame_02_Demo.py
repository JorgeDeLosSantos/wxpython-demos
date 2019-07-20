# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx

class WXDemoFrame(wx.Frame):
    def __init__(self,parent,title):
        # Not resizable frame 
        _styles = (wx.CLOSE_BOX|wx.CAPTION)
        wx.Frame.__init__(self,parent,title=title,size=(300,200), 
                          style=_styles)
        # Setting background color
        self.SetBackgroundColour("#aafafa")
        
        # Center and show 
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxFrame Demo")
    app.MainLoop()
