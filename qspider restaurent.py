print('\t\t\t\t\tWELCOME TO THE QSPIDERS RESTAURENT')
print('1.breakfast\n2.lunch\n3.dinner')
option=input('choose the food type:').lower()
if option=='breakfast':
    print('\t\tMENU')
    print('-'*20)
    print('1.idli---10rs\n2.vada---5rs\n3.dosa---20rs')
    choose=input('enter the food:').lower()
    quantity=int(input(f"enter number of {choose}'s:"))
    if choose=='idli':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*10}rs')
        print('-'*20)
    elif choose=='vada':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*5}rs')
        print('-'*20)
    elif choose=='dosa':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*20}rs')
        print('-'*20)
    else:
        print('food not available')
elif option=='lunch':
    print('\t\tMENU')
    print('-'*20)
    print('1.chicken biryani---200rs\n2.mutton biryani---250rs\n3.veg biryani---180rs')
    choose=input('enter the food:').lower()
    quantity=int(input(f"enter number of {choose}'s:"))
    if choose=='chicken biryani':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*200}rs')
        print('-'*20)
    elif choose=='mutton biryani':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*250}rs')
        print('-'*20)
    elif choose=='veg biryani':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*180}rs')
        print('-'*20)
    else:
        print('food not available')
elif option=='dinner':
    print('\t\tMENU')
    print('-'*20)
    print('1.parotta---15rs\n2.chappathi---15rs\n3.fried rice---120rs')
    choose=input('enter the food:').lower()
    quantity=int(input(f"enter number of {choose}'s:"))
    if choose=='parotta':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*15}rs')
        print('-'*20)
    elif choose=='chappathi':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*15}rs')
        print('-'*20)
    elif choose=='fried rice':
        print('\t\treceipt')
        print('-'*20)
        print(f'order_item:{choose}\nquantity:{quantity}\namount:{quantity*120}rs')
        print('-'*20)
    else:
        print('food not available')