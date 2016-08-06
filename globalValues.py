import wx

app = wx.PySimpleApp()

isWindowsOpen = {'mainFrame' : False, 'notificationFrame' : False,
                 'loginDialog' : False, 'taskBar' : False}

openWindowId = {'mainFrame' : None, 'notificationFrame' : None,
                'loginDialog' : None, 'taskBar' : None}

USERID = -1
USERNAME = ''
PASSWORD = ''

LOGGEDIN = False

Timer = wx.Timer()

NOTIFICATION = []
GROUPS = []
NOTES = []
