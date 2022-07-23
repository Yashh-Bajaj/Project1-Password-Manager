from cryptography.fernet import Fernet
print("Welcome to the password manager")
'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_pwd=input("Enter the master Password")
key= load_key() + master_pwd.encode()
fer=Fernet(key)


def view():
    with open("Password_Manager.txt", "r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw = data.split("|")

            print("User:",user,", Password:",fer.decrypt(passw.encode()))

def write():
    acc=input("Enter Account name or Number")
    pwd=input("Enter Password")
    with open("Password_Manager.txt","a") as f:
        f.write(acc+"|"+str(fer.encrypt(pwd.encode()).decode()) + "\n" )



while True:
    mode = input("If you want to enter the passwords press write\n If you want to see the passwords press view \n If you want to quit press q")
    if mode=="write" or mode =="Write":
        write()
        print("Successfully Saved")
    elif mode=="q" or mode=="Q":
        break
    elif mode=="View" or mode=="view":
        view()
