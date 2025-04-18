# Problem 4: Function Composition
# Given two functions, compose them into a new function that applies the second function to its input and then applies the first function to the result.
# For example, if the first function is `f(x) = x^2` and the second function is `g(x) = x + 1`, then the composed function should be `h(x) = f(g(x)) = (x + 1)^2`.


# Example usage:
if __name__ == "__main__":


    def compose(self, func1, func2) :
        """
        This function takes two functions as input and returns a new function that is the composition of the two.
        The new function applies func2 to its arguments and then applies func1 to the result of func2.
        """

        def inner_function(*args, **kwargs):
            return func1(func2(*args, **kwargs))
        return inner_function
    

    # def compose(self, f, g):
    #     """
    #     This function takes two functions f and g as input and returns a new function that is the composition of f and g.
    #     The composition of two functions f and g is defined as (f o g)(x) = f(g(x)).
    #     """
    #     return lambda x: f(g(x))
    
    def inc(x):
        return x + 1
    
    def square(x):
        return x * x
    
    h = compose(square, inc)
    print(h(6))  # Output: 49 (since (6 + 1)^2 = 7^2 = 49)

    # Test cases
    assert compose(square, inc)(6) == 49  # (6 + 1)^2 = 7^2 = 49
   
    print("All test cases passed!")
