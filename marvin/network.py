#Imports
import socket


######################################
# File with functions for networking #
######################################


# Function to get ip of local device on network no 127.0.0.1
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # defining socket
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1)) # connect
        IP = s.getsockname()[0] # get ip
    except: # when no ip found
        IP = '127.0.0.1' # local ip to return if no ip found
    finally: # at end of code
        s.close() # close connection
    return IP # return that was found

def checkConnection(host="8.8.8.8", port=53, timeout=3):
    '''
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port)) # check connection
        return True # connection found
    except Exception as e:
        return False # connection not found