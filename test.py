


dftest = (15.49964652559102, 1.0, 6, 9, {'1%': -4.473135048010974, '5%': -3.28988060356653, '10%': -2.7723823456790124}, -114.9946897099733)


results = {"Test statistic": dftest[0], "p-value": dftest[1], "Laggs used": dftest[2], \
           "Number of observations used": dftest[3], "Critical value 1%": dftest[4]['1%'], \
           "Critical value 5%": dftest[4]['5%'],"Critical value 10%": dftest[4]['10%'] }

# print(results)

# order = 1

# for order in range(order):
#     print(order)
order = 2

d = [1,2,3]
d = [0]*order + d

print(d)