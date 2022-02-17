import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (IntrusionSet, parse)

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_itset_name","type":"string"}],"name":"getIntrusionSet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getIntrusionSets","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"intrusion_setIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_itset_name","type":"string"}],"name":"setIntrusionSet","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#Address from Remix once deployed
intrusion_set_address = "0x938781b9796aeA6376E40ca158f67Fa89D5d8a18"
#Sets an instance of the smart contract
intrusion_set_contract = web3.eth.contract(address=intrusion_set_address, abi=abi)

def uploadIntrusionSet():
   
    intrusion_setSTIX = IntrusionSet(
        #type ^ specified in class,  id - random uuid4 appended to type string, created=defined in object when created  spec_version=2.1(v used),, modified=intrusion_set["created"], pattern_version=2.1(v used), valid_from=intrusion_set["created"],        
        name=input("\nintrusion set name: "),
        description=input("intrusion set description: "),
        aliases = ov.aliases(),
        goals = ov.goals(),
        resource_level=ov.attackResourceLevel(),
        primary_motivation=ov.attackMotivation()
    )
    #STIX object
    print(type(intrusion_setSTIX), "\n\n" , intrusion_setSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        intrusion_set = json.loads(str(intrusion_setSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(intrusion_set)
        print("ipfs content address: ", contentAddr)

        stixID = intrusion_set["id"]
        i_set_name = intrusion_set["name"]

        tx_hash = intrusion_set_contract.functions.setIntrusionSet(contentAddr, stixID, i_set_name).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadIntrusionSet()
    
def retrieveIntrusionSet():  
    query = input("\n\nenter intrusion set name: ")
    get_intrusion_set = intrusion_set_contract.functions.getIntrusionSet(query).call()
    get_content_id = intrusion_set_contract.functions.getContentID(get_intrusion_set).call()
    #print("\n\nintrusion_set ID:", get_intrusion_set)
    #print("content ID:" , get_content_id, "\n")

    retrieved_intrusion_set = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXis = parse(retrieved_intrusion_set)
    print("\n", type(STIXis), "\n", STIXis)
    return STIXis

