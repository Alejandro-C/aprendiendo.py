'''
Si gasto hasta $100, pago con dinero en efectivo. Sino, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Sino, pago con tarjeta de crédito.
'''

# if    si
# elif  sino, si
# else  sino

valorCompra = int(input('Digite el valor de la compra: '))

if valorCompra <= 100:
    print('Pago en efectivo')
elif valorCompra > 100 and valorCompra < 300:
    print('Pago con tarjeta de debito')
else:
    print('Pago con targeta de credito')