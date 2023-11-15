from flask import Flask, render_template, request
import math

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def binomial_calculator():
    if request.method == "POST":
        n = int(request.form["n"])
        p = float(request.form["p"])
        q = 1 - p
        condition = request.form["condition"]
        k = int(request.form["k"])

        probability = calculate_probability(n, p, q, condition, k)
        formula = format_latex_formula(n, p, q, condition, k)

        return render_template("index.html", probability=probability, formula=formula)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
