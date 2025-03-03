import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, sympify

# Function to check if the equation is exact
def check_exactness(m_expr, n_expr):
    try:
        x, y = symbols('x y')
        M = sympify(m_expr)
        N = sympify(n_expr)
        
        dM_dy = diff(M, y)
        dN_dx = diff(N, x)
        
        if dM_dy == dN_dx:
            return "The equation is exact."
        else:
            return "The equation is not exact."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to check homogeneity and return degree
def check_homogeneity(m_expr, n_expr):
    try:
        x, y = symbols('x y')
        M = sympify(m_expr)
        N = sympify(n_expr)
        
        m_degree = check_degree(M, x, y)
        n_degree = check_degree(N, x, y)
        
        if m_degree == n_degree:
            return f"Both are homogeneous of degree {m_degree}."
        else:
            return "The functions are not homogeneous or not of the same degree."
    except Exception as e:
        return f"Error: {str(e)}"

# Helper function to find the degree of a homogeneous function
def check_degree(expression, x, y):
    terms = expression.as_ordered_terms()
    degree = None
    
    for term in terms:
        if term.has(x) and term.has(y):
            term_degree = term.as_poly().degree(x) + term.as_poly().degree(y)
        elif term.has(x):
            term_degree = term.as_poly().degree(x)
        elif term.has(y):
            term_degree = term.as_poly().degree(y)
        else:
            term_degree = 0
        
        if degree is None:
            degree = term_degree
        elif degree != term_degree:
            return -1
    
    return degree

def open_exactness_window():
    exactness_window = tk.Toplevel(root)
    exactness_window.title("Check Exactness")
    exactness_window.geometry("400x300")
    
    tk.Label(exactness_window, text="Enter M(x, y):").pack(pady=5)
    m_entry = tk.Entry(exactness_window)
    m_entry.pack(pady=5)
    
    tk.Label(exactness_window, text="Enter N(x, y):").pack(pady=5)
    n_entry = tk.Entry(exactness_window)
    n_entry.pack(pady=5)
    
    def on_check_exactness():
        result = check_exactness(m_entry.get(), n_entry.get())
        messagebox.showinfo("Exactness Check", result)
    
    tk.Button(exactness_window, text="Check Exactness", command=on_check_exactness).pack(pady=10)
    tk.Button(exactness_window, text="Back", command=exactness_window.destroy).pack(pady=10)

def open_homogeneity_window():
    homogeneity_window = tk.Toplevel(root)
    homogeneity_window.title("Check Homogeneity and Degree")
    homogeneity_window.geometry("400x300")
    
    tk.Label(homogeneity_window, text="Enter M(x, y):").pack(pady=5)
    m_entry = tk.Entry(homogeneity_window)
    m_entry.pack(pady=5)
    
    tk.Label(homogeneity_window, text="Enter N(x, y):").pack(pady=5)
    n_entry = tk.Entry(homogeneity_window)
    n_entry.pack(pady=5)
    
    def on_check_homogeneity():
        result = check_homogeneity(m_entry.get(), n_entry.get())
        messagebox.showinfo("Homogeneity Check", result)
    
    tk.Button(homogeneity_window, text="Check Homogeneity", command=on_check_homogeneity).pack(pady=10)
    tk.Button(homogeneity_window, text="Back", command=homogeneity_window.destroy).pack(pady=10)

# Create main window
root = tk.Tk()
root.title("Differential Equation Analyzer")
root.geometry("400x200")

tk.Label(root, text="Choose an Option:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Check Exactness", command=open_exactness_window).pack(pady=5)
tk.Button(root, text="Check Homogeneity and Degree", command=open_homogeneity_window).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
