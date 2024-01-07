from server_proxy import ServerProxy
from server_interface import ServerInterface
from server import Server


if __name__ == '__main__':
    try:
        server_interface: ServerInterface = ServerProxy(Server())

        server_interface.create('ADMIN', 'Dummy resource')
        server_interface.insert('ADMIN', 'Dummy resource')
        server_interface.create('USER', 'Dummy resource')

    except Exception as e:
        print(f"Exception is : {e}")