import re

while True:
    valida = True
    password = input("dimmi la password da inserire: ")
    if len(password) < 8:
        print("la password deve essere lunga almeno 8 caratteri!")
        valida = False
    if not re.search("[A-Z]+", password): 
        print("la password deve contenre almeno una lettera maiuscola!")
        valida = False 
    if not re.search("[a-z]+", password): 
        print("la password deve contenre almeno una lettera minuscola!")
        valida = False
    if not re.search("[0-9]+", password): 
        print("la password deve contenre almeno un numero!")
        valida = False 
    if not re.search("[\.,_-]+", password): 
        print("la password deve contenre almeno un carattere speciale!")
        valida = False 

    if valida == True:
     print("la password è valida!")
     break
    else: 
        continue
    

print("Chiudo il programma.")