import requests, json
import sys, getpass, base64
 
IDMPEP_URL = "http://idm"
GET_URL = IDMPEP_URL + "/v2/entities"
HEADERS = {'content-type': 'application/json','accept': 'application/json'} #NOT NOW 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
#CLIENT_ID="629cd23fe9bb42c58d3fde77e0323a7e"
#CLIENT_SECRET="4169a39bc95d47f2b19019ab587e0fe2"

#NUM_ARG=len(sys.argv)

def get_credentials():
    user = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    client_id = "629cd23fe9bb42c58d3fde77e0323a7e" #raw_input("Client ID: ")
    client_secret = "4169a39bc95d47f2b19019ab587e0fe2" #raw_input("Client Secret : ")
    auth_header = base64.b64encode(client_id + ":" + client_secret)

    payload = ('grant_type=password&username=%s&password=%s&client_id=%s&client_secret=%s' %
               (user, password, client_id, client_secret))
    headers =  {'Content-Type': 'application/x-www-form-urlencoded', 
                'Authorization': 'Basic %s' % auth_header}
    url = "http://idm:8000/oauth2/token"

    resp = requests.post(url, data=payload, headers=headers) #TODO Handle error...
    #print resp.text
    if resp.status_code in (200, 201):
       token = resp.json()["access_token"]
       token_expiration = resp.json()["expires_in"]     
       print "\nFIWARE Oauth2.0 Token: "+token
       print "Token expires: "+str(token_expiration)
       return token
    else:
       print "Credentials not valid! - " + resp.json()["error"]["message"]
       return "0"

def get_user_info(token):
    print "\nTesting authentication... Getting user info..."
    try:
       user_info = requests.get("http://idm:8000/user?access_token=%s" % token)
       if user_info.status_code in (200, 201):
          print "The user has id '" + user_info.json()["id"] + "' and email '" + user_info.json()["email"] 
       else:
          print "Something is wrong! - " + user_info.text
    except requests.exceptions.RequestException as e:
       print e
       sys.exit(1)    

def get_orion_entities(token):
    print "\nGetting Orion registered entities..."
    try:
       orion = requests.get(GET_URL,headers={'X-Auth-Token': token}) 
       if orion.status_code in (200, 201):
          entities = json.loads(orion.text)
          print entities
          for entity in entities:
              print entity['id']
       else:
          print "Something is wrong! - " + orion.text

    except requests.exceptions.RequestException as e:
       print e 
       sys.exit(1)

if __name__ == "__main__":
    token = get_credentials()
    if token != 0:
       get_user_info(token)
       get_orion_entities(token)

