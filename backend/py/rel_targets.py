import attack_pattern_store as APS
import course_of_action_store as COAS
import indicator_store as INDS
import infrastructure_store as INFS
import intrusion_set_store as INSS
import malware_store as MS
import threat_actor_store as TAS
import tool_store as TS
import vulnerability_store as VS


def ind_targets():
    ind_targets = {
    "1": "malware",
    "2": "tool",
    "3": "attack pattern",
    "4": "threat actor",
    "5": "infrastructure",
    "6": "intrusion set"
    }
    print("\nindicator targets: ")

    for i in ind_targets:
        print(i, ":", ind_targets[i])
    ind_val = input("target type 1-6 : ")
    if int(ind_val) > 0 and int(ind_val) < 7:
        trgt_ref = str(ind_targets[ind_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "attack pattern":
            trgt_val = APS.retrieveAttackPattern()
            
        elif trgt_ref == "threat actor":
            trgt_val = TAS.retrieveThreatActor()
            
        elif trgt_ref == "infrastructure":
            trgt_val = INFS.retrieveInfrastructure()
            
        elif trgt_ref == "intrusion set":
            trgt_val = INSS.retrieveIntrusionSet()
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()

def mal_targets():
    mal_targets = {
    "1": "malware",
    "2": "tool",
    "3": "attack pattern",
    "4": "threat actor",
    "5": "infrastructure",
    "6": "intrusion set",
    "7": "vulnerability"
    }
    print("\nmalware targets: ")

    for i in mal_targets:
        print(i, ":", mal_targets[i])
    mal_val = input("target type 1-7 : ")
    if int(mal_val) > 0 and int(mal_val) < 8:
        trgt_ref = str(mal_targets[mal_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "attack pattern":
            trgt_val = APS.retrieveAttackPattern()
            
        elif trgt_ref == "threat actor":
            trgt_val = TAS.retrieveThreatActor()
            
        elif trgt_ref == "infrastructure":
            trgt_val = INFS.retrieveInfrastructure()
            
        elif trgt_ref == "intrusion set":
            trgt_val = INSS.retrieveIntrusionSet()

        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()
   
def tool_targets():
    tool_targets = {
        "1": "malware",
        "2": "infrastructure",
        "3": "vulnerability"
    }
    print("\ntool targets: ")

    for i in tool_targets:
        print(i, ":", tool_targets[i])
    tool_val = input("target type 1-3 : ")
    if int(tool_val) > 0 and int(tool_val) < 4:
        trgt_ref = str(tool_targets[tool_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="infrastructure":
            trgt_val = INFS.retrieveInfrastructure()

        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()     
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()

def attack_pattern_targets():
    ap_targets = {
        "1": "malware",
        "2": "tool",
        "3": "vulnerability"
    }
    print("\nattack pattern targets: ")

    for i in ap_targets:
        print(i, ":", ap_targets[i])
    ap_val = input("target type 1-3 : ")
    if int(ap_val) > 0 and int(ap_val) < 4:
        trgt_ref = str(ap_targets[ap_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()

        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()     
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()

    

def coa_targets():
    coa_targets = {
        "1": "malware",
        "2": "tool",
        "3": "attack pattern",
        "4": "indicator",
        "5": "vulnerability"
        }
    print("\ncourse of action targets: ")

    for i in coa_targets:
        print(i, ":", coa_targets[i])
    coa_val = input("target type 1-5 : ")
    if int(coa_val) > 0 and int(coa_val) < 6:
        trgt_ref = str(coa_targets[coa_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "attack pattern":
            trgt_val = APS.retrieveAttackPattern()
            
        elif trgt_ref == "indicator":
            trgt_val = INDS.retrieveIndicator()

        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()     
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()

def threat_actor_targets():   
    ta_targets = {
        "1": "malware",
        "2": "tool",
        "3": "attack pattern",
        "4": "vulnerability",
        "5": "infrastructure"
    }
    print("\nthreat actor targets: ")

    for i in ta_targets:
        print(i, ":", ta_targets[i])
    ta_val = input("target type 1-5 : ")
    if int(ta_val) > 0 and int(ta_val) < 6:
        trgt_ref = str(ta_targets[ta_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "attack pattern":
            trgt_val = APS.retrieveAttackPattern()
            
        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()
            
        elif trgt_ref == "infrastructure":
            trgt_val = INFS.retrieveInfrastructure()
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()

def infrastructure_targets():
    infrastructure_targets = {
    "1": "malware",
    "2": "tool",
    "3": "indicator",
    "4": "vulnerability",
    "5": "infrastructure"
    }
    print("\ninfrastructure targets: ")

    for i in inf_targets:
        print(i, ":", inf_targets[i])
    inf_val = input("target type 1-5 : ")
    if int(inf_val) > 0 and int(inf_val) < 6:
        trgt_ref = str(inf_targets[inf_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "indicator":
            trgt_val = INDS.retrieveIndicator()
            
        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()
            
        elif trgt_ref == "infrastructure":
            trgt_val = INFS.retrieveInfrastructure()

        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()
   
def intrusion_set_targets():
        
    int_set_targets = {
        "1": "malware",
        "2": "tool",
        "3": "attack pattern",
        "4": "threat actor",
        "5": "infrastructure",
        "6": "vulnerability"
    }
    print("\nintrusion set targets: ")

    for i in int_set_targets:
        print(i, ":", int_set_targets[i])
    int_set_val = input("target type 1-6 : ")
    if int(int_set_val) > 0 and int(int_set_val) < 7:
        trgt_ref = str(int_set_targets[int_set_val])
        if trgt_ref == "malware":
            trgt_val = MS.retrieveMalware()
            
        elif trgt_ref =="tool":
            trgt_val = TS.retrieveTool()
            
        elif trgt_ref== "attack pattern":
            trgt_val = APS.retrieveAttackPattern()
            
        elif trgt_ref == "threat actor":
            trgt_val = TAS.retrieveThreatActor()
            
        elif trgt_ref == "infrastructure":
            trgt_val = INFS.retrieveInfrastructure()
            
        elif trgt_ref == "vulnerability":
            trgt_val = VS.retrieveVulnerability()
            
        else:
            print("\nFEATURE NOT SUPPORTED\n")
            targetRef()
        return trgt_val
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        targetRef()
    




