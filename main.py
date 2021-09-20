import matplotlib.pyplot as plt
import myclass as mc
import averageClass as ac
import math


plt.ion()
ax = plt.axes()
plt.xlim(0, 1)
plt.ylim(0, 1)
ax.grid(b = 1)


  #FirstClass create
x1 = [0.05, 0.14, 0.16, 0.07, 0.2]
y1 = [0.91, 0.96, 0.9, 0.7, 0.63]

firstclass = mc.MyClass(ac.AverageClass(x1).Average, ac.AverageClass(y1).Average, '$\clubsuit$', 'green')

ax.scatter(x1, y1, c = firstclass.color, s = 400, marker = firstclass.marker)


  #SecondClass create
x2 = [0.49, 0.34, 0.36, 0.47, 0.52]
y2 = [0.89, 0.81, 0.67, 0.49, 0.53]

secondclass = mc.MyClass(ac.AverageClass(x2).Average, ac.AverageClass(y2).Average, '$F$', '#46351D')

ax.scatter(x2, y2, c = secondclass.color, s = 400, marker = secondclass.marker)


  #ThirdClass create
x3 = [0.62, 0.79, 0.71, 0.78, 0.87]
y3 = [0.83, 0.92, 0.92, 0.83, 0.92]

thirdclass = mc.MyClass(ac.AverageClass(x3).Average, ac.AverageClass(y3).Average, '*', 'r')

ax.scatter(x3, y3, c = thirdclass.color, s = 400, marker = thirdclass.marker)


  #FourthClass create
x4 = [0.55, 0.66, 0.74, 0.89, 0.77]
y4 = [0.4, 0.32, 0.49, 0.3, 0.2]

fourthclass = mc.MyClass(ac.AverageClass(x4).Average, ac.AverageClass(y4).Average, '1', 'b')

ax.scatter(x4, y4, c = fourthclass.color, s = 400, marker = fourthclass.marker)


print('Input x')
x = float(input())
print('Input y')
y = float(input())

ax.scatter(x, y, c = '#FFC069', s = 400, marker = 'd')

print('Press Enter to calculate distances')
input()


line_1 = ax.plot([x, ac.AverageClass(x1).Average ], [y, ac.AverageClass(y1).Average], color = firstclass.color)

line_2 = ax.plot([x, ac.AverageClass(x2).Average], [y, ac.AverageClass(y2).Average], color = secondclass.color)

line_3 = ax.plot([x, ac.AverageClass(x3).Average], [y, ac.AverageClass(y3).Average], color = thirdclass.color)

line_4 = ax.plot([x, ac.AverageClass(x4).Average], [y, ac.AverageClass(y4).Average], color = fourthclass.color)

distance = 100
resultclass = ''

classes = [firstclass, secondclass, thirdclass, fourthclass]

for cl in classes:
  dist = math.sqrt(math.pow(x - cl.xcenter, 2) + math.pow(y - cl.ycenter, 2))
  if(dist < distance):
    distance = dist
    resultclass = cl

ax.collections[4].remove()

ax.scatter(x, y, s = 600, marker = resultclass.marker, c = resultclass.color)
