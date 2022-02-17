from web3 import Web3
import ipfshttpclient

provider = ""

ipfs_cli = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')

permissionedUsers = {
    "TCN1": "pass1",
    "TCN2": "pass2",
    "TCN3": "pass3",
    "TCN4": "pass4"
}

userNodes = {
    "TCN1": "http://172.16.239.1:22000",
    "TCN2": "http://172.16.239.1:22001",
    "TCN3": "http://172.16.239.1:22002",
    "TCN4": "http://172.16.239.1:22003"

}

print("Threat-Chain CLI Application")

while provider == "":  
    user = input("\nenter org name: ")
    usPass = input("enter password: ")
    
    if user in permissionedUsers:
        for i in permissionedUsers:
            if permissionedUsers[i] == usPass:
                provider = userNodes[user]
                web3 = Web3(Web3.HTTPProvider(provider))
                account = web3.eth.accounts[0]
                web3.eth.defaultAccount = account
                print("\nWelcome", user, ", your address is " + web3.eth.defaultAccount)              

        