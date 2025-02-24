import sympy as sp

def checkExactnessFormula(self):

    mInput = self.mXYInput.text()
    nInput = self.nXYInput.text()

    x, y = sp.symbols('x y')

    try:
        M = sp.sympify(mInput)
        N = sp.sympify(nInput)

        partial_M_y = sp.diff(M,y)
        partial_N_x = sp.diff(N,x)

        if partial_M_y == partial_N_x:
            result = "The equation is exact."
        else:
            result = "The equation is not exact."

        self.resultText.setText(result)

    except Exception as e:
        self.resultText.setText("Invalid Input. Please enter a valid equations for M(x, y) and N(x, y).")