# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#

import wx
import wx.grid as wxgrid

class WXDemoFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,250))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        self.grid = wxgrid.Grid(self)
        # Creating 10x2 grid
        self.grid.CreateGrid(10,2)
        # Assign values to cells
        for i in range(10):
            for j in range(2):
                val = "(%s,%s)"%(i,j)
                self.grid.SetCellValue(i,j,val)
        
        self.sz.Add(self.grid, 1, wx.EXPAND|wx.ALL, 2)
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"Simple Grid Demo")
    app.MainLoop()
