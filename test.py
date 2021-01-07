

# slices    = []

# for year in [1,2]:
#     for month in range(1,13):
#         slices.append("year"+str(year)+"month"+str(month))

slices = [ 'year1month1', 'year1month2', 'year1month3', 'year1month4', 'year1month5'] + \
         [ 'year1month6', 'year1month7', 'year1month8', 'year1month9', 'year1month10'] + \
         [ 'year1month11', 'year1month12', 'year2month1', 'year2month2', 'year2month3'] + \
         [ 'year2month4', 'year2month5', 'year2month6', 'year2month7', 'year2month8'] + \
         [ 'year2month9', 'year2month10', 'year2month11', 'year2month12']

print(slices[0:2])