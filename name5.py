from getopt import gnu_getopt

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# print(list(students))
studentsL=sorted(students)
#print(len(grades))
#Slovar={'':''}
Slovar=dict(zip(studentsL, grades))
j=0
for i in Slovar:
  Slovar[i]=sum(grades[j])/len(grades[j])
  print(i)
  j=j+1
#print(dict(zip(studentsL, grades)))
print(Slovar)

