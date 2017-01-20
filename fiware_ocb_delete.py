import requests
from requests import Request, Session
import json, sys
from fiware_auth import get_credentials

CB_HOST = "127.0.0.1"  #change to this ip "192.168.56.101" if you are using the context broker configured at VM as "Host Only Adapter"
CB_PORT = "1026"
CB_URL = "http://" + CB_HOST+ ":" + CB_PORT
IDMPEP_URL = "http://idm"
DELETE_URL = IDMPEP_URL + "/v2/entities/"
#HEADERS = {'content-type': 'application/json','accept': 'application/json'} #NOT NOW 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}

# register entities
def delete_entities():
    print "WELCOME TO FIWARE WORLD! LET'S REMOVE SOME ENTITIES FROM THE ORION CONTEXT BROKER!\n"
    print "Removing some entities...\n"
    token = get_credentials()
    headers = {'X-Auth-Token': token}
    n_entities = input("Enter the number of entities you want to remove: ")

    for e in range(0, n_entities):
       print "######################################################"
       entity_id = raw_input("Enter the ID of the entity %d: " % (e+1))
       print "------------------------------------------------------------"
       try:
          print "This entity is being removed..."
          s = Session()
          r = requests.delete(DELETE_URL + entity_id, headers=headers)
          #request = Request('DELETE', "http://orion:1026/v2/entities/" + entity_id)#, headers=headers)
          #prepped = request.prepare()
          #del prepped.headers['Content-Length']
          #r = s.send(prepped)

          print "The status of this operation is: " + str(r.status_code) + (" OK! Successful operation!"
            if r.status_code==204 or r.status_code==201 or r.status_code==200 else " Some error occurred!")
          print r.text
          print "------------------------------------------------------------"
       except requests.exceptions.RequestException as e:
          print e
          sys.exit(1)


if __name__ == "__main__":
    #test_version()
    delete_entities()


 
