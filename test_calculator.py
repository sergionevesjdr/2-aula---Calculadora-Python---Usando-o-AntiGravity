"""
Suíte de Testes Unitários para a Calculadora Python
Executa validações completas usando o framework 'unittest' nativo do Python.

Para rodar os testes:
    python -m unittest test_calculator.py -v
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        """Cria uma instância nova da calculadora para cada teste."""
        self.calc = Calculator()

    def test_addition(self) -> None:
        """Testa adição com inteiros e números de ponto flutuante."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self) -> None:
        """Testa subtração."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 12), -7)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiplication(self) -> None:
        """Testa multiplicação."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 6), -18)
        self.assertEqual(self.calc.multiply(0, 999), 0)

    def test_division(self) -> None:
        """Testa divisão comum."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)

    def test_division_by_zero(self) -> None:
        """Testa se a divisão por zero levanta ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_power(self) -> None:
        """Testa exponenciação."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_square_root(self) -> None:
        """Testa raiz quadrada."""
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertEqual(self.calc.square_root(0), 0.0)

    def test_square_root_negative(self) -> None:
        """Testa se raiz quadrada de negativo levanta ValueError."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)

    def test_percentage(self) -> None:
        """Testa cálculo de porcentagem simples (X% de Y)."""
        self.assertEqual(self.calc.percentage(200, 15), 30.0)
        self.assertEqual(self.calc.percentage(500, 20), 100.0)
        self.assertEqual(self.calc.percentage(100, 0), 0.0)

    def test_percentage_ratio(self) -> None:
        """Testa cálculo de proporção percentual."""
        self.assertEqual(self.calc.percentage_ratio(50, 200), 25.0)
        self.assertEqual(self.calc.percentage_ratio(100, 100), 100.0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.percentage_ratio(50, 0)

    def test_percentage_increase(self) -> None:
        """Testa acréscimo percentual."""
        self.assertEqual(self.calc.percentage_increase(100, 15), 115.0)
        self.assertEqual(self.calc.percentage_increase(50, 50), 75.0)

    def test_percentage_discount(self) -> None:
        """Testa desconto percentual."""
        self.assertEqual(self.calc.percentage_discount(200, 20), 160.0)
        self.assertEqual(self.calc.percentage_discount(100, 10), 90.0)

    def test_render_ascii_bar(self) -> None:
        """Testa a geração de gráfico de barra ASCII proporcional."""
        bar_50 = self.calc.render_ascii_bar(50, width=10)
        self.assertEqual(bar_50, "[█████░░░░░] 50.0%")
        bar_100 = self.calc.render_ascii_bar(100, width=10)
        self.assertEqual(bar_100, "[██████████] 100.0%")
        bar_0 = self.calc.render_ascii_bar(0, width=10)
        self.assertEqual(bar_0, "[░░░░░░░░░░] 0.0%")

    def test_modulo(self) -> None:
        """Testa resto da divisão."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)

    def test_memory_functions(self) -> None:
        """Testa operações de memória (M+, M-, Store, Clear)."""
        self.calc.memory_store(50)
        self.assertEqual(self.calc.memory, 50.0)
        self.calc.memory_add(25)
        self.assertEqual(self.calc.memory, 75.0)
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory, 0.0)

    def test_history(self) -> None:
        """Testa gravação e limpeza do histórico de operações."""
        self.calc.add(2, 2)
        self.calc.percentage(200, 10)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)


if __name__ == "__main__":
    unittest.main()
