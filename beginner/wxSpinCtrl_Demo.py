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
        wx.Frame.__init__(self,parent,title=title,size=(200,150))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        # Creando el SpinCtrl
        self.spin1 = wx.SpinCtrl(self, -1, min=0, max=100, size=(-1,20))
        self.spin2 = wx.SpinCtrl(self, -1, min=1, max=10, size=(-1,20))
        self.spin3 = wx.SpinCtrl(self, -1, min=-5, max=5, size=(-1,20))
        # Agregando al sizer
        self.sz.Add(self.spin1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.sz.Add(self.spin2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.sz.Add(self.spin3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        # Configurar sizer
        self.SetSizer(self.sz)
        # Centrar y mostra el Frame
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxSpinCtrl Demo")
    app.MainLoop()
