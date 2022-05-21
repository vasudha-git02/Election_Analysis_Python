x = 0
while x <= 5:
    print(x)
    x = x+1

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print (county)

for num in range(7):
    print (num)

counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict.values():
    print(county)


counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(counties_dict.get(county))


counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county,voters in counties_dict.items():
    print(str(county) + " has "+str(voters) +" registered voters. ")
    print(f"{county} county has {voters} registerd voters")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
      print(value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
      print(county_dict['registered_voters'])      

