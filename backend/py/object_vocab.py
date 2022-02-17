from stix2 import (ExternalReference)

def aliases():
    #STIX Open Vocabulary
    attack_pattern_aliases = []
    #Retrieve all values from the dictionary
    aliasesVal = input("\nenter number of aliases: ")
    if int(aliasesVal) > 0:
        for i in range(int(aliasesVal)):
            attack_pattern_alias = input("enter alias: ")
            attack_pattern_aliases.append(attack_pattern_alias)
    elif int(aliasesVal) == 0:
        attack_pattern_alias.append("no aliases identified")
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        attack_patternTypes()
    return attack_pattern_aliases

def attackMotivation():
    attack_motivations = {
        "1": "accidental",
        "2": "coercion",
        "3": "dominance",
        "4": "ideology",
        "5": "notoriety",
        "6": "organizational-gain",
        "7": "personal-gain",
        "8": "personal-satisfaction",
        "9": "revenge",
        "10": "unpredictable"
      }
    print("\nattacker motivations: ")
    for i in attack_motivations:
        print(i + ": " + attack_motivations[i])
    amVal = input("\nattacker motivations 1-10: ")
    if int(amVal) > 0 and int(amVal) < 11:
        attack_motivation = attack_motivations[amVal]
        return attack_motivation
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        attackMotivation()

def attackResourceLevel():
    attack_resource_levels = {
        "1": "individual",
        "2": "club",
        "3": "contest",
        "4": "team",
        "5": "organization",
        "6": "government"
    }
    print("\nresource levels: ")
    for i in attack_resource_levels:
        print(i + ": " + attack_resource_levels[i])
    arlVal = input("\nresource levels 1-6: ")
    if int(arlVal) > 0 and int(arlVal) < 7:
        attack_resource = attack_resource_levels[arlVal]
        return attack_resource
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        attackResourceLevel()


def enumerateKCP():
    kill_chain_phases = []  
    num_of_kcp = input("\nnumber of killchain phases: ")

    if int(num_of_kcp) != 0:
        for i in range(int(num_of_kcp)):
            kcp = killchainPhases()
            kchain_dict = {"kill_chain_name": "lockheed-martin-cyber-kill-chain", "phase_name":kcp}
            kill_chain_phases.append(kchain_dict)
        return kill_chain_phases
    else:
        print("\nCANNOT BE EMPTY\n")
        enumerateKCP()

def externalReference():
    #def hashes():
     #   hash_type = hashingVocab()
      #  hash_value = input("enter file hash: ") 

    print("\nenter external reference: \n")
    er_src_name = input("enter source name: ")
    er_descr = input("enter description: ")
    urlChoice = input("\nenter url y/n: ")
   
    if urlChoice == "y":
        urlVal = input("enter url: "),
        idChoice = input("\nenter id y/n: ")
        if idChoice == "y":
            externalRefs = ExternalReference(
                source_name=er_src_name,
                description=er_descr,
                url= urlVal,
                external_id=input("enter external id: ")
            )
        else:
            externalRefs = ExternalReference(
                source_name=er_src_name,
                description=er_descr,
                url= urlVal
            )
    else: 
        idChoice = input("\nenter id y/n: ")
        if idChoice == "y":
            externalRefs = ExternalReference(
                source_name=er_src_name,
                description=er_descr,
                external_id=input("enter external id: ")
            )
        else:
            externalRefs = ExternalReference(
                source_name=er_src_name,
                description=er_descr
            )
    return externalRefs

def fileHash():
    hash_type = hashingVocab()
    hash_value = input("enter file hash: ")     
    file_pattern = "[file:hashes.'{0}' = '{1}']".format(hash_type, hash_value)
    # "md5 - d64fde938f4f9c83df63b9da26c0fc26"
    #sha256 - d600474b1b8e50d3633c91c0cf1efc454b79c9624a43fd7de441ee71745726ab
    return file_pattern    

def goals():
    goals = []  
    num_of_goals = input("\nnumber of goals: ")

    if int(num_of_goals) != 0:
        for i in range(int(num_of_goals)):
            goals_input = input("enter goal: ")
            goals.append(goals_input)
        return goals
    else:
        print("\nCANNOT BE EMPTY\n")
        goals()


