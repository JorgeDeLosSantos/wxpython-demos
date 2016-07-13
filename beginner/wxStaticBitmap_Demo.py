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
        wx.Frame.__init__(self,parent,title=title,size=(350,250))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        self.bmp = wx.Bitmap("img/wxpython-logo.png")
        self.bmp_ctrl = wx.StaticBitmap(self, -1, self.bmp)
        
        self.sz.Add(self.bmp_ctrl, 1, wx.EXPAND)
        
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"wxStaticBitmap Demo")
    app.MainLoop()
