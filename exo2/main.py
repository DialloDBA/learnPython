import bcrypt
from datetime import datetime, date
from pprint import pprint
import os
import locale

lang = locale.getlocale()
encodage = locale.getpreferredencoding()
try:
    locale.setlocale(locale.LC_ALL, "")
except ValueError:
    locale.setlocale(locale.LC_ALL, "C")


def clear_console():
    # Vérifie si le système d'exploitation est Windows
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Mac/Linux


authenticated = False
attemptCount = 0
users = [
    {
        "username": "D2",
        "password": "12345",
        "is_admin": False,
        "login_at": "",
        "logout_at": "",
        "birthdate": "",
    },
    {
        "username": "D1",
        "password": "12345",
        "is_admin": False,
        "login_at": "",
        "logout_at": "",
        "birthdate": "",
    },
]
Auth = None


def register():
    print("Creer un nouvel Utilisateur")


def login():
    global authenticated
    global attemptCount
    global Auth

    print("******* Authentification *******")
    print(f"tentative : {attemptCount}")

    _u = getUsername()
    _ph = getUserPassword().strip()

    if AuthVerify(_u, _ph):
        print("connected")
        authenticated = True
        attemptCount = 0
        submenu()
    else:
        attemptCount = attemptCount + 1
        login()


def getUserByUsername(_username):
    global users
    for u in users:
        if u["username"] == _username:
            return u
    return None


def choixMenu(choix):
    match choix:
        case 0:
            login()
        case 1:
            register()
        case _:
            menu()


def menu():
    options = ["Se connecter ", "S'enregister "]
    print("Que voulez-vous faire Aujourd'hui ??  \n")

    for index, i in enumerate(options):
        print("{} : {}".format(index, i))

    print("Entrez votre choix \n")
    while True:
        try:
            c = int(input().strip())
            if c in [0, 1]:
                return c
            else:
                print("Veuillez saisir une valeur entre 0 et 1")
        except ValueError:
            print("Veuillez saisir une valeur entre 0 et 1")


def submenu():
    clear_console()
    options = [
        "Informations Personnelle",
        "Changement Mot de Passe",
        "Modifier date de Naissance",
        "Modifier mes Informations Personnelle",
        "Deconnexion",
    ]
    global Auth
    print("Utilisateur Connecté : " " " + Auth["username"] + " " " \n")
    for index, op in enumerate(options):
        print(f"{index} : {op}")


def getUsername():
    username = input("Saisir votre nom d'utilisateur  \n")
    while username == "":
        username = input("Saisir un nom d'utilisateur valide  \n")
    return username


def calAge(_date):
    _today = date.today()
    _dd = datetime.strptime(_date, "%d/%m/%Y").date()
    _age = _today.year - _dd.year
    if _today.month < _dd.month or \
       (_today.month == _dd.month and _today.day < _dd.day):
        _age -= 1
    
    return _age


def getUserPassword():
    password = input("Saisir votre password \n")
    while password == "":
        password = input("Saisir un mot de passe valide \n ")
    return password.encode("utf-8")


def createUserPassword():
    password = input("Saisir votre nouveau mot de passe \n")
    while password == "":
        password = input("Saisir un mot de passe valide \n ")

    passwordConfirm = input("Confirmez votre  mot de passe \n")
    while passwordConfirm == "":
        passwordConfirm = input("Confirmez votre  mot de passe \n ")

    while passwordConfirm != password:
        passwordConfirm = input(
            "Les deux de passe ne correspond pas. Confirmez votre  mot de passe \n "
        )

    return password.encode("utf-8")


def hashMe(_password):
    salt = bcrypt.gensalt()
    _hashed = bcrypt.hashpw(_password, salt)
    return _hashed


def passVerify(_pass, _current):
    return bcrypt.checkpw(_pass.encode("utf-8"), _current)


def createBirthdate(_format="%d/%m/%Y"):
    while True:
        try:
            _date = input(
                "Entrer votre date de Naissance au format : Jour/Mois/Annee \n"
            )
            _dateNaissance = datetime.strptime(_date, _format)
            return _dateNaissance
        except ValueError:
            print(
                "Attention : Entrer votre date de Naissance au format : Jour/Mois/Annee \n"
            )


def AuthVerify(_username, _password):
    global Auth
    user = getUserByUsername(_username)

    if user is None:
        print(f"L'utilisateur {_username} n'a pas été trouvé. \n")
        return False  # Utilisateur non trouvé

    _u = user["username"]
    _currentP = user["password"]
    salt = bcrypt.gensalt()
    _hashed1 = bcrypt.hashpw(_password, salt)
    _currentP = str(_currentP).encode("utf-8")
    _hashed2 = bcrypt.hashpw(_currentP, salt)
    Auth = user
    return _u == _username and bcrypt.checkpw(_password, _hashed2)


print("Bonjour ! \n")
# cc = menu()
# choixMenu(cc)
# _dd = createBirthdate()
# print("date N : " + _dd.strftime("%d %B %Y"))
print (calAge ("10/07/1995"))

