from wx.lib.pubsub import Publisher
from appThread import sThread, runningThread

from globalValues import *
from contentParser import *

import wx
import memoGUI
import virtualDatabase
import cPickle
import time

USERNAME = ''
USERID = ''
PASSWORD = ''

class mainFrame( memoGUI.mainFrame ):
    def __init__( self, parent ):
        if isWindowsOpen['mainFrame'] == False:
            memoGUI.mainFrame.__init__( self, parent )

            isWindowsOpen['mainFrame'] = True
            openWindowId['mainFrame'] = self

            self.populateTree()
        else:
            self = openWindowId['mainFrame']

    def newButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser(url.newNote)

    def editButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser(url.editNote)

    def delButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser(url.deleteNote)

    def accountButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser(url.account)

    def populateTree(self):
        global USERNAME
        self.noteList.DeleteAllItems()

        NOTES = virtualDatabase.readDB('NOTE')
        GROUPS = virtualDatabase.readDB('GROUP')

        root = self.noteList.AddRoot(USERNAME)
        for Group in GROUPS:
            parent = self.noteList.AppendItem(root, Group.GROUP_NAME)
            self.noteList.SetPyData(root, Group.ID)
            for Note in NOTES:
                if Note.GROUP_ID == Group.ID:
                    child = self.noteList.AppendItem(parent, Note.TITLE)
                    self.noteList.SetPyData(child, Note.ID)
            self.noteList.Expand(parent)
        self.noteList.Expand(root)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.noteList)

    def OnSelChanged(self, evt):
        self.item = evt.GetItem()
        noteID = self.noteList.GetPyData(self.item)
        if(self.noteList.ItemHasChildren(self.item) == False):
            f = open("blankTemp.dmp", 'wb')
            f.close()
            self.noteWindow.LoadFile("blankTemp.dmp")
            self.noteWindow.AppendToPage(getNote(virtualDatabase.readDB('NOTE'), noteID).CONTENT)


    def mainFrameOnClose( self, event ):
        self.Destroy()

    def Destroy( self ):
        isWindowsOpen['mainFrame'] = False
        openWindowId['mainFrame'] = None
        memoGUI.mainFrame.Destroy( self )

#######################################################

