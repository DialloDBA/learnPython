import bcrypt
message = "Bienvenue en python coding ! ;\n"
print (message)
userName = input("Entrez votre nom d'utilisateur ! \n")
userPassword = input("Bien ! Maintenant Entrez votre Mot de passe ! \n")
salt = bcrypt.gensalt()
passHashed = bcrypt.hashpw(userPassword.encode("utf-8"), salt)

print("votre nom d'utilisateur et mot de passe enrigistrer avec succeès . \n")

userConti = input("Voulez-vous continuer ?")
responsesKeys = ["oui","o","yes","y"]

print(userConti)
nextUserNavigate = False
if userConti.lower() in responsesKeys :
    nextUserNavigate = True

if nextUserNavigate :
    print("Connectez vous au serveur pour acceder a votre Espace de travail \n")
    u_username =  input("Entrez votre nom d'utilisateur ! \n");
    u_password = input("Bien ! Maintenant Entrez votre Mot de passe ! \n")
    u_hashed = bcrypt.hashpw(u_password.encode("utf-8"),salt)
    while userName!=u_username or not bcrypt.checkpw(u_password.encode("utf-8"),passHashed) :
        print("Oups ! Nom d'utilisateur ou mot de passe incorrect. \n")
        u_username = input("Entrez votre nom d'utilisateur ! \n")
        u_password = input("Bien ! Maintenant Entrez votre Mot de passe ! \n")
    print("Bon Retour Parmi Nous "+userName.upper())
else :
    print("Merci et à Bientôt !")




