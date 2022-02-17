import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (Infrastructure, parse)

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_infra_name","type":"string"}],"name":"getInfrastructure","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getInfrastructures","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"infrastructureIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_infra_name","type":"string"}],"name":"setInfrastructure","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#Address from Remix once deployed
infrastructure_address = "0x8a5E2a6343108bABEd07899510fb42297938D41F"
#Sets an instance of the smart contract
infrastructure_contract = web3.eth.contract(address=infrastructure_address, abi=abi)

def infrastructureTypes():
    #STIX Open Vocabulary
    infrastructure_types = {
        "1": "amplification",
        "2": "anonymization", 
        "3": "botnet",
        "4": "command-and-control", 
        "5": "exfiltration", 
        "6": "hosting-malware",
        "7": "hosting-target-lists",
        "8": "phishing",
        "9": "reconnaissance",
        "10": "staging",
        "11": "unknown"
    }
    #Retrieve all values from the dictionary
    print("\ninfrastructure types: ")
    for i in infrastructure_types:
        print(i + ": " + infrastructure_types[i])
    infrastructure_type_val = input("infrastructure type 1-11 : ")
    if int(infrastructure_type_val) > 0 and int(infrastructure_type_val) < 12:
        infrastructure_type = str(infrastructure_types[infrastructure_type_val])
        return infrastructure_type
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        infrastructureTypes()



def uploadInfrastructure():
   
    infrastructureSTIX = Infrastructure(
        #type ^ specified in class,  id - random uuid4 appended to type string, created=defined in object when created  spec_version=2.1(v used),, modified=infrastructure["created"], pattern_version=2.1(v used), valid_from=infrastructure["created"],        
        name=input("\ninfrastructure name: "),
        description=input("infrastructure description: "),
        infrastructure_types=infrastructureTypes(),
        aliases=ov.aliases(),
        kill_chain_phases=ov.enumerateKCP() 
    )
    #STIX object
    print(type(infrastructureSTIX), "\n\n" , infrastructureSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        infrastructure = json.loads(str(infrastructureSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(infrastructure)
        print("ipfs content address: ", contentAddr)

        stixID = infrastructure["id"]
        infrastructureName = infrastructure["name"]

        tx_hash = infrastructure_contract.functions.setInfrastructure(contentAddr, stixID, infrastructureName).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadInfrastructure()
    
def retrieveInfrastructure():  
    query = input("\n\nenter infrastructure name: \n")

    get_infrastructure = infrastructure_contract.functions.getInfrastructure(query).call()
    get_content_id = infrastructure_contract.functions.getContentID(get_infrastructure).call()
    #print("\n\ninfrastructure ID:", get_infrastructure)
    #print("content ID:" , get_content_id, "\n")

    retrieved_infrastructure = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXi = parse(retrieved_infrastructure)
    print("\n", type(STIXi), "\n", STIXi)
    return STIXi


  
