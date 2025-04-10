user_password={'dinga':1234,'dingi':5678}
user_pin={'dinga':1111,'dingi':2222}
user_amount={'dinga':1000,'dingi':500}
print('\t\t\t\tWELCOME TO THE BANK OF INDIAN OVERSEAS BANK')
print('_'*50)
u_n=input('enter your name:')
print(' ')
print(f'\t\t\t\twelcome {u_n}.'.upper())
print('_'*50)
print('1.Login\n2.sign up')
option=int(input('choose the option:'))
print('_'*50)
if option==1:
        name=input('enter the user_name:')
        if name in user_password:
                password=int(input('enter the password:'))
                if password == user_password[u_n]:
                        print('1.deposit\n2.withdraw\n3.balance')
                        print('_'*50)
                        option=int(input('choose the option:'))
                        if option==1:
                                pin=int(input('enter the pin:'))
                                if pin == user_pin[u_n]:
                                        amt=int(input('enter the amount:'))
                                        print(f'deposit the money and your bank balance{amt+user_amount[u_n]}')
                                else:
                                        print('invalid pin')
                        elif option==2:
                                pin=int(input('enter the pin:'))
                                if pin == user_pin[u_n]:
                                        amt=int(input('enter the amount:'))
                                        if amt<=user_amount[u_n]:
                                                print(f'withdraw the money and your bank balance {amt-user_amount[u_n]} ')
                                        else:
                                                print('insuficient balance ')
                                else:
                                        print('invalid pin')

                        elif option==3:
                                pin=int(input('enter the pin:'))
                                if pin == user_pin[u_n]:
                                        print(f'your bank balance{user_amount[u_n]}')
                                else:
                                        print('invalid pin')
                        else:
                                print('invalid option')

                else:
                        print('invalid password')

elif option==2:
        name=input('enter the user_name:')
        if name in user_password:
                password=int(input('enter the password:'))
                confirm_password=int(input('confirm_password:'))
                if password==confirm_password:
                        pin=int(input('create new pin:'))
                        print('pin created successfully')
                else:
                        print('wrong password')
else:
        print('invalid option')





























