#!/usr/bin/env python
import pwd, spwd, ldap

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

def ldapAuthQuery(name):
	basedn = 'ou=people, dc=example, dc=com'
	searchfilter = 'uid={}'.format(name)
	attributes = ['accountStatus','uid','uidNumber','gidNumber','cn','homeDirectory','loginShell']
	conn = ldap.initialize('ldap://ldap.example.com')
	conn.protocol_version = 3
	try:
		connection = conn.simple_bind_s()
	except ldap.INVALID_CREDENTIALS:
		return "Invalid Credentials"
	except ldap.SERVER_DOWN:
		return "Server Down"
	query_result = conn.search_s(basedn, ldap.SCOPE_SUBTREE, searchfilter, attributes)
	ldap_result = [entry for dn,entry in query_result if isinstance(entry,dict)]
	return ldap_result
