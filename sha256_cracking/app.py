from pwn import *
import sys

if(len(sys.argv)!=2):
    print("[-]Invalid Argument")
    print(f"usage: {sys.argv[0]} <sha256sum>")
    exit()
input_hash = sys.argv[1]
password_file = "word.txt"
attempt = 0
with log.progress(f"Attempting to crack {input_hash}") as p:
    with open(password_file,"r",encoding='utf-8') as passlist:
        for password in passlist:
            password = password.strip("\n").encode('utf-8')
            password_hash = sha256sumhex(password)
            #print(password_hash)
            password = password.decode('utf-8')
            p.status(f"[{attempt}] {password} == {password_hash}")
            if password_hash == input_hash:
                p.success(f"Password hash found after {attempt} attempts! {password} hashes to {input_hash}")
                exit()
            attempt += 1
        p.failure("Password hash not found")