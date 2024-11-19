# Make pizza according to the toppins desired by each person
#Toppings--->mushroom,paneer,corn,jalapeno,tomato,olives
def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)
Joe=make_pizza("olives","mushroom","tomato")
print("********")
Karen=make_pizza("Jalapeno")
print("********")
Bill=make_pizza("Paneer","Olives","Jalapeno","Tomato")
print("********")
# max is smilar function which can take multipel args
print(max(4,15,18))
print(max(12,23,34,45,56))
print(max(2,3))