name={"raj":55,"ram":66,}#dictonary
print(name)
print(type(name))#type
print(name.get("raj")) #give output by index
name["khana"]=77#add in dict
print(name)
name["raj"]=88 #change value
print(name)
del name["raj"] #delet from dict
print(name)
print(name.keys()) #SHOW KEYS
print(name.values()) #show value
# multi  dimesnion dict
d1={"name":"steve","age":25,"marks":60}
d2={"name":"anjli","age":23,"marks":75} 
d3={"name":"ashu","age":20,"marks":70}
std={1:d1,2:d2,3:d3}
print(std)
print(len(name)) #give size
print(max(name)) #give largest velue
print(min(name)) #give smalest value
print(name.pop("ram")) #pops ram
print(name)
print(name.items())