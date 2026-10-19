Operators = ["+", "-", "*", "/"]

def Lommeregner(Operators):
    num=0
    while True:
        quitter = input(f"Skriv quit hvis du gerne vil afslutte, tryk Enter for at fortsætte\n")
        if quitter.lower() == "quit":
            break
        tal1 = float(input(f"Skriv det første tal: "))
        print(f"Nu skal du vælge en operation")
        for ops in Operators:
            num =num+1
            print(f"{num} vil bruge {ops} i regnestykket")
        value = int(input(f"Vælg din operator: "))
        tal2 = float(input(f"Skriv det næste tal: "))
        print("Resultatet bliver: ")

        match value:
            case 1:
                print(f"{tal1 + tal2}")
            case 2:
                print(f"{tal1 - tal2}")
            case 3:
                print(f"{tal1 * tal2}")
            case 4:
                print(f"{tal1 / tal2}")
Lommeregner(Operators)