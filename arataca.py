import hashlib 

flag = 0


pass_hash = input ("Insira o Md5 hash:")

wordlist = input("Arquive o nome: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("Arquivo não encontrado")
    quit()

for word in pass_file:

  enc_wrd = word.encode('utf-8')
  digest = hashlib.md5(enc_wrd.strip()) .hexdigest()

  if digest == pass_hash:
    print("Senha descoberta")
    print("A senha é " + word)
    flag = 1
    break 

if flag == 0: 
  print("password/passfrase is not in the list")
