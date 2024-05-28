class Calculatrice:
    def addition(self, x, y):
        return x + y

    def soustract(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

def main():
    calc = Calculatrice()
    
    print("Sélectionnez l'opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choix = input("Entrez votre choix (1/2/3/4) : ")

        if choix in ['1', '2', '3', '4']:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le second nombre : "))

            if choix == '1':
                print(f"Résultat : {num1} + {num2} = {calc.addition(num1, num2)}")
            elif choix == '2':
                print(f"Résultat : {num1} - {num2} = {calc.soustract(num1, num2)}")
            elif choix == '3':
                print(f"Résultat : {num1} * {num2} = {calc.multiplication(num1, num2)}")
            elif choix == '4':
                try:
                    result = calc.division(num1, num2)
                    print(f"Résultat : {num1} / {num2} = {result}")
                except ZeroDivisionError as e:
                    print(e)
        else:
            print("Choix invalide")

        next_calcul = input("Voulez-vous faire un autre calcul ? (oui/non) : ")
        if next_calcul.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
