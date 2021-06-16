#import dat shiyt
import http.client, json, threading, ssl
import time
print(f"""
░██████╗███╗░░░███╗░█████╗░██████╗░████████╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝████╗░████║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚█████╗░██╔████╔██║███████║██████╔╝░░░██║░░░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚═══██╗██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
#love letter
print('Made by a hippo')
print('For the coolest macho kid there is <3')
#inputs
name = input('Name: ')
bearer = input('Bearer: ')

def runRequest():
    headers = {"Accept": "application/json", "Authorization": "Bearer " + bearer}
    #jsn     = {"profileName": name}
    #jsn     = json.dumps(jsn)
    conn    = http.client.HTTPSConnection("api.minecraftservices.com")
    conn.request("GET", "/")
    conn.getresponse().read()
    conn.request("PUT", "/minecraft/profile/name/" + name, None, headers)
    response = conn.getresponse()
    print("Got answer at", time.time(), "with response", response.status)
    #print(response.status, response.reason)
    #print(response.read().decode())
    if response.status == 429:
        print('Uh oh, a 429! Waiting 40 extra seconds!!!!')
        time.sleep(40)

print('runRequest defined! Starting requests on ' + name + '. Keep in mind, you might not get it!')

def work():
    runRequest()
    time.sleep(31)
while(True):
    work()
