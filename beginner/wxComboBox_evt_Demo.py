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
        
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect, self.cbbox)
        
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()
        
    def OnSelect(self,event):
        opciones = {"Python":"#be00be",
                    "C":"#ff0000",
                    "C++":"#a0a0a0",
                    "Fortran":"#906090",
                    "Java":"#fe7788",
                    "Perl":"#0077ee",
                    "JavaScript":"#550033"}
        sel = event.GetString()
        self.SetBackgroundColour(opciones[sel])
        self.Refresh()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxComboBox Demo")
    app.MainLoop()
