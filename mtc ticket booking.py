print('\t\t\t\t\tWELCOME TO MTC TICKET BOOKING')
loc={'vadapalani':1,'arumbakam':2,'cmbt':3,'koyambedu':4,'annanagar':5}
gen={'male':1,'female':2}
male={'adult':1,'child':2}
female={'free ticket':2}
start=input('from:')
if start in loc:
    end=input('to:')
    if end in loc:
        gen=input('select the gender:').lower()
    if gen=='male':
        print('1.adult\n2.child')
        type=input('enter the type:').lower()
        if type=='adult':
            price=(loc[end]-loc[start])*5
            print(f'ticket price:{price}')
            count=int(input('enter the number of ticket:'))
            print('total price',price * count)
        elif type=='child':
            price=(((loc[end]-loc[start])*5)*80)//100
            print(f'ticket price:{price}')
            count = int(input('enter the number of ticket:'))
            print('total price', price * count)

        else:
            print('invalid type')
    elif gen=='female':
        print('free ticket')
    else:
        print('invalid gender')
else:
    print('invalid station')








