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
        wx.Frame.__init__(self,parent,title=title,size=(300,200))
        # Panels
        self.p1 = wx.Panel(self,-1)
        self.p2 = wx.Panel(self,-1)
        
        # Sizers
        self.szmain = wx.BoxSizer(wx.VERTICAL)
        self.szp1 = wx.BoxSizer(wx.HORIZONTAL)
        self.szp2 = wx.GridSizer(rows=3, cols=3)
        
        # Controls for panel 1
        self.bt1 = wx.Button(self.p1, -1, u"Button 1")
        self.bt2 = wx.Button(self.p1, -1, u"Button 2")
        
        # Controls for panel 2
        for txt in range(9):
            # Creating control
            tctrl = wx.TextCtrl(self.p2, -1)
            # Add control to sizer of panel 2
            self.szp2.Add(tctrl, 1, wx.EXPAND|wx.ALL, 1)
        
        # Add to sizers
        self.szp1.Add(self.bt1, 1, wx.EXPAND|wx.ALL, 5)
        self.szp1.Add(self.bt2, 1, wx.EXPAND|wx.ALL, 5)
        
        self.szmain.Add(self.p1, 1, wx.EXPAND|wx.ALL, 5)
        self.szmain.Add(self.p2, 4, wx.EXPAND|wx.ALL, 5)
        
        # Setting sizers
        self.p1.SetSizer(self.szp1)
        self.p2.SetSizer(self.szp2)
        self.SetSizer(self.szmain)
        
        # Center and show
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"Sizers Demo")
    app.MainLoop()
