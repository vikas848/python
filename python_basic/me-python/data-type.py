#int -- integer me number store kiya jata h ex- 0 , 1, -1 .

a = 10 
print(a)

b = -5
print(type(b))


#float -- float me decimal number store kiya jata h ex- 0.0 , 1.5 , -1.0 .


c = 0.1
print(c)

d = -5.1
print(type(d))


#srting -- Characters ka sequence hota hai jo text represent karta hai. Strings ko " " ya ' ' ke andar likha jata hai.

e = "vikas"
print(e)


f= "vikas"
print(type(f))

j= "vikas"+" "+"singh"
print(type(j))


k= "devil"
print(k[3])

l= "me"*5
print(l)

#tuple -- Ordered collection of elements jo immutable hoti hai (iska data change nahi ho sakta). Tuple ko () ke andar likhte hain.

# g = (0.0, 1.7, -0.2, 7, "vikas")
# print(type(g))


# h = 2, 3, 4, 5
# i = h ,9
# print(type(i))
# print(i)


# m = (1,2,3,4,5)
# print(m)
# print(type(m))

# m = (1,2,3,4,5,6,7)
# print(m)

n = input("Enter your name: ")
print(n)
o = n
print(type(o))


n = get_dynamic_input("Enter something: ")
print("Value:", n)
print("Type:", type(n))    