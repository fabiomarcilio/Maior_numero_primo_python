numero = int(input('Entre com um número inteiro:'))
i = 1
x = 1
while (i <= numero):
    result = 0
    x = 1
    while(x <= i):
        if(i % x == 0):
            result = result + 1
            x = x + 1
        else:
            x = x + 1

    if (result > 2):
        i = i + 1
    else:
        primo = i
        i = i + 1
print(primo)
    
