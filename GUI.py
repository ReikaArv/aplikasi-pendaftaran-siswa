# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

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

		self.loginBtn = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		gSizer3.Add( self.loginBtn, 0, wx.ALL, 5 )

		self.regBtn = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		gSizer3.Add( self.regBtn, 0, wx.ALL, 5 )


		fgSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )


		bSizer7.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer6.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.adminName_placeholder = wx.StaticText( self, wx.ID_ANY, u"NAMA_LENGKAP_ADMINISTRATOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adminName_placeholder.Wrap( -1 )

		bSizer6.Add( self.adminName_placeholder, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer6.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ButtonShow = wx.Button( self, wx.ID_ANY, u"Tampilkan Data Siswa", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		bSizer6.Add( self.ButtonShow, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		bSizer6.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ButtonShow.Bind( wx.EVT_BUTTON, self.ShowSiswaData )
		self.m_button11.Bind( wx.EVT_BUTTON, self.goLogOut )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ShowSiswaData( self, event ):
		event.Skip()

	def goLogOut( self, event ):
		event.Skip()


###########################################################################
## Class MainFrameUser
###########################################################################

class MainFrameUser ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.username_placeholder = wx.StaticText( self, wx.ID_ANY, u"NAMA_LENGKAP_SISWA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username_placeholder.Wrap( -1 )

		fgSizer2.Add( self.username_placeholder, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.PlaceHolderNama = wx.StaticText( self, wx.ID_ANY, u"_Nama_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderNama.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderNama, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Lahir :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.PlaceHolderTanggal = wx.StaticText( self, wx.ID_ANY, u"_Tanggal Lahir_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderTanggal.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderTanggal, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Gender :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.PlaceHolderGender = wx.StaticText( self, wx.ID_ANY, u"_Gender_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderGender.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderGender, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tinggi  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer2.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.PlaceHolderTinggi = wx.StaticText( self, wx.ID_ANY, u"_Tinggi_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderTinggi.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderTinggi, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Berat :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer2.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.PlaceHolderBerat = wx.StaticText( self, wx.ID_ANY, u"_berat_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderBerat.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderBerat, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"NIK   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		fgSizer2.Add( self.m_staticText77, 0, wx.ALL, 5 )

		self.PlaceHolderNIK = wx.StaticText( self, wx.ID_ANY, u"_NIK_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderNIK.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderNIK, 0, wx.ALL, 5 )

		self.m_staticText79 = wx.StaticText( self, wx.ID_ANY, u"NO HP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer2.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.PlaceHolderNOHP = wx.StaticText( self, wx.ID_ANY, u"_NOHP_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderNOHP.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderNOHP, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Alamat :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer2.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.PlaceHolderAlamat = wx.StaticText( self, wx.ID_ANY, u"_Alamat_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderAlamat.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderAlamat, 0, wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u" NIlai UN :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer2.Add( self.m_staticText83, 0, wx.ALL, 5 )

		self.PlaceHolderNilaiUN = wx.StaticText( self, wx.ID_ANY, u"_NIlaiUN_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderNilaiUN.Wrap( -1 )

		fgSizer2.Add( self.PlaceHolderNilaiUN, 0, wx.ALL, 5 )


		bSizer18.Add( fgSizer2, 1, wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer12.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		fgSizer12.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.AsalSekolah = wx.StaticText( self, wx.ID_ANY, u"Asal Sekolah : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AsalSekolah.Wrap( -1 )

		fgSizer12.Add( self.AsalSekolah, 0, wx.ALL, 5 )

		self.PlaceHolderAsalSekolah = wx.StaticText( self, wx.ID_ANY, u"_AsalSekolah__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderAsalSekolah.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderAsalSekolah, 0, wx.ALL, 5 )

		self.m_staticText89 = wx.StaticText( self, wx.ID_ANY, u"Jurusan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		fgSizer12.Add( self.m_staticText89, 0, wx.ALL, 5 )

		self.PlaceHolderJurusan = wx.StaticText( self, wx.ID_ANY, u"_Jurusan_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderJurusan.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderJurusan, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Nama Ayah :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer12.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.PlaceHoldeNamaAyah = wx.StaticText( self, wx.ID_ANY, u"_NamaAyah_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHoldeNamaAyah.Wrap( -1 )

		fgSizer12.Add( self.PlaceHoldeNamaAyah, 0, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, u"Nama Ibu :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		fgSizer12.Add( self.m_staticText93, 0, wx.ALL, 5 )

		self.PlaceHolderNamaIbu = wx.StaticText( self, wx.ID_ANY, u"_NamaIbu_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderNamaIbu.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderNamaIbu, 0, wx.ALL, 5 )

		self.JumlahSaudara = wx.StaticText( self, wx.ID_ANY, u"Jumlah Saudara :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.JumlahSaudara.Wrap( -1 )

		fgSizer12.Add( self.JumlahSaudara, 0, wx.ALL, 5 )

		self.PlaceHolderJumlahSaudara = wx.StaticText( self, wx.ID_ANY, u"_JumlahSaudara_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderJumlahSaudara.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderJumlahSaudara, 0, wx.ALL, 5 )

		self.label1 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ayah :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )

		fgSizer12.Add( self.label1, 0, wx.ALL, 5 )

		self.PlaceHolderPekerjaanAyah = wx.StaticText( self, wx.ID_ANY, u"_PekerjaanAyah_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderPekerjaanAyah.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderPekerjaanAyah, 0, wx.ALL, 5 )

		self.label2 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ibu : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )

		fgSizer12.Add( self.label2, 0, wx.ALL, 5 )

		self.PlaceHolderPekerjaanIbu = wx.StaticText( self, wx.ID_ANY, u"_PekerjaanIbu_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderPekerjaanIbu.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderPekerjaanIbu, 0, wx.ALL, 5 )

		self.lbel3 = wx.StaticText( self, wx.ID_ANY, u"Status :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbel3.Wrap( -1 )

		fgSizer12.Add( self.lbel3, 0, wx.ALL, 5 )

		self.PlaceHolderStatus = wx.StaticText( self, wx.ID_ANY, u"_Status_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlaceHolderStatus.Wrap( -1 )

		fgSizer12.Add( self.PlaceHolderStatus, 0, wx.ALL, 5 )


		bSizer18.Add( fgSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.goShowUser )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goShowUser( self, event ):
		event.Skip()


###########################################################################
## Class ShowData
###########################################################################

class ShowData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 814,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.ButtonTambahData = wx.Button( self, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer3.Add( self.ButtonTambahData, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Edit Data", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Hapus Data", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer3.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer3.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		bSizer3.Add( self.m_button43, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer3, 0, wx.ALIGN_CENTER, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid.CreateGrid( 6, 21 )
		self.grid.EnableEditing( False )
		self.grid.EnableGridLines( True )
		self.grid.EnableDragGridSize( False )
		self.grid.SetMargins( 0, 0 )

		# Columns
		self.grid.EnableDragColMove( False )
		self.grid.EnableDragColSize( True )
		self.grid.SetColLabelSize( 30 )
		self.grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid.AutoSizeRows()
		self.grid.EnableDragRowSize( True )
		self.grid.SetRowLabelSize( 80 )
		self.grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.grid, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.goShow )
		self.ButtonTambahData.Bind( wx.EVT_BUTTON, self.TambahData )
		self.m_button6.Bind( wx.EVT_BUTTON, self.EditData )
		self.m_button5.Bind( wx.EVT_BUTTON, self.HapusData )
		self.m_button37.Bind( wx.EVT_BUTTON, self.goShow )
		self.m_button43.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goShow( self, event ):
		event.Skip()

	def TambahData( self, event ):
		event.Skip()

	def EditData( self, event ):
		event.Skip()

	def HapusData( self, event ):
		event.Skip()


	def Cancel( self, event ):
		event.Skip()


###########################################################################
## Class EditData
###########################################################################

class EditData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 569,518 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText361 = wx.StaticText( self, wx.ID_ANY, u"Edit Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )

		self.m_staticText361.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		sizer1.Add( self.m_staticText361, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer1011 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer61 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"ID User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer61.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.BoxIDUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxIDUser, 0, wx.ALL, 5 )

		self.m_staticText381 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )

		fgSizer61.Add( self.m_staticText381, 0, wx.ALL, 5 )

		self.BoxUsernameEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxUsernameEdit, 0, wx.ALL, 5 )

		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )

		fgSizer61.Add( self.m_staticText391, 0, wx.ALL, 5 )

		self.BoxPasswordEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxPasswordEdit, 0, wx.ALL, 5 )

		self.m_staticText401 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )

		fgSizer61.Add( self.m_staticText401, 0, wx.ALL, 5 )

		self.BoxNamaEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNamaEdit, 0, wx.ALL, 5 )

		self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"Tanggal lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		fgSizer61.Add( self.m_staticText411, 0, wx.ALL, 5 )

		self.BoxTanggalLahirEdit = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT )
		fgSizer61.Add( self.BoxTanggalLahirEdit, 0, wx.ALL, 5 )

		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )

		fgSizer61.Add( self.m_staticText421, 0, wx.ALL, 5 )

		GenderEditChoices = [ u"Laki Laki", u"Perempuan" ]
		self.GenderEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), GenderEditChoices, 0 )
		self.GenderEdit.SetSelection( 1 )
		fgSizer61.Add( self.GenderEdit, 0, wx.ALL, 5 )

		self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )

		fgSizer61.Add( self.m_staticText431, 0, wx.ALL, 5 )

		self.BoxTinggiBadanEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxTinggiBadanEdit, 0, wx.ALL, 5 )

		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"Berat badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )

		fgSizer61.Add( self.m_staticText441, 0, wx.ALL, 5 )

		self.BoxBeratBadanEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxBeratBadanEdit, 0, wx.ALL, 5 )

		self.m_staticText451 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText451.Wrap( -1 )

		fgSizer61.Add( self.m_staticText451, 0, wx.ALL, 5 )

		self.BoxNIKEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNIKEdit, 0, wx.ALL, 5 )

		self.m_staticText551 = wx.StaticText( self, wx.ID_ANY, u"Nomor HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText551.Wrap( -1 )

		fgSizer61.Add( self.m_staticText551, 0, wx.ALL, 5 )

		self.BoxNomorHpEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNomorHpEdit, 0, wx.ALL, 5 )

		self.m_staticText461 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )

		fgSizer61.Add( self.m_staticText461, 0, wx.ALL, 5 )

		self.BoxAlamatEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxAlamatEdit, 0, wx.ALL, 5 )

		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"Nilai UN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )

		fgSizer61.Add( self.m_staticText471, 0, wx.ALL, 5 )

		self.BoxNilaiUNEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNilaiUNEdit, 0, wx.ALL, 5 )


		bSizer1011.Add( fgSizer61, 1, wx.EXPAND, 5 )

		fgSizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button36 = wx.Button( self, wx.ID_ANY, u"Cari ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_button36, 0, wx.ALL, 5 )


		fgSizer71.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText491 = wx.StaticText( self, wx.ID_ANY, u"Jurusan Pilihan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )

		fgSizer71.Add( self.m_staticText491, 0, wx.ALL, 5 )

		JurusanEditChoices = [ u"IPA", u"IPS", u"BAHASA" ]
		self.JurusanEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), JurusanEditChoices, 0 )
		self.JurusanEdit.SetSelection( 0 )
		fgSizer71.Add( self.JurusanEdit, 0, wx.ALL, 5 )

		self.m_staticText501 = wx.StaticText( self, wx.ID_ANY, u"Nama Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText501.Wrap( -1 )

		fgSizer71.Add( self.m_staticText501, 0, wx.ALL, 5 )

		self.BoxNamaAyahEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxNamaAyahEdit, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Nama Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		fgSizer71.Add( self.m_staticText511, 0, wx.ALL, 5 )

		self.BoxNamaIbuEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxNamaIbuEdit, 0, wx.ALL, 5 )

		self.m_staticText561 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Saudara", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText561.Wrap( -1 )

		fgSizer71.Add( self.m_staticText561, 0, wx.ALL, 5 )

		self.BoxJumlahSaudaraEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxJumlahSaudaraEdit, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		fgSizer71.Add( self.m_staticText521, 0, wx.ALL, 5 )

		PekerjaanAyahEditChoices = [ u"PNS", u"Petani", u"Wirausaha", u"Wiraswasta", u"Nelayan", u"Polisi", u"Tidak Bekerja", wx.EmptyString ]
		self.PekerjaanAyahEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), PekerjaanAyahEditChoices, 0 )
		self.PekerjaanAyahEdit.SetSelection( 4 )
		fgSizer71.Add( self.PekerjaanAyahEdit, 0, wx.ALL, 5 )

		self.m_staticText531 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )

		fgSizer71.Add( self.m_staticText531, 0, wx.ALL, 5 )

		PekerjaanIbuEditChoices = [ u"PNS", u"Petani", u"Wirausaha", u"Wiraswasta", u"Nelayan", u"Polisi", u"Tidak Bekerja", wx.EmptyString ]
		self.PekerjaanIbuEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), PekerjaanIbuEditChoices, 0 )
		self.PekerjaanIbuEdit.SetSelection( 0 )
		fgSizer71.Add( self.PekerjaanIbuEdit, 0, wx.ALL, 5 )

		self.m_staticText541 = wx.StaticText( self, wx.ID_ANY, u"Status Penerimaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )

		fgSizer71.Add( self.m_staticText541, 0, wx.ALL, 5 )

		StatusEditChoices = [ u"Diterima ", u"Tidak Diterima", u"Menunnggu Konfirmasi" ]
		self.StatusEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, StatusEditChoices, 0 )
		self.StatusEdit.SetSelection( 2 )
		fgSizer71.Add( self.StatusEdit, 0, wx.ALL, 5 )

		self.m_staticText481 = wx.StaticText( self, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText481.Wrap( -1 )

		fgSizer71.Add( self.m_staticText481, 0, wx.ALL, 5 )

		AsalSekolahEditChoices = [ u"SMPN 1 Pekoland", u"SMP 5 Curahtatal", u"SMPK 14 Axioma", u"SMP 2 Jember", u"SMPN 3 Bondowoso", u"MTS Al-Ahlan" ]
		self.AsalSekolahEdit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AsalSekolahEditChoices, 0 )
		self.AsalSekolahEdit.SetSelection( 0 )
		fgSizer71.Add( self.AsalSekolahEdit, 0, wx.ALL, 5 )


		bSizer1011.Add( fgSizer71, 1, wx.EXPAND, 5 )


		sizer1.Add( bSizer1011, 1, 0, 5 )

		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button42.SetMinSize( wx.Size( -1,30 ) )

		bSizer231.Add( self.m_button42, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button43.SetMinSize( wx.Size( -1,30 ) )

		bSizer231.Add( self.m_button43, 0, wx.ALL, 5 )


		sizer1.Add( bSizer231, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( sizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.goEdit )
		self.m_button36.Bind( wx.EVT_BUTTON, self.idSearch )
		self.m_button42.Bind( wx.EVT_BUTTON, self.Submit )
		self.m_button43.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def goEdit( self, event ):
		event.Skip()

	def idSearch( self, event ):
		event.Skip()

	def Submit( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()


###########################################################################
## Class TempEditData
###########################################################################

class TempEditData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.Edit = wx.StaticText( self, wx.ID_ANY, u"Edit Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Edit.Wrap( -1 )

		self.Edit.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.Edit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"Apanya yang ingin di edit ??", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		bSizer11.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Usename", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button11, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button12, 0, wx.ALL, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button13, 0, wx.ALL, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Tanggal lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button14, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Tinggi Badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button16, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Berat Badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Nomor HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Nilai UN", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Nama Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button25 = wx.Button( self, wx.ID_ANY, u"Nama Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button25, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer8, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		bSizer13.Add( self.m_staticText63, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Pekerjaan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button26, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Pekerjaan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Jml Saudara", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button28, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button29, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.EditUsername )
		self.m_button12.Bind( wx.EVT_BUTTON, self.EditPassword )
		self.m_button13.Bind( wx.EVT_BUTTON, self.EditNama )
		self.m_button14.Bind( wx.EVT_BUTTON, self.EditTanggalLahir )
		self.m_button15.Bind( wx.EVT_BUTTON, self.EditGender )
		self.m_button16.Bind( wx.EVT_BUTTON, self.EditTinggiBadan )
		self.m_button17.Bind( wx.EVT_BUTTON, self.EditBeratBadan )
		self.m_button18.Bind( wx.EVT_BUTTON, self.EditNIK )
		self.m_button19.Bind( wx.EVT_BUTTON, self.EditNomorHP )
		self.m_button20.Bind( wx.EVT_BUTTON, self.EditAlamat )
		self.m_button21.Bind( wx.EVT_BUTTON, self.EditNIlaiUN )
		self.m_button22.Bind( wx.EVT_BUTTON, self.EditAsalsekolah )
		self.m_button23.Bind( wx.EVT_BUTTON, self.EditJurusan )
		self.m_button24.Bind( wx.EVT_BUTTON, self.EditNamaAyah )
		self.m_button25.Bind( wx.EVT_BUTTON, self.EditNamaIbu )
		self.m_button26.Bind( wx.EVT_BUTTON, self.EditPekerjaanAyah )
		self.m_button27.Bind( wx.EVT_BUTTON, self.EditPekerjaanIbu )
		self.m_button28.Bind( wx.EVT_BUTTON, self.EditJmlSaudara )
		self.m_button29.Bind( wx.EVT_BUTTON, self.EditStatus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def EditUsername( self, event ):
		event.Skip()

	def EditPassword( self, event ):
		event.Skip()

	def EditNama( self, event ):
		event.Skip()

	def EditTanggalLahir( self, event ):
		event.Skip()

	def EditGender( self, event ):
		event.Skip()

	def EditTinggiBadan( self, event ):
		event.Skip()

	def EditBeratBadan( self, event ):
		event.Skip()

	def EditNIK( self, event ):
		event.Skip()

	def EditNomorHP( self, event ):
		event.Skip()

	def EditAlamat( self, event ):
		event.Skip()

	def EditNIlaiUN( self, event ):
		event.Skip()

	def EditAsalsekolah( self, event ):
		event.Skip()

	def EditJurusan( self, event ):
		event.Skip()

	def EditNamaAyah( self, event ):
		event.Skip()

	def EditNamaIbu( self, event ):
		event.Skip()

	def EditPekerjaanAyah( self, event ):
		event.Skip()

	def EditPekerjaanIbu( self, event ):
		event.Skip()

	def EditJmlSaudara( self, event ):
		event.Skip()

	def EditStatus( self, event ):
		event.Skip()


###########################################################################
## Class TambahData
###########################################################################

class TambahData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 569,518 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bsizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText361 = wx.StaticText( self, wx.ID_ANY, u"TambahData", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )

		self.m_staticText361.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bsizer1.Add( self.m_staticText361, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer1011 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer61 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText381 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )

		fgSizer61.Add( self.m_staticText381, 0, wx.ALL, 5 )

		self.BoxUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxUsername, 0, wx.ALL, 5 )

		self.m_staticText391 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )

		fgSizer61.Add( self.m_staticText391, 0, wx.ALL, 5 )

		self.BoxPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxPassword, 0, wx.ALL, 5 )

		self.m_staticText401 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText401.Wrap( -1 )

		fgSizer61.Add( self.m_staticText401, 0, wx.ALL, 5 )

		self.BoxNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNama, 0, wx.ALL, 5 )

		self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"Tanggal lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		fgSizer61.Add( self.m_staticText411, 0, wx.ALL, 5 )

		self.BoxTanggalLahir = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT )
		fgSizer61.Add( self.BoxTanggalLahir, 0, wx.ALL, 5 )

		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )

		fgSizer61.Add( self.m_staticText421, 0, wx.ALL, 5 )

		GenderChoices = [ u"Laki Laki", u"Perempuan" ]
		self.Gender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), GenderChoices, 0 )
		self.Gender.SetSelection( 0 )
		fgSizer61.Add( self.Gender, 0, wx.ALL, 5 )

		self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )

		fgSizer61.Add( self.m_staticText431, 0, wx.ALL, 5 )

		self.BoxTinggiBadan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxTinggiBadan, 0, wx.ALL, 5 )

		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"Berat badan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )

		fgSizer61.Add( self.m_staticText441, 0, wx.ALL, 5 )

		self.BoxBeratBadan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxBeratBadan, 0, wx.ALL, 5 )

		self.m_staticText451 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText451.Wrap( -1 )

		fgSizer61.Add( self.m_staticText451, 0, wx.ALL, 5 )

		self.BoxNIK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNIK, 0, wx.ALL, 5 )

		self.m_staticText551 = wx.StaticText( self, wx.ID_ANY, u"Nomor HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText551.Wrap( -1 )

		fgSizer61.Add( self.m_staticText551, 0, wx.ALL, 5 )

		self.BoxNomorHp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNomorHp, 0, wx.ALL, 5 )

		self.m_staticText461 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText461.Wrap( -1 )

		fgSizer61.Add( self.m_staticText461, 0, wx.ALL, 5 )

		self.BoxAlamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxAlamat, 0, wx.ALL, 5 )

		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"Nilai UN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )

		fgSizer61.Add( self.m_staticText471, 0, wx.ALL, 5 )

		self.BoxNilaiUN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer61.Add( self.BoxNilaiUN, 0, wx.ALL, 5 )

		self.m_staticText481 = wx.StaticText( self, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText481.Wrap( -1 )

		fgSizer61.Add( self.m_staticText481, 0, wx.ALL, 5 )

		AsalSekolahChoices = [ u"SMPN 1 Pekoland", u"SMP 5 Curahtatal", u"SMPK 14 Axioma", u"SMP 2 Jember", u"SMPN 3 Bondowoso", u"MTS Al-Ahlan" ]
		self.AsalSekolah = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AsalSekolahChoices, 0 )
		self.AsalSekolah.SetSelection( 0 )
		fgSizer61.Add( self.AsalSekolah, 0, wx.ALL, 5 )


		bSizer1011.Add( fgSizer61, 1, 0, 5 )

		fgSizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText491 = wx.StaticText( self, wx.ID_ANY, u"Jurusan Pilihan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )

		fgSizer71.Add( self.m_staticText491, 0, wx.ALL, 5 )

		JurusanChoices = [ u"IPA", u"IPS", u"BAHASA" ]
		self.Jurusan = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 125,-1 ), JurusanChoices, 0 )
		self.Jurusan.SetSelection( 0 )
		fgSizer71.Add( self.Jurusan, 0, wx.ALL, 5 )

		self.m_staticText501 = wx.StaticText( self, wx.ID_ANY, u"Nama Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText501.Wrap( -1 )

		fgSizer71.Add( self.m_staticText501, 0, wx.ALL, 5 )

		self.BoxNamaAyah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxNamaAyah, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Nama Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		fgSizer71.Add( self.m_staticText511, 0, wx.ALL, 5 )

		self.BoxNamaIbu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxNamaIbu, 0, wx.ALL, 5 )

		self.m_staticText561 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Saudara", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText561.Wrap( -1 )

		fgSizer71.Add( self.m_staticText561, 0, wx.ALL, 5 )

		self.BoxJumlahSaudara = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		fgSizer71.Add( self.BoxJumlahSaudara, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		fgSizer71.Add( self.m_staticText521, 0, wx.ALL, 5 )

		PekerjaanAyahChoices = [ u"PNS", u"Petani", u"Wirausaha", u"Wiraswasta", u"Nelayan", u"Polisi", u"Tidak Bekerja", wx.EmptyString ]
		self.PekerjaanAyah = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PekerjaanAyahChoices, 0 )
		self.PekerjaanAyah.SetSelection( 0 )
		fgSizer71.Add( self.PekerjaanAyah, 0, wx.ALL, 5 )

		self.m_staticText531 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )

		fgSizer71.Add( self.m_staticText531, 0, wx.ALL, 5 )

		PekerjaanIbuChoices = [ u"PNS", u"Petani", u"Wirausaha", u"Wiraswasta", u"Nelayan", u"Polisi", u"Tidak Bekerja", wx.EmptyString ]
		self.PekerjaanIbu = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PekerjaanIbuChoices, 0 )
		self.PekerjaanIbu.SetSelection( 0 )
		fgSizer71.Add( self.PekerjaanIbu, 0, wx.ALL, 5 )

		self.m_staticText541 = wx.StaticText( self, wx.ID_ANY, u"Status Penerimaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )

		fgSizer71.Add( self.m_staticText541, 0, wx.ALL, 5 )

		StatusChoices = [ u"Diterima ", u"Tidak Diterima", u"Menunnggu Konfirmasi" ]
		self.Status = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, StatusChoices, 0 )
		self.Status.SetSelection( 2 )
		fgSizer71.Add( self.Status, 0, wx.ALL, 5 )


		bSizer1011.Add( fgSizer71, 1, 0, 5 )


		bsizer1.Add( bSizer1011, 1, 0, 5 )

		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer231.Add( self.m_button42, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer231.Add( self.m_button43, 0, wx.ALL, 5 )


		bsizer1.Add( bSizer231, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bsizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button42.Bind( wx.EVT_BUTTON, self.Submit )
		self.m_button43.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Submit( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()


###########################################################################
## Class EditUsername
###########################################################################

class EditUsername ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.Edit = wx.StaticText( self, wx.ID_ANY, u"Edit Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Edit.Wrap( -1 )

		self.Edit.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.Edit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		bSizer14.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.m_staticText681 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText681.Wrap( -1 )

		bSizer14.Add( self.m_staticText681, 0, wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"ID User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer10.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.BoxID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer10.Add( self.BoxID, 0, wx.ALL, 5 )

		self.Username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Username.Wrap( -1 )

		fgSizer10.Add( self.Username, 0, wx.ALL, 5 )

		self.BoxUserName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer10.Add( self.BoxUserName, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer10, 0, wx.EXPAND, 5 )

		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		bSizer14.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_button36 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button36, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button36.Bind( wx.EVT_BUTTON, self.Submit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Submit( self, event ):
		event.Skip()


###########################################################################
## Class EditPassword
###########################################################################

class EditPassword ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.Edit = wx.StaticText( self, wx.ID_ANY, u"Edit Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Edit.Wrap( -1 )

		self.Edit.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.Edit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		bSizer14.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.m_staticText681 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText681.Wrap( -1 )

		bSizer14.Add( self.m_staticText681, 0, wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"ID User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer10.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.BoxID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer10.Add( self.BoxID, 0, wx.ALL, 5 )

		self.Password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )

		fgSizer10.Add( self.Password, 0, wx.ALL, 5 )

		self.BoxPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer10.Add( self.BoxPassword, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer10, 0, wx.EXPAND, 5 )

		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		bSizer14.Add( self.m_staticText84, 0, wx.ALL, 5 )

		self.m_button36 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button36, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button36.Bind( wx.EVT_BUTTON, self.Submit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Submit( self, event ):
		event.Skip()


###########################################################################
## Class DeleteData
###########################################################################

class DeleteData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 835,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid.CreateGrid( 6, 21 )
		self.grid.EnableEditing( False )
		self.grid.EnableGridLines( True )
		self.grid.EnableDragGridSize( False )
		self.grid.SetMargins( 0, 0 )

		# Columns
		self.grid.EnableDragColMove( False )
		self.grid.EnableDragColSize( True )
		self.grid.SetColLabelSize( 30 )
		self.grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid.EnableDragRowSize( True )
		self.grid.SetRowLabelSize( 80 )
		self.grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer33.Add( self.grid, 0, wx.ALL, 5 )

		self.m_staticText180 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText180.Wrap( -1 )

		bSizer33.Add( self.m_staticText180, 0, wx.ALL, 5 )


		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"ID User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )

		fgSizer20.Add( self.m_staticText178, 0, wx.ALL, 5 )

		self.BoxHapus = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.BoxHapus, 0, wx.ALL, 5 )

		self.m_button45 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button45, 0, wx.ALL, 5 )

		self.m_button46 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button46, 0, wx.ALL, 5 )


		bSizer32.Add( fgSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button45.Bind( wx.EVT_BUTTON, self.HapusData )
		self.m_button46.Bind( wx.EVT_BUTTON, self.Cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HapusData( self, event ):
		event.Skip()

	def Cancel( self, event ):
		event.Skip()


