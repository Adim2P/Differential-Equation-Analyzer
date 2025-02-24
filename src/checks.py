from sympy import symbols, diff, sympify

# Function to check if the equation is exact
def check_exactness(m_expr, n_expr):
    try:
        x, y = symbols('x y')

        # Convert the input expressions to sympy expressions
        M = sympify(m_expr)
        N = sympify(n_expr)

        # Calculate partial derivatives
        dM_dy = diff(M, y)
        dN_dx = diff(N, x)

        # Check exactness
        if dM_dy == dN_dx:
            return "The equation is exact."
        else:
            return "The equation is not exact."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to check if the equation is homogeneous and return the degree
def check_homogeneity(m_expr, n_expr):
    try:
        x, y = symbols('x y')

        # Convert the input expressions to sympy expressions
        M = sympify(m_expr)
        N = sympify(n_expr)

        # Calculate degree of both functions
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
    degree = None  # Start with None to check for consistent degree across all terms

    for term in terms:
        # Get the degree of the current term with respect to both x and y
        if term.has(x) and term.has(y):
            term_degree = term.as_poly().degree(x) + term.as_poly().degree(y)
        elif term.has(x):
            term_degree = term.as_poly().degree(x)
        elif term.has(y):
            term_degree = term.as_poly().degree(y)
        else:
            term_degree = 0  # If the term has no x or y, degree is 0

        # Check if degree is consistent across all terms
        if degree is None:
            degree = term_degree
        elif degree != term_degree:
            return -1  # If degrees don't match, return -1 indicating inconsistency

    return degree