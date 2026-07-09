bookprice=int(input("enter price of  book"))
discount=int(input("enter discount"))
disprice=(bookprice*discount)/100
netprice=bookprice-disprice
print(f"the net price is {netprice}\n the {disprice}")
