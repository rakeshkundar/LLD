from server_interface import ServerInterface


class Server(ServerInterface):
    def create(self):
        print(f"Resource created")

    def insert(self):
        print(f"Resource inserted")

    def update(self):
        print(f"Resource updated")

    def delete(self):
        print(f"Resource deleted")