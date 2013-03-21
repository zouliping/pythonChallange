import xmlrpclib

server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.Server(server_url)

print server.system.listMethods()
print server.phone('Bert')