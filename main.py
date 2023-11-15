def calculate_binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient (n choose k).
    """
    if k == 0 or k == n:
        return 1
    if k > n or k < 0:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= (n - i + 1) / i
    return int(result)

def calculate_binomial_probability(n, p, q, k):
    """
    Calculate the binomial probability for P(X = k) given n trials, success probability p, and failure probability q.
    """
    return calculate_binomial_coefficient(n, k) * (p ** k) * (q ** (n - k))

def calculate_cumulative_probability(n, p, q, k):
    """
    Calculate the cumulative binomial probability for P(X <= k) given n trials, success probability p, and failure probability q.
    """
    cumulative_probability = 0
    for i in range(k + 1):
        cumulative_probability += calculate_binomial_probability(n, p, q, i)
    return cumulative_probability

def calculate_probability(n, p, q, condition, k):
    """
    Calculate the specified binomial probability given n trials, success probability p, failure probability q, condition, and k.
    """
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

# Get user input
n_trials = int(input("Enter the number of trials (n): "))
success_probability = float(input("Enter the probability of success (p): "))
failure_probability = 1 - success_probability
condition = input("Enter the condition (=, <, <=, >, >=): ")
k_value = int(input("Enter the value of k: "))

# Calculate the specified probability
result_probability = calculate_probability(n_trials, success_probability, failure_probability, condition, k_value)

# Display the result
print(f"Probability: {result_probability:.4f}")
