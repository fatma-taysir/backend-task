# Problem 4: Function Composition

# Example usage:
if __name__ == "__main__":

    def compose(func1, func2) :

        def inner_function(*args, **kwargs):
            return func1(func2(*args, **kwargs))
        return inner_function
        
        
    def inc(x):
        return x + 1
    
    def square(x):
        return x * x
    
    h = compose(square, inc)
    print(h(6))  # Output: 49 (since (6 + 1)^2 = 7^2 = 49)

    # Test cases
    assert compose(square, inc)(6) == 49  # (6 + 1)^2 = 7^2 = 49
   
    print("All test cases passed!")
