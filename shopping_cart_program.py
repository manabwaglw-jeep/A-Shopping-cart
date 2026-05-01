# Shopping cart program
foods=[]
prices=[]
total=0

while True:
    food=input("enter the food to buy and type q to (quit):")
    if food.lower() == "q":    # food.lower() is used because python is case sensitive
        break 
    
    else:
     price=float(input(f"enter the price of  {food} :$"))
     foods.append(food)
     prices.append(price)


print(" :YOUR CART:")
for food in foods:
    print(f"{food}={price}")
    
for price in prices:
        total=sum(prices)
        
print(f"The Total price is :{total}")        
    
    


         
         
         
         
        
        
        
      
         
         
         
    
    