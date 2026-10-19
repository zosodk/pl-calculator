import re


def tokenize(expr: str) -> list[str]:
    """Opdeler en regnestreng i tal, operatorer og parenteser."""
    # Matcher decimaltal/heltal eller operatorer/parenteser
    tokens = re.findall(r"\d+\.?\d*|[+\-*/()]", expr)
    return tokens


def infix_to_postfix(tokens: list[str]) -> list[str]:
    """Dijkstra's Shunting-yard algoritme: Omsætter infiks til postfix (RPN)."""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    op_stack = []

    for token in tokens:
        # Hvis token er et tal
        if re.match(r"^\d+\.?\d*$", token):
            output.append(token)
        elif token in precedence:
            # Tøm stakken for operatorer med højere eller samme præcedens
            while (op_stack and op_stack[-1] != "(" and
                   precedence.get(op_stack[-1], 0) >= precedence[token]):
                output.append(op_stack.pop())
            op_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            # Tøm over i output indtil startparentes findes
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            if op_stack and op_stack[-1] == "(":
                op_stack.pop()  # Fjern '('
            else:
                raise ValueError("Ubalancerede parenteser!")

    while op_stack:
        op = op_stack.pop()
        if op in "()":
            raise ValueError("Ubalancerede parenteser!")
        output.append(op)

    return output


def evaluate_postfix(postfix_tokens: list[str]) -> float:
    """Evaluerer et postfix-udtryk via en stak."""
    eval_stack = []

    for token in postfix_tokens:
        if re.match(r"^\d+\.?\d*$", token):
            eval_stack.append(float(token))
        else:
            if len(eval_stack) < 2:
                raise ValueError("Ugyldigt udtryk!")
            b = eval_stack.pop()
            a = eval_stack.pop()

            match token:
                case "+":
                    eval_stack.append(a + b)
                case "-":
                    eval_stack.append(a - b)
                case "*":
                    eval_stack.append(a * b)
                case "/":
                    if b == 0:
                        raise ZeroDivisionError("Division med 0 er ikke tilladt!")
                    eval_stack.append(a / b)

    if len(eval_stack) != 1:
        raise ValueError("Ugyldigt udtryk!")

    return eval_stack[0]


def avanceret_lommeregner():
    print("=== Avanceret Lommeregner ===")
    print("Understøtter: +, -, *, /, parenteser () og decimaler.")
    print("Skriv 'quit' for at afslutte.\n")

    while True:
        expr = input("Indtast regnestykke: ").strip()
        if expr.lower() == "quit":
            break
        if not expr:
            continue

        try:
            tokens = tokenize(expr)
            if not tokens:
                print("Intet genkendeligt regnestykke indtastet.")
                continue

            postfix = infix_to_postfix(tokens)
            resultat = evaluate_postfix(postfix)

            # Vis pænt som heltal hvis der ikke er decimaler
            if resultat.is_integer():
                print(f"= {int(resultat)}")
            else:
                print(f"= {resultat:.4f}")

        except ZeroDivisionError as e:
            print(f"Fejl: {e}")
        except Exception as e:
            print(f"Fejl i udregning: {e}")


if __name__ == "__main__":
    avanceret_lommeregner()