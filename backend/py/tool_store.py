import json
import datetime
import object_vocab as ov
from web3 import Web3
from app_authentication import web3, ipfs_cli
from stix2 import (Tool, parse)

#not even remotely done

#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_tool_val","type":"string"}],"name":"getTool","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTools","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_tool_val","type":"string"}],"name":"setTool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"toolIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]')

#Address from Remix once deployed
tool_address = "0x3950943D8D86267c04A4BBa804F9f0b8A01c2FB8"
#Sets an instance of the smart contract
tool_contract = web3.eth.contract(address=tool_address, abi=abi)

def toolTypes():
    #STIX Open Vocabulary
    tool_type = []
    tool_types = {
        "1": "denial-of-service",
        "2": "exploitation", 
        "3": "information-gathering",
        "4": "network-capture", 
        "5": "credential-exploitation", 
        "6": "remote-access",
        "7": "vulnerability-scanning",
        "8": "unknown"
    }
    print("\ntool types: ")
    for i in tool_types:
        print(i + ": " + tool_types[i])

    toolVal = input("enter number of tool types: ")
    if int(toolVal) > 0:
        for i in range(int(toolVal)):
            tool_type_val = input("enter tool type: ")
            tool_type.append(tool_types[tool_type_val])
    elif int(toolVal) == 0:
        tool_type.append("no tool type identified")
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        toolTypes()
    return tool_type


def uploadTool():
   
    toolSTIX = Tool(
        #type ^ specified in class,  id - random uuid4 appended to type string, created=defined in object when created  spec_version=2.1(v used),, modified=tool["created"], pattern_version=2.1(v used), valid_from=tool["created"],        
        name=input("\ntool name: "),
        description=input("tool description: "),
        tool_types=toolTypes(),
        aliases=ov.aliases(),
        kill_chain_phases=ov.enumerateKCP(),
        tool_version= input("enter tool version: ")
    )
    #STIX object
    print("\n", type(toolSTIX), "\n\n" , toolSTIX)

    confirm = input("correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        tool = json.loads(str(toolSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(tool)
        print("ipfs content address: ", contentAddr)

        stixID = tool["id"]
        toolName = tool["name"]

        tx_hash = tool_contract.functions.setTool(contentAddr, stixID, toolName).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("block: " , blockNum)
    else:
        uploadTool()
    
def retrieveTool():  
    query = input("\n\nenter tool name:\n")

    get_tool = tool_contract.functions.getTool(query).call()
    get_content_id = tool_contract.functions.getContentID(get_tool).call()
    #print("\n\ntool ID:", get_tool)
    #print("content ID:" , get_content_id, "\n")

    retrieved_tool = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix object
    STIXt = parse(retrieved_tool)
    print("\n", type(STIXt), "\n", STIXt)
    return STIXt


  
