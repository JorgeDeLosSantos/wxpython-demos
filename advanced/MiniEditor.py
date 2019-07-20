# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#

import wx
import wx.adv as wxadv
import os

class MiniEditor(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title="MiniEditor 0.1.0",size=(600,400))
        self.icono = wx.Icon('img/editor_icon.png')
        self.SetIcon(self.icono)
        self.this_file = 'untitled.txt' # Default file name
        
        # Sizer
        sz = wx.BoxSizer(wx.VERTICAL)
        
        # Editor
        self.editor = wx.TextCtrl(self, -1, u"", style=wx.TE_MULTILINE)
        self.initEditor()
        
        # Create menu bar
        self.crearMenu()
        
        # Add to sizer
        sz.Add(self.editor, 1, wx.EXPAND|wx.ALL,)
        self.SetSizer(sz)
        
        # Centre and show
        self.Centre(True)
        self.Show()
        
        
    def initEditor(self):
        """
        Set initial properties
        """
        self.this_font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.this_font.SetFaceName("Courier New")
        self.editor.SetFont(self.this_font)
        self.editor.SetBackgroundStyle(True)
    
    def crearMenu(self):        
        """
        Create menu bar
        """
        mfile=wx.Menu()
        open_m=mfile.Append(-1, "Open\tCtrl-O")
        save_m=mfile.Append(-1, "Save\tCtrl-S")
        saveAs=mfile.Append(-1, "Save as...")
        
        medit=wx.Menu()
        copy=medit.Append(-1, "Copy\tCtrl-C")
        paste=medit.Append(-1, "Paste\tCtrl-V")
        
        self.mtheme=wx.Menu()
        classic=self.mtheme.Append(-1, "Classic")
        dark=self.mtheme.Append(-1, "Dark")
        retro=self.mtheme.Append(-1, "Retro")
        pink=self.mtheme.Append(-1, "Pink")
        
        mayuda=wx.Menu()
        app_help=mayuda.Append(-1, "Help")
        about=mayuda.Append(-1, "About...")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(mfile, "File")
        menu_bar.Append(medit, "Edit")
        menu_bar.Append(self.mtheme, "Select theme")
        menu_bar.Append(mayuda, "Help")
        self.SetMenuBar(menu_bar)
        
        # Bind events
        self.Bind(wx.EVT_MENU, self.openFile, open_m)
        self.Bind(wx.EVT_MENU, self.saveAs, saveAs)
        self.Bind(wx.EVT_MENU, self.saveFile, save_m)
        
        self.Bind(wx.EVT_MENU, self.copy, copy)
        self.Bind(wx.EVT_MENU, self.paste, paste)
        
        self.Bind(wx.EVT_MENU, self.setTheme, classic)
        self.Bind(wx.EVT_MENU, self.setTheme, dark)
        self.Bind(wx.EVT_MENU, self.setTheme, retro)
        self.Bind(wx.EVT_MENU, self.setTheme, pink)
        
        self.Bind(wx.EVT_MENU, self.about, about)
        self.Bind(wx.EVT_MENU, self.app_help, app_help)
    
    def openFile(self, event):
        dlg=wx.FileDialog(self, "Open file", os.getcwd(), style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            try:
                fid=open(dlg.GetPath(),'r')
                text=fid.readlines()
                self.text="".join(text)
                self.text = self.text
                fid.close()
                self.editor.SetValue(self.text)
                self.this_file=dlg.GetPath()
                self.SetTitle("MiniEditor "+self.this_file)
            except:
                wx.MessageBox("Invalid file", "Error")
        dlg.Destroy()
    
    def saveAs(self, event):
        """
        Save file as... 
        """
        dlg=wx.FileDialog(self, "Save", os.getcwd(), style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            fid=open(dlg.GetPath(),'w')
            txt=str(self.editor.GetValue().encode('utf8'))
            fid.write(txt)
            fid.close()
            self.this_file=dlg.GetPath()
        dlg.Destroy()
        
    def saveFile(self,event):
        """
        Save current file
        """
        if hasattr(self, 'this_file'):
            fid=open(self.this_file,'w')
            txt=str(self.editor.GetValue().encode('utf8'))
            fid.write(txt)
            fid.close()
            wx.MessageBox("Done...","MiniEditor")
        else:
            self.saveAs(None)
    
    def copy(self,event):
        """
        Copy selected text to the clipboard
        """
        text=wx.TextDataObject(self.editor.GetStringSelection())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text)
            wx.TheClipboard.Close()
            
    def paste(self,event):
        """
        Paste the text contained in the clipboard
        """
        txt=wx.TextDataObject()
        if wx.TheClipboard.Open():
            success=wx.TheClipboard.GetData(txt)
            wx.TheClipboard.Close()
        if success:
            self.editor.SetInsertionPoint(self.editor.GetInsertionPoint())    
            self.editor.write(txt.GetText())
    
        
    def setTheme(self,event):
        """
        Update background and font color
        """
        sel_theme=self.mtheme.FindItemById(event.GetId()).GetText()
        themes = {'Classic':((0,0,255),(255,255,255)),
        'Dark':((200,200,200),(0,0,0)),
        'Retro':((0,255,0),(0,0,0)),
        'Pink':((20,50,50),(250,180,180))}
        self.editor.SetForegroundColour(themes[sel_theme][0])
        self.editor.SetBackgroundColour(themes[sel_theme][1])
        self.editor.Refresh()
        
    def app_help(self,event):
        wx.MessageBox("Unavailable","MiniEditor")
        
    def about(self, event):
        """
        Show info about app
        """
        description="Plain text editor developed using wxPython"
        info=wxadv.AboutDialogInfo()
        info.SetName('MiniEditor')
        info.SetDescription(description)
        info.SetVersion('0.1.1')
        info.SetLicense('MIT License')
        info.SetDevelopers(['Pedro Jorge De Los Santos'])
        info.SetWebSite("numython.github.io", "Numython")
        info.SetCopyright('(c) 2019')
        wxadv.AboutBox(info)


if __name__=='__main__':
    app=wx.App()
    frame = MiniEditor(None)
    app.MainLoop()
