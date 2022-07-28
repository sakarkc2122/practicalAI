# AND
from ast import Not


A= 0 #False
B= 1 #True

x = (1 and 0) #x= A and B
print(x)
# >> 0
x = (1 and 1)
print(x)
# >> 1
x = (False and True)
print(x)
# >> False
x = (True and True)
print(x)
# >> True

# OR
x = (0 or 0)
print(x)
x = (1 or 0)
print(x)
x = (1 or 1)
print(x)
x = (False or False)
print(x)
x = (False or True)
print(x)
x = (True or True)
print(x)

# NOT
x = (not 0)
print(x)
# >> True
x = (not True)
print(x)
# >> False

# Implies | Conditional
def conditional(x, z):
  if x == True:
    return z
  return True

#x and z assign value
x = True
z = False
#function call
print(conditional(x, z))

# If and only if | Biconditional
def main(a, b):
  def conditional(a, b):
    if a == True:
      return b
    return True
  A = conditional(a, b)
  B = conditional(b, a)
  if A == B:
    return True
  else:
    return False

a, b = True, False
print(main(a, b))

a, b = True, True
print(main(a, b))

a, b = False, True
print(main(a, b))

a, b = False, False
print(main(a, b))