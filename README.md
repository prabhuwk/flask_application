# flask_application

Flask is a microframework for Python based on Werkzeug, Jinja 2.
- built in development server and debugger
- RESTful request dispatching
- uses Jinja2 templating
- support for secure cookies (client side sessions) 
- 100% WSGI 1.0 compliant 

Application is installed with flask extensions and sqlalchemy for ORM.

It basically helps teams to login using ldap authentication and perform basic userid checks which includes 
- Active Users
- Disabled Password
- Re-Hire Account
- Non-Existent Users

It also connects to openldap to fetch userid information. 
