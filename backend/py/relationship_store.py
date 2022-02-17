import json
import datetime
import object_vocab
import attack_pattern_store as APS
import course_of_action_store as COAS
import indicator_store as INDS
import infrastructure_store as INFS
import intrusion_set_store as INSS
import malware_store as MS
import threat_actor_store as TAS
import tool_store as TS
import vulnerability_store as VS
import rel_targets as RT
from web3 import Web3

from app_authentication import web3, ipfs_cli
from stix2 import (Relationship, parse)

#Getting data from a smart contract
#ABI from Remix
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"contentIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_stixID","type":"string"}],"name":"getContentID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContentIDs","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_srcID","type":"string"}],"name":"getRelationship","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRelationships","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"relationshipIDs","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_contentID","type":"string"},{"internalType":"string","name":"_stixID","type":"string"},{"internalType":"string","name":"_srcID","type":"string"}],"name":"setRelationship","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#Address from Remix once deployed
relationship_address = "0x4D3bfd7821E237fFE84209d8E638f9f309865b87"
#Sets the contract to a variable
relationship_contract = web3.eth.contract(address= relationship_address, abi=abi)

def sourceRef():
    ti_types = {
    "1": "indicator",
    "2": "malware",
    "3": "tool",
    "4": "attack pattern",
    "5": "course of action",
    "6": "threat actor",
    "7": "infrastructure",
    "8": "intrusion set",
    }

    print("\nrelationship sources: ")
    for i in ti_types:
        print(i, ":", ti_types[i])
    src_val = input("source type 1-9 : ")

    if int(src_val) > 0 and int(src_val) < 10:
        source_ref = str(ti_types[src_val])
        if source_ref == "indicator":
            #gets user input for the indicator queriable value
            source_val = INDS.retrieveIndicator()
            #sets target ref
            target_val = RT.ind_targets()
            rel_val = "indicates"
    
        elif source_ref == "malware":
            source_val = MS.retrieveMalware()
            target_val = RT.mal_targets()
            if target_val["type"] == "malware":
                mTOm = {
                    "1": "controls",
                    "2": "downloads",
                    "3": "drops",
                    "4": "uses",
                    "5": "variant-of" 
                }
                for i in mTOm:                           
                    print(i, ":", mTOm[i])
                rel_choice = input("relationship type 1-5 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 6:
                    rel_val = str(mTOm[rel_choice])

            elif target_val["type"] == "tool":
                mTOtool = {
                    "1": "downloads",
                    "2": "drops",
                    "3": "uses",
                }
                for i in mTOtool:                           
                    print(i, ":", mTOtool[i])

                rel_choice = input("relationship type 1-3 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 6:
                    rel_val = str(mTOtool[rel_choice])

            elif target_val["type"] == "vulnerability":
                mTOv = {
                    "1": "exploits",
                    "2": "targets"
                }
                for i in mTOv:                           
                    print(i, ":", mTOv[i])

                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3:
                    rel_val = str(mTOv[rel_choice])
            
            elif target_val["type"] == "infrastructure":
                mTOi = {
                    "1": "beacons-to",
                    "2": "exfiltrates-to",
                    "3": "targets",
                    "4": "uses"
                }
                for i in mTOi:                           
                    print(i, ":", mTOi[i])

                rel_choice = input("relationship type 1-4 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 5:
                    rel_val = str(mTOi[rel_choice])
           
            elif target_val["type"] == "threat-actor" or target_val["type"] =="intrusion-set":
                rel_val = "authored-by"
            
            elif target_val["type"] == "attack-pattern":
                rel_val = "uses"
            
        elif source_ref == "tool":
            source_val = TS.retrieveTool()
            target_val = RT.tool_targets()
            if target_val["type"] == "malware":
                tTOm = {
                    "1": "delivers",
                    "2": "drops",
                }
                for i in tTOm:                           
                    print(i, ":", tTOm[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3 :
                    rel_val = str(tTOm[rel_choice])
            elif target_val["type"] == "vulnerability":
                tTOv = {
                    "1": "has",
                    "2": "targets",
                }
                for i in tTOv:                           
                    print(i, ":", tTOv[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3 :
                    rel_val = str(tTOv[rel_choice])
            elif target_val["type"] == "infrastructure":
                tTOinf = {
                    "1": "uses",
                    "2": "targets",
                }
                for i in tTOinf:                           
                    print(i, ":", tTOinf[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3:
                    rel_val = str(tTOinf[rel_choice])

        elif source_ref == "attack pattern":
            source_val = APS.retrieveAttackPattern()
            target_val = RT.attack_pattern_targets()
            if target_val["type"] == "malware":
                apTOm = {
                    "1": "delivers",
                    "2": "uses",
                }
                for i in apTOm:                           
                    print(i, ":", apTOm[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3:
                    rel_val = str(apTOm[rel_choice])
            elif target_val["type"] == "vulnerability":
                rel_val = "delivers"
            elif target_val["type"] == "tool":
                rel_val = "uses"

        elif source_ref == "course of action":
            source_val = COAS.retrieveCourseOfAction()
            target_val = RT.coa_targets()
            if target_val["type"] == "indicator":
                coaTOi = {
                    "1": "investigates",
                    "2": "mitigates",
                }
                for i in coaTOi:                           
                    print(i, ":", coaTOi[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3:
                    rel_val = str(coaTOi[rel_choice])
            elif target_val["type"] == "malware" or target_val["type"] == "vulnerability":
                coaTOmv = {
                    "1": "remediates",
                    "2": "mitigates",
                }
                for i in coaTOmv:                           
                    print(i, ":", coaTOmv[i])
                rel_choice = input("relationship type 1-2 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 3:
                    rel_val = str(coaTOmv[rel_choice])
            elif target_val["type"] == "tool" or target_val["type"] == "attack-pattern":
                rel_val = "mitigates"

        elif source_ref == "threat actor":
            source_val = TAS.retrieveThreatActor()
            target_val = RT.threat_actor_targets()
            if target_val["type"] == "infrastructure":
                taTOinf = {
                    "1": "compromises",
                    "2": "hosts",
                    "3": "owns",
                    "4": "uses"
                }
                for i in taTOinf:                           
                    print(i, ":", taTOinf[i])
                rel_choice = input("relationship type 1-4: ")
                if int(rel_choice) > 0 and int(rel_choice) < 5:
                    rel_val = str(taTOinf[rel_choice])
            elif target_val["type"] == "vulnerability":
                rel_val = "targets"            
            elif target_val["type"] == "attack-pattern" or target_val["type"] == "malware" or target_val["type"] == "tool":
                rel_val = "uses"

        elif source_ref == "infrastructure":
            source_val = INFS.retrieveInfrastructure()
            target_val = RT.infrastructure_targets()

            if target_val["type"] == "infrastructure" or target_val["type"] == "indicator":
                infTOinfind = {
                    "1": "communicates-with",
                    "2": "consists-of",
                    "3": "controls",
                    "4": "uses"
                }
                for i in infTOinfind:                           
                    print(i, ":", infTOinfind[i])

                rel_choice = input("relationship type 1-4: ")
                if int(rel_choice) > 0 and int(rel_choice) < 5:
                    rel_val = str(infTOinfind[rel_choice])

            elif target_val["type"] == "malware":
                infTOm = {
                    "1": "controls",
                    "2": "delivers",
                    "3": "hosts"
                }
                for i in infTOm:                           
                    print(i, ":", infTOm[i])

                rel_choice = input("relationship type 1-3 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 4:
                    rel_val = str(infTOm[rel_choice])

            elif target_val["type"] == "vulnerability":
                rel_val ="has"
            
            elif target_val["type"] == "tool":
                rel_val ="hosts"

        elif source_ref == "intrusion set":
            source_val = INSS.retrieveIntrusionSet()
            target_val = RT.intrusion_set_targets()
            if target_val["type"] == "threat-actor":
                rel_val = "attributed to"
            elif target_val["type"] == "vulnerability":
                rel_val = "targets"
            elif target_val["type"] == "attack-pattern" or target_val["type"] == "malware" or target_val["type"] == "tool":
                rel_val = "uses"
            elif target_val["type"] == "infrastructure":
                intsTOinf = {
                    "1": "compromises",
                    "2": "hosts",
                    "3": "owns",
                    "4": "uses"
                }
                for i in intsTOinf:                           
                    print(i, ":", intsTOinf[i])
                rel_choice = input("relationship type 1-4 : ")
                if int(rel_choice) > 0 and int(rel_choice) < 5:
                    rel_val = str(intsTOinf[rel_choice])
       
        print("\n\n    relationship: \n    -------------")
        print(source_val, "\n", rel_val, "\n", target_val)
        
        relationshipSTIX = Relationship(
            source_ref= source_val,
            target_ref= target_val,
            relationship_type= rel_val
        )

        return relationshipSTIX

    else:
        print("\nFEATURE NOT SUPPORTED\n")
        sourceRef()





def uploadRelationship():
    relationshipSTIX = sourceRef()   
    #STIX object
    print("\n\n", type(relationshipSTIX), "\n" , str(relationshipSTIX) + "\n\n")
    confirm = input("Is this data correct? (y/n): ")
    if (confirm.upper() == "Y"):
        #converts the STIX object into a JSON object
        relationship = json.loads(str(relationshipSTIX))
        #uploads json object to IPFS and records the content address
        contentAddr = ipfs_cli.add_json(relationship)
        print("ipfs content address: ", contentAddr)
        stixID = relationship["id"]
        relType = relationship["type"]
        srcID = relationship["source_ref"]
        tx_hash =  relationship_contract.functions.setRelationship(contentAddr, stixID, srcID).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        blockNum = web3.eth.blockNumber
        #print("This is block:" , blockNum)
    else:
        uploadRelationship()
    


def retrieveRelationship(STIXid):
    #print(STIXid)
    get_relationship =  relationship_contract.functions.getRelationship(STIXid).call()
    get_content_id = relationship_contract.functions.getContentID(get_relationship).call()
    retrieved_relationships = ipfs_cli.cat(get_content_id)
    #Retrieve event value and parse into stix relationship as
    STIXr = parse(retrieved_relationships)
    print("\n", type(STIXr), "\n", STIXr)
    #targetVal = STIXr["target_ref"]
    
    return STIXr


  