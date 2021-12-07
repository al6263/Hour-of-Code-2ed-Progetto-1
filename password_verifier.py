import re

while True:
    password = input("dimmi la password da inserire: ")
    if len(password) < 8:
        print("la password deve essere lunga almeno 8 caratteri!")
        continue
    if not re.search("[A-Z]+", password): 
        print("la password deve contenre almeno una lettera maiuscola!")
        continue
    if not re.search("[a-z]+", password): 
        print("la password deve contenre almeno una lettera minuscola!")
        continue
    if not re.search("[0-9]+", password): 
        print("la password deve contenre almeno un numero!")
        continue
    if not re.search("[\.,_-]+", password): 
        print("la password deve contenre almeno un carattere speciale!")
        continue

    print("la password è valida!")
    break

    

print("Chiudo il programma.")