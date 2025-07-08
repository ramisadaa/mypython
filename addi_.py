# result = [ ]
# a = 0 
# b = 1 
# x= int (input ("your number :"))
# def fib(n):    # write Fibonacci series less than n
#     """Print a Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < n:

#         print (a, end=', ')
#         result.append(a)
#         a, b = b, a+b
#     print()
#     print(result)

# # Now call the function we just defined:
# fib(x)

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(50))
import turtle

def star(x, y):
    """Draws a star shape at the given (x, y) coordinates using turtle graphics."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(36):
        turtle.forward(250)
        turtle.left(170)

star(0, 0)
turtle.done()