# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        lista = "Python|C|C++|Fortran|Java|Perl|JavaScript".split("|")
        self.cbbox = wx.ComboBox(self, -1, choices=lista, size=(-1,25))
        self.sz.Add(self.cbbox, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
        
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxComboBox Demo")
    app.MainLoop()
