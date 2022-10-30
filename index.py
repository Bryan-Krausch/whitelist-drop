import json

# Mettre toute les addresse dans la variable address
whitelistText = open('caller.txt', 'r')
walletAddressText = whitelistText.readlines()

fileName = "whitelist.json"
# jsonString = '[{"handle": "AEU9U8Tq3bcxDAf272zDVMcEkJccuCbLrpPMuxnYasn6", "amount": "2"},'

walletAddress = []

i = 0

while i < len(walletAddressText):
    temp = {
        "handle": walletAddressText[i].replace('\n', ' '),
        "amount": 2  
    }
    print(temp)
    walletAddress.append(temp)
    i = i +1

file = open(fileName, "w")
json.dump(walletAddress, file)
file.close

