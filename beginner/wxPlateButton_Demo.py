# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#

import wx
import wx.lib.platebtn as pbtn

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(250,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self, -1)
        
        # Botón normal
        self.button = pbtn.PlateButton(self.panel, label=u"Plate Button")
        
        self.sz.Add(self.button, 0, wx.ALL, 5)
        self.panel.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxButton Demo")
    app.MainLoop()
