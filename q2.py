import json
accOrLog=input("if you wanna add accounts,enter 1,if you want to login,press 2:")
if accOrLog=="1":
    uname=input("enter username to add:")
    pwd=input("enter password to add:")
    towrite={"uname":uname,"pwd":pwd} 
    with open("account.json","a")as f:
        accounts=json.load(f)
    accounts.append(towrite)
    accounts=json.dumps(accounts)
    with open("accounts.json","w")as f:
        f.write(accounts)
        # json.dump(towrite,f,indent=4)
        # f.write(",\
elif accOrLog=="2":
    pass
else:
    print("you must enter 1 or 2")
