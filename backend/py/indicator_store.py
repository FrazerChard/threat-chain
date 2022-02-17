import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (Indicator, parse)
#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_ind_pat_val","type":"string"}],"name":"setIndicator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_ind_pat_val","type":"string"}],"name":"getIndicator","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getIndicators","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"indicatorIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')
#Address from Remix once deployed
indicator_address = "0xd9d64b7DC034fAfDbA5DC2902875A67b5d586420"
#Sets an instance of the smart contract
indicator_contract = web3.eth.contract(address=indicator_address, abi=abi)

def indicatorTypes():
    #STIX Open Vocabulary
    indicator_types = {
        "1": "anomalous-activity",
        "2": "anonymization", 
        "3": "benign",
        "4": "compromised", 
        "5": "malicious-activity", 
        "6": "attribution"
    }
    #Retrieve all values from the dictionary
    print("\nindicator types: ")
    for i in indicator_types:
        print(i + ": " + indicator_types[i])
    ind_type_val = input("indicator type 1-7 : ")
    if int(ind_type_val) > 0 and int(ind_type_val) < 8:
        indicator_type = str(indicator_types[ind_type_val])
        return indicator_type
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        indicatorTypes()

def patternTypes():
    print("\npattern types:\n1: file \n2: ipv4 \n3: url")
    observable_type = input("pattern type 1-3: ")
    if observable_type== "1":
        file_pattern = ov.fileHash() #md5: d64fde938f4f9c83df63b9da26c0fc26
        return file_pattern
    elif observable_type =="2":
       file_pattern = ov.ipv4Address() #ipv4: 126.66.69.12
       return file_pattern
    elif observable_type =="3":
       file_pattern = ov.urlAddress() #url: http://
       return file_pattern
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        patternTypes()

def uploadIndicator():
   
    indicatorSTIX = Indicator(
        #type ^ specified in class,  id - random uuid4 appended to type string, created=defined in object when created  spec_version=2.1(v used),, modified=indicator["created"], pattern_version=2.1(v used), valid_from=indicator["created"],        
        name=input("\nindicator name: "),
        description=input("indicator description: "),
        indicator_types=indicatorTypes(),
        pattern=patternTypes(),
        pattern_type="stix" 
    )
    #STIX object
    print(type(indicatorSTIX), "\n\n" , indicatorSTIX)

    #confirmation that STIX Object is valid
    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        indicator = json.loads(str(indicatorSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(indicator)
        print("ipfs content address: ", contentAddr)


        stixID = indicator["id"]
        patVal = (indicator["pattern"][indicator["pattern"].find("= '")+len("= '"):indicator["pattern"].rfind("']")])

        tx_hash = indicator_contract.functions.setIndicator(contentAddr, stixID, patVal).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadIndicator()
    
def retrieveIndicator():  
    query = input("\n\nenter the file hash, url link or ip address:\n")
    get_indicator = indicator_contract.functions.getIndicator(query).call()
    get_content_id = indicator_contract.functions.getContentID(get_indicator).call()
    #print("\n\nindicator ID:", get_indicator)
    #print("content ID:" , get_content_id, "\n")

    retrieved_indicator = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXi = parse(retrieved_indicator)
    print("\n", type(STIXi), "\n", STIXi)
    return STIXi
