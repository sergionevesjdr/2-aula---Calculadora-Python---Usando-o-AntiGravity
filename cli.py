"""
Interface de Linha de Comando (CLI) para a Calculadora Python
Suporte às operações básicas, porcentagens e gráficos ASCII.
"""

import sys
import argparse
from calculator import Calculator


def show_banner() -> None:
    print("=" * 55)
    print("       🐍 CALCULADORA EM PYTHON COM GRÁFICOS CLI       ")
    print("=" * 55)


def handle_percentage_menu(calc: Calculator) -> None:
    print("\n--- Submenu de Porcentagem & Gráficos ---")
    print("  [1] Calcular X% de um Total (ex: 20% de 500)")
    print("  [2] Proporção: Saber quantos % uma Parte é do Total (ex: 50 de 200)")
    print("  [3] Aplicar Aumento Percentual (ex: 100 + 15%)")
    print("  [4] Aplicar Desconto Percentual (ex: 200 - 10%)")
    print("  [0] Voltar ao menu principal")

    sub_choice = input("\nEscolha uma opção de porcentagem (0-4): ").strip()
    if sub_choice == "0":
        return

    try:
        if sub_choice == "1":
            tot = float(input("Digite o valor Total: "))
            pct = float(input("Digite a Porcentagem (%): "))
            res = calc.percentage(tot, pct)
            remaining = tot - res
            print(f"\n>>> Resultado: {pct}% de {tot} = {res}")
            print(f"    Restante (100% - {pct}%): {remaining}")
            print(f"\n📊 Gráfico de Proporção (100% Stacked Bar):")
            print(f"    {calc.render_ascii_bar(pct, width=32)}")
            print(f"    Legenda: [█ = Parte Calculada ({res}) | ░ = Restante ({remaining})]")

        elif sub_choice == "2":
            parte = float(input("Digite o valor da Parte: "))
            tot = float(input("Digite o valor do Total: "))
            pct = calc.percentage_ratio(parte, tot)
            print(f"\n>>> Resultado: {parte} representa {pct:.2f}% de {tot}")
            print(f"\n📊 Gráfico de Proporção (100% Stacked Bar):")
            print(f"    {calc.render_ascii_bar(pct, width=32)}")

        elif sub_choice == "3":
            val = float(input("Digite o valor original: "))
            pct = float(input("Digite a porcentagem de acréscimo (%): "))
            res = calc.percentage_increase(val, pct)
            print(f"\n>>> Resultado com {pct}% de acréscimo: {res}")
            print(f"    Acréscimo de: +{res - val}")

        elif sub_choice == "4":
            val = float(input("Digite o valor original: "))
            pct = float(input("Digite a porcentagem de desconto (%): "))
            res = calc.percentage_discount(val, pct)
            print(f"\n>>> Resultado com {pct}% de desconto: {res}")
            print(f"    Economia de: -{val - res}")
            print(f"\n📊 Gráfico do Desconto aplicado:")
            print(f"    {calc.render_ascii_bar(pct, width=32)}")
        else:
            print("[X] Opção inválida!")
    except ZeroDivisionError as err:
        print(f"\n[X] Erro: {err}")
    except ValueError as err:
        print(f"\n[X] Erro: Digite apenas números válidos. ({err})")


def interactive_mode() -> None:
    calc = Calculator()
    show_banner()

    while True:
        print("\nOperações disponíveis:")
        print("  [1] Adição (+)")
        print("  [2] Subtração (-)")
        print("  [3] Multiplicação (*)")
        print("  [4] Divisão (/)")
        print("  [5] Porcentagem & Gráficos (%)")
        print("  [6] Potência (^)")
        print("  [7] Raiz Quadrada (√)")
        print("  [8] Ver Histórico")
        print("  [9] Limpar Histórico")
        print("  [0] Sair")

        choice = input("\nEscolha uma opção (0-9): ").strip()

        if choice == "0":
            print("\nAté logo! Obrigado por usar a Calculadora Python.")
            break

        if choice == "5":
            handle_percentage_menu(calc)
            continue

        if choice == "8":
            history = calc.get_history()
            if not history:
                print("\n[!] Histórico vazio.")
            else:
                print("\n--- Histórico de Cálculos ---")
                for i, item in enumerate(history, 1):
                    print(f"  {i}. {item['operation']} = {item['result']}")
            continue

        if choice == "9":
            calc.clear_history()
            print("\n[✓] Histórico limpo com sucesso!")
            continue

        try:
            if choice == "7":
                num = float(input("Digite o número para extrair a raiz: "))
                res = calc.square_root(num)
                print(f"\n>>> Resultado: √{num} = {res}")
            elif choice in ["1", "2", "3", "4", "6"]:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))

                if choice == "1":
                    res = calc.add(a, b)
                    print(f"\n>>> Resultado: {a} + {b} = {res}")
                elif choice == "2":
                    res = calc.subtract(a, b)
                    print(f"\n>>> Resultado: {a} - {b} = {res}")
                elif choice == "3":
                    res = calc.multiply(a, b)
                    print(f"\n>>> Resultado: {a} * {b} = {res}")
                elif choice == "4":
                    res = calc.divide(a, b)
                    print(f"\n>>> Resultado: {a} / {b} = {res}")
                elif choice == "6":
                    res = calc.power(a, b)
                    print(f"\n>>> Resultado: {a} ^ {b} = {res}")
            else:
                print("\n[X] Opção inválida! Escolha entre 0 e 9.")
        except ZeroDivisionError as err:
            print(f"\n[X] Erro: {err}")
        except ValueError as err:
            print(f"\n[X] Erro: {err}")
        except Exception as err:
            print(f"\n[X] Ocorreu um erro inesperado: {err}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora simples em Python via CLI.")
    parser.add_argument("--add", nargs=2, type=float, metavar=("A", "B"), help="Soma A + B")
    parser.add_argument("--sub", nargs=2, type=float, metavar=("A", "B"), help="Subtrai A - B")
    parser.add_argument("--mul", nargs=2, type=float, metavar=("A", "B"), help="Multiplica A * B")
    parser.add_argument("--div", nargs=2, type=float, metavar=("A", "B"), help="Divide A / B")
    parser.add_argument("--pct", nargs=2, type=float, metavar=("TOTAL", "PERC"), help="Calcula PERC% de TOTAL com gráfico")
    parser.add_argument("--sqrt", type=float, metavar="N", help="Raiz quadrada de N")

    args = parser.parse_args()
    calc = Calculator()

    if args.pct:
        total, pct = args.pct[0], args.pct[1]
        res = calc.percentage(total, pct)
        print(f"{pct}% de {total} = {res}")
        print(calc.render_ascii_bar(pct))
    elif args.add:
        print(f"{args.add[0]} + {args.add[1]} = {calc.add(args.add[0], args.add[1])}")
    elif args.sub:
        print(f"{args.sub[0]} - {args.sub[1]} = {calc.subtract(args.sub[0], args.sub[1])}")
    elif args.mul:
        print(f"{args.mul[0]} * {args.mul[1]} = {calc.multiply(args.mul[0], args.mul[1])}")
    elif args.div:
        try:
            print(f"{args.div[0]} / {args.div[1]} = {calc.divide(args.div[0], args.div[1])}")
        except ZeroDivisionError as e:
            print(f"Erro: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.sqrt is not None:
        try:
            print(f"√{args.sqrt} = {calc.square_root(args.sqrt)}")
        except ValueError as e:
            print(f"Erro: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
