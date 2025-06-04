import streamlit as st
import pandas as pd
from newton import newton_raphson

st.title("Newton-Raphson Method Calculator")

st.write("### Input Parameters")

func_expr = st.text_input("Enter the function f(x):", value="x**3 - x - 2")
x0 = st.number_input("Initial Guess (x₀):", value=1.5)
tol = st.number_input("Tolerance:", value=1e-6, format="%.1e")
max_iter = st.number_input("Max Iterations:", value=20, step=1)

if st.button("Run Newton-Raphson"):
    try:
        steps, result = newton_raphson(func_expr, x0, tol, max_iter)

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"Root approximated at x = {result:.6f}")
            df = pd.DataFrame(steps)
            st.write("### Iteration Table")
            st.dataframe(df)

            st.line_chart(df.set_index("Iteration")[["Error"]])
    except Exception as e:
        st.error(f"Error: {e}")
