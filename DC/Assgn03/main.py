import random
import threading
import time

# Server class to track the number of active connections
class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0

    def process_request(self, request_id):
        self.active_connections += 1
        print(f"Request {request_id} assigned to {self.name}")
        print(f"{self.name} processing request {request_id} (Active connections: {self.active_connections})")
        time.sleep(random.uniform(1, 3))  # Simulating processing time
        self.active_connections -= 1
        print(f"{self.name} completed request {request_id} (Active connections: {self.active_connections})")

# Load balancer class
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.request_count = 0
        self.lock = threading.Lock()

    def round_robin(self):
        """Assigns requests in a sequential manner to available servers."""
        with self.lock:
            server = self.servers[self.request_count % len(self.servers)]
            self.request_count += 1
        return server

    def least_connections(self):
        """Assigns requests to the server with the least active connections."""
        return min(self.servers, key=lambda s: s.active_connections)

    def random_selection(self):
        """Randomly assigns a request to any server."""
        return random.choice(self.servers)

    def distribute_request(self, request_id, algorithm):
        """Handles request distribution based on the selected algorithm."""
        if algorithm == "round_robin":
            server = self.round_robin()
        elif algorithm == "least_connections":
            server = self.least_connections()
        elif algorithm == "random":
            server = self.random_selection()
        else:
            print("Invalid algorithm selected!")
            return
        
        threading.Thread(target=server.process_request, args=(request_id,)).start()

# Main program
if __name__ == "__main__":
    servers = [Server("Server 1"), Server("Server 2"), Server("Server 3")]
    load_balancer = LoadBalancer(servers)

    print("\nChoose Load Balancing Algorithm:")
    print("1. Round Robin")
    print("2. Least Connections")
    print("3. Random Selection")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        algorithm = "round_robin"
    elif choice == "2":
        algorithm = "least_connections"
    elif choice == "3":
        algorithm = "random"
    else:
        print("Invalid choice! Defaulting to Round Robin.")
        algorithm = "round_robin"

    # Simulating multiple client requests
    for request_id in range(1, 5):
        load_balancer.distribute_request(request_id, algorithm)
        time.sleep(0.5)  # Delay between requests for better simulation
