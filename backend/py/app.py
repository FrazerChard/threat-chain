import json
import sys
from attack_pattern_store import retrieveAttackPattern, uploadAttackPattern
from course_of_action_store import retrieveCourseOfAction, uploadCourseOfAction
from indicator_store import retrieveIndicator, uploadIndicator
from infrastructure_store import retrieveInfrastructure, uploadInfrastructure
from intrusion_set_store import retrieveIntrusionSet, uploadIntrusionSet
from malware_store import retrieveMalware, uploadMalware
from relationship_store import uploadRelationship, retrieveRelationship
from threat_actor_store import retrieveThreatActor, uploadThreatActor
from tool_store import retrieveTool, uploadTool
from vulnerability_store import retrieveVulnerability, uploadVulnerability

from web3 import Web3
from web3.middleware import geth_poa_middleware
from app_authentication import web3

web3.middleware_onion.inject(geth_poa_middleware, layer=0)


def appMenu():

    ti_types = {
        "1": "indicator",
        "2": "malware",
        "3": "tool",
        "4": "vulnerability",
        "5": "attack pattern",
        "6": "course of action",
        "7": "threat actor",
        "8": "infrastructure",
        "9": "intrusion set",
    }


    choice = input("\n1: upload threat intelligence object \n2: retrieve threat intelligence object\nenter: ")

    print("\nthreat intelligence objects: ")
    if int(choice) == 1:
        for i in ti_types:
            print(i, ":", ti_types[i])
        print("0: relationship")
        object_choice = input("select 0 - 9: ")

        if int(object_choice) == 0:
            uploadRelationship()

        elif int(object_choice) == 1:
            uploadIndicator()
            
        elif int(object_choice) == 2:
            uploadMalware()
            
        elif int(object_choice) == 3:
            uploadTool()
            
        elif int(object_choice) == 4:
            uploadVulnerability()
            
        elif int(object_choice) == 5:
            uploadAttackPattern()
            
        elif int(object_choice) == 6:
            uploadCourseOfAction()
            
        elif int(object_choice) == 7:
            uploadThreatActor()
            
        elif int(object_choice) == 8:
            uploadInfrastructure()
            
        elif int(object_choice) == 9:
            uploadIntrusionSet()
            
        else:
            print("\nFEATURE NOT SUPPORTED")
                


    elif choice == "2":
            for i in ti_types:
                print(i, ":", ti_types[i])
            object_choice = input("select 1 - 9: ")
                
            if int(object_choice) == 1:
                STIXi = retrieveIndicator()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXi["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")               
                
            elif int(object_choice) == 2:
                STIXm = retrieveMalware()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXm["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")
                
            elif int(object_choice) == 3:
                STIXt = retrieveTool()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXt["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")
                
            elif int(object_choice) == 4:
                STIXv = retrieveVulnerability()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXv["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")

            elif int(object_choice) == 5:
                STIXap = retrieveAttackPattern()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXap["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")

            elif int(object_choice) == 6:
                STIXc = retrieveCourseOfAction()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXc["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")

            elif int(object_choice) == 7:
                STIXta = retrieveThreatActor()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXta["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")
                                    
            elif int(object_choice) == 8:
                STIXinf = retrieveInfrastructure()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXinf["id"]
                        retrieveRelationship(STIXid)                
                except:
                    print("\nNo related data found")
                                    
            elif int(object_choice) == 9:
                STIXis = retrieveIntrusionSet()
                try:
                    retrieve_related = input("\nretrieve related data y/n: ")
                    if retrieve_related =="y":
                        STIXid = STIXis["id"]
                        retrieveRelationship(STIXid)
                except:
                    print("\nNo related data found")                

            else:
                print("\nFEATURE NOT SUPPORTED")
    else: 
        print("\nFEATURE NOT SUPPORTED")

    continueChoice = input("\ncontinue y/n: ")
    if continueChoice == "y":
        appMenu()
    
        

appMenu()


