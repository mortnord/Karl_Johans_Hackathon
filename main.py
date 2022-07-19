import mariadb
import sys


def Connect_with_all():
    print("Skriv in IP adresse")
    IP_text = input()
    print("Skriv in port")
    Port_text = input()
    try:
        conn = mariadb.connect(
            user="root",
            password="marvel",
            host=IP_text,
            port=int(Port_text),
            database="Test")
    except mariadb.Error as e:

        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute("SELECT Fornavn, Etternavn FROM names")
    for fornavn, etternavn in cur:
        print(f"First name: {fornavn}, Last name: {etternavn}")




def Connect_with_some():
    print("Skriv in IP adresse")
    IP_text = input()
    print("Skriv in port")
    Port_text = input()
    print("Skriv in brukernavn")
    user_name = input()
    print("Skriv in passord")
    password_text = input()
    try:
        conn = mariadb.connect(
            user=user_name,
            password=password_text,
            host=IP_text,
            port=int(Port_text),
            database="Test")
    except mariadb.Error as e:

        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


def Task_1(conn):
    cur = conn.cursor()
    cur.execute(input())
    for fornavn, etternavn in cur:
        print(f"First name: {fornavn}, Last name: {etternavn}")


def Task_2(conn):
    cur = conn.cursor()
    cur.execute("SELECT Fornavn, Etternavn FROM names")
    for fornavn, etternavn in cur:
        print(f"First name: {fornavn}, Last name: {etternavn}")


print("Hva task skal du løse?")
player_command = str(input())
if player_command == "0":
    Connect_with_all()
if player_command == "1":
    Task_1(Connect_with_some())
if player_command == "2":
    Task_2(Connect_with_some())
