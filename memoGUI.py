# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html

###########################################################################
## Class notificationFrame
###########################################################################

class notificationFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 321,271 ), style = wx.FRAME_NO_TASKBAR|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 321,271 ), wx.Size( 321,271 ) )
		
		notificationSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.parentPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.TAB_TRAVERSAL )
		self.parentPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.parentPanel.SetMinSize( wx.Size( 300,200 ) )
		self.parentPanel.SetMaxSize( wx.Size( 300,200 ) )
		
		parentSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
		parentSizer.AddGrowableCol( 1 )
		parentSizer.AddGrowableRow( 1 )
		parentSizer.SetFlexibleDirection( wx.BOTH )
		parentSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.titleLabel = wx.StaticText( self.parentPanel, wx.ID_ANY, u"memoKAD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titleLabel.Wrap( -1 )
		self.titleLabel.SetFont( wx.Font( 14, 74, 90, 92, False, "Calibri" ) )
		
		parentSizer.Add( self.titleLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		parentSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.infoPanel = wx.ScrolledWindow( self.parentPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.VSCROLL )
		self.infoPanel.SetScrollRate( 5, 5 )
		self.infoPanel.SetMinSize( wx.Size( 300,200 ) )
		self.infoPanel.SetMaxSize( wx.Size( 300,200 ) )
		
		parentSizer.Add( self.infoPanel, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		parentSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.parentPanel.SetSizer( parentSizer )
		self.parentPanel.Layout()
		notificationSizer.Add( self.parentPanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( notificationSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.notificationFrameOnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def notificationFrameOnClose( self, event ):
		pass
	

###########################################################################
## Class loginDialog
###########################################################################

class loginDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"memoKAD Login", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		loginFrameSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.parentPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		parentSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.loginMessage = wx.StaticText( self.parentPanel, wx.ID_ANY, u"It seems that you are not logged in on this computer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loginMessage.Wrap( -1 )
		parentSizer.Add( self.loginMessage, 0, wx.ALL, 5 )
		
		inputSizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		inputSizer.AddGrowableCol( 1 )
		inputSizer.SetFlexibleDirection( wx.BOTH )
		inputSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.userLabel = wx.StaticText( self.parentPanel, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.userLabel.Wrap( -1 )
		inputSizer.Add( self.userLabel, 0, wx.ALL, 5 )
		
		self.userNameInput = wx.TextCtrl( self.parentPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		inputSizer.Add( self.userNameInput, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.passwordLabel = wx.StaticText( self.parentPanel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.passwordLabel.Wrap( -1 )
		inputSizer.Add( self.passwordLabel, 0, wx.ALL, 5 )
		
		self.passwordInput = wx.TextCtrl( self.parentPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		inputSizer.Add( self.passwordInput, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		parentSizer.Add( inputSizer, 0, wx.EXPAND, 5 )
		
		buttonsSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.loginButton = wx.Button( self.parentPanel, wx.ID_ANY, u"Sign in", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.loginButton, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.forgotButton = wx.Button( self.parentPanel, wx.ID_ANY, u"Forgot Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.forgotButton, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.registerButton = wx.Button( self.parentPanel, wx.ID_ANY, u"Join", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.registerButton, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.cancelButton = wx.Button( self.parentPanel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		buttonsSizer.Add( self.cancelButton, 0, wx.TOP|wx.BOTTOM, 5 )
		
		
		parentSizer.Add( buttonsSizer, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.parentPanel.SetSizer( parentSizer )
		self.parentPanel.Layout()
		parentSizer.Fit( self.parentPanel )
		loginFrameSizer.Add( self.parentPanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( loginFrameSizer )
		self.Layout()
		loginFrameSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.loginButton.Bind( wx.EVT_BUTTON, self.loginButtonOnButtonClick )
		self.forgotButton.Bind( wx.EVT_BUTTON, self.forgotButtonOnButtonClick )
		self.registerButton.Bind( wx.EVT_BUTTON, self.registerButtonOnButtonClick )
		self.cancelButton.Bind( wx.EVT_BUTTON, self.cancelButtonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loginButtonOnButtonClick( self, event ):
		pass
	
	def forgotButtonOnButtonClick( self, event ):
		pass
	
	def registerButtonOnButtonClick( self, event ):
		pass
	
	def cancelButtonOnButtonClick( self, event ):
		pass
	

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 750,450 ), wx.Size( -1,-1 ) )
		
		mainFrameSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.parentPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		parentSizer = wx.FlexGridSizer( 1, 3, 0, 1 )
		parentSizer.AddGrowableCol( 1 )
		parentSizer.AddGrowableRow( 0 )
		parentSizer.SetFlexibleDirection( wx.HORIZONTAL )
		parentSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.noteList = wx.TreeCtrl( self.parentPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TR_DEFAULT_STYLE|wx.TR_SINGLE )
		self.noteList.SetMinSize( wx.Size( 150,450 ) )
		
		parentSizer.Add( self.noteList, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.noteWindow = wx.html.HtmlWindow( self.parentPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO|wx.SIMPLE_BORDER )
		self.noteWindow.SetMinSize( wx.Size( -1,430 ) )
		
		parentSizer.Add( self.noteWindow, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.buttonPanel = wx.ScrolledWindow( self.parentPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER )
		self.buttonPanel.SetScrollRate( 5, 5 )
		self.buttonPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.buttonPanel.SetMinSize( wx.Size( 130,-1 ) )
		
		buttonSizer = wx.BoxSizer( wx.VERTICAL )
		
		buttonSizer.SetMinSize( wx.Size( 100,100 ) ) 
		self.newButton = wx.Button( self.buttonPanel, wx.ID_ANY, u"New", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		buttonSizer.Add( self.newButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.editButton = wx.Button( self.buttonPanel, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		buttonSizer.Add( self.editButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.delButton = wx.Button( self.buttonPanel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		buttonSizer.Add( self.delButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.accountButton = wx.Button( self.buttonPanel, wx.ID_ANY, u"Account Settings", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		buttonSizer.Add( self.accountButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.buttonPanel.SetSizer( buttonSizer )
		self.buttonPanel.Layout()
		buttonSizer.Fit( self.buttonPanel )
		parentSizer.Add( self.buttonPanel, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.parentPanel.SetSizer( parentSizer )
		self.parentPanel.Layout()
		parentSizer.Fit( self.parentPanel )
		mainFrameSizer.Add( self.parentPanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( mainFrameSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.mainFrameOnClose )
		self.newButton.Bind( wx.EVT_BUTTON, self.newButtonOnButtonClick )
		self.editButton.Bind( wx.EVT_BUTTON, self.editButtonOnButtonClick )
		self.delButton.Bind( wx.EVT_BUTTON, self.delButtonOnButtonClick )
		self.accountButton.Bind( wx.EVT_BUTTON, self.accountButtonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def mainFrameOnClose( self, event ):
		pass
	
	def newButtonOnButtonClick( self, event ):
		pass
	
	def editButtonOnButtonClick( self, event ):
		pass
	
	def delButtonOnButtonClick( self, event ):
		pass
	
	def accountButtonOnButtonClick( self, event ):
		pass
	

###########################################################################
## Class consoleFrame
###########################################################################

class consoleFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		consoleSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer11.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.console = wx.StaticText( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,300 ), 0 )
		self.console.Wrap( -1 )
		self.console.SetMinSize( wx.Size( 500,300 ) )
		self.console.SetMaxSize( wx.Size( 500,-1 ) )
		
		bSizer11.Add( self.console, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer11 )
		self.m_panel5.Layout()
		bSizer11.Fit( self.m_panel5 )
		consoleSizer.Add( self.m_panel5, 1, wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		
		self.SetSizer( consoleSizer )
		self.Layout()
		consoleSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

