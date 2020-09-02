import json
import sys
import requests
import time
import base64
from datetime import datetime

if __name__ == '__main__':
    code = ""
    client = ""
    secret = ""
    #Carrego els tokens 
    with open("./env.sh", 'r') as fd:
        for line in fd.readlines():
            if 'ID' in line:
                client = line.split('=')[1].replace('\n','')
                print("client: " + client)
            if 'SECRET' in line:
                secret = line.split('=')[1].replace('\n','')
                print("secret: " + secret)
        fd.close()

    while True:
        fd = open("src/tokens.json", 'r')
        if (fd.read()!=""):                     #Si el JSON es buit = no hi ha token i cal esperar
            fd.seek(0,0)  #Poso fd a l'inici del fitxer
            tokens = json.load(fd)
            code = tokens["auth_code"]
            fd.close()
            break
        fd.close()
        time.sleep(2)
    #Aqui acaba el primer pas de l'autenticació i comença el segon
    auth = "Basic " + str( base64.b64encode((client + ':' + secret).encode("utf-8")), "utf-8")
    print(auth)
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization":auth }
    data = {"grant_type":"authorization_code", "code":code, "redirect_uri":"http://127.0.0.1:5000/retrieve"}
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    if r.status_code != 200:
        print("API error " + str(r.status_code) + " " + r.reason)
        print(r.text)
        sys.exit(0)
    json = r.json()
    print(json)
    tokens["access_token"] = json["access_token"]
    tokens["token_type"] = json["token_type"]
    tokens["scope"] = json["scope"]
    tokens["expiration_date"] = time.mktime(datetime.today().timetuple()) + json["expires_in"] # Els segons epoch en els que expirarà el codi
    tokens["refresh_token"] = json["refresh_token"]

    with open("src/tokens.json", 'w') as f:
        json.dump(tokens,f)
        f.close()
    print("Token will expire in " + json["expires_in"] + " seconds") 
    
