import requests, socket
from flask import *
import json
from socket import *

app = Flask(__name__)

@app.route('/fibonacciserver', methods = ['GET'])
logging.getLogger().setLevel(logging.DEBUG)

def acceptrequest():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = int(request.args.get('as_port'))

    if hostname == '' or fs_port == '' or as_ip == '' or as_port == '' or number == ''):
        return 'bad format', status.HTTP_400_BAD_REQUEST

    fs_ip = query_as(as_ip, as_port, hostname)
    fs_address = fs_ip + '=fibonacci.com&fs_port=' + fs_port
    
    result = requests.get('/fibonacci?' +fs_address + 'number'+number+'&as_ip='+as_ip+'asport='+as_port)
    return result.text, status.HTTP_200_OK

def query_as(as_ip, as_port, hostname):
    clients = socket(AF_INET, SOCK_DGRAM)
    queryjson = {'TYPE': 'A', 'NAME': hostname}
    clients.sendto(json.dumps(queryjson).encode(), (as_ip, as_port))
    ip_add, server_add = client_socket.recvfrom(2048)
    return ip_add.decode()

app.run(host = '0.0.0.0', port = '8080', debug = True)
