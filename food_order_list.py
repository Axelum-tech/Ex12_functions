#HW: finish the code:
# 1: complete the function code
# 2: for loop-> calculate order_cost
# 3: for loop-> print the bill


########## Function #############
def calculate_cost(quantity, price):
    cost=quantity*price
    return cost
########## Function #############


############ Data ###############
# input data

food_names= ["Salad", "Pizza", "Soup"]
food_price= [15.00,    75.00,   25.00]
food_q=     [    5,         1,      3]

order_cost= [ 0.00,     0.00,    0.00]
############ Data ###############


############ Testing ###############

# order_cost[0]=food_price[0]*food_q[0]
# order_cost[1]=food_price[1]*food_q[1]
# order_cost[2]=food_price[2]*food_q[2]

############ Testing ###############


############ Scripts ###############

for i in range(3):
    order_cost[i]=calculate_cost(food_price[i],food_q[i])

print()
print()
print(">>>>>>>>YOUR BILL<<<<<<<<")
print("-------------------------")
for i in range(3):
    print(i+1,".",food_names[i],"x",food_q[i],"->",order_cost[i],"Units")
    total=sum(order_cost)
print("-------------------------")
print("TOTAL", total, "Units")
print("-------------------------")
print()
print()

############ Scripts ###############
  
 
