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
        self.rojo = wx.CheckBox(self, -1, u"Rojo")
        self.verde = wx.CheckBox(self, -1, u"Verde")
        self.azul = wx.CheckBox(self, -1, u"Azul")
        
        # Agregando controles al sizer
        self.sz.Add(self.rojo, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(self.verde, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(self.azul, 1, wx.EXPAND|wx.LEFT, 20)
        
        # 
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck)
        
        # Configurar sizer
        self.SetSizer(self.sz)
        
        # Centrar y mostrar el Frame
        self.Centre(True)
        self.Show()
        
    def OnCheck(self,event):
        R = float(self.rojo.GetValue())
        G = float(self.verde.GetValue())
        B = float(self.azul.GetValue())
        color = wx.Colour(R*255,G*255,B*255)
        self.SetBackgroundColour(color)
        self.Refresh()
        

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxCheckBox Demo")
    app.MainLoop()
