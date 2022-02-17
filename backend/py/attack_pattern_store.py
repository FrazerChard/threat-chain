import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (AttackPattern, parse)

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"attack_patternIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_att_pat_val","type":"string"}],"name":"getAttackPattern","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAttackPatterns","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_att_pat_val","type":"string"}],"name":"setAttackPattern","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#Address from Remix once deployed
attack_pattern_address = "0x1349F3e1B8D71eFfb47B840594Ff27dA7E603d17"
#Sets an instance of the smart contract
attack_pattern_contract = web3.eth.contract(address=attack_pattern_address, abi=abi)

def uploadAttackPattern():
   
    attack_patternSTIX = AttackPattern(
        name = input("\nattack pattern name: "),
        description=input("attack pattern description: "),
        external_references=ov.externalReference(),
        aliases=ov.aliases(),
        kill_chain_phases= ov.enumerateKCP()
    )

    #STIX object
    print(type(attack_patternSTIX), "\n\n" , attack_patternSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        attack_pattern = json.loads(str(attack_patternSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(attack_pattern)
        print("ipfs content address: ", contentAddr)
        stixID = attack_pattern["id"]
        attName = attack_pattern["name"]

        tx_hash = attack_pattern_contract.functions.setAttackPattern(contentAddr, stixID, attName).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadAttackPattern()
    


def retrieveAttackPattern():  
    query = input("\n\nenter the attack pattern name:\n")
    get_attack_pattern = attack_pattern_contract.functions.getAttackPattern(query).call()
    get_content_id = attack_pattern_contract.functions.getContentID(get_attack_pattern).call()
    #print("\n\nattack_pattern ID:", get_attack_pattern)
    #print("content ID:" , get_content_id, "\n")

    retrieved_attack_pattern = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXap = parse(retrieved_attack_pattern)
    print("\n", type(STIXap), "\n", STIXap)
    return STIXap


