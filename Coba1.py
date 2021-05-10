# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 420,240 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Login ke E-learning", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.uname_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		fgSizer1.Add( self.uname_text, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.pwd_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		fgSizer1.Add( self.pwd_text, 0, wx.ALL, 5 )


		fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.loginBtn = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.loginBtn, 0, wx.ALL, 5 )

		self.regBtn = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.regBtn, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.loginBtn.Bind( wx.EVT_BUTTON, self.goLogin )
		self.regBtn.Bind( wx.EVT_BUTTON, self.goReg )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goLogin( self, event ):
		event.Skip()

	def goReg( self, event ):
		event.Skip()


###########################################################################
## Class MainFrameAdmin
###########################################################################

class MainFrameAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 440,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.adminName_placeholder = wx.StaticText( self, wx.ID_ANY, u"NAMA_LENGKAP_ADMINISTRATOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adminName_placeholder.Wrap( -1 )

		fgSizer3.Add( self.adminName_placeholder, 0, wx.ALL, 5 )

		self.ShowSiswaData = wx.Button( self, wx.ID_ANY, u"Tampilkan Data Siswa", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		fgSizer3.Add( self.ShowSiswaData, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Tambah Data Siswa", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		fgSizer3.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"gatau button apa", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		fgSizer3.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		fgSizer3.Add( self.m_button11, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.goLogout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goLogout( self, event ):
		event.Skip()


###########################################################################
## Class MainFrameUser
###########################################################################

class MainFrameUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.nama_placeholder = wx.StaticText( self, wx.ID_ANY, u"NAMA_LENGKAP_SISWA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_placeholder.Wrap( -1 )

		fgSizer2.Add( self.nama_placeholder, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.username_placeholder = wx.StaticText( self, wx.ID_ANY, u"_username_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_placeholder.Wrap( -1 )

		fgSizer2.Add( self.username_placeholder, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer2.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


