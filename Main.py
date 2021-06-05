from sqlite3.dbapi2 import connect
import wx
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
        self.grid.ClearGrid()

        metadata = cursor.execute('SELECT * from User')
        labels = []
        for i in metadata.description:
            labels.append(i[0])
        labels = labels[1:]
        for i in range(len(labels)):
            self.grid.SetColLabelValue(i, labels[i])

        logins = cursor.execute('SELECT * from User')
        for row in logins:
            row_num = row[0]
            cells = row[1:]
            for i in range(0,len(cells)):
                if cells[i] != None and cells[i] != "null":
                    self.grid.SetCellValue(row_num-1, i, str(cells[i]))
        self.Show()
        conn.commit()

#daftar Frame
FrameLogin = LoginFrame(None)
FrameMainAdmin = MainFrameAdmin(None)
FrameMainUser = MainFrameUser(None)
FrameShowData = ShowDataFrame(None)
FrameShowData.Show()
app.MainLoop()
    