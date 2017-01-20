import requests
import json
from fiware_auth import get_credentials
#import matplotlib.pyplot as plt

CB_HOST = "127.0.0.1"  #change to this ip "192.168.56.101" if you are using the context broker configured at VM
CB_PORT = "1026"
IDMPEP_URL = "http://idm"  #"http://" + CB_HOST+ ":" + CB_PORT
POST_URL = IDMPEP_URL + "/v2/entities"
HEADERS = {'content-type': 'application/json','accept': 'application/json'} #NOT NOW 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}


# fiware version - just for test
def fiware_version():
    r = requests.get(CB_URL/version)
    print r.text

# test
def test_version():
    fiware_version()


# register entities
def register_entities():
    print "WELCOME TO FIWARE WORLD! LET'S TEST THE ORION CONTEXT BROKER GENERIC ENABLER!\n"
    print "Let's register some entities...\n"
    token = get_credentials()
    n_entities = input("Enter the number of entities you want to register: ")
    
    for e in range(0, n_entities):
       print "######################################################"
       entity_id = raw_input("Enter the ID of the entity %d: " % (e+1))
       entity_type = raw_input("Enter the type of the entity %d: " % (e+1))
       n_attrs = input("Enter the number of attributes this entity has: ")

       PAYLOAD = '{ \
              "id": "'+entity_id+'", \
              "type": "'+entity_type+'", '\
               
       print "------------------------------------------------------------"       
       for a in range(0, n_attrs):
           attr_name = raw_input("Enter the name of the attribute %d: " % (a+1))
           attr_type = raw_input("Enter the type of the attribute %d: " % (a+1))
           attr_value = raw_input("Enter the value of the attribute %d: " % (a+1))
           #TODO: add metadata handling...

           PAYLOAD += '"'+attr_name+'": {  \
                          "type": "'+attr_type+'", \
                          "value": "'+attr_value+'"' \
                      + ('}, ' if (a != n_attrs-1) else '}  }')


       print "------------------------------------------------------------"
    
       print json.dumps(json.loads(PAYLOAD), indent=4)
       print "This entity is being registered..."
       try:
          HEADERS.update({'X-Auth-Token': token})
          print HEADERS
          r = requests.post(POST_URL, data=PAYLOAD, headers=HEADERS)
          if r.status_code in (200, 201):
             print "The status of this operation is: " + str(r.status_code) + " OK! Successful register!" 
          else:
             print " Some error occurred! Status: " + str(r.status_code)
             print r.text
       except requests.exceptions.RequestException as e:
          print e
          sys.exit(1)



if __name__ == "__main__":
    #test_version()
    register_entities()
