import xmlrpc.client

# Connect to the RPC server 
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Taking user input
num = int(input("What's your number = "))

# Call the remote fact func
result = server.factorial(num)

print(f"Factorial of {num} is {result}")

#-----------------------------------------------------------------