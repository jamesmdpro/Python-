from turtle import st


pesos = input("cuentos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar= 5000
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("tienes $ " + dolares + "dolares")