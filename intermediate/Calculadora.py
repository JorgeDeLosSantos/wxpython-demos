# -*- coding: utf8 -*-
from __future__ import division # python 2.X version
import wx

class Calculator(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(150,240),
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX|wx.RESIZE_BORDER))
        self.Centre(True)
        
        # Panels
        self.panel_screen = wx.Panel(self, -1)
        self.panel_onoff = wx.Panel(self, -1)
        self.panel_keyboard = wx.Panel(self, -1)
        
        # Sizers
        self.mainsz=wx.FlexGridSizer(1,3,1) # Main sizer
        self.screensz=wx.FlexGridSizer(1,1,1) 
        self.onoffsz=wx.BoxSizer(wx.HORIZONTAL)
        self.keyboardsz=wx.FlexGridSizer(4,4,1)
        
        # Creating components
        self.initScreen()
        self.initOnOff()
        self.initKeyboard()
        
        # Add to sizers
        self.mainsz.Add(self.panel_screen, 1, wx.EXPAND|wx.ALL)
        self.mainsz.Add(self.panel_onoff, 1, wx.EXPAND|wx.ALL)
        self.mainsz.Add(self.panel_keyboard, 5, wx.EXPAND|wx.ALL)
        
        self.panel_screen.SetSizer(self.screensz)
        self.panel_onoff.SetSizer(self.onoffsz)
        self.panel_keyboard.SetSizer(self.keyboardsz)
        self.SetSizer(self.mainsz)
        
        self.Fit()
        # Init default values
        self.show_string=""
        self.eval_string=""
        
    def initScreen(self):
        """
        Create screen
        """
        self.screen=wx.TextCtrl(self.panel_screen, -1, u"")
        # ~ self.screen.SetFont(wx.Font(16, wx.MODERN, wx.NORMAL, wx.BOLD, face="Courier New"))
        self.screensz.Add(self.screen, 1, wx.EXPAND|wx.ALL, 2)
        self.screensz.AddGrowableCol(0)
        
    def initOnOff(self):
        """
        Create ON/OFF buttons
        """
        self.on=wx.Button(self.panel_onoff, -1, "ON")
        self.off=wx.Button(self.panel_onoff, -1, "OFF")
        self.on.SetBackgroundColour((200,10,10))
        self.on.SetForegroundColour('WHITE')
        self.off.SetBackgroundColour((10,10,200))
        self.off.SetForegroundColour('WHITE')
        
        # Bind events
        self.Bind(wx.EVT_BUTTON, self.OnOn, self.on)
        self.Bind(wx.EVT_BUTTON, self.OnOff, self.off)
        
        self.onoffsz.Add(self.on, 1, wx.EXPAND|wx.ALL, 2)
        self.onoffsz.Add(self.off, 1, wx.EXPAND|wx.ALL, 2)
        #self.onoffsz.AddGrowableRow(0)
    
    def initKeyboard(self):
        """ 
        Create main keyboard
        """
        keys="7 8 9 / 4 5 6 * 1 2 3 - 0 . = +".split()
        for key in keys:
            this=wx.Button(self.panel_keyboard, -1, key, size=(40,-1))
            self.keyboardsz.Add(this, 1, wx.EXPAND|wx.ALL, 2)
            self.Bind(wx.EVT_BUTTON, self.calcular, this)
        
    def calcular(self,event):
        key=wx.FindWindowById(event.GetId()).GetLabelText()
        numbers='1234567890.' # Including decimal dot
        operators='+-*/'
        evaluator='='
        if numbers.find(key)!=-1:
            self.show_string=self.show_string+key
            self.eval_string=self.eval_string+key
            self.screen.SetValue(self.show_string)
        elif operators.find(key)!=-1:
            self.eval_string=self.eval_string+key
            self.screen.SetValue(self.show_string)
            self.show_string=""
        elif key == evaluator:
            try:
                resultado=eval(self.eval_string)
                self.screen.SetValue(str(resultado))
            except:
                wx.MessageBox("Some error detected","Calculator")
            self.OnOn
        
    def OnOn(self,event):
        self.eval_string=""
        self.show_string=""
        self.screen.SetValue("0")
            
    def OnOff(self,event):
        self.screen.SetValue(wx.EmptyString)
        self.eval_string=""
        self.show_string=""

if __name__=='__main__':
    app=wx.App()
    frame=Calculator(None, "Calculator")
    frame.Show()
    app.MainLoop()
            
