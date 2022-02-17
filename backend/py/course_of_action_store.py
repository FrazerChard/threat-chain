import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (CourseOfAction, parse)

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"course_of_actionIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_coa_val","type":"string"}],"name":"getCourseOfAction","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCourseOfActions","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_coa_val","type":"string"}],"name":"setCourseOfAction","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#Address from Remix once deployed
course_of_action_address = "0x9d13C6D3aFE1721BEef56B55D303B09E021E27ab"
#Sets an instance of the smart contract
course_of_action_contract = web3.eth.contract(address=course_of_action_address, abi=abi)

def uploadCourseOfAction():
   
    course_of_actionSTIX = CourseOfAction(
        name=input("\ncourse of action name: "),
        description=input("course of action description: ")
    )
    #STIX object
    print(type(course_of_actionSTIX), "\n\n" , course_of_actionSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        course_of_action = json.loads(str(course_of_actionSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(course_of_action)
        print("ipfs content address: ", contentAddr)

        stixID = course_of_action["id"]
        coaName = course_of_action["name"]

        tx_hash = course_of_action_contract.functions.setCourseOfAction(contentAddr, stixID, coaName).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadCourseOfAction()
    
def retrieveCourseOfAction():  
    query = input("\n\nenter course of action:\n")
    get_course_of_action = course_of_action_contract.functions.getCourseOfAction(query).call()
    get_content_id = course_of_action_contract.functions.getContentID(get_course_of_action).call()
    #print("\n\ncourse_of_action ID:", get_course_of_action)
    #print("content ID:" , get_content_id, "\n")

    retrieved_course_of_action = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXcoa = parse(retrieved_course_of_action)
    print("\n", type(STIXcoa), "\n", STIXcoa)
    return STIXcoa

  
