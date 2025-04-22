import Pyro4

class StringConcatenator:
    @Pyro4.expose
    def concatenate(self, str1, str2):
        return str1 + str2

def start_server():
    concatenator = StringConcatenator()
    daemon = Pyro4.Daemon()
    uri = daemon.register(concatenator)
    print("Server URI:", uri)
    print("Server is ready. Waiting for requests...")
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()