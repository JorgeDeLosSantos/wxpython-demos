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
        # Modificando el estilo del Framen (No redimensionable)
        _styles = (wx.CLOSE_BOX|wx.CAPTION)
        wx.Frame.__init__(self,parent,title=title,size=(300,200), 
                          style=_styles)
        # Configurando el color de fondo
        self.SetBackgroundColour("#aafafa")
        
        # Centrando y mostrando la ventana
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxFrame Demo")
    app.MainLoop()
