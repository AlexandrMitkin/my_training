my_dict={"name":"год рождения", "alex":2005, "alex2":2007, "alex3":2008}
print(my_dict)
print(my_dict["alex"])
my_dict["alex5"]=2000
print(my_dict)
# print(my_dict.get("alex3"))
my_dict.update({"alex6":2001,"alex7":1908})
a=my_dict.pop("alex")
print(a)
print(my_dict)
my_set={a,"c","f","b",2,3,4,4,0,"string",2,2}
print(my_set)
my_set.add(5)
my_set.discard("f")
print(my_set)