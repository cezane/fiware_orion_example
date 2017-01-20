# fiware_orion_example
This is an example of the Orion Context Broker GE in use.

This simple application considers you have the Orion Context Broker (OCB) running locally in your machine or in a VM (also in your machine). It was implemented in Python and it does register of entities at OCB. Also, it is possible to remove the entities from OCB.

TODO: finish the application to query information at OCB.

# FIWARE - How to begin with Orion Context Broker

* Download the Orion VirtualBox image: http://bit.ly/fiware-orion024-vbox 
* Once you have the Orion VirtualBox image, configure it on your VirtualBox and run. 1GB RAM and 8GB HD storage were enough.
* For Network Settings, you can choose NAT. You have to setup the following “Port fowarding” rule in VirtualBox: 
    *Protocol - TCP
    *HOST IP - Your host IP
    *HOST Port -  1026 (default)
    *Guest IP - Your VM IP
    *Guest Port - 1026
* Now, you have a CentOS with Orion installed. Login and user for CentOS are both: fiware.
* Test if you can ping your host machine ip and if you have access to Internet.
* Update the Orion version with the command: sudo yum install contextBroker

