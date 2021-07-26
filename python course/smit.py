import hashlib
flag = 0
pass_hash = input("Enter mds hash: " )

wordlist = input("file name")

try:
    pass_file =open (wordlist, "r")
except:
    print("no file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.mds(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("password found")
        print("password is  " + word)
        break

if flag == 0:
    print("password is not in the list")
















