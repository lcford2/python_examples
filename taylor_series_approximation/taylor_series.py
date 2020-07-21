
from scipy.special import factorial

class TaylorSerApprox(object):
    """
    A simple python representation of the Taylor Series Approximation.
    Taylor Series Approximations are often useful in representing non-linear 
    equations as a linear summation of terms relating to those non-linear equations.
    
    This allows the user to perform an approximation of arbitrary order, 
    as long as the function and the derivatives of that function are provided. 
    """
    def __init__(self, functions):
        """
        The `functions` argument should be an iterator containing in the first
        position the actual function to be evaluated. The remaining items should 
        be the derivatives of the function to be evaluated ascendingly ranked
        based on their order.
        e.g. functions = [function, prime1, prime2, ..., primeN]
        Where function is what should be evaluated, prime# are the derivatives of 
        function, and the numbers on prime# correspond to their rank.
        
        Arguments:
            functions {iterable} -- container of evaluation function and its derivatives
        """
        self.functions = list(functions)
        self.order = len(functions)
        
    
    def approximate(self, x, a):
        """
        Use this method to approximate the function supplied as the first
        item in the `functions` argument when instantiating the class at the 
        value of `x` (f(x)). Choose `a` such that it can easily be calculated by the 
        the function of interest. 

        The basic form of the equation is as follows:
        f(x) ~ f(a) + f'(a)(x-a)/1! + f"(a)((x-a)^2)/2! + f'''(a)((x-a)^3)/3! ... etc
        
        Arguments:
            x {float} -- desired value for function evaluation
            a {float} -- variable used in the approximation to prevent difficult evaluations of your function
        
        Returns:
            float -- Taylor Series Approximation of f(x)
        """
        fun = self.functions[0]
        initial = fun(a)
        for i, fun in enumerate(self.functions[1:]):
            coef = fun(a)/factorial(i+1)
            right = (x-a)**(i+1)
            initial += coef*right
        return initial
    
    def __str__(self):
        return f"Taylor Series Approximation of order {self.order} for {self.functions[0].__name__}"

def example(x, a):
    def function(x):
        return 5*x**3 + 6*x**2 - 4*x + 7

    def prime1(x):
        return 15*x**2 + 12*x - 4

    def prime2(x):
        return 30*x + 12

    def prime3(x):
        return 30

    O1 = [function]
    O2 = [function, prime1]
    O3 = [function, prime1, prime2]
    O4 = [function, prime1, prime2, prime3]

    orders = [("O1", O1), ("O2", O2), ("O3", O3), ("O4", O4)]
    actual = function(x)
    for name, funcs in orders:
        tsa = TaylorSerApprox(funcs)
        answer = tsa.approximate(x, a)
        print(tsa)
        print(f"Order {name}: Actual Value = {actual}; Approximation = {answer}")
        

if __name__ == "__main__":
    x = 0.05
    a = 1
    example(x, a)
