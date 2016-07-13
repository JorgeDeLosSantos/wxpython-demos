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
        self.panel = wx.Panel(self, -1)
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        lista = ["Azul","Verde","Rojo"]
        self.rbox = wx.RadioBox(self.panel, label = 'Colores', choices = lista,
                                style=wx.RA_HORIZONTAL)
        
        self.Bind(wx.EVT_RADIOBOX, self.OnSelect, self.rbox)
        
        self.sz.Add(self.rbox, 1, wx.EXPAND|wx.ALL, 10)
        
        self.panel.SetSizer(self.sz)
        # Centrando la ventana
        self.Centre(True)
        self.Show()
        
    def OnSelect(self,event):pass

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxRadioBox Demo")
    app.MainLoop()
