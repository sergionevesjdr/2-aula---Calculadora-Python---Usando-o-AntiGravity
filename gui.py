"""
Interface Gráfica (GUI) para a Calculadora Python usando Tkinter
Não requer instalação de nenhuma biblioteca externa (Tkinter já vem integrado ao Python).
Para executar no seu computador:
    python gui.py
"""

import tkinter as tk
from tkinter import messagebox
from calculator import Calculator


class CalculatorGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculadora Python (PyCalc)")
        self.root.geometry("360x530")
        self.root.resizable(False, False)
        self.root.configure(bg="#0F172A")

        self.calc = Calculator()
        self.expression = ""

        # Display
        self.display_var = tk.StringVar(value="0")
        self.create_display()
        self.create_buttons()

    def create_display(self) -> None:
        display_frame = tk.Frame(self.root, bg="#020617", bd=0)
        display_frame.pack(fill="both", padx=14, pady=(16, 10))

        label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Consolas", 28, "bold"),
            bg="#020617",
            fg="#F8FAFC",
            anchor="e",
            padx=12,
            pady=16
        )
        label.pack(fill="both")

    def create_buttons(self) -> None:
        btn_frame = tk.Frame(self.root, bg="#0F172A")
        btn_frame.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        buttons = [
            ("C", 0, 0, "#EF4444", self.clear),
            ("√", 0, 1, "#334155", self.square_root),
            ("% Gráfico", 0, 2, "#0D9488", self.open_percentage_window),
            ("/", 0, 3, "#3B82F6", lambda: self.press("/")),

            ("7", 1, 0, "#1E293B", lambda: self.press("7")),
            ("8", 1, 1, "#1E293B", lambda: self.press("8")),
            ("9", 1, 2, "#1E293B", lambda: self.press("9")),
            ("*", 1, 3, "#3B82F6", lambda: self.press("*")),

            ("4", 2, 0, "#1E293B", lambda: self.press("4")),
            ("5", 2, 1, "#1E293B", lambda: self.press("5")),
            ("6", 2, 2, "#1E293B", lambda: self.press("6")),
            ("-", 2, 3, "#3B82F6", lambda: self.press("-")),

            ("1", 3, 0, "#1E293B", lambda: self.press("1")),
            ("2", 3, 1, "#1E293B", lambda: self.press("2")),
            ("3", 3, 2, "#1E293B", lambda: self.press("3")),
            ("+", 3, 3, "#3B82F6", lambda: self.press("+")),

            ("±", 4, 0, "#334155", self.toggle_sign),
            ("0", 4, 1, "#1E293B", lambda: self.press("0")),
            (".", 4, 2, "#334155", lambda: self.press(".")),
            ("=", 4, 3, "#10B981", self.calculate),
        ]

        for text, row, col, bg_color, cmd in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 11 if "Gráfico" in text else 14, "bold"),
                bg=bg_color,
                fg="#FFFFFF",
                activebackground="#475569",
                activeforeground="#FFFFFF",
                bd=0,
                relief="flat",
                command=cmd,
                cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

    def press(self, char: str) -> None:
        if self.display_var.get() == "0" and char not in [".", "/", "*", "-", "+"]:
            self.expression = char
        else:
            self.expression += char
        self.display_var.set(self.expression)

    def clear(self) -> None:
        self.expression = ""
        self.display_var.set("0")

    def toggle_sign(self) -> None:
        if not self.expression:
            return
        try:
            val = float(self.expression)
            val = -val
            self.expression = str(int(val)) if val.is_integer() else str(val)
            self.display_var.set(self.expression)
        except ValueError:
            pass

    def square_root(self) -> None:
        try:
            val = float(self.display_var.get())
            result = self.calc.square_root(val)
            formatted = str(int(result)) if result.is_integer() else f"{result:.4f}".rstrip("0").rstrip(".")
            self.display_var.set(formatted)
            self.expression = formatted
        except ValueError as err:
            messagebox.showerror("Erro Matemático", str(err))

    def calculate(self) -> None:
        if not self.expression:
            return
        try:
            safe_dict = {"__builtins__": {}}
            result = eval(self.expression, safe_dict, {})
            formatted = str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
            self.display_var.set(formatted)
            self.expression = formatted
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida!")
            self.clear()
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida.")
            self.clear()

    def open_percentage_window(self) -> None:
        """Abre a janela gráfica com Donut Chart e Barra 100%."""
        win = tk.Toplevel(self.root)
        win.title("Porcentagem & Gráfico")
        win.geometry("380x520")
        win.resizable(False, False)
        win.configure(bg="#0F172A")

        title = tk.Label(
            win,
            text="📊 Gráfico de Porcentagem (Donut & Barra)",
            font=("Segoe UI", 12, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        )
        title.pack(pady=(12, 6))

        frame_input = tk.Frame(win, bg="#0F172A")
        frame_input.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_input, text="Valor Total:", bg="#0F172A", fg="#94A3B8", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=2)
        total_entry = tk.Entry(frame_input, font=("Consolas", 11), bg="#1E293B", fg="#FFFFFF", insertbackground="white")
        total_entry.insert(0, "200")
        total_entry.grid(row=0, column=1, pady=2, padx=(10, 0))

        tk.Label(frame_input, text="Porcentagem (%):", bg="#0F172A", fg="#94A3B8", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=2)
        pct_entry = tk.Entry(frame_input, font=("Consolas", 11), bg="#1E293B", fg="#FFFFFF", insertbackground="white")
        pct_entry.insert(0, "35")
        pct_entry.grid(row=1, column=1, pady=2, padx=(10, 0))

        result_label = tk.Label(win, text="35% de 200 = 70.0 (Restante: 130.0)", font=("Segoe UI", 10, "bold"), bg="#0F172A", fg="#10B981")
        result_label.pack(pady=6)

        canvas = tk.Canvas(win, width=320, height=260, bg="#020617", highlightthickness=1, highlightbackground="#334155")
        canvas.pack(pady=8)

        def draw_charts():
            try:
                tot = float(total_entry.get())
                pct = float(pct_entry.get())
                pct_clamped = max(0.0, min(100.0, pct))
                part = self.calc.percentage(tot, pct)
                rest = tot - part

                result_label.config(text=f"{pct}% de {tot} = {part:.2f} (Restante: {rest:.2f})")
                canvas.delete("all")

                # Donut Chart
                canvas.create_arc(60, 20, 260, 220, start=0, extent=359.9, fill="#334155", outline="")
                angle = (pct_clamped / 100.0) * 360.0
                if angle > 0:
                    canvas.create_arc(60, 20, 260, 220, start=90, extent=-angle, fill="#14B8A6", outline="")
                canvas.create_oval(95, 55, 225, 185, fill="#020617", outline="")
                canvas.create_text(160, 110, text=f"{pct:.1f}%", fill="#FFFFFF", font=("Segoe UI", 20, "bold"))
                canvas.create_text(160, 135, text=f"Parte: {part:.1f}", fill="#38BDF8", font=("Segoe UI", 9))

                # Barra 100% Horizontal
                bar_y = 230
                bar_w = 260
                bar_x = 30
                canvas.create_rectangle(bar_x, bar_y, bar_x + bar_w, bar_y + 16, fill="#334155", outline="")
                filled_w = (pct_clamped / 100.0) * bar_w
                if filled_w > 0:
                    canvas.create_rectangle(bar_x, bar_y, bar_x + filled_w, bar_y + 16, fill="#10B981", outline="")

            except ValueError:
                messagebox.showerror("Erro", "Insira valores numéricos válidos!")

        btn_calc = tk.Button(
            win,
            text="Calcular & Atualizar Gráfico",
            font=("Segoe UI", 10, "bold"),
            bg="#0D9488",
            fg="white",
            relief="flat",
            command=draw_charts,
            cursor="hand2"
        )
        btn_calc.pack(pady=4)
        draw_charts()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
