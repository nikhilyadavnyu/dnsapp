from flask import Flask,request
from socket import *
import json
app = Flask(_name_)


@app.route('/fibonacciserver', methods = ['GET'])
def fibonacciserver():
    num = request.args.get['number']
    Fibonacci_result = cal_fibonacciserver_number(num)
    return str(Fibonacci_result)

def cal_fibonacciserver_number(number):
   if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return f(number - 1) + f(number - 2)

@app.route('/register', methods = ["PUT"])
def register():
    cont = request.get_json()
    fibonacci = cont.get('hostname')
    ip_add = cont.get('ip')
    as_ip = cont.get('as_ip')
    as_port = int(cont.get('as_port'))
    register_json = {'TYPE': 'A',
                     'NAME': fibonacci, 
                     'VALUE': ip_add, 
                     'TTL': 10}

    clients = socket(AF_INET, SOCK_DGRAM)

    clients.sendto(json.dumps(register_json).encode(),(as_ip, as_port))
    responsemessage, serveraddress = client_s.recvfrom(2048)
    return 'successfully registered', status.HTTP_201_CREATED
    
app.run(host='0.0.0.0', port = 9090,debug=True)