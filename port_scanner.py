import socket
import threading

a=input("enter target IP address or hostname:")
b=int(input("enter starting port:"))
c=int(input("enter ending port:"))

def scan_Port(a,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # AF_NET is for IPv4 and SOCK_STREAM for TCP connection
    s.settimeout(1)
    try:
        s.connect((a,port))
        try:
            port_name=socket.getservbyport(port)           
        except:
            port_name="unknown service"           
        print(f"Port {port} : {port_name} is open")    
    except:
        pass
    finally:
        s.close()

try:
    threads=[]
    for i in range(b,c+1):
        t=threading.Thread(target=scan_Port,args=(a,i))
        threads.append(t)
        t.start()
    for k in threads:
        k.join()
except:
    pass   

try:
    host_name=socket.gethostbyaddr(a)
    #it tells about domain name, any alias name of that host,and the address
    #([domain_name],[alias name],[IP address])
except:
    host_name="unknown host"     
print("PORT SCANNING COMPLETED SUCCESSFULLY !!")       
print(f"Host name of IP address or hostname {a} is '{host_name[0]}'") #it will only print domain name 
