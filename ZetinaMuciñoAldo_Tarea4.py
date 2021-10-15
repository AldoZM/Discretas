A={1,2,3,4}
B={2,4,6,8}
C={3,4,5,6}
U={1,2,3,4,5,6,7,8,9}

Z = A|B
X = A|C
W = B|C
C = B|B

Z1 = A&B
X1 = A&C
W1 = B&C
C1 = B&B

Z2 = A-B
X2 = A-C
W2 = B-C
C2 = B-B

Z3 = A-U
X3 = B-U
W3 = (A&B)-U
C3 = (A|B)-U
M = A
N = (B-C)-U



print("La union de Z = ", Z)
print("La union de X = ", X)
print("La union de W = ", W)
print("La union de C = ", C)


print("La interseccion de Z1 = ", Z1)
print("La interseccion de X1 = ", X1)
print("La interseccion de W1 = ", W1)
print("La interseccion de C1 = ", C1)

print("La diferencia de Z2 = ", Z2)
print("La diferencia de X1 = ", X2)
print("La diferencia de W1 = ", W2)
print("La diferencia de C1 = ", C2)

print("La convinacion de Z3 = ", Z3)
print("La convinacion de X3 = ", X3)
print("La convinacion de W3 = ", W3)
print("La convinacion de C3 = ", C3)
print("La convinacion de M = ", M)
print("La convinacion de N = ", N)

