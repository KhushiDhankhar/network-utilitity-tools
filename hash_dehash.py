import hashlib
import os
import pyfiglet
def save(data,filename):
    with open(filename,"w") as f:
        for hash_value,text in data.items():
            f.write(f"{hash_value}:{text}\n")

def load_data(filename):
    data={}
    if os.path.exists(filename):
        with open(filename ,"r") as f:
            for line in f:
                line=line.strip()
                if ":" in line:
                    hash_value,text=line.strip().split(':',1)
                    data[hash_value]=text
    return data               

def main():
    text = "HASH MASTER"
    banner = pyfiglet.figlet_format(text)
    print(banner)
    filename=r"C:\Users\kumar\OneDrive\Desktop\MSIL ITSEC PROJECTS\sha256Hash.txt"
    k=load_data(filename)
    fname=r"C:\Users\kumar\OneDrive\Desktop\MSIL ITSEC PROJECTS\md5Hash.txt"
    h=load_data(fname)
    while True:
        choice=int(input("\t\t\t\t ENTER YOUR CHOICE:\n 1. HASH\n 2. DEHASH\n"))
        if(choice==1):
            ch=int(input("\t\t\t\t ENTER YOUR CHOICE:\n 1. MD5-HASH\n 2. SHA256-HASH\n"))
            if(ch==1):
                s=input("enter text to turn into MD5 HASHDIGEST :")
                r=hashlib.md5(s.encode())
                md5hash=r.hexdigest()
                if md5hash not in h:
                    h[md5hash]=s
                    save(h,fname)
                print(" MD5 hashdigest of enterd text is : ",md5hash)
            elif(ch==2):
                text=input("enter text to turn into SHA256 HASHDIGEST :")
                rt=hashlib.sha256(text.encode())
                sha256hash=rt.hexdigest()
                if sha256hash not in k:
                    k[sha256hash]=text
                    save(k,filename)
                print(" SHA256 hashdigest of enterd text is : ",sha256hash)
            
            c=int(input("Do you want to continue?\n 1. Yes\n 2. No\n"))
            if(c==1):
                continue
            else:
                print("THANKYOU")
                break

        elif(choice==2):
            choicee=int(input("\t\t\t\t ENTER YOUR CHOICE:\n 1. MD5-DEHASH\n 2. SHA256-DEHASH\n"))
            if(choicee==1):
                a=input("enter MD5 hashdigest: ")   
                print("Plaintext to corresponding MD5 hashdigest is: ",h.get(a,"Not in database"))   
            elif(choicee==2):
                aa=input("enter SHA256 hashdigest: ")   
                print("Plaintext to corresponding SHA256 hashdigest is: ",k.get(aa,"Not in database")) 
            c=int(input("Do you want to continue?\n 1. Yes\n 2. No\n"))
            if(c==1):
                continue
            else:
                print("THANKYOU")
                break
        
        else:
            print("you have entered a wrong choice.\n enter a valid choice")
            c=int(input("Do you want to continue?\n 1. Yes\n 2. No\n"))
            if(c==1):
                continue
            else:
                print("THANKYOU")
                break

if __name__=="__main__":
    main()
