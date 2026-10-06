Operators = ["+", "-", "*", "/"]

def Lommeregner(Operators):
    num=0
    while True:
        quitter = input(f"skriv quit hvis du gerne vil quitte, tryk enter for at fortsætte\n")
        if quitter.lower() == "quit":
            break
        tal1 = float(input(f"giv mig et tal"))
        print(f"nu skal du vælge en operation")
        for ops in Operators:
            num =num+1
            print(f"{num} vil bruge {ops} i regnestykket")
        value = int(input(f"vælg din operation"))
        tal2 = float(input(f"giv mig et tal"))

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