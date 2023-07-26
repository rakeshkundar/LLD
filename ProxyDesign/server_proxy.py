from server_interface import ServerInterface
from server import Server

class ServerProxy(ServerInterface):

    server: Server

    def __init__(self, server: Server) -> None:
        self.server = server

    def create(self, client, resource):
        if(client != 'ADMIN'):
            raise Exception('Access Denied')

        self.server.create()

    def insert(self, client, resource):
        if(client != 'ADMIN'):
            raise Exception('Access Denied')

        self.server.insert()

    def update(self, client, resource):
        if(client != 'ADMIN'):
            raise Exception('Access Denied')

        self.server.update()
    
    def delete(self, client, resource):
        if(client != 'ADMIN'):
            raise Exception('Access Denied')

        self.server.delete()