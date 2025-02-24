import sympy as sp

def checkHomogeneityFormula(self):

    mInput = self.mXYInput.text()
    nInput = self.nXYInput.text()

    x, y = sp.symbols('x y')

    try:
        M = sp.sympify(mInput)
        N = sp.sympify(nInput)

        degreeM = M.as_poly(x, y).degree()
        degreeN = N.as_poly(x, y).degree()

        if degreeM == degreeN:
            result = f"The equation is homogeneous of degree {degreeM}."
        else:
            result = "The equation is not homogeneous."

        self.resultText.setText(result)

    except Exception as e:
        self.resultText.setText("Invalid input. Please enter valid equations for M(x, y) and N(x, y)")