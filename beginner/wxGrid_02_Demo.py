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
from random import randint

class WXDemoFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(280,250))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        self.grid = wxgrid.Grid(self)
        # Creating 10x3 grid
        rows, cols = 10, 3
        self.grid.CreateGrid(rows,cols)
        # Assign values to cells
        for i in range(rows):
            for j in range(cols):
                val = "%s"%(randint(0,100))
                self.grid.SetCellValue(i,j,val)
        
        # Assign random colors
        for ii in range(rows):
            for jj in range(cols):
                clr = wx.Colour(randint(0,255),randint(0,255),randint(0,255))
                self.grid.SetCellBackgroundColour(ii,jj,clr)
        
        # Deleting row labels
        self.grid.SetRowLabelSize(0)
        
        # Updating column labels
        lbl = {0:"Time", 1:"Temperature", 2:u"Pressure"}
        for col,header in lbl.items():
            self.grid.SetColLabelValue(col,header)
        
        self.sz.Add(self.grid, 1, wx.EXPAND|wx.ALL, 2)
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"Simple Grid Demo")
    app.MainLoop()
