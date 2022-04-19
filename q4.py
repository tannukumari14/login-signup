import json, re
print("hello welcome to login sign up page")
loginsignup=input("enter loginsignup:-")
if True:
    if loginsignup=="signup":
        a= open("account.json","r")
        c=a.read()
        data=json.loads(c)
        username=input("enter the name:-")
        surname=input("enter the surname:-")
        phone_no=int(input("enter the phone_no:-"))
        if (len(str(phone_no)))==10:
            otp=int(input("enter the otp:-"))
            if (len(str(otp)))==6:
                dop=input("enter the dop:-")
                gender=input("enter the gender:-")
                if gender=="male" or gender=="female" or gender=="other":
                    bio=input("enter the bio")
                    password=input("enter the password:-")
                    if re.fullmatch(r'[0-9,A-Z,a-z,@#$!]{8,}',password):
                        print("strong password")
                        conifrm_password=input("enter the password:-")
                        username= {"username":username,"surname":surname,"password":password,"phone_no":phone_no,"bio":bio,"gender":gender,"dop":dop}
                        data.update(username)
                        if password==conifrm_password:
                            print("it is succefully done")
                            with open("tanu kumari.json","a")as f:
                                b=json.dump(data,f,indent=4)
                        else:
                            print("your password is wrong")
                    else:
                        print("your password is invalid")
                else:
                    print("your gender is wrong")
            else:
                print("your otp is non valid")
        else:
            print("your mobile number is non valid")
    elif loginsignup=="login":
        username=input("enter the username:-")
        password=input("enter the pasword:-")
        loginsignup=open("tanu kumari.json","r")
        a=json.load(loginsignup)
        b={}
        for i in a:
            print(i)
            b.update({i:a})
            print(b)
            break
        print("login sucessfull")
