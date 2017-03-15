



import xmlrpclib
server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
eg_obj = server.phone("Bert")

print eg_obj