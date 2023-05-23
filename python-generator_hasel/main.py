import secrets
import string

letters = string.ascii_letters  #litery, duze i male
digits = string.digits  #cyfry od 0 do 9

password_resources = letters + digits  #konkatenacja poszczegolnych elementow hasla w jeden zbior

print("Podaj dlugosc hasla, ktore chcesz otrzymac")

password_lenght = input()   #dlugosc hasla

password_lenght = int(password_lenght)

password = ''

for i in range(password_lenght):
    password += ''.join(secrets.choice(password_resources))

print("Wygenerowane dla ciebie hasło to:" + " " + password)
