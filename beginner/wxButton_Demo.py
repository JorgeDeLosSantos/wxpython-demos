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
        wx.Frame.__init__(self,parent,title=title,size=(250,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Standard Button
        self.button = wx.Button(self, -1, u"Button")
        # Updating font button
        self.font1 = self.button.GetFont()
        self.font1.SetPointSize(14)
        self.button.SetFont(self.font1)
        # Button with icon
        self.bitbutton = wx.Button(self, -1, u"Button with icon")
        self.bitbutton.SetBitmap(wx.Bitmap("img/ic_button_01.png"))
        # Flat button
        self.flatbutton = wx.Button(self, -1, u"Flat button", 
                                    style=wx.BORDER_NONE)
        
        self.sz.Add(self.button, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.bitbutton, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.flatbutton, 1, wx.EXPAND|wx.ALL, 5)
        
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxButton Demo")
    app.MainLoop()
