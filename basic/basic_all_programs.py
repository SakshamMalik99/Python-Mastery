import math
#WAP  to add 2 numbers.[R=a+b]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
R=a+b;
print("The Sum is : ",R)
#WAP to multiply 3 numbers.[R=a*b*c]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
c=int(input("Enter Value of c: "))
R=a*b*c;
print("The Sum is : ",R)
#WAP to add 4 numbers.[R=a+b+c+d]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
c=int(input("Enter Value of c: "))
d=int(input("Enter Value of d: "))
R=a+b+c+d
print("The Sum is : ",R)
#WAP to find average 5 numbers[R=(a+b+c+d+e)/5]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
c=int(input("Enter Value of c: "))
d=int(input("Enter Value of d: "))
e=int(input("Enter Value of e: "))
s=a+b+c+d+e
avg=s/5
print("The Sum is : ",s)
print("The Avg is : ",avg)
#WAP to display age after 15 years.[nage =age+15]
a=int(input("Enter your Age of a: "))
na=a+15
print("The New Age  is : ",na)
#WAP to display a3 numbers [R=a*a*a]
a=int(input("Enter Value of a: "))
R=a*a*a
print("The R is : ",R)
#WAP to find the area of squire. [A=a*a]
a=int(input("Enter Value of a: "))
R=a*a
print("The R is : ",R)
#WAP to find the area of rectangle [A=a*b]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
R=a*b
print("The R is : ",R)
#WAP to find the result XN pow(X,N)
x=int(input("Enter Value of x: "))
n=int(input("Enter Value of n: "))
R=pow(x,n)
print("The R is : ",R)
#WAP to find the perimeter of rectangle[A=2*(l+ b) ]
b=int(input("Enter Value of b: "))
l=int(input("Enter Value of l: "))
R=2*(l+b)
print("The R is : ",R)
#WAP to find the area of circle [A=3.14*r*r]
r=int(input("Enter Value of r: "))
R=3.14*r*r
print("The R is : ",R)
#WAP to find the circumference of circle [C=2*3.14*r]
r=int(input("Enter Value of r: "))
R=2*3.14*r
print("The R is : ",R)
#WAP to swap the values of two variables.[a= a + b; b=a – b; a= a – b;]
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
a=a+b
b=a-b
a=a-b
print("The a is : ",a)
print("The b is : ",b)
#WAP to input Hours, Minutes and Seconds and display in seconds. [TS=H*60*60+M*60+S]
h=int(input("Enter Value of h: "))
m=int(input("Enter Value of m: "))
s=int(input("Enter Value of s: "))
TS=h*60*60+m*60+s
print("The TS is : ",TS)
#WAP to input cost and display cost after increasing 25% [cost+(cost*25)/100]
cost=int(input("Enter Value of cost: "))
R=cost+(cost*25)/100
print("The R is : ",R)
#WAP to find the volume of sphere.[v=4/3*3.14*r^3]
r=int(input("Enter Value of r: "))
R=4/3*3.14*pow(r,3)
print("The R is : ",R)
#WAP to find the area of triangle using HEROS formula[s= (a + b + c)/2, R=√(s(s-a)(s-b)(s-c) )]sqrt()
a=int(input("Enter Value of a: "))
b=int(input("Enter Value of b: "))
c=int(input("Enter Value of c: "))
s= (a + b + c)/2
R=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The Sum is : ",s)
print("The R is : ",R)
#WAP to take principal, rate and time and display C.I. (Compound Interest) CI=p*(1+R/100)^ T pow()
p=int(input("Enter Value of p: "))
r=int(input("Enter Value of r: "))
t=int(input("Enter Value of t: "))
CI=p*pow((1+r/100),t)

print("The CI is : ",CI)
#WAP to calculate sum of 5 subjects & find percentage[TOT=s1+s2+s3+s4+s5,Per=TOT/5]
s1=int(input("Enter Value of s1: "))
s2=int(input("Enter Value of s2: "))
s3=int(input("Enter Value of s3: "))
s4=int(input("Enter Value of s4: "))
s5=int(input("Enter Value of s5: "))
TOT=s1+s2+s3+s4+s5
print("The TOT is : ",TOT)
Per=TOT/5
print("The Per. is : ",Per)
#WAP which accept temperature in Fahrenheit and print it in centigrade[c=5/9*(T-32)]
T=int(input("Enter Value of T: "))
C=5/9*(T-32)
print("The C is : ",C)
#WAP which accept temperature in centigrade and print it in Fahrenheit[F=(1.8*T)+32]
T=int(input("Enter Value of T: "))
F=(1.8*T)+32
print("The C is : ",F)
#WAP to calculate simple interest. [SI=(PRT)/100]
P=int(input("Enter Value of p: "))
R=int(input("Enter Value of r: "))
T=int(input("Enter Value of t: "))
SI=(P*R*T)/100
print("The SI is : ",SI)
#WAP to find gross salary [GS=BASIC+DA-PF+HRA]
BASIC=int(input("Enter Value of BASIC: "))
DA=int(input("Enter Value of DA: "))
PF=int(input("Enter Value of PF: "))
HRA=int(input("Enter Value of HRA: "))
GS=BASIC+DA-PF+HRA
print("The GS is : ",GS)