def hashingVocab():
    hashing_types = {
        "1": "md5",
        "2": "sha-1",
        "3": "sha-256",
        "4": "sha-512",
        "5": "sha3-256",
        "6": "sha3-512",
        "7": "ssdeep",
        "8": "tlsh"
    }
    print("\nhashing algorithms: ")
    for i in hashing_types:
        print(i + ": " + hashing_types[i])

    hashval = input("hash algorithm 1-8: ")
    if int(hashval) > 0 and int(hashval) < 9:
        hash_type = hashing_types[hashval]
        return hash_type
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        hashingVocab()

def ipv4Address():
    ind_pattern = input("\nenter ipv4 address: ")
    file_pattern = "[ipv4-addr:value = '{0}']".format(ind_pattern) 
    return file_pattern

def killchainPhases():
    killchain_phases = {
        "1": "reconnaissance",
        "2": "weaponization",
        "3": "delivery",
        "4": "exploitation",
        "5": "installation",
        "6": "command and control (C2)",
        "7": "actions on objectives"
    }
    #Retrieve all values from the dictionary
    print("\nlockheed martin killchain phases: ")
    for i in killchain_phases:
        print(i + ": " + killchain_phases[i])
    killchain_val = input("kill-chain phase 1-7: ")
    if int(killchain_val) > 0 and  int(killchain_val) < 8:
        killchain_phase = killchain_phases[killchain_val]
        return killchain_phase
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        killchainPhases()

def malwareCapabilities():
    malware_capabilities = {
        '1': 'accesses-remote-machines',
        '2': 'anti-debugging', 
        '3': 'anti-disassembly', 
        '4': 'anti-emulation', 
        '5': 'anti-memory-forensics', 
        '6': 'anti-sandbox', 
        '7': 'anti-vm', 
        '8': 'captures-input-peripherals', 
        '9': 'captures-output-peripherals', 
        '10': 'captures-system-state-data', 
        '11': 'cleans-traces-of-infection', 
        '12': 'commits-fraud', 
        '13': 'communicates-with-c2', 
        '14': 'compromises-data-availability', 
        '15': 'compromises-data-integrity', 
        '16': 'compromises-system-availability', 
        '17': 'controls-local-machine', 
        '18': 'degrades-security-software', 
        '19': 'degrades-system-updates', 
        '20': 'determines-c2-server', 
        '21': 'emails-spam', 
        '22': 'escalates-privileges', 
        '23': 'evades-av', 
        '24': 'exfiltrates-data', 
        '25': 'fingerprints-host',
        '26': 'hides-artifacts', 
        '27': 'hides-executing-code', 
        '28': 'infects-files', 
        '29': 'infects-remote-machines', 
        '30': 'installs-other-components', 
        '31': 'persists-after-system-reboot', 
        '32': 'prevents-artifact-access', 
        '33': 'prevents-artifact-deletion', 
        '34': 'probes-network-environment', 
        '35': 'self-modifies', 
        '36': 'steals-authentication-credentials', 
        '37': 'violates-system-operational-integrity'
        }
    print("malware capabilities: ")
    for i in malware_capabilities:
        print(i + ": " + malware_capabilities[i])
    
    malware_cap_val = input("\nmalware capability 1-37: ")
    if int(malware_cap_val) > 0 and int(malware_cap_val) < 38:
        malware_capabilities = malware_capabilities[malware_cap_val]
        return malware_capabilities
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        malwareCapabilities()

def malwareTypeVocab():
    malware_types = {
        "1": "adware",
        "2": "backdoor",
        "3": "bot",
        "4": "bootkit",
        "5": "ddos",
        "6": "downloader",
        "7": "dropper",
        "8": "exploit-kit",
        "9": "keylogger",
        "10": "ransomware",
        "11": "remote-access-trojan",
        "12": "resource-exploitation",
        "13": "rogue-security-software",
        "14": "rootkit",
        "15": "screen-capture",
        "16": "spyware",
        "17": "trojan",
        "18": "unknown",
        "19": "virus",
        "20": "webshell",
        "21": "wiper",
        "22": "worm"
    }
    print("\nmalware types: ")
    for i in malware_types:
        print(i + ": " + malware_types[i])
    maltypeval = input("malware type 1-22: ")
    if int(maltypeval) > 0 and int(maltypeval) < 23:
        malware_type = malware_types[maltypeval]
        return malware_type
    else:
        print("\nFEATURE NOT SUPPORTED\n")
        malwareTypeVocab()

def urlAddress():
    ind_pattern = input("\nenter url: ")
    file_pattern = "[url:value = '{0}']".format(ind_pattern) 
    return file_pattern
    #www.flashy.org.uk

 

     