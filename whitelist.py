#Run in "playerdata" folder

from os import listdir
import requests
import json

whiteListJson = []

x = listdir()

for i in x:
	if i.endswith(".dat"):
		#creating a blank set
		whiteListEntry = {"uuid":"", "name":""}
		#creating UUID string without the .dat extension
		usrUUID = i[:-4]
		
		#adding player UUID to entry
		whiteListEntry["uuid"] = usrUUID
		
		#taking the dashes out of the UUID to work with the API
		trimmedUUID = usrUUID.replace("-", "")
		
		#getting API response
		response = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/" + trimmedUUID).json()
		
		#adding player's current username to entry
		whiteListEntry["name"] = response["name"]
		
		#adding entry to master JSON file
		whiteListJson.append(whiteListEntry)

#creating a whitelist.json file
f = open("whitelist.json", 'w')
#converting master json to pretty print and then writing it to the file
f.write(json.dumps(whiteListJson, indent = 2, sort_keys=True))
#closing file
f.close()
