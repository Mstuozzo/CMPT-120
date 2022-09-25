def main():

    #'''ask the user for their age. If the user is 25 or older, tell them they can buy alcohol, nicotine products, and they can rent a car
     #   If they're 21 or older but younger than 25, tell them they can buy alcohol and nicotine products, but cannot rent a car
    #    If they're 18 and older but younger than 21, tell them they can only buy nicotine products in some states
    #    If they're less than 18, they can only purchase candy cigarettes and sody pops
   # '''

    age = input("How old are you?")
    age = int(age)
    if age >= 25:
        print("You can buy pure Ethanol and Nicotine, and rent a car")
    elif age >= 21 and age <= 25:
        print("you can buy alc nicotine but rent no car")
    elif age >= 18 and age <= 21:
        print("you can buy nicotine only in some states")
    elif age >18 and age <= 1:
        print("you can only buy candy cigarettes and soda pops!!!")

  
  
  
main()
