import pandas as pd
import random
import string
import sys
import nltk


'''
Cette fonction génère un mot de passe aléatoire de la longueur spécifiée.
characters définit les caractères autorisés pour les mots de passe, en excluant 'O' et '0' pour éviter toute confusion.
La boucle while garantit que le mot de passe généré respecte certaines contraintes spécifiées (majuscules, minuscules, chiffres, caractères spéciaux, etc.).
'''
def generate_password(length=12, dictionary_words=None):
    characters = (
        string.ascii_letters.replace('O', '') +
        string.ascii_lowercase +
        string.digits.replace('0', '') +
        "!@#$%&*+-=.<>?:"
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    # Vérification des contraintes
    while (
        len([c for c in password if c.isupper()]) < 2 or
        len([c for c in password if c.islower()]) < 2 or
        len([c for c in password if c.isdigit()]) < 2 or
        len([c for c in password if c in "!@#$%&*+-=.<>?"]) < 2 or
        ' ' in password or
        password.startswith('!') or password.startswith('@') or password.startswith('#') or
        password.endswith('!') or password.endswith('@') or password.endswith('#') or
        password in dictionary_words
    ):
        password = ''.join(random.choice(characters) for _ in range(length))

    return password

'''
Cette fonction utilise nltk pour télécharger une liste de mots du dictionnaire en anglais.
'''
def load_dictionary_words():
    nltk.download('words')
    dictionary_words = nltk.corpus.words.words()
    return dictionary_words


'''
Cette fonction génère une liste de mots de passe à l'aide de la fonction generate_password et les stocke dans un DataFrame pandas.
Le DataFrame est ensuite enregistré dans un fichier CSV spécifié par file_path.
'''
def create_password_csv(file_path, num_passwords):
    header = ["password"]
    dictionary_words = load_dictionary_words()
    passwords = [generate_password(length=12, dictionary_words=dictionary_words) for _ in range(num_passwords)]

    df = pd.DataFrame({"password": passwords})
    df.to_csv(file_path, index=False, encoding='utf-8-sig')



'''
Cette partie du script vérifie si le nombre correct d'arguments a été fourni en ligne de commande.
Elle récupère le nombre de mots de passe à générer à partir des arguments de la ligne de commande.
Ensuite, elle appelle la fonction create_password_csv pour générer les mots de passe et les enregistrer dans un fichier CSV.
'''
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python createPassword.py <num_passwords>")
        sys.exit(1)

    try:
        num_passwords = int(sys.argv[1])
    except ValueError:
        print("Veuillez fournir un nombre valide.")
        sys.exit(1)

    create_password_csv("usersPassword2.csv", num_passwords)
    print(f"{num_passwords} mots de passe ont été générés et enregistrés dans 'usersPassword2.csv'.")

