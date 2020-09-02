#!/bin/bash

echo "Spotify controller installation. We aware of having graphic interface avaliable (use option -X if you are using ssh connection with the server)"

pip3 install -r req.txt

source ./env.sh   

rm ./src/.json

touch src/tokens.json

python ./src/config.py&

firefox "https://accounts.spotify.com/authorize?client_id=$CLIENT_ID&response_type=$RESPONSE_TYPE&redirect_uri=$REDIRECT_URI&scope=user-read-private%20user-read-email&state=34fFs29kd09"

echo "Give spotify credentials to the firefox already opened"

python src/authII.py
killall python

