"""Assignment No : 01  | Sub: CL - I (DC)  |  Name: Kanaka Amin  | Roll No: 42501 """
# Server.py 
import xmlrpc.server
import xmlrpc.client
print('XLM-RPC module is available!')  # Checkign if RPC module of Python is present!

from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial 
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)

# Creating a RPC Server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000... ")

# Register the factorial func
server.register_function( factorial , "factorial")
server.serve_forever()

#-----------------------------------------------------------------