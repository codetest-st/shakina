children=int(input("enter number of children"))
youngs=int(input("enter number of youngs"))
olds=int(input("enter number of olds"))

fare_children=children*450
fare_youngs=youngs*650
fare_olds=olds*500

total_fare=fare_children+fare_youngs+fare_olds
print(f"the fare of chid is {fare_children}\nthe fare of young is {fare_youngs}\nthe fare of old {fare_olds}\n the total fare is {total_fare}")