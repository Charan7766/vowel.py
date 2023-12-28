print('welcome to cinema........!') 

enter=(input('plese enter your name.....!'))
seats=eval(input('select no of seats.......!'))
select=eval(input('1 for diamond 2 for gold 3 for silver.......!'))
rate1=200
rate2=150
rate3=100
if seats==1:
    rate1*seats
    print('you selected diamond class')
    print(rate1)
elif seats==2:
    rate2*seats
    print('you selected gold class')
    print(rate2)
elif seats==3:
    rate3*seats
    print('you silver class')
    print(rate3)
    print('your booking was sucussful')
    print(seats)
    print(enter)
    




     
