import wx
from wx.core import Choice
import GUI
import sqlite3

dbconn = sqlite3.connect("E:/data kuliah/semester 4/PBO 2/project/coding/db_test.db")
conn= sqlite3.connect("E:/data kuliah/semester 4/PBO 2/project/coding/dbbaru.db")

app = wx.App()

class LoginFrame(GUI.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def goLogin(self, event):
        uname = self.uname_text.GetValue()
        pwd = self.pwd_text.GetValue()

        getUserDB = 'SELECT * FROM User WHERE username="%s" AND password="%s"' % (uname, pwd)
        getAdminDB = 'SELECT * FROM Admin WHERE username = "%s" AND password = "%s"' % (uname, pwd)

        cur = dbconn.cursor()
        cur.execute(getUserDB)
        if (len(list(cur)) < 1):
            curs = dbconn.cursor()
            curs.execute(getAdminDB)
            if (len(list(curs)) > 0):
                print('admin ada')
                FrameMainAdmin.Show()
                FrameLogin.Hide()
                # for row in dbconn.execute(getAdminDB):
                #     FrameMainUser.
            else:
                wx.MessageBox('Username / password salah!')

        else:
           FrameMainUser.Show()
           FrameLogin.Hide()
           for row in dbconn.execute(getUserDB):
               FrameMainUser.nama_placeholder.SetLabel(row[3])
               FrameMainUser.username_placeholder.SetLabel(row[1])
           
           print('user ada')

class MainFrameAdmin(GUI.MainFrameAdmin):
    def __init__(self, parent):
        super().__init__(parent)

    def ShowSiswaData(self, event):
        FrameShowData.Show()
        FrameMainAdmin.Hide()
    
    def goLogOut(self, event):
        FrameLogin.Show()
        FrameMainAdmin.Hide()
    
class MainFrameUser(GUI.MainFrameUser):
    def __init__(self, parent):
        super().__init__(parent)

class ShowDataFrame(GUI.ShowData):

    def __init__(self, parent):
        super().__init__(parent)
        cursor = conn.cursor()

        metadata = cursor.execute('SELECT * from User')
        labels = []
        for i in metadata.description:
            labels.append(i[0])
        labels = labels[0:]
        for i in range(len(labels)):
            self.grid.SetColLabelValue(i, labels[i])

        Data = cursor.execute('SELECT * from User')
        for row in Data:
            row_num = row[0]
            cells = row[0:]
            for i in range(0,len(cells)):
                if cells[i] != None and cells[i] != "null":
                    self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        conn.commit()

    def TambahData(self,event):
        FrameAddData.Show()
        FrameShowData.Hide()
    
    def EditData(self, event):
        FrameEditData.Show()
        FrameShowData.Hide()
    
    def HapusData(self, event):
        FrameHapusData.Show()
        FrameShowData.Hide()

    def Cancel(self, event):
        FrameMainAdmin.Show()
        FrameShowData.Hide()

class AddDataFrame(GUI.TambahData):
    def __init__(self, parent):
        super().__init__(parent)
    
    def Submit(self, event):
       Username = self.BoxUsername.GetValue()
       Password = self.BoxPassword.GetValue()
       Nama = self.BoxNama.GetValue()
       TanggalLahir= self.BoxTanggalLahir.GetValue()
       JenisKelamin = self.Gender.GetStringSelection()
       TinggiBadan = self.BoxTinggiBadan.GetValue()
       BeratBadan = self.BoxBeratBadan.GetValue()
       NIK = self.BoxNIK.GetValue()
       NoHP = self.BoxNomorHp.GetValue()
       Alamat = self.BoxAlamat.GetValue()
       NilaiUN = self.BoxNilaiUN.GetValue()
       AsalSekolah = self.AsalSekolah.GetStringSelection()
       Jurusan = self.Jurusan.GetStringSelection()
       NamaAyah = self.BoxNamaAyah.GetValue()
       NamaIbu= self.BoxNamaIbu.GetValue()
       JumlahSaudara = self.BoxJumlahSaudara.GetValue()
       PekerjaanAyah = self.PekerjaanAyah.GetStringSelection()
       PekerjaanIbu = self.PekerjaanIbu.GetStringSelection()
       Status = self.Status.GetStringSelection()

    def Cancel(self, event):
        FrameShowData.Show()
        FrameAddData.Hide()
    
class EditDataFrame(GUI.EditData):
    def __init__(self, parent):
        super().__init__(parent)
    
    def Submit(self, event):
       Username = self.BoxUsernameEdit.GetValue()
       Password = self.BoxPasswordEdit.GetValue()
       Nama = self.BoxNamaEdit.GetValue()
       TanggalLahir= self.BoxTanggalLahirEdit.GetValue()
       JenisKelamin = self.GenderEdit.GetStringSelection()
       TinggiBadan = self.BoxTinggiBadanEdit.GetValue()
       BeratBadan = self.BoxBeratBadanEdit.GetValue()
       NIK = self.BoxNIKEdit.GetValue()
       NoHP = self.BoxNomorHpEdit.GetValue()
       Alamat = self.BoxAlamatEdit.GetValue()
       NilaiUN = self.BoxNilaiUNEdit.GetValue()
       AsalSekolah = self.AsalSekolahEdit.GetStringSelection()
       Jurusan = self.JurusanEdit.GetStringSelection()
       NamaAyah = self.BoxNamaAyahEdit.GetValue()
       NamaIbu= self.BoxNamaIbuEdit.GetValue()
       JumlahSaudara = self.BoxJumlahSaudaraEdit.GetValue()
       PekerjaanAyah = self.PekerjaanAyahEdit.GetStringSelection()
       PekerjaanIbu = self.PekerjaanIbuEdit.GetStringSelection()
       Status = self.StatusEdit.GetStringSelection()

    def Cancel(self, event):
        FrameShowData.Show()
        FrameEditData.Hide()

class DeleteDataFrame(GUI.DeleteData):
    def __init__(self, parent):
        super().__init__(parent)
        cursor = conn.cursor()

        metadata = cursor.execute('SELECT * from User')
        labels = []
        for i in metadata.description:
            labels.append(i[0])
        labels = labels[0:]
        for i in range(len(labels)):
            self.grid.SetColLabelValue(i, labels[i])

        Data = cursor.execute('SELECT * from User')
        for row in Data:
            row_num = row[0]
            cells = row[0:]
            for i in range(0,len(cells)):
                if cells[i] != None and cells[i] != "null":
                    self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        conn.commit()

    def HapusData(self, event):
        Hapus = self.BoxHapus.GetValue()

    def Cancel(self, event):
        FrameShowData.Show()
        FrameHapusData.Hide()


    

#daftar Frame
FrameLogin = LoginFrame(None)
FrameMainAdmin = MainFrameAdmin(None)
FrameMainUser = MainFrameUser(None)
FrameShowData = ShowDataFrame(None)
FrameAddData= AddDataFrame(None)
FrameEditData = EditDataFrame(None) 
FrameHapusData = DeleteDataFrame(None)
FrameLogin.Show()
app.MainLoop()
    
