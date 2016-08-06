import urllib
import json
import url

'''
	def parseUsers(URL = url.allUsers):
		USER = []
		try:
			contents = download(URL)
		except:
			return None
		for items in contents:
			ID = (items.get('id'))
			USERNAME = (items.get('username'))
			PASSWORD = (items.get('password'))
			PASSWORD = (items.get('password'))
			FIRSTNAME = (items.get('firstname'))
			LASTNAME = (items.get('lastname'))
			EMAIL = (items.get('email'))
			UPDATED_AT = (items.get('updated_at'))
			CREATED_AT = (items.get('created_at'))
			POST_ADDED = (items.get('post_added'))
			POST_EDITED = (items.get('post_edited'))
			POST_DELETED = (items.get('post_deleted'))
			tempUser = User (ID, USERNAME, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, UPDATED_AT, CREATED_AT, POST_ADDED, POST_EDITED, POST_DELETED)
			USER.append(tempUser)
		return USER

	def parseNotes(URL = url.allNotes):
		NOTE = []
		try:
			contents = download(URL)
		except:
			return None
		for items in contents:
			ID = (items.get('id'))
			OWNER = (items.get('owner'))
			TITLE = (items.get('title'))
			CONTENT = (items.get('content'))
			GROUP_ID = (items.get('group_id'))
			CREATED = (items.get('created_at'))
			UPDATED = (items.get('updated_at'))
			MODIFIED_BY = (items.get('modified_by'))
			tempNote = Note (ID, OWNER, TITLE, CONTENT, GROUP_ID, CREATED, UPDATED, MODIFIED_BY)
			NOTE.append(tempNote)
		return NOTE

	def parseGroups(URL = url.allGroups):
		GROUP = []
		try:
			contents = download(URL)
		except:
			return None
		for items in contents:
			ID = (items.get('id'))
			GROUP_NAME = (items.get('group_name'))
			USERS = (items.get('users'))
			ADMIN_USERS = (items.get('admin_users'))
			tempGroup = Group (ID, GROUP_NAME, USERS, ADMIN_USERS)
			GROUP.append(tempGroup)
		return GROUP

	class Note():
		def __init__(self, ID, OWNER, TITLE, CONTENT, GROUP_ID, CREATED, UPDATED, MODIFIED_BY):
			self.ID = ID
			self.OWNER = OWNER
			self.TITLE = TITLE
			self.CONTENT = CONTENT
			self.GROUP_ID = GROUP_ID
			self.CREATED = CREATED
			self.UPDATED = UPDATED
			self.MODIFIED_BY = MODIFIED_BY

		def jsonDump(self):
			jsonEntry = {u'modified_by': self.MODIFIED_BY, u'title': self.TITLE, u'content': self.CONTENT, u'updated_at': self.UPDATED, u'created_at': self.CREATED, u'owner': self.OWNER, u'group_id': self.GROUP_ID}
			return jsonEntry

	class User():
		def __init__(self, ID, USERNAME, FIRSTNAME, LASTNAME, PASSWORD, EMAIL, UPDATED_AT, CREATED_AT, POST_ADDED, POST_EDITED, POST_DELETED):
			self.ID = ID
			self.USERNAME = USERNAME
			self.FIRSTNAME = FIRSTNAME
			self.LASTNAME = LASTNAME
			self.PASSWORD = PASSWORD
			self.EMAIL = EMAIL
			self.UPDATED_AT = UPDATED_AT
			self.CREATED_AT = CREATED_AT
			self.POST_ADDED = POST_ADDED
			self.POST_EDITED = POST_EDITED
			self.POST_DELETED = POST_DELETED


		def jsonDump(self):
			jsonEntry = {u'id':self.ID, u'username':self.USERNAME, u'firstname':self.FIRSTNAME, u'lastname':self.LASTNAME, u'password':self.PASSWORD, u'email':self.EMAIL, u'updated_at':self.UPDATED_AT, u'created_at':self.CREATED_AT, u'post_added':self.POST_ADDED, u'post_edited':self.POST_EDITED, u'post_deleted':self.POST_DELETED}
			return jsonEntry

	class Group():
		def __init__(self, ID, GROUP_NAME, USERS, ADMIN_USERS):
			self.ID = ID
			self.GROUP_NAME = GROUP_NAME
			self.USERS = USERS
			self.ADMIN_USERS = ADMIN_USERS

		def jsonDump(self):
			jsonEntry = {u'id':self.ID, u'group_name':self.GROUP_NAME, u'users':self.USERS, u'admin_users':self.ADMIN_USERS}
			return jsonEntry


	def parseNotes(Notes):
		NOTE = []
		for items in Notes:
			ID = (items.get('id'))
			OWNER = (items.get('owner'))
			TITLE = (items.get('title'))
			CONTENT = (items.get('content'))
			GROUP_ID = (items.get('group_id'))
			MODIFIED_BY = (items.get('modified_by'))
			tempNote = Note (ID, OWNER, TITLE, CONTENT, GROUP_ID, MODIFIED_BY)
			NOTE.append(tempNote)
		return NOTE

	def parseGroups(Groups):
		GROUP = []
		for items in groups:
			ID = (items.get('id'))
			GROUP_NAME = (items.get('group_name'))
			tempGroup = Group (ID, GROUP_NAME)
			GROUP.append(tempGroup)
		return GROUP
'''
###############################################

class Note():
	def __init__(self, ID, OWNER, TITLE, CONTENT, GROUP_ID, MODIFIED_BY):
		self.ID = ID
		self.OWNER = OWNER
		self.TITLE = TITLE
		self.CONTENT = CONTENT
		self.GROUP_ID = GROUP_ID
		self.MODIFIED_BY = MODIFIED_BY

	def jsonDump(self):
		jsonEntry = {u'id': self.ID, u'title': self.TITLE, u'content': self.CONTENT, u'group_id': self.GROUP_ID, u'owner':self.OWNER}
		return jsonEntry

class Group():
	def __init__(self, ID, GROUP_NAME):
		self.ID = ID
		self.GROUP_NAME = GROUP_NAME

	def jsonDump(self):
		jsonEntry = {u'id':self.ID, u'group_name':self.GROUP_NAME}
		return jsonEntry

class Notification():
	def __init__(self, ID, DATE, VALUE, TYPE):
		self.ID = ID
		self.DATE = DATE
		self.VALUE = VALUE
		self.TYPE = TYPE

	# def jsonDump(self):
	# 	jsonEntry = {u'id':self.ID, u'date':self.DATE, u'value':self.}
	# 	return jsonEntry


###############################################

def getNote(NOTES, ID):
	for NOTE in NOTES:
		if ID == NOTE.ID: return NOTE
	return None

def getGroup(GROUPS, ID):
	for GROUP in GROUPS:
		if ID == GROUP.ID: return GROUP
	return None

