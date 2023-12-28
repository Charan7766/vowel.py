def cinema():
age=int(input("Please enter your age: "))

if age < 18:
    print("Sorry. You are not over 18 years old. You cannot watch this movie.")

if age >= 18:
     print("You are allowed to see the film. Standard ticket price is £14.95 ")


def buyTicket(percentageDiscount):
    if age <= 20:
        print("You are under 20 years old. You are eligible for a 10% discount. Your ticket price will be", percentageDiscount)

    elif age >= 65:
        print("You are 65 years or over. You are eligible for a 15% discount. Your ticket price will be", percentageDiscount)
    else:
        print("You are", age, "years old. Your ticket price will be £14.95")



while (True):
   cinema()
   anotherticket = input("Do you want to find out more information about another ticket? (Yes/No): ")
   if anotherticket == 'No':
    exit()

