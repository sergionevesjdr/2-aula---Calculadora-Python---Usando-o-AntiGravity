"""
Calculadora Simples em Python
Módulo principal contendo a classe Calculator com suporte a operações aritméticas,
cálculos avançados de porcentagem, geração de gráficos em barra de texto (ASCII)
e gerenciamento de histórico.
"""

from typing import List, Dict, Union, Optional
import math

Number = Union[int, float]


class Calculator:
    """Classe que implementa operações matemáticas e gerencia o histórico de cálculos."""

    def __init__(self) -> None:
        """Inicializa a calculadora com histórico e memória vazios."""
        self._history: List[Dict[str, Union[str, Number]]] = []
        self._memory: float = 0.0

    @property
    def memory(self) -> float:
        """Retorna o valor atual armazenado na memória."""
        return self._memory

    def memory_store(self, value: Number) -> None:
        """Armazena um valor na memória."""
        self._memory = float(value)

    def memory_add(self, value: Number) -> None:
        """Adiciona um valor à memória (M+)."""
        self._memory += float(value)

    def memory_subtract(self, value: Number) -> None:
        """Subtrai um valor da memória (M-)."""
        self._memory -= float(value)

    def memory_clear(self) -> None:
        """Limpa a memória (MC)."""
        self._memory = 0.0

    def add(self, a: Number, b: Number) -> Number:
        """Soma dois números: a + b."""
        result = a + b
        self._record(f"{a} + {b}", result)
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtrai dois números: a - b."""
        result = a - b
        self._record(f"{a} - {b}", result)
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiplica dois números: a * b."""
        result = a * b
        self._record(f"{a} * {b}", result)
        return result

    def divide(self, a: Number, b: Number) -> float:
        """
        Divide dois números: a / b.
        
        Raises:
            ZeroDivisionError: Se b for igual a zero.
        """
        if b == 0:
            raise ZeroDivisionError("Erro matemático: Divisão por zero não é permitida.")
        result = a / b
        self._record(f"{a} / {b}", result)
        return result

    def power(self, base: Number, exponent: Number) -> Number:
        """Calcula a potência: base ** exponent."""
        result = math.pow(base, exponent)
        if result.is_integer() and isinstance(base, int) and isinstance(exponent, int) and exponent >= 0:
            result = int(result)
        self._record(f"{base} ^ {exponent}", result)
        return result

    def square_root(self, value: Number) -> float:
        """
        Calcula a raiz quadrada: √value.
        
        Raises:
            ValueError: Se o valor for negativo.
        """
        if value < 0:
            raise ValueError("Erro matemático: Raiz quadrada de número negativo não permitida nos reais.")
        result = math.sqrt(value)
        self._record(f"√{value}", result)
        return result

    # ==========================================
    # SUÍTE DE OPERAÇÕES DE PORCENTAGEM
    # ==========================================

    def percentage(self, total: Number, percent: Number) -> float:
        """
        Calcula o valor percentual de um total: (total * percent) / 100.
        Exemplo: 15% de 200 = 30.0
        """
        result = (total * percent) / 100.0
        self._record(f"{percent}% de {total}", result)
        return result

    def percentage_ratio(self, part: Number, total: Number) -> float:
        """
        Calcula quantos por cento uma parte representa de um total: (part / total) * 100.
        Exemplo: 50 representa 25% de 200.
        
        Raises:
            ZeroDivisionError: Se o total for zero.
        """
        if total == 0:
            raise ZeroDivisionError("Erro matemático: O total não pode ser zero para cálculo de proporção percentual.")
        result = (part / total) * 100.0
        self._record(f"Proporção de {part} em {total}", f"{result:.2f}%")
        return result

    def percentage_increase(self, value: Number, percent: Number) -> float:
        """
        Aplica um acréscimo percentual: value + (value * percent / 100).
        Exemplo: R$ 100 com 15% de aumento = R$ 115.0
        """
        increase = (value * percent) / 100.0
        result = value + increase
        self._record(f"{value} + {percent}%", result)
        return result

    def percentage_discount(self, value: Number, percent: Number) -> float:
        """
        Aplica um desconto percentual: value - (value * percent / 100).
        Exemplo: R$ 200 com 20% de desconto = R$ 160.0
        """
        discount = (value * percent) / 100.0
        result = value - discount
        self._record(f"{value} - {percent}%", result)
        return result

    def render_ascii_bar(self, percent: float, width: int = 30) -> str:
        """
        Gera uma representação gráfica em barra 100% (Progress Bar / Stacked Bar).
        Segundo especialistas em visualização de dados (Cole Knaflic, Stephen Few),
        a barra horizontal é a forma mais precisa e intuitiva para o cérebro humano
        interpretar proporções de porcentagem (parte vs. todo).
        
        Exemplo de saída:
        [███████████████░░░░░░░░░░░░░░░] 50.0%
        """
        clamped = max(0.0, min(100.0, float(percent)))
        filled_length = int(round(width * clamped / 100.0))
        empty_length = width - filled_length

        filled_char = "█"
        empty_char = "░"

        bar = filled_char * filled_length + empty_char * empty_length
        return f"[{bar}] {percent:.1f}%"

    def modulo(self, a: Number, b: Number) -> Number:
        """
        Retorna o resto da divisão inteira: a % b.
        
        Raises:
            ZeroDivisionError: Se b for zero.
        """
        if b == 0:
            raise ZeroDivisionError("Erro matemático: Módulo por zero não é permitido.")
        result = a % b
        self._record(f"{a} % {b}", result)
        return result

    def _record(self, operation: str, result: Union[Number, str]) -> None:
        """Salva a operação realizada no histórico."""
        self._history.append({"operation": operation, "result": result})

    def get_history(self) -> List[Dict[str, Union[str, Number]]]:
        """Retorna uma cópia do histórico de operações."""
        return list(self._history)

    def clear_history(self) -> None:
        """Limpa todo o histórico de operações."""
        self._history.clear()


if __name__ == "__main__":
    calc = Calculator()
    print("=" * 45)
    print("   🐍 TESTE DIRETO DA CALCULADORA PYTHON   ")
    print("=" * 45)
    print("1. Soma: 125 + 75 =", calc.add(125, 75))
    print("2. Subtração: 100 - 35 =", calc.subtract(100, 35))
    print("3. Multiplicação: 8 * 7 =", calc.multiply(8, 7))
    print("4. Divisão: 100 / 4 =", calc.divide(100, 4))
    print("5. Porcentagem: 15% de 200 =", calc.percentage(200, 15))
    print("6. Gráfico de Barra (15%):", calc.render_ascii_bar(15))
    print("7. Gráfico de Barra (50%):", calc.render_ascii_bar(50))
    print("8. Gráfico de Barra (75%):", calc.render_ascii_bar(75))
    print("=" * 45)
    print("Todos os cálculos foram executados com sucesso!")
