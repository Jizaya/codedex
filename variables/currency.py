#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.
pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))
usd = (pesos * .06) + (soles * .27) + (reais * .20)
print(f"You have ${usd} in US Dollars!")
