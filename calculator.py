def multiply(a,b):
    return a * b

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def divide(a,b):
	return a/b

def square(a):
    return a * a

def cube(a):
    return a ** 3

def square_n_times(a, n):
      result = a
      total = 0
      for _ in range(n):
          result = square(result)
          total += result
      return total
      
print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)