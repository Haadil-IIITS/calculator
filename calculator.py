import calculator.art1 as art1
print(art1.logo)
def add(n1, n2):
    output=n1+n2
    print(f"{n1} {operation} {n2} = ",output)
    return output
def sub(n1,n2):
    output = n1 - n2
    print(f"{n1} {operation} {n2} = ", output)
    return output
def mul(n1,n2):
    output = n1 * n2
    print(f"{n1} {operation} {n2} = ", output)
    return output
def div(n1,n2):
    output = n1 / n2
    print(f"{n1} {operation} {n2} = ", output)
    return output
again='n'
while True:
    if again=='n':
        n1=int(input("Whats's the first number?: "))
    else:
        n1=output
    print("+\n-\n*\n/")
    operation=str(input("Pick an operation: "))
    n2=int(input("enter next number"))
    if operation=='+':
        output=add(n1,n2)