import random
kort1 = random.randint(1, 11)
kort2 = random.randint(1, 11)
hus1 = random.randint(1, 11)
hus2 = random.randint(1, 11)

print (f"Din giv är {kort1} och {kort2}, vilket ger totalen {kort1 + kort2}")

if kort1 + kort2 == 21:
   print("Blackjack")
else: 
   hus1 = random.randint(1, 11)
   hus2 = random.randint(1, 11)
   print (f"Huset drar {hus1} och {hus2}, vilket ger totalen {hus1 + hus2}")

stanna = "n" 
summa = kort1 + kort2
while stanna.lower() != "j":
        print(f"Din totala summa är {summa}")
        stanna = input("Stanna? [j/n]")
        if stanna.lower() == "j":
            print(f"Du stannar på {summa}")
            break
        elif summa == 21:
            print("Blackjack")
            break
        elif summa > 21:
            print("Du blev tjock, du suger")
            break

        stanna = input("Stanna? [j/n]")
        if stanna.lower() == "j":
            break
        else:
           summa += random.randint(1, 11)

    
