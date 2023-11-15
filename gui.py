import tkinter as tk
from tkinter import ttk

def calculate_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    if k > n or k < 0:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= (n - i + 1) / i
    return int(result)

def calculate_binomial_probability(n, p, q, k):
    return calculate_binomial_coefficient(n, k) * (p ** k) * (q ** (n - k))

def calculate_cumulative_probability(n, p, q, k):
    cumulative_probability = 0
    for i in range(k + 1):
        cumulative_probability += calculate_binomial_probability(n, p, q, i)
    return cumulative_probability

def calculate_probability(n, p, q, condition, k):
    if condition == "=":
        return calculate_binomial_probability(n, p, q, k)
    elif condition == "<":
        return calculate_cumulative_probability(n, p, q, k - 1)
    elif condition == "<=":
        return calculate_cumulative_probability(n, p, q, k)
    elif condition == ">":
        return 1 - calculate_cumulative_probability(n, p, q, k)
    elif condition == ">=":
        return 1 - calculate_cumulative_probability(n, p, q, k - 1)
    else:
        raise ValueError("Invalid condition. Use '=', '<', '<=', '>', or '>='.")

def format_latex_formula(n, p, q, condition, k):
    formula = f"P(X {condition} {k}) = "
    if condition == "=":
        formula += f"{p}^{{{k}}} \\cdot {q}^{{{n - k}}}"
    elif condition in ("<", "<="):
        formula += f"\\sum_{{i=0}}^{{{k}}} {calculate_binomial_coefficient(n, k)} \\cdot {p}^{{i}} \\cdot {q}^{{{{{n} - i}}}}"
    elif condition in (">", ">="):
        formula += f"1 - \\sum_{{i=0}}^{{{k - 1}}} {calculate_binomial_coefficient(n, k)} \\cdot {p}^{{i}} \\cdot {q}^{{{{{n} - i}}}}"
    return formula

class BinomialCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binomial Probability Calculator")

        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10))
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Number of Trials (n):").grid(row=0, column=0, sticky="w")
        self.n_var = tk.IntVar()
        ttk.Entry(input_frame, textvariable=self.n_var).grid(row=0, column=1)

        ttk.Label(input_frame, text="Probability of Success (p):").grid(row=1, column=0, sticky="w")
        self.p_var = tk.DoubleVar()
        ttk.Entry(input_frame, textvariable=self.p_var).grid(row=1, column=1)

        ttk.Label(input_frame, text="Condition (=, <, <=, >, >=):").grid(row=2, column=0, sticky="w")
        self.condition_var = tk.StringVar(value="=")
        ttk.Entry(input_frame, textvariable=self.condition_var).grid(row=2, column=1)

        ttk.Label(input_frame, text="Value of k:").grid(row=3, column=0, sticky="w")
        self.k_var = tk.IntVar()
        ttk.Entry(input_frame, textvariable=self.k_var).grid(row=3, column=1)

        # Calculate Button
        ttk.Button(input_frame, text="Calculate", command=self.calculate_probability).grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # Output Frame
        output_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10))
        output_frame.grid(row=1, column=0, padx=10, pady=10)

        self.output_text = tk.Text(output_frame, height=10, width=80, wrap="word", state="disabled")
        self.output_text.grid(row=0, column=0)

    def calculate_probability(self):
        n = self.n_var.get()
        p = self.p_var.get()
        q = 1 - p
        condition = self.condition_var.get()
        k = self.k_var.get()

        probability = calculate_probability(n, p, q, condition, k)
        formula = format_latex_formula(n, p, q, condition, k)

        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Probability: {probability:.4f}\n\nFormula:\n{formula}")
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinomialCalculatorApp(root)
    root.mainloop()
