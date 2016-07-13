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
        wx.Frame.__init__(self,parent,title=title,size=(200,150))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        chb1 = wx.CheckBox(self, -1, u"Mathematics")
        chb2 = wx.CheckBox(self, -1, u"Physics")
        chb3 = wx.CheckBox(self, -1, u"Chemistry")
        
        # Selecting "chb1"
        chb1.SetValue(True)
        
        # Add controls to sizer
        self.sz.Add(chb1, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(chb2, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(chb3, 1, wx.EXPAND|wx.LEFT, 20)
        
        # Set sizer
        self.SetSizer(self.sz)
        
        # Centre and show
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxCheckBox Demo")
    app.MainLoop()
