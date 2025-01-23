weight = 41.5

print("Package Weight:", str(weight) + "lb")

#Ground Shipping#
if weight <= 2:
  print("Ground Shipping Fee:", "$" + str(weight * 1.50 + 20)) 
  #this does the maths to work out the price of shipping by multiplying weight by price per pound. the result is then converted to a string, which allows us to concatenate the dollar sign in front#
elif weight >= 3 and weight <= 6:
    print("Ground Shipping Fee:", "$" + str(weight * 3.00 + 20))
elif weight > 6 and weight <= 10:
  print("Ground Shipping Fee:", "$" + str(weight * 4.00 + 20))
else:
  print("Ground Shipping Fee:", "$" + str(weight * 4.75 + 20))

Ground_Shipping_Premium = False

if Ground_Shipping_Premium == True:
  total += 125.00


cost_ground_premium = 125.00

print("Ground Shipping Premium - Flat Charge:", "$" + str(cost_ground_premium))


#Drone Shipping#
if weight <= 2:
  print("Drone Shipping Fee:", "$" + str(weight * 4.50))
elif weight > 2 and weight <= 6:
  print("Drone Shipping Fee:", "$" + str(weight * 9.00))
elif weight > 6 and weight <= 10:
  print("Drone Shipping Fee:", "$" + str(weight * 12.00))
else:
  print ("Drone Shipping Fee:", "$" + str(weight * 14.25))



