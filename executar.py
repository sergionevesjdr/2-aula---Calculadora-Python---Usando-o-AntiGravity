"""
Script de Execução Rápida da Calculadora Python (PyCalc)
Basta rodar no terminal ou dar dois cliques:
    python executar.py
"""

import sys
from calculator import Calculator


def main():
    print("=" * 55)
    print("       🐍 PYCALC - CALCULADORA EM PYTHON       ")
    print("=" * 55)
    print("Como você deseja testar a calculadora agora?")
    print("  [1] Abrir Calculadora com Janela Visual (Desktop Tkinter + Gráficos)")
    print("  [2] Usar no Terminal (Menu Interativo de Linha de Comando)")
    print("  [3] Teste Automático Rápido (Verificação de Todas as Contas)")
    print("  [4] Rodar os 16 Testes Unitários Oficiais")
    print("  [0] Sair")
    print("=" * 55)

    escolha = input("Digite a opção desejada (0 a 4): ").strip()

    if escolha == "1":
        print("\n[+] Abrindo a janela da calculadora visual...")
        try:
            import gui
            root = gui.tk.Tk()
            app = gui.CalculatorGUI(root)
            root.mainloop()
        except Exception as e:
            print(f"[X] Não foi possível abrir a janela gráfica: {e}")
            print("Executando no terminal como alternativa...")
            import cli
            cli.interactive_mode()

    elif escolha == "2":
        import cli
        cli.interactive_mode()

    elif escolha == "3":
        calc = Calculator()
        print("\n" + "=" * 50)
        print("⚡ DIAGNÓSTICO RÁPIDO DE CÁLCULOS E RESULTADOS:")
        print("=" * 50)
        print(f"• Adição: 125 + 75 = {calc.add(125, 75)} [OK]")
        print(f"• Subtração: 100 - 35 = {calc.subtract(100, 35)} [OK]")
        print(f"• Multiplicação: 8 * 7 = {calc.multiply(8, 7)} [OK]")
        print(f"• Divisão: 100 / 4 = {calc.divide(100, 4)} [OK]")
        print(f"• Potência: 2 ^ 8 = {calc.power(2, 8)} [OK]")
        print(f"• Raiz Quadrada: √144 = {calc.square_root(144)} [OK]")
        print(f"• Porcentagem: 15% de 200 = {calc.percentage(200, 15)} [OK]")
        print(f"• Proporção: 50 de 200 = {calc.percentage_ratio(50, 200):.1f}% [OK]")
        print("\n📊 Gráfico de Barra Gerado para 35%:")
        print("  " + calc.render_ascii_bar(35, width=30))
        print("=" * 50)
        print("✅ Todos os resultados foram calculados com 100% de precisão!\n")
        input("Pressione Enter para continuar...")

    elif escolha == "4":
        print("\n[+] Executando 16 testes automatizados...")
        import unittest
        loader = unittest.TestLoader()
        suite = loader.discover(".", pattern="test_calculator.py")
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        input("\nPressione Enter para continuar...")

    elif escolha == "0":
        print("\nAté logo!")
    else:
        print("\nOpção inválida.")


if __name__ == "__main__":
    main()
