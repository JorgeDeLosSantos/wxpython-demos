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
        wx.Frame.__init__(self,parent,title=title,size=(200,150))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creando los controles
        chb1 = wx.CheckBox(self, -1, u"Matemáticas")
        chb2 = wx.CheckBox(self, -1, u"Física")
        chb3 = wx.CheckBox(self, -1, u"Química")
        
        # "Seleccionando" o "marcando" el chb1
        chb1.SetValue(True)
        
        # Agregando controles al sizer
        self.sz.Add(chb1, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(chb2, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(chb3, 1, wx.EXPAND|wx.LEFT, 20)
        
        # Configurar sizer
        self.SetSizer(self.sz)
        
        # Centrar y mostrar el Frame
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxCheckBox Demo")
    app.MainLoop()
