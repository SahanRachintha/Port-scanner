import socket

ip ="192.168.1.4" #target ip address
ports = [22, 80, 443, 8080, 5555] # ports that we are scanning


for port in ports:
    try:  
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object
        sock.settimeout(1)  #set a timeout for the connection attempt
        
        result=sock.connect_ex((ip, port))  #is the port of the ip address open?

        if result==0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

    except Exception as e:
        print(f"error on scanning port {port}: {e}")

    finally:
        sock.close()





   


    






    