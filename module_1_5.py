immutable_var=1,2,'string',True
print(immutable_var)
# immutable_var[0]=3 TypeError: 'tuple' object does not support item assignment
# кортеж не поддерживает изменение объекта, т.е. он содержит ссылки на объекты, которые не меняет
mutable_list=[1,2,'string',True]
mutable_list[0]=mutable_list[0]+1
mutable_list[1]=3
mutable_list[2]="new string"
mutable_list[3]=False
mutable_list.append("new")
print(mutable_list)

