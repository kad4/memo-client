import cPickle
from contentParser import *

def readDB(key = 'NOTE'):
    Note = []
    Group = []

    f = open('memokad055.dmp', 'rb')


    try:
        Note = cPickle.load(f)
        Group = cPickle.load(f)
    except:
        pass

    f.close()

    if key == 'NOTE':
        return Note
    elif key == 'GROUP':
        return Group
    else:
        return []

def writeDB(LIST, key = 'NOTE'):
    Note = []
    Group = []

    f = open('memokad055.dmp', 'rb')

    try:
        Note = cPickle.load(f)
        Group = cPickle.load(f)
    except:
        pass

    if key == 'NOTE':
        Note = LIST
    elif key == 'GROUP':
        Group = LIST

    f.close()
    f = open('memokad055.dmp', 'wb')
    for item in [Note, Group]:
        cPickle.dump(item,f, protocol = cPickle.HIGHEST_PROTOCOL)
    f.close()

def rebuildDatabase(NOTES):
    deleteNotes(readDB('NOTE'))

    writeDB(NOTES, 'NOTE')


def storeNote(NOTES):
    dbNOTES = readDB('NOTE')

    for note in dbNOTES:
        for newNote in NOTES:
            if note.ID == newNote.ID:
                note = newNote
                NOTES.remove(newNote)

    dbNOTES.extend(NOTES)

    writeDB(NOTES, 'NOTE')

def storeGroup(GROUPS):
    writeDB(GROUPS, 'GROUP')

def deleteNotes(NOTES):
    dbNOTES = readDB('GROUP')

    for note in dbNOTES:
        for NoteID in NOTES:
            if note.ID == NoteID:
                dbNOTES.remove(note)

    writeDB(NOTES, 'NOTE')

def createDatabase():
    f = open('memokad055.dmp', 'wb')
    f.close()

def createFakeDatabase():
    f = open('memokad055.dmp', 'wb')
    Notes = []
    for i in range(5):
        Notes.append(Note(i, 11, 'Title '+str(i), 'Content'+str(i),0,11))
    writeDB(Notes)
    f.close()

if __name__ == '__main__':
    createDatabase()