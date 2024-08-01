from pathlib import Path
from time import sleep
from os import system

def main():
    while True:
        print("RECETARIO \"EL MAIK\"")
        Greeting()
        base = Path.home()
        print(f"The directory of the recets are on {Path(base, "Recetas")} if you want consult")
        Count_recets()

def Greeting():
    name = input("Hey! What's your name bro? \nName: ")
    print(f"Nice to meet you {name} and welcome to RECETARIO \"EL MAIK\"")

def Count_recets():
    Count = Path(Path.home(), "Recetas").glob("**/*.txt")
    b = 0
    for i in Count:
        b +=1
    print(f"I find {b} recipes")

main()