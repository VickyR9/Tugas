print('=== Chasier ===')

item_name = input('Input item Name :')
price = int(input('Input Price item :'))
quantity = int(input('item Quantity'))
total_money = int(input('Total Money You Pay'))
re_money = total_money - quantity * price

#Note

text = f'''
===================================
            Fatin's Shop
===================================
- Your Item         :  {item_name}
- Your Item Price   :  {price}
- Your Item Quantity:  {quantity}
- Your Total Money  :  {total_money}
- Your Total Change :  IDR{re_money}
'''

file = open('Nota.txt','w')


file.write(text)