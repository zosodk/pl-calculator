operators = ["+", "-", "*", "/"]


def lommeregner(ops_list):
    while True:
        quitter = input("\nSkriv 'quit' for at afslutte, tryk Enter for at fortsætte: ").strip().lower()
        if quitter == "quit":
            print("Afslutter lommeregner...")
            break

        tal1 = float(input("Skriv det første tal: "))

        print("Nu skal du vælge en operation:")
        for idx, op in enumerate(ops_list, start=1):
            print(f"{idx} vil bruge {op} i regnestykket")

        valg = int(input("Vælg din operator (1-4): "))
        tal2 = float(input("Skriv det næste tal: "))

        print("Resultatet bliver: ", end="")
        match valg:
            case 1:
                print(tal1 + tal2)
            case 2:
                print(tal1 - tal2)
            case 3:
                print(tal1 * tal2)
            case 4:
                if tal2 == 0:
                    print("Fejl: Kan ikke dividere med 0!")
                else:
                    print(tal1 / tal2)
            case _:
                print("Ugyldigt valg!")


lommeregner(operators)