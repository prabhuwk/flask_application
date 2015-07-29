#!/usr/bin/env python
import pwd, spwd

def localUserCheck(name):
	useriddetails = []
	useriddetails.append(name)
	try:
		foundId = pwd.getpwnam(name)[0]
		useriddetails.append(foundId)
		passwdfield = spwd.getspnam(name)[1]
		if passwdfield == 'DISABLED':
			useriddetails.append(passwdfield)
		else:
			useriddetails.append('None')
	except KeyError:
		pass
	try:
		xusername = 'X' + name
		xuserid = pwd.getpwnam(xusername)[0]
		if xuserid:
			useriddetails.append(xuserid)
		else:
			useriddetails.append('None')
	except KeyError:
		pass
	return useriddetails
