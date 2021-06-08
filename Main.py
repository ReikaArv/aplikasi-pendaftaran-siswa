import wx
from wx.core import COMPOSITION_ATOP, Choice, DateSpan, DateTime
import GUI
import sqlite3

# dbconn = sqlite3.connect("E:/data kuliah/semester 4/PBO 2/project/coding/db_test.db")
conn= sqlite3.connect("E:/Kuliah/Semester 4/PBO/ProjectPBO/database.db")
app = wx.App()

uname_cache = 'test'

class LoginFrame(GUI.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def goLogin(self, event):
        uname = self.uname_text.GetValue()
        pwd = self.pwd_text.GetValue()

        getUserDB = 'SELECT * FROM User WHERE username="%s" AND password="%s"' % (uname, pwd)
        getAdminDB = 'SELECT * FROM Admin WHERE username = "%s" AND password = "%s"' % (uname, pwd)

        cur = conn.cursor()
        cur.execute(getUserDB)
        if (len(list(cur)) < 1):
            curs = conn.cursor()
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
           for row in conn.execute(getUserDB):
               # FrameMainUser.nama_placeholder.SetLabel(row[3])
               FrameMainUser.username_placeholder.SetLabel(row[1])
               uname_cache = row[1]
               print(uname_cache)
           
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

    def goShowUser(self, event):
        uname = self.username_placeholder.GetLabel()
        print(uname)
        getUserDB = 'SELECT * FROM User WHERE username="%s"' % (uname)
        cur = conn.cursor()
        cur.execute(getUserDB)
        data = (cur.fetchall())
        print(data)
        print(uname_cache)
        for row in data:
            Nama = self.PlaceHolderNama.SetLabel(row[3])
            TanggalLahir= self.PlaceHolderTanggal.SetLabel(row[4])
            JenisKelamin = self.PlaceHolderGender.SetLabel(row[5])
            TinggiBadan = self.PlaceHolderTinggi.SetLabel(str(row[6]))
            BeratBadan = self.PlaceHolderBerat.SetLabel(str(row[7]))
            nik = self.PlaceHolderNIK.SetLabel(row[8])
            NoHP = self.PlaceHolderNOHP.SetLabel(row[9])
            Alamat = self.PlaceHolderAlamat.SetLabel(row[10])
            NilaiUN = self.PlaceHolderNilaiUN.SetLabel(str(row[11]))
            AsalSekolah = self.PlaceHolderAsalSekolah.SetLabel(row[12])
            Jurusan = self.PlaceHolderJurusan.SetLabel(row[13])
            NamaAyah = self.PlaceHoldeNamaAyah.SetLabel(row[14])
            NamaIbu= self.PlaceHolderNamaIbu.SetLabel(row[15])
            JumlahSaudara = self.PlaceHolderJumlahSaudara.SetLabel(str(row[16]))
            PekerjaanAyah = self.PlaceHolderPekerjaanAyah.SetLabel(row[17])
            PekerjaanIbu = self.PlaceHolderPekerjaanIbu.SetLabel(row[18])
            Status = self.PlaceHolderStatus.SetLabel(row[19])
        


class ShowDataFrame(GUI.ShowData):

    def __init__(self, parent):
        super().__init__(parent)

    def goShow(self, event):
        cursor = conn.cursor()

        metadata = cursor.execute('SELECT * from User')
        labels = []
        for i in metadata.description:
            labels.append(i[0])
        labels = labels[0:]
        for i in range(len(labels)):
            self.grid.SetColLabelValue(i, labels[i])

        Data = cursor.execute('SELECT * from User')
        # for data_length in range(Data):
        #     self.grid.AppendRows(1)
        #     row_num = data_length[0]
        #     cells = data_length[0:]
        #     for i in range(0,len(cells)):
        #         if cells[i] != None and cells[i] != "null":
        #             self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        # conn.commit()

        for row in Data:
            # self.grid.AppendRows(1)
            # print(row)
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
        TanggalLahir= str(self.BoxTanggalLahir.GetValue())
        JenisKelamin = self.Gender.GetStringSelection()
        TinggiBadan = self.BoxTinggiBadan.GetValue()
        BeratBadan = self.BoxBeratBadan.GetValue()
        nik = self.BoxNIK.GetValue()
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

        addQuery = f'INSERT INTO User (Username, Password, NamaLengkap, TanggalLahir, Gender, Tinggi, Berat, NIK, NoHP, Alamat, NilaiUN, AsalSekolah, Jurusan, NamaAyah, NamaIbu, JmlSaudara, PekerjaanAyah, PekerjaanIbu, Status) VALUES ("{Username}", "{Password}", "{Nama}", "{TanggalLahir}", "{JenisKelamin}", "{TinggiBadan}", "{BeratBadan}", "{nik}", "{NoHP}", "{Alamat}", "{NilaiUN}", "{AsalSekolah}", "{Jurusan}", "{NamaAyah}", "{NamaIbu}", "{JumlahSaudara}", "{PekerjaanAyah}", "{PekerjaanIbu}", "{Status}")'

        conn.execute(addQuery)
        conn.commit()

        # wx.MessageBox('Data Telah Ditambahkan')
        # FrameAddData.Close()
        # FrameShowData.Show()

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
       nik = self.BoxNIKEdit.GetValue()
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

    # def goEdit(self, event):
    #     # wx.Dialog(CekID = input('Masukkan ID yang mau di edit'))
    #     wx.MessageBox(CekID = input("Masukkan ID yang mau di edit"))

    def idSearch(self, event):
        queryID = self.BoxIDUser.GetValue()
        searchQuery = f'SELECT * FROM User WHERE userId = {queryID}'
        cur = conn.cursor()
        cur.execute(searchQuery)
        data = (cur.fetchall())
        for row in data:
            Username = self.BoxUsernameEdit.SetValue(row[1])
            Password = self.BoxPasswordEdit.SetValue(row[2])
            Nama = self.BoxNamaEdit.SetValue(row[3])
            # TanggalLahir= self.BoxTanggalLahirEdit.SetValue(row[4])
            JenisKelamin = self.GenderEdit.SetStringSelection(row[5])
            TinggiBadan = self.BoxTinggiBadanEdit.SetValue(str(row[6]))
            BeratBadan = self.BoxBeratBadanEdit.SetValue(str(row[7]))
            nik = self.BoxNIKEdit.SetValue(row[8])
            NoHP = self.BoxNomorHpEdit.SetValue(row[9])
            Alamat = self.BoxAlamatEdit.SetValue(row[10])
            NilaiUN = self.BoxNilaiUNEdit.SetValue(str(row[11]))
            AsalSekolah = self.AsalSekolahEdit.SetStringSelection(row[12])
            Jurusan = self.JurusanEdit.SetStringSelection(row[13])
            NamaAyah = self.BoxNamaAyahEdit.SetValue(row[14])
            NamaIbu= self.BoxNamaIbuEdit.SetValue(row[15])
            JumlahSaudara = self.BoxJumlahSaudaraEdit.SetValue(str(row[16]))
            PekerjaanAyah = self.PekerjaanAyahEdit.SetStringSelection(row[17])
            PekerjaanIbu = self.PekerjaanIbuEdit.SetStringSelection(row[18])
            Status = self.StatusEdit.SetStringSelection(row[19])

        

    
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
                self.grid.AppendRows(1)
                if cells[i] != None and cells[i] != "null":
                    self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        conn.commit()

    def HapusData(self, event):
        IdHapus = self.BoxHapus.GetValue()
        deleteQuery = f'DELETE * FROM User WHERE userId = {IdHapus}'
        conn.execute(deleteQuery)
        conn.commit()
        FrameHapusData.Close()
        FrameShowData.Show()

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
    
