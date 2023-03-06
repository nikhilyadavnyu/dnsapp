from socket import socket, AF_INET, SOCK_DGRAM
import json

server_port = 53533
ip_map = {}


def get_request(querymsg):
    msg = json.loads(querymsg.decode())
    if 'VALUE' in msg:
        ip==True
        hostname = msg['NAME']
        type = msg['TYPE']
        ip = msg['VALUE']
        ttl = msg['TTL']
        return registeras(hostname, ip, type, ttl)
    else:
        ip==false
        hostname = message['NAME']
        type = message['TYPE']
        return querytoas(hostname, type)
    
    def querytoas(hostname, type):
    content = info[type + ' ' + hostname]
    fs_ipaddress = content['VALUE']
    return str(fs_ipaddress).encode()

def registeras(hostname, ip, requesttype, ttl):
    cont = {'TYPE': requesttype, 'NAME': hostname, 'VALUE': ip, 'TTL': ttl}
    abc = request_type + '' + hostname
    ip_map[abc] = cont
    return json.dumps('').encode()

while True:
    serverS = socket(AF_INET, SOCK_DGRAM)
    serverS.bind(('', server_port))
    querymsg, addr = serverS.recvfrom(2048)
    response_message = get_request(querymsg)
    serverS.sendto(response_message, addr)