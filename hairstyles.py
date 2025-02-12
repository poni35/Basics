hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#sum of all the prices of haircuts
total_price = 0

#for loop, loops through prices list and stores value to temp var total
for total in prices:
  total_price += total

print(total_price)

#calculates average price of hairstyle
average_price = total_price / len(prices)
print ("Average Haircut Price:", average_price)

#list comprehension used to loop through prices and subtract 5 from each element then assign result to new var
new_prices = [minus - 5 for minus in prices]
print(new_prices)


#REVENUE#

total_revenue = 0
 #loop that assigned the range of hairstyles from the number of items it contains to i - total revenue is then generated  and added to new variable as i loops through list performing the requested multiplication each iteration
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]


  print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)\

#comprehension list that iterates of new prices list, if it meets selected condition then hairstyle value is applied to variable
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)