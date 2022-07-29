# AND
def AND(A, B):
  print("\nConjunction (AND)")
  print("The output of", A, "and", B, "is:", A and B)

# OR
def OR(A, B):
  print("\nDisjunction (OR)")
  print("The output of", A, "or", B, "is:", A or B)

# NOT
def NOT(A):
  print("\nNegation (NOT)")
  print("The output of not", A, "is:", not A)

# Implies | Conditional
def conditional(A, B):
  print("\nImplication (conditional)")
  if A == 'True':
    print("If A =", A, "and B =", B, ", A->B =", B)
  else:
    print("If A =", A, "and B =", B, ", A->B =", True)

# If and only if | Biconditional
def biConditional(a, b):
  print("\nBi-implication (bi-conditional) statement")
  def conditional(a, b):
    if a == True:
      return b
    return True
  A = conditional(a, b)
  B = conditional(b, a)
  if A == B:
    print("If A =", A, "and B =", B, ", A<->B =", True)
  else:
    print("If A =", A, "and B =", B, ", A<->B =", False)

A = input("A: ")
B = input("B: ")
AND(A, B)
OR(A, B)
NOT(A)
conditional(A, B)
biConditional(A, B)