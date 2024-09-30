import random
import string
def password_gene(n):
    password=[]
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    for i in range(0,n):
        password.append(random.choice(all_characters))
    x=''.join(password)
    return x

n=int(input("entrer le nombre de caracterer de votre password: "))
print("votre password generer est: ",password_gene(n))