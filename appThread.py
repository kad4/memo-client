from globalValues import *

from wx.lib.pubsub import Publisher
from threading import Thread

import wx
import json
import urllib
import cPickle
import url
import contentParser

runningThread = []

APP = wx.PySimpleApp()

SILENT = wx.NewId()

class sThread(Thread):
    def __init__(self, parent, key, *param):
        if (key in runningThread):
            self.key = 'NONE'

        self.PID = key

        Thread.__init__(self)

        self.parent = parent
        self.key = key
        self.param = param

        runningThread.append(self.PID)
        self.start()

    def run(self):
        param = self.param
        parent = self.parent

        if self.key == 'URL':
            URL(parent, *param)
        elif self.key == 'NOTIFICATION':
            Notify(parent, *param)
        elif self.key == 'UPDATE':
            UpdateDatabase(parent, *param)
        elif self.key == 'LOGIN':
            Login(parent, *param)
        else:
            pass
        runningThread.remove(self.PID)


def URL(parent, URL, data = None):
    try:
        if data == None:
            sendData = urllib.urlopen(URL)
        else:
            sendData = urllib.urlopen(URL, data)

        response = sendData.getcode()
        content = sendData.read()

        if response != 200:
            raise
        else:
            if parent != 'sameThread':
                wx.CallAfter(Publisher().sendMessage, "url", content)
            else:
                return content
    except:
        if parent != 'sameThread':
            wx.CallAfter(Publisher().sendMessage, "url", 'URL_ERROR')
        else:
            return 'URL_ERROR'

def Login(parent, username, password, type = None):
    data = urllib.urlencode({'username':username, 'password':password})

    postData = URL (parent = 'sameThread', URL = url.userLogin, data = data)
    URLERROR = False

    if postData == 'URL_ERROR':
        URLERROR = True
        USERID = -1
    else:
        output = json.loads(postData)

        if output['status'] == True:
            USERID = output['userid']

            loginInfo = open("loginInfo.obj","wb")

            for inputData in [username, USERID, password]:
                cPickle.dump(inputData,loginInfo, protocol = cPickle.HIGHEST_PROTOCOL)

            loginInfo.close()
        else:
            USERID = -1

    if parent == 'sameThread':
        return {'userid':USERID, 'error':URLERROR}
    else:
        if URLERROR:
            wx.CallAfter(Publisher().sendMessage, 'error', 'URL_ERROR')
        elif USERID == -1:
            wx.CallAfter(Publisher().sendMessage, 'error', 'LOGIN_ERROR')
        else:
            wx.CallAfter(Publisher().sendMessage, 'login', USERID)

def Notify(parent, username, password):
    LoginResponse = Login('sameThread', username, password)
    if LoginResponse['userid'] == -1:
        if LoginResponse['error'] == False:
            dlg = wx.MessageDialog(None, 'You have been logged out\n\nLog in again', 'Error', wx.OK | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            wx.CallAfter(Publisher().sendMessage, 'error', 'LOGIN_ERROR')
        else:
            wx.CallAfter(Publisher().sendMessage, 'error', 'URL_ERROR')
        return

    data = urllib.urlencode({'userid':LoginResponse['userid']})
    postData = URL('sameThread', url.newChange, data)

    if postData != "URL_ERROR":
        serverResponse = json.loads(postData)

        if serverResponse['update'] != False:
            data = urllib.urlencode({'userid':LoginResponse['userid']})
            postData = URL('sameThread', url.newNotification, data)
            notifications = json.loads(postData)
            wx.CallAfter(Publisher().sendMessage, 'notification', notifications)

def UpdateDatabase(parent, username, password):
    LoginResponse = Login('sameThread', username, password)
    if LoginResponse['userid'] == -1:
        if LoginResponse['error'] == False:
            dlg = wx.MessageDialog(None, 'You have been logged out\n\nLog in again', 'Error', wx.OK | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            wx.CallAfter(Publisher().sendMessage, 'error', 'LOGIN_ERROR')
        else:
            wx.CallAfter(Publisher().sendMessage, 'error', 'URL_ERROR')
        return

    _URL = url.newGroups
    HANDLER = 'groups'
    for i in range(3):
        data = urllib.urlencode({'userid':LoginResponse['userid']})
        postData = URL('sameThread', _URL, data)

        if postData != "URL_ERROR":
            if (i != 1):
                jData = json.loads(postData)
                wx.CallAfter(Publisher().sendMessage, HANDLER, jData)

        if (i==0):
            _URL = url.newNotes
            HANDLER = 'notes'
        elif (i==1):
            _URL = url.allNotes
            HANDLER = 'allnotes'

if __name__ == '__main__':
    temp = sThread(None, 'NOTIFICATION', 'aayush', 'kathmandu')
