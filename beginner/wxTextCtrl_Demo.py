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
        
        self.txt_ctrl = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        self.sz.Add(self.txt_ctrl, 1, wx.EXPAND)
        
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxTextCtrl Demo")
    app.MainLoop()
