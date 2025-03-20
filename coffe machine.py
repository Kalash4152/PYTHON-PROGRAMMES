emoji='''☕'''
introduction=("welcome to the coffe machine, What would u like to have","we have latte:$250 expresso:$200 and mocha:$300")
print(introduction,emoji)
menue={ 
    "latte" : {'water':70,'milk':150,'coffe powder':30,'sugar':20},
     "mocha" : {'water':50,'milk':150,'coffe powder':30,'sugar':20,'vanilla':30},
     "expresso":{'water':100,'milk':100,'coffe powder':30}}
print("here is the menue")
print("latte:")
print(menue["latte"])
print("mocha:")
print(menue["mocha"])
print("expresso")
print(menue["expresso"])
res={"milk":400,
     "sugar":50,
       "water":250,
       "coffe":120,
       "vanilla":100}
print("available resources:",res)

latte_money=250
mocha_money=300
expresso_money=200
order =True




while  order:
    x=input("do u want to order:")
    if x=="yes":
        q=input("what do u want to order:")
    if q== "latte":
        pay=int(input("please pay the money"))
        if pay==latte_money:
            print("here is your latte ",emoji)
            new_milk= milk-150
            new_water=water-70
            new_coffe=coffe_powder-30
            new_sugar=sugar-20
            print("resources left:","milk:",new_milk,"sugar",new_sugar,"coffe",new_coffe,"water",new_water)
        elif pay<latte_money:
            print("payment is insufficient")
        elif pay>latte_money:
            x=pay-latte_money
            print("here is the change:",x)
            print("here is your latte ",emoji)
            new_milk= milk-150
            new_water=water-70
            new_coffe=coffe_powder-30
            new_sugar=sugar-20
            print("resources left:","milk:",new_milk,"sugar",new_sugar,"coffe",new_coffe,"water",new_water)
    elif q== "mocha":
        pay=int(input("please pay the money"))
        if pay==mocha_money:
            print("here is your mocha ",emoji)
            new_milk= milk-150
            new_water=water-50
            new_coffe=coffe_powder-30
            new_sugar=sugar-20
            new_vanilla= vanilla-30
            print("resources left:",new_milk,new_sugar,new_coffe,new_water,new_vanilla)
        elif pay<mocha_money:
            print("payment is insufficient")
        elif pay>mocha_money:
            x=pay-mocha_money
            print("here is the change:",x)
            print("here is your mocha ",emoji)
            new_milk= milk-150
            new_water=water-50
            new_coffe=coffe_powder-30
            new_sugar=sugar-20
            new_vanilla= vanilla-30
            print("resources left:",new_milk,new_sugar,new_coffe,new_water,new_vanilla)
    elif q== "expresso":
        pay=int(input("please pay the money"))
        if pay==expresso_money:
            print("here is your expresso",emoji)
        elif pay<expresso_money:
            print("payment is insufficient")
        elif pay>expresso_money:
            x=pay-expresso_money
            print("here is the change:",x)
            print("here is your expresso ",emoji)
    
    elif x=="no":
        
        order=False
check()




