'''
union   |

'''
A = {1,2,3,4}
B={4,5,6,7}
#Sea el conjunto U
U = A | B

print("Conjunto de union: ", U)


'''
Interseccion    &
'''

C = {1,2,3,5}
D = {3,5,4,8,0}

I = D & C

print("Conjunto de interseccion: ", I)

'''
Diferencia -
'''

E ={2,3,6,2,34,7}

F= {6,2}

D2= E-F
D1 = F-E
print("Conjunto de la Diferencia (E-F): ", D2)
print("Conjunto de la Diferencia (F-E): ", D1)

'''
Igualdad ==
'''

G={'a','b','c'}
H={'c','b','a'}

if G == H:
    print("si son iguales")
else:
    print("No son iguales")

'''
Subconjuntos 
'''

R ={1,2,3,4}
J={2,3}

if J.issubset(R):
    print("El conjunto J es subconjunto del conjunto R")
else:
    print("El conjunto J no es subconjunto del conjunto R")