class notificationFrame( memoGUI.notificationFrame ):
    def __init__( self, parent ):
        global Unread
        if isWindowsOpen['notificationFrame'] == False:
            memoGUI.notificationFrame.__init__( self, parent )

            isWindowsOpen['notificationFrame'] = True
            openWindowId['notificationFrame'] = self
        else:
            self = openWindowId['notificationFrame']

        currentResolution = wx.GetDisplaySize()
        borderSize = (wx.SYS_FRAMESIZE_X, wx.SYS_FRAMESIZE_Y)
        frameSize = self.GetClientSize()
        taskBarInfo = getTaskbarPos()

        if taskBarInfo[1] == 'right':
            framePositionX = currentResolution[0] - (frameSize[0] + borderSize[0] + taskBarInfo[0])
            framePositionY = currentResolution[1] - (frameSize[1] + borderSize[1])
        elif taskBarInfo[1] == 'top':
            framePositionX = currentResolution[0] - frameSize[0] - borderSize[0]
            framePositionY = borderSize[1] + taskBarInfo[0]
        elif taskBarInfo[1] == 'left':
            framePositionX = borderSize[0] + taskBarInfo[0]
            framePositionY = currentResolution[1] - (frameSize[1] + borderSize[1])
        elif taskBarInfo[1] == 'bottom':
            framePositionX = currentResolution[0] - frameSize[0] - borderSize[0]
            framePositionY = currentResolution[1] - frameSize[1] - borderSize[1] - taskBarInfo[0]
        else:
            framePositionX = currentResolution[0] - (frameSize[0] + borderSize[0])
            framePositionY = currentResolution[1] + borderSize[1]

        self.infoSizer = wx.BoxSizer( wx.VERTICAL )

        self.SetPosition((framePositionX, framePositionY))

        self.populateNotifications(NOTIFICATION)

        self.Bind(wx.EVT_ACTIVATE, self.OnActivate)

    def OnActivate(self, evt):
        if (evt.GetActive() == False):
            self.Close()

    def Destroy( self ):
        global NOTIFICATION
        isWindowsOpen['notificationFrame'] = False
        openWindowId['notificationFrame'] = None
        NOTIFICATION = []
        memoGUI.notificationFrame.Destroy( self )

    def notificationFrameOnClose( self, event ):
        self.Destroy()

    def populateNotifications(self, NOTIFICATION):
        print "NOTIFICITATION:", NOTIFICATION
        self.infoSizer.Clear(True)
        FEEDS = []
        for item in NOTIFICATION:
            FEEDS.append(self.createNewPanel(item))

        if (NOTIFICATION.__len__() == 0):
            FEEDS.append(self.createNewPanel(Notification('-1','Today','You have no new notifications!', 'default')))
        for feed in FEEDS:
            static = wx.StaticLine( self.infoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            self.infoSizer.Add(feed, wx.ALL)
            self.infoSizer.Add(static, 0, wx.EXPAND|wx.ALL, 5)


        self.infoPanel.SetSizer(self.infoSizer)
        self.infoPanel.Layout()
        self.infoSizer.Fit( self.infoPanel )

    def createNewPanel(self, Notification):
        tempPanel = wx.Panel(self.infoPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 290, 33 ), wx.TAB_TRAVERSAL )
        tempPanel.SetMinSize(wx.Size(290,33))
        tempSizer = wx.BoxSizer(wx.HORIZONTAL)
        tempSizer.SetMinSize(wx.Size(290,33))

        label = Notification.VALUE
        type = Notification.TYPE

        tempLabel = wx.StaticText( tempPanel, wx.ID_ANY, label, wx.DefaultPosition, wx.Size(220, 33))
        tempLabel.SetMinSize(wx.Size(220,33))
        tempSizer.Add(tempLabel, 0)

        if (type == 'invite'):
            tempButton = wx.Button( tempPanel, wx.ID_ANY, u"Review", wx.DefaultPosition, wx.Size( 50,30 ) )
            tempButton.SetMinSize(wx.Size(50,30))
            tempSizer.Add( tempButton, 0)

            tempButton.Bind( wx.EVT_BUTTON, self.reviewFeed )


        tempSizer.AddSpacer( wx.Size(30,30))

        tempPanel.SetSizer(tempSizer)
        tempPanel.Layout()
        tempSizer.Fit(tempPanel)
        return tempPanel

    def reviewFeed(self, event):
        wx.LaunchDefaultBrowser("http://memokad.com/memo/public/home?id=3434")

#######################################################

