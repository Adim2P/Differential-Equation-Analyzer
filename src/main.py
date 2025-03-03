import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, sympify

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🌸 Differential Equation Analyzer 🌸")
        self.geometry("900x700")
        self.config(bg="#1A1A2E")  
        self.attributes('-transparentcolor', '#1A1A2E')

        self.header = tk.Label(
            self, text="🌸 Differential Equation Analyzer 🌸",
            font=("Comic Sans MS", 36, "bold"), fg="#FFC0CB", bg="#1A1A2E"
        )
        self.header.pack(fill="x", pady=(10, 30))

        self.label = tk.Label(self, text="Choose an Option", font=("Comic Sans MS", 20, "italic"), fg="#E94560", bg="#1A1A2E")
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(self, bg="#1A1A2E")
        self.button_frame.pack(pady=20)

        self.create_button("✨ Check Exactness ✨", self.open_exactness_page, "#FFC0CB")
        self.create_button("⚡ Check Homogeneity ⚡", self.open_homogeneity_page, "#00ADB5")
        self.create_button("❌ Exit", self.quit, "#FF165D")

    def create_button(self, text, command, color):
        btn = tk.Button(
            self.button_frame, text=text, font=("Comic Sans MS", 18, "bold"),
            width=35, height=2, bg=color, fg="#1A1A2E",
            bd=0, relief="flat", highlightthickness=0,
            activebackground="#222831", activeforeground="white",
            command=command
        )
        btn.pack(pady=15)

    def open_exactness_page(self):
        self.withdraw()
        exactness_page = ExactnessPage(self)
        self.wait_window(exactness_page)
        self.deiconify()

    def open_homogeneity_page(self):
        self.withdraw()
        homogeneity_page = HomogeneityPage(self)
        self.wait_window(homogeneity_page)
        self.deiconify()

class AnimePage(tk.Toplevel):
    def __init__(self, parent, title, icon):
        super().__init__(parent)
        self.title(title)
        self.geometry("900x700")
        self.config(bg="#1A1A2E")
        self.attributes('-transparentcolor', '#1A1A2E')

        self.label = tk.Label(
            self, text=f"{icon} {title} {icon}", font=("Comic Sans MS", 30, "bold"),
            fg="#FFC0CB", bg="#1A1A2E", padx=20, pady=20
        )
        self.label.pack(fill="x", pady=(0, 20))

        self.form_frame = tk.Frame(self, bg="#222831", padx=30, pady=30, relief="ridge", borderwidth=3)
        self.form_frame.pack(pady=20)

        self.create_input_field("M(x, y)", "#FFC0CB")
        self.create_input_field("N(x, y)", "#00ADB5")

        self.checkButton = tk.Button(
            self, text="✨ Check Now ✨", font=("Comic Sans MS", 16, "bold"),
            bg="#E94560", fg="white", relief="flat", width=20,
            command=self.process_check
        )
        self.checkButton.pack(pady=20)

        self.resultLabel = tk.Label(self, text="Results will be displayed here.", font=("Comic Sans MS", 18), fg="#FFC0CB", bg="#1A1A2E")
        self.resultLabel.pack(pady=10)

        self.backButton = tk.Button(
            self, text="⬅ Back", font=("Comic Sans MS", 16, "bold"),
            bg="#FF165D", fg="white", relief="flat", width=20,
            command=self.back_to_main
        )
        self.backButton.pack(pady=10)

    def create_input_field(self, label_text, color):
        label = tk.Label(self.form_frame, text=label_text + " =", font=("Comic Sans MS", 20), fg=color, bg="#222831")
        label.pack(anchor="w", pady=(10, 5))

        entry = tk.Entry(self.form_frame, font=("Comic Sans MS", 18), width=40, relief="solid", borderwidth=2)
        entry.pack(pady=(0, 10))

        setattr(self, label_text.split("(")[0].lower(), entry)

    def process_check(self):
        m_expr = self.m.get()
        n_expr = self.n.get()
        try:
            x, y = symbols('x y')
            M = sympify(m_expr)
            N = sympify(n_expr)

            if isinstance(self, ExactnessPage):
                dM_dy = diff(M, y)
                dN_dx = diff(N, x)
                result = "The equation is exact." if dM_dy == dN_dx else "The equation is not exact."
            else:
                m_degree = check_degree(M, x, y)
                n_degree = check_degree(N, x, y)
                result = f"Both are homogeneous of degree {m_degree}." if m_degree == n_degree else "The functions are not homogeneous or not of the same degree."
        except Exception as e:
            result = f"Error: {str(e)}"
        
        self.resultLabel.config(text=result)

    def back_to_main(self):
        self.destroy()
        self.master.deiconify()

class ExactnessPage(AnimePage):
    def __init__(self, parent):
        super().__init__(parent, "Exactness Checking", "📜")

class HomogeneityPage(AnimePage):
    def __init__(self, parent):
        super().__init__(parent, "Homogeneity & Degree", "🔢")

def check_degree(expr, x, y):
    
    expr = sympify(expr)
    if expr.is_Add:
        terms = expr.args
    else:
        terms = [expr]

    degrees = []
    for term in terms:
        degree = 0
        for factor in term.as_ordered_factors():
            base_exp = factor.as_base_exp()
            if isinstance(base_exp, tuple):
                base, exp = base_exp
                if base in [x, y]:
                    degree += exp if exp.is_Number else 1
        degrees.append(degree)

    return max(degrees) if degrees else 0

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()