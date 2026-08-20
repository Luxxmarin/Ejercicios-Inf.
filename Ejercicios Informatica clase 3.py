a = (10 / 5) ** 4 > 15 and (8 + 4) == 12
print(a)  

P, Q = 4, 8
b = not (P <= Q / P) and not (P < 5)
print(b)  

A, B, C = True, False, False
c = not A and not C or B
print(c) 

d = "Bio" + "ingenieria " + "de" + " la " + "UdeA" == "Bio ingeniería de la UdeA"
print(d) 

e = (10 / 2 * 3) 
print (e)

f = (5 + 3 * 8 - 18 / 6)  
print (f)

F = ((5 + 3) * (8 - 18) / 6)  
print (F)

M = 5
print(M > 5)  

x, y = 2, 10
g = (x > 3 and x < 2) or (y > 10 or x == 2)
print(g)

x, y = 9, 5
h = (not (x > 9 and x < 1) or (y > 10 or x != 9))  
print (h)
i = (not ((x > 9 and x < 1) and (y > 10 or x != 9)))  
print (i)

P, Q, R = True, False, False
print(not (P or Q) and (not Q or P)) 
print((P and R) or (Q or R) or (P and not Q)) 