from datetime import datetime
name = input('Enter your name: ')
lists = '''
Rice      Rs20/kg
Sugar     Rs30/kg
Salt      Rs20/kg
Oil       Rs80/kg
Paneer    Rs110/kg
Maggi     Rs50/kg
Boost     Rs90/kg
Colgate   Rs85/kg

'''
# Declaration

price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {'rice':20,
         'sugar':30,
         'salt':20,
         'oil':80,
         'panner':110,
         'Maggi':50,
         'boost':90,
         'Colgate':85}

option = int(input('for list of items press 1  : '))

if option ==1:
    print(lists)
    
for i in range(len(items)):
    inp1 = int(input('if you want buy press 1 or 2 for exit: '))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input('Enter your items: ')
        quantity = int(input('Enter Quantity: '))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity, items, price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) / 100
            finalamount = gst + totalprice
        else:
            print('Sorry...you entered items is not avilable')
    else:
        print('You entered wrong number')
    inp = input('Can i bill the items yes or no: ')
    if inp == 'yes':
        pass
        if finalamount != 0:
            print(25*"=",'AMAR Supermarket',25*"=")
            print(28*" ",'Tirumalasetti')
            print('Name:',name, 30*" ",'Date:',datetime.now())
            print(75*"-")
            print('sno',8*" ",'items',8*" ",'Quantity',3*' ','price')
            for i in range(len(pricelist)):
                print(i, 8*' ',1*' ',ilist[i],10*' ',qlist[i],10*" " ,plist[i])
            print(75*"-")
            print(50 * ' ', 'TotalAmount: ', 'Rs',totalprice)
            print('gst amount',40*' ', 'Rs',gst)
            print(75*"-")
            print(50 * ' ', 'FinalAmount: ', 'Rs',finalamount)
            print(75*"-")
            print(20 * ' ', 'Thanks for visiting')
            print(75*"-")