class taskBar( wx.TaskBarIcon ):
    # Setting Ids for the menu items
    MEMO_MAIN = wx.NewId()
    MEMO_LOGOUT = wx.NewId()
    MEMO_LOGIN = wx.NewId()
    MEMO_EXIT = wx.NewId()

    def __init__(self):
        if isWindowsOpen['taskBar'] == False:
            global Timer
            wx.TaskBarIcon.__init__(self)

            isWindowsOpen['taskBar'] = True
            openWindowId['taskBar'] = self

            Timer = wx.Timer(self)

            # Set the image
            self.tbIcon = wx.Icon("favicon.ico", wx.BITMAP_TYPE_ICO)

            self.SetIcon(self.tbIcon, "memoKAD")

            # bind some evts
            self.Bind(wx.EVT_TIMER, OnTimeOut, Timer)
            self.Bind(wx.EVT_TASKBAR_LEFT_UP, self.OnTaskBarLeft)
            self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.OnTaskBarRight)
            self.Bind(wx.EVT_MENU, self.OnTaskBarMain, id=self.MEMO_MAIN)
            self.Bind(wx.EVT_MENU, self.OnTaskBarLogOut, id=self.MEMO_LOGOUT)
            self.Bind(wx.EVT_MENU, self.OnTaskBarLogIn, id=self.MEMO_LOGIN)
            self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.MEMO_EXIT)
        else:
            self = openWindowId['taskBar']

    def Destroy( self ):
        self.RemoveIcon()
        wx.TaskBarIcon.Destroy( self )
        isWindowsOpen['taskBar'] = False
        openWindowId['taskBar'] = None

    def createPopupMenu(self):
        global LOGGEDIN
        print LOGGEDIN
        menu = wx.Menu()
        menu.Append(self.MEMO_MAIN, "Show memoKAD")
        if LOGGEDIN == True:
            menu.Append(self.MEMO_LOGOUT, "Log Out")
        else:
            menu.Append(self.MEMO_LOGIN, "Log In")

        menu.AppendSeparator()
        menu.Append(self.MEMO_EXIT, "Exit")
        return menu

    '''
    Assigning events to menu items
    '''

    def OnTaskBarClose(self, event):
        exitApp()


    def OnTaskBarRight(self, event):
        menu = self.createPopupMenu()

        if isWindowsOpen['loginDialog'] == False:
            self.PopupMenu(menu)
            menu.Destroy()

    def OnTaskBarLeft(self, event):
        if LOGGEDIN == True:
            print "Logged in yet"
            if isWindowsOpen['notificationFrame'] == True:
                openWindowId['notificationFrame'].Destroy()
            else:
                notify = notificationFrame(parent=None)
                notify.Show()
        else:
            if isWindowsOpen['notificationFrame']:
                openWindowId['notificationFrame'].Destroy()
            if isWindowsOpen['mainFrame']:
                openWindowId['mainFrame'].Destroy()

    def OnTaskBarLogOut(self, event):
        dlg = wx.MessageDialog(wx.Frame(parent=None), 'Are you sure you want to logout?\n\nAll your data will be cleared', 'Confirm Logout?',
            wx.YES_NO | wx.ICON_QUESTION)

        if dlg.ShowModal() == wx.ID_NO:
            return

        global LOGGEDIN, Unread
        LOGGEDIN = False
        print "Logout!!!!!"
        Unread = []
        try:
            Timer.Stop()
        except: pass

        if isWindowsOpen['notificationFrame']:
            openWindowId['notificationFrame'].Destroy()
        if isWindowsOpen['mainFrame']:
            openWindowId['mainFrame'].Destroy()

        f = open("loginInfo.obj","wb")
        f.close()

        loginDialogBox = loginDialog(parent=None)
        loginDialogBox.ShowModal()

    def OnTaskBarLogIn(self, event):
        if isWindowsOpen['notificationFrame']:
            openWindowId['notificationFrame'].Destroy()
        if isWindowsOpen['mainFrame']:
            openWindowId['mainFrame'].Destroy()

        loginDialogBox = loginDialog(parent=None)
        loginDialogBox.ShowModal()

    def OnTaskBarMain(self, event):
        mainframe = mainFrame(parent=None)
        mainframe.Show()

#######################################################

