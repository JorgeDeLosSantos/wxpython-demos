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
        # Creating listbox
        lang_list = "Python|C|C++|Fortran|Java|Perl|JavaScript".split("|")
        self.listbox = wx.ListBox(self, -1, choices=lang_list)
        # Add listbox to sizer
        self.sz.Add(self.listbox, 1, wx.EXPAND|wx.ALL, 10)
        # Set sizer
        self.SetSizer(self.sz)
        # Center and show
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxListBox Demo")
    app.MainLoop()
