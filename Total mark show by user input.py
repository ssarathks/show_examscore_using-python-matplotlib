import matplotlib.pyplot as pt


'''
Now we create a dictionary to maintain the data to be shown in the stacked bars
'''
data={'Name':  [],
      'first': [],
      'second':[],
      'third':[]}


num_of_stud=int(input("Enter the number of students whose marks are to be entered"))

for i in range(num_of_stud):
    data['Name'].insert(i,input("Enter name of student"))


print("\nNow enter 1st internal marks\n")
for i in range(num_of_stud):
    print("Enter mark of",data['Name'][i])
    data['first'].insert(i,int(input()))


print("\nNow enter 2nd internal marks\n")
for i in range(num_of_stud):
    print("Enter mark of",data['Name'][i])
    data['second'].insert(i,int(input()))

print("\nNow enter final semester exam marks\n")
for i in range(num_of_stud):
    print("Enter mark of",data['Name'][i])
    data['third'].insert(i,int(input()))

'''Mark insertion completed
Now creating the stacked Bars
'''

fig=pt.figure("Stacked bars")
sp=fig.add_subplot(1,1,1)

width=0.5
bar_x_pos=[i+1 for i in range(len(data['first']))]
ticks=bar_x_pos

line_end=max(bar_x_pos)+width


sp.bar(bar_x_pos,data['first'],width=width,color='y',label='First Internal')

sp.bar(bar_x_pos,data['second'],color='orange',width=width,label='Second Internal',bottom=[i for i in data['first']])

sp.bar(bar_x_pos,data['third'],color='r',width=width,label='Final Semester Exam',bottom=[i+j for i,j in zip(data['first'],data['second'])])

sp.plot([0,line_end],[23,23],color='b',label="Minimum Requirement")


pt.legend(loc='upper right')
pt.xticks(ticks,data['Name'])
pt.show()