class loginDialog( memoGUI.loginDialog ):
    def __init__( self, parent ):
        if isWindowsOpen['loginDialog'] == False:
            memoGUI.loginDialog.__init__( self, parent )

            isWindowsOpen['loginDialog'] = True
            openWindowId['loginDialog'] = self
        else:
            self = openWindowId['loginDialog']

    def Destroy( self ):
        memoGUI.loginDialog.Destroy( self )
        isWindowsOpen['loginDialog'] = False
        openWindowId['loginDialog'] = None

    def loginButtonOnButtonClick( self, event ):
        if self.userNameInput.IsEmpty() or self.passwordInput.IsEmpty():
            dlg = wx.MessageDialog(self, 'Enter both Username and Password.', 'Incomplete data',
                  wx.OK | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
        else:
            USERNAME = self.userNameInput.GetValue()
            PASSWORD = self.passwordInput.GetValue()

            sThread(self, 'LOGIN', USERNAME, PASSWORD)
            self.Destroy()

    def forgotButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser("http://memokad.com/forgot")
        self.Destroy()

    def registerButtonOnButtonClick( self, event ):
        wx.LaunchDefaultBrowser("http://memokad.com/signup")
        self.Destroy()

    def cancelButtonOnButtonClick( self, event ):
        self.Destroy()

#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################

def exitApp(confirm = True):
    global runningThread
    if confirm == True:
        dlg = wx.MessageDialog(wx.Frame(parent=None), 'Are you sure you want to exit memoKAD?', 'Confirm Exit?',
            wx.YES_NO | wx.ICON_QUESTION)

    while runningThread.__len__() != 0:
        print runningThread.__len__(), "Thread Running", runningThread
        time.sleep(.5)
        pass

    if ((confirm == True and dlg.ShowModal() == wx.ID_YES) or (confirm == False)):
        for windowKey in isWindowsOpen:
                if isWindowsOpen[windowKey]:
                        print 'Closing ', windowKey
                        openWindowId[windowKey].Destroy()

        try:
            startTimer(False)
        except: pass
        app.ExitMainLoop()

    dlg.Destroy()

def Login(msg):
    global LOGGEDIN
    if msg.data == -1:
        LOGGEDIN = False;
        print "Logged out ", LOGGEDIN
        loginDialogBox = loginDialog(parent = None)
        loginDialogBox.ShowModal()
    else:
        USERID = msg.data
        LOGGEDIN = True
        print "Logged in ", LOGGEDIN
        sThread(None, 'UPDATE', USERNAME, PASSWORD)
        sThread(None, 'NOTIFICATION', USERNAME, PASSWORD)

    startTimer(LOGGEDIN, 10000)
Publisher().subscribe(Login, "login")

def loadURL(msg):
    return msg.data
Publisher().subscribe(loadURL, "url")

def Notify(msg):
    global NOTIFICATION
    NOTIFICATION = []
    for items in msg.data:
        id = items.get('id')
        date = items.get('date')
        value = items.get('value')
        type = items.get('type')
        NOTIFICATION.append(Notification(id, date, value, type))
    sThread(None, 'URL', url.clearNotification, USERID)
Publisher().subscribe(Notify, "notification")

def Update(msg):
    if msg.topic[0] == 'notes':
        for items in msg.data:
            id = items.get('id')
            group_id = items.get('group_id')
            title = items.get('title')
            content = items.get('content')
            modified_by = items.get('modified_by')
            owner = items.get('owner')
            NOTES.append(Note(id, owner, title, content, group_id, modified_by))
            virtualDatabase.storeNote(NOTES)
            print "Storing Database"
    elif msg.topic[0] == 'allnotes':
        NOTES = []
        for items in msg.data:
            id = items.get('id')
            group_id = items.get('group_id')
            title = items.get('title')
            content = items.get('content')
            modified_by = items.get('modified_by')
            owner = items.get('owner')
            NOTES.append(Note(id, owner, title, content, group_id, modified_by))
            virtualDatabase.rebuildDatabase(NOTES)
            for note in NOTES:
                print note.jsonDump()
    elif msg.topic[0] == 'groups':
        GROUPS = []
        for items in msg.data:
            id = items.get('id')
            group_name = items.get('group_name')
            GROUPS.append(Group(id, group_name))
            virtualDatabase.storeGroup(GROUPS)
        for group in GROUPS:
            print group.jsonDump()
Publisher().subscribe(Update, "allnotes")
Publisher().subscribe(Update, "notes")
Publisher().subscribe(Update, "groups")

def ErrorHandler(msg):
    if msg.data == "LOGIN_ERROR":
        loginDialogBox = loginDialog(parent = None)
        loginDialogBox.ShowModal()
    elif msg.data == "URL_ERROR":
        startTimer(True, 60000)
Publisher().subscribe(ErrorHandler, "error")

def startTimer(option = True, timeOut = 60000):
    global Timer
    try:
        if option and Timer.IsRunning() == False:
            Timer.Start(timeOut)
        elif option == False and Timer.IsRunning() == True:
            Timer.Stop()
    except:
        pass

def getTaskbarPos():
    d_w, d_h = wx.DisplaySize()
    c_x, c_y, c_w, c_h = wx.ClientDisplayRect()

    l = [(c_y, "top"), (d_h - c_y - c_h, "bottom"), (c_x, "left"), (d_w - c_x - c_w, "right")]

    def sorter(a,b):
        if a[0]<b[0] : return 1
        if a[0]>b[0] : return -1
        return 0

    l.sort(sorter)
    return l[0]

def OnTimeOut(evt):
    sThread(None, 'LOGIN', USERNAME, PASSWORD)

    if isWindowsOpen['mainFrame'] == True:
        openWindowId['mainFrame'].populateTree()


#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################
#######################################################

if __name__ == '__main__':
    taskBarIcon = taskBar()

    try:
        loginInfo = open("loginInfo.obj","rb")

        USERNAME = cPickle.load(loginInfo)
        USERID = cPickle.load(loginInfo)
        PASSWORD = cPickle.load(loginInfo)

        loginInfo.close()
        sThread(None, 'LOGIN', USERNAME, PASSWORD)
    except:
        loginDialogBox = loginDialog(parent = None)
        loginDialogBox.ShowModal()

    app.MainLoop()
