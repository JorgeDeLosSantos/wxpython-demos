# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
"""
DataGrid es una modificación de la clase wx.grid.Grid 
"""

import wx
import numpy as np
import wx.grid as wxgrid

class DataGrid(wxgrid.Grid):
    def __init__(self,parent,gridsize,**kwargs):
        wxgrid.Grid.__init__(self,parent=parent,id=-1,**kwargs)
        rows = int(gridsize[0])
        cols = int(gridsize[1])
        self.CreateGrid(rows,cols)
        self.SetRowLabelSize(20)
        self.Bind(wxgrid.EVT_GRID_CELL_CHANGE, self.OnCellEdit)
        self.Bind(wxgrid.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightClick)
        
    def UpdateGridSize(self,rows,cols):
        self.ClearGrid()
        ccols = self.GetNumberCols()
        crows = self.GetNumberRows()
        
        if rows > crows:
            self.AppendRows(rows-crows)
        elif rows < crows:
            self.DeleteRows(0,crows-rows)
            
        if cols > ccols:
            self.AppendCols(cols-ccols)
        elif cols < ccols:
            self.DeleteCols(0,ccols-cols)
            
    def SetArrayData(self,data):
        """
        Data must be a numpy array
        """
        r,c = data.shape # For numpy array
        self.UpdateGridSize(r,c)
        for i in range(r):
            for j in range(c):
                val = str(data[i][j])
                self.SetCellValue(i,j,val)
        
    def GetArrayData(self):
        nrows = self.GetNumberRows()
        ncols = self.GetNumberCols()
        X = np.zeros((nrows,ncols))
        for i in range(nrows):
            for j in range(ncols):
                cval = self.GetCellValue(i,j)
                if not self.isempty(cval):
                    X[i][j] = float(cval)
                else:
                    X[i][j] = np.nan
        return X
        
    def GetSelectedCols(self):
        scols = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not self.isempty(bottom_right) and not self.isempty(top_left):
            max_col = bottom_right[0][1]
            min_col = top_left[0][1]
            scols = range(min_col,max_col+1)
        return scols
        
    def GetSelectedRows(self):
        srows = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not self.isempty(bottom_right) and not self.isempty(top_left):
            max_row = bottom_right[0][0]
            min_row = top_left[0][0]
            srows = range(min_row,max_row+1)
        return srows
        
    def SetGridAlignment(self,halign,valign):
        nrows=self.GetNumberRows()
        ncols=self.GetNumberCols()
        for ii in range(nrows):
            for jj in range(ncols):
                self.SetCellAlignment(ii,jj,halign,valign)
        
        
    def OnCellEdit(self,event):
        """
        """
        row,col = (event.GetRow(),event.GetCol())
        cval = self.GetCellValue(row,col)
        if cval.startswith("="):
            try:
                cval = str(eval(cval[1:]))
                self.SetCellValue(row,col,cval)
            except:
                pass
        try:
            cval = float(cval)
        except ValueError:
            cval = np.nan
        self.SetCellValue(row,col,str(cval))
        
            
    def OnRightClick(self,event):
        pum = wx.Menu()
        delrows = wx.MenuItem(pum, -1, "Eliminar filas")
        pum.AppendItem(delrows)
        delcols = wx.MenuItem(pum, -1, "Eliminar columnas")
        pum.AppendItem(delcols)
        pum.AppendSeparator()
        addrow = wx.MenuItem(pum, -1, "Agregar fila...")
        pum.AppendItem(addrow)
        addcol = wx.MenuItem(pum, -1, "Agregar columna...")
        pum.AppendItem(addcol)
        pum.AppendSeparator()
        editcollabel = wx.MenuItem(pum, -1, "Editar etiqueta de columna")
        pum.AppendItem(editcollabel)
        pum.AppendSeparator()
        randomfill = wx.MenuItem(pum, -1, "Rellenar columnas aleatoriamente")
        pum.AppendItem(randomfill)
        
        # Binds
        pum.Bind(wx.EVT_MENU, self.del_rows, delrows)
        pum.Bind(wx.EVT_MENU, self.del_cols, delcols)
        pum.Bind(wx.EVT_MENU, self.add_row, addrow)
        pum.Bind(wx.EVT_MENU, self.add_col, addcol)
        pum.Bind(wx.EVT_MENU, self.edit_collabel, editcollabel)
        pum.Bind(wx.EVT_MENU, self.random_fill, randomfill)
        # Show 
        self.PopupMenu(pum)
        pum.Destroy()

    def del_rows(self,event):
        rows = self.GetSelectedRows()
        self.DeleteRows(rows[0],len(rows))
        
    def del_cols(self,event):
        cols = self.GetSelectedCols()
        self.DeleteCols(cols[0],len(cols))
        
    def add_row(self,event):
        self.AppendRows(1)
        
    def add_col(self,event):
        self.AppendCols(1)
        
    def edit_collabel(self,event):
        ccols = self.GetSelectedCols()
        dlg = wx.TextEntryDialog(None, "Inserte etiqueta...",
        "wxPython Demos")
        if dlg.ShowModal() == wx.ID_OK:
            label = dlg.GetValue()
        for col in ccols:
            self.SetColLabelValue(col,label)
    
    def random_fill(self,event):
        cols = self.GetSelectedCols()
        nrows = self.GetNumberRows()
        #data = np.random.random((nrows,1))
        for ii in range(nrows):
            data = np.random.random((nrows,1))
            for col in cols:
                val = str(data[ii][0])
                self.SetCellValue(ii,col,val)

    def isempty(self,iterable):
        if not iterable:
            return True
        else:
            return False
            


if __name__=='__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, u"Simple Grid Demo", size=(300,200))
    gd = DataGrid(frame, (10,2))
    gd.SetGridAlignment(wx.ALIGN_CENTRE,wx.ALIGN_CENTRE)
    frame.Show()
    app.MainLoop()
