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
        wx.Frame.__init__(self,parent,title=title,size=(250,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        # Creando el listbox
        lista = "Python|C|C++|Fortran|Java|Perl|JavaScript".split("|")
        self.listbox = wx.ListBox(self, -1, choices=lista)
        # Agregando listbox al sizer
        self.sz.Add(self.listbox, 1, wx.EXPAND|wx.ALL, 10)
        # Configurar sizer
        self.SetSizer(self.sz)
        # Centrar y mostra el Frame
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxListBox Demo")
    app.MainLoop()
