import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (ThreatActor, parse)

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_ta_name","type":"string"}],"name":"setThreatActor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_ta_name","type":"string"}],"name":"getThreatActor","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getThreatActors","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"threat_actorIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')
#Address from Remix once deployed
threat_actor_address = "0xA501AfD7d6432718daF4458Cfae8590d88de818E"
#Sets an instance of the smart contract
threat_actor_contract = web3.eth.contract(address=threat_actor_address, abi=abi)

def threatActorTypes():
    #STIX Open Vocabulary
    threat_actor_type = []
    threat_actor_types = {
        "1": "activist",
        "2": "competitor", 
        "3": "crime-syndicate",
        "4": "criminal", 
        "5": "hacker", 
        "6": "insider-accidental",
        "7": "insider-disgruntled",
        "8": "nation-state",
        "9": "sensationalist",
        "10": "spy",
        "11": "terrorist",
        "12": "unknown"
    }
    #Retrieve all values from the dictionary
    print("\nthreat actor types: ")
    for i in threat_actor_types:
        print(i + ": " + threat_actor_types[i])

    ta_typeVal = input("\nnumber of threat actor types: ")
    if int(ta_typeVal) != 0:
        for i in range(int(ta_typeVal)):
            threat_actor_type_val = input("threat actor type 1-12 : ")
            if int(threat_actor_type_val) > 0 and int(threat_actor_type_val) < 13:
                threat_actor_type.append(str(threat_actor_types[threat_actor_type_val]))
        return threat_actor_type
    else:
        print("\nCANNOT BE EMPTY\n")
        threat_actorTypes()

def threatActorRoles():
        #STIX Open Vocabulary
    ta_role_list = []
    threat_actor_roles = {
        "1": "agent",
        "2": "director", 
        "3": "independant",
        "4": "infrastructure-architect", 
        "5": "infrastructure-operator", 
        "6": "malware-author",
        "7": "sponser"
    }
    #Retrieve all values from the dictionary
    print("\nthreat actor roles: ")
    for i in threat_actor_roles:
        print(i + ": " + threat_actor_roles[i])

    ta_roleVal = input("\nnumber of threat actor roles: ")
    if int(ta_roleVal) != 0:
        for i in range(int(ta_roleVal)):
            threat_actor_role_val = input("threat actor role 1-7 : ")
            if int(threat_actor_role_val) > 0 and int(threat_actor_role_val) < 8:
                ta_role_list.append(str(threat_actor_roles[threat_actor_role_val]))
        return ta_role_list
    else:
        print("\nCANNOT BE EMPTY\n")
        threatActorRoles()

def threatActorSophistication():
    threat_actor_sophistication = {
        "1": "none",
        "2": "minimal",
        "3": "intermediate",
        "4": "advanced",
        "5": "expert",
        "6": "innovator",
        "7": "strategic"
    }
    print("\nthreat actor sophistication: ")
    for i in threat_actor_sophistication:
        print(i + ": " + threat_actor_sophistication[i])
    tasVal = input("\nsophistication levels 1-6: ")
    if int(tasVal) > 0 and int(tasVal) < 7:
        ta_sophistication = threat_actor_sophistication[tasVal]
        return ta_sophistication
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        threatActorSophistication()


def uploadThreatActor():
   
    threat_actorSTIX = ThreatActor(
        #type ^ specified in class,  id - random uuid4 appended to type string, created=defined in object when created  spec_version=2.1(v used),, modified=threat_actor["created"], pattern_version=2.1(v used), valid_from=threat_actor["created"],        
        name=input("\nthreat actor name: "),
        description=input("threat actor description: "),
        threat_actor_types=threatActorTypes(),
        aliases=ov.aliases(),
        roles=threatActorRoles(),
        goals=ov.goals(),
        sophistication=threatActorSophistication(),
        resource_level=ov.attackResourceLevel(),
        primary_motivation=ov.attackMotivation()
    )
    #STIX object
    print(type(threat_actorSTIX), "\n\n" , threat_actorSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        threat_actor = json.loads(str(threat_actorSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(threat_actor)
        print("ipfs content address: ", contentAddr)

        stixID = threat_actor["id"]
        ta_name = threat_actor["name"]

        tx_hash = threat_actor_contract.functions.setThreatActor(contentAddr, stixID, ta_name).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadThreatActor()
    
def retrieveThreatActor():
            
    query = input("\n\nenter threat actor name: ")

    get_threat_actor = threat_actor_contract.functions.getThreatActor(query).call()
    get_content_id = threat_actor_contract.functions.getContentID(get_threat_actor).call()
    #print("\n\nthreat_actor ID:", get_threat_actor)
    #print("content ID:" , get_content_id, "\n")

    retrieved_threat_actor = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXta = parse(retrieved_threat_actor)
    print("\nn", type(STIXta), "\n", STIXta)
    return STIXta

