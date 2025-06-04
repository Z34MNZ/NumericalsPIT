import sympy as sp

def newton_raphson(func_expr, x0, tol, max_iter):
    x = sp.symbols('x')
    f = sp.sympify(func_expr)
    f_prime = sp.diff(f, x)

    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    f_prime_lambda = sp.lambdify(x, f_prime, modules=['numpy'])

    steps = []
    current_x = x0

    for i in range(1, max_iter + 1):
        f_val = f_lambda(current_x)
        f_prime_val = f_prime_lambda(current_x)

        if f_prime_val == 0:
            return steps, "Zero derivative. No solution found."

        next_x = current_x - f_val / f_prime_val
        error = abs(next_x - current_x)

        steps.append({
            'Iteration': i,
            'x': current_x,
            'f(x)': f_val,
            "f'(x)": f_prime_val,
            'Next x': next_x,
            'Error': error
        })

        if error < tol:
            break

        current_x = next_x

    return steps, next_x
