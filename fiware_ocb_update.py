import requests
import json

CB_HOST = "127.0.0.1"  #change to this ip "192.168.56.101" if you are using the context broker configured at VM
CB_PORT = "1026"
CB_URL = "http://" + CB_HOST+ ":" + CB_PORT
POST_URL = CB_URL + "/v2/entities"
HEADERS = {'content-type': 'application/json'} #,'accept': 'application/json'}  #NOT NOW 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}

# register entities
def update_entities():
    print "WELCOME TO FIWARE WORLD! LET'S TEST THE ORION CONTEXT BROKER GENERIC ENABLER."
    print "Let's update some entities...\n"
    n_entities = input("Enter the number of entities you want to update: ")

    for e in range(0, n_entities):
       print "######################################################"
       ENTITY_ID = raw_input("Enter the ID of the entity %d: " % (e+1))
       n_attrs = input("Enter the number of attributes you want to update for this entity: ")

       PAYLOAD = "{"
       print "------------------------------------------------------------"
       for a in range(0, n_attrs):
           ATTR_NAME = raw_input("Enter the name of the attribute %d: " % (a+1))
           ATTR_VALUE = raw_input("Enter the value of the attribute %d: " % (a+1))

           PAYLOAD += '"'+ATTR_NAME+'": {"value": '+ATTR_VALUE+ \
                      ('}, ' if (a != n_attrs-1) else '}  }')


       print "------------------------------------------------------------"
       print json.dumps(json.loads(PAYLOAD), indent=4)
       print "This entity is being updated..."
       r = requests.post(POST_URL+"/"+ENTITY_ID+"/attrs", data=PAYLOAD, headers=HEADERS)
       
       print "The status of this operation is: " + str(r.status_code) + (" OK! Successful update!"
       if r.status_code==201 or r.status_code==200 or r.status_code==204 else " Some error occurred!")
       print r.text



if __name__ == "__main__":
    #test_version()
    update_entities()

