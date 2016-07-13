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
        wx.Frame.__init__(self,parent,title=title,size=(200,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        self.rb1 = wx.RadioButton(self, -1, label = 'Blue')
        self.rb2 = wx.RadioButton(self, -1, label = 'Red')
        self.rb3 = wx.RadioButton(self, -1, label = 'Green')
        self.rb4 = wx.RadioButton(self, -1, label = 'White')
        
        self.sz.Add(self.rb1, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.rb2, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.rb3, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.rb4, 1, wx.EXPAND|wx.ALL, 10)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.OnSelect)
        
        self.SetSizer(self.sz)
        # Center frame
        self.Centre(True)
        self.Show()
        
    def OnSelect(self,event):
        sel = event.GetEventObject().GetLabel()
        self.SetBackgroundColour(sel)
        self.Refresh()
        

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxRadioButtton Demo")
    app.MainLoop()
