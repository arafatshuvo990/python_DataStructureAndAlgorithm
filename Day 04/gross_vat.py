def calculaate_vat(price, vat_rate):
    return price + (price*vat_rate)/100

price = [100,200,231,144]

for prices in price:
    print(f"Regular price is {prices} and after vat - {calculaate_vat(prices, 30)}")
