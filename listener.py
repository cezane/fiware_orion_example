import socket, json

HOST = "10.30.0.21"      # Endereco IP do Servidor
PORT = 1028            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
i = e_consumption = acc_consumption = noise = temperature = 0

print("Listening on %s:%s..." % (HOST, str(PORT)))

while True:
      con, client = tcp.accept()
      print 'Connected by', client
      while True:
           i += 1
           msg = con.recv(1024)
           if not msg: break
           print '\n\n==', msg, '=='

           json_msg = json.loads(msg[msg.index('{'):])
           e_consumption = json_msg['data'][0]['energy_consumption']['value']
           noise = json_msg['data'][0]['noise']['value']
           temperature = json_msg['data'][0]['temperature']['value']
           print '\nThe energy consumption was updated to: %s.' % e_consumption
           print '\nThe noise is %sdB and the temperature is %s Celsius.' % (noise, temperature)
           acc_consumption += e_consumption
           print 'The accumulated consumption is %s.' % acc_consumption
      print 'Closing connection with server...', client
      con.close()
