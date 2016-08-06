from wx.lib.pubsub import Publisher
from threading import Thread

from contentParser import *

import wx

APP = wx.PySimpleApp()


class sThread(Thread):
    def __init__(self, a,b):
        Thread.__init__(self)
        self.a = a
        self.b = b

        self.start()

    def run(self):
        for i in range(5):
            self.a += 2
            self.b -= 1
            wx.CallAfter(Publisher().sendMessage, 'HANDLER', {'result':self.a+self.b})
            wx.CallAfter(Publisher().sendMessage, 'CHANDLER', {'result':self.a-self.b})

def hellNo (msg):
	print msg.topic[0], msg.data
Publisher().subscribe(hellNo, 'HANDLER')
Publisher().subscribe(hellNo, 'CHANDLER')

if __name__ == '__main__':
    dbNOTES = [Note(1,2,3,4,5,6),Note(1,2,3,4,5,6),Note(1,2,3,4,5,6),Note(1,2,3,4,5,6),Note(1,2,3,4,5,6),Note(1,2,3,4,5,6),Note(1,2,3,4,5,6)]
    tempList = []
    for NOTE in dbNOTES:
        tempList.append((NOTE.ID,NOTE.OWNER,NOTE.TITLE,NOTE.CONTENT,NOTE.GROUP_ID,NOTE.MODIFIED_BY))

    noteTuple = tuple(tempList)
    print noteTuple