import requests
import json

CB_HOST = "127.0.0.1"  #change to this ip "192.168.56.101" if you are using the context broker configured at VM as "Host Only Adapter"
CB_PORT = "1026"
CB_URL = "http://" + CB_HOST+ ":" + CB_PORT
DELETE_URL = CB_URL + "/v2/entities"
#HEADERS = {'content-type': 'application/json','accept': 'application/json'} #NOT NOW 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}

# register entities
def delete_entities():
    print "WELCOME TO FIWARE WORLD! LET'S REMOVE SOME ENTITIES FROM THE ORION CONTEXT BROKER!\n"
    print "Removing some entities...\n"
    n_entities = input("Enter the number of entities you want to remove: ")

    for e in range(0, n_entities):
       print "######################################################"
       ENTITY_ID = raw_input("Enter the ID of the entity %d: " % (e+1))
       print "------------------------------------------------------------"

       print "This entity is being removed..."
       r = requests.delete(DELETE_URL + "/" + ENTITY_ID)

       print "The status of this operation is: " + str(r.status_code) + (" OK! Successful register!"
            if r.status_code==204 or r.status_code==201 or r.status_code==200 else " Some error occurred!")
       print r.text
       print "------------------------------------------------------------"



if __name__ == "__main__":
    #test_version()
    delete_entities()


 
