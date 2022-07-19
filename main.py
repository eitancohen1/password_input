import getpass
import os
accounts={
    1:{"username":"eitan","password":"1234","fullname":"eitan the king"},
    2:{"username":"avram","password":"4321","fullname":"avram avino"},
    3:{"username":"uri","password":"6789","fullname":"uri bori"},
    4:{"username":"haim","password":"4567","fullname":"haim ha arnav"},
    }
    
def finduser(name):
    for y,x in accounts.items():
        if accounts[y]["username"]==name:
            return 1
            
def findpassword(name,password):
    for y,x in accounts.items():
        if accounts[y]["username"]==name and accounts[y]["password"]==password:
            return 1


def printditails(name):
    for y,x in accounts.items():
        if accounts[y]["username"]==name:
            print("hello", accounts[y]["fullname"])        
    

def main():
    name=input("enter username: ")
    if finduser(name):
        password= getpass.getpass("enter password: ")
        if findpassword(name,password):
            printditails(name)
        else:
            os.system('clear')
            print("worng")
            main()
    
    else:
        os.system('clear')
        print("worng")
        main()
        
        
main()
