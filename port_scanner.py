import socket
import threading
import logging
from logging.handlers import RotatingFileHandler
import uuid

handler = RotatingFileHandler(
    "audit.log",
    maxBytes=50000,
    backupCount=5
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
session_id = str(uuid.uuid4())[:8]

logger.info("")
logger.info("=" * 60)
logger.info(f"NEW PORT SCAN SESSION | ID={session_id}")
logger.info("=" * 60)

a=input("enter target IP address or hostname:")
b=int(input("enter starting port:"))
c=int(input("enter ending port:"))

logger.info(
    f"Port scan initiated | Target={a} | Range={b}-{c}"
)

open_ports = []
lock = threading.Lock()

try:
    target_ip = socket.gethostbyname(a)
    logger.info(
        f"Target resolved | Host={a} | IP={target_ip}"
    )
except socket.gaierror:
    logger.error(
        f"Unable to resolve target {a}"
    )
    exit()

def scan_Port(target_ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # AF_NET is for IPv4 and SOCK_STREAM for TCP connection
    s.settimeout(1)
    try:
        s.connect((target_ip,port))
        try:
            port_name=socket.getservbyport(port)           
        except:
            port_name="unknown service"           
        with lock:
            open_ports.append(port)

        print(f"Port {port} : {port_name} is open")

    
        logger.info(
            f"Open port detected | Target={a} | Port={port} | Service={port_name}"
        )  

    except Exception as e:
        logger.debug(
            f"Connection failed | Target={a} | Port={port}"
        )
    finally:
        s.close()

try:
    threads=[]
    for i in range(b,c+1):
        t=threading.Thread(target=scan_Port,args=(target_ip,i))
        threads.append(t)
        t.start()
    for k in threads:
        k.join()
except Exception as e:
    logger.error(
        f"Unexpected error during scan: {e}"
    )  

try:
    host_name=socket.gethostbyaddr(a)
    logger.info(
        f"Hostname resolved | Target={a} | Hostname={host_name[0]}"
    )
    #it tells about domain name, any alias name of that host,and the address
    #([domain_name],[alias name],[IP address])
except Exception:
    host_name=["unknown host"]
    logger.warning(
        f"Hostname resolution failed | Target={a}"
    )

logger.info(
    f"Scan completed | Target={a} | OpenPorts= {sorted(open_ports)} | Total={len(open_ports)}"
)
print("PORT SCANNING COMPLETED SUCCESSFULLY !!")       
print(f"Host name of IP address or hostname {a} is '{host_name[0]}'") #it will only print domain name 