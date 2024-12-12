# import matplotlib as plt
import matplotlib.pyplot as plt

#define the plot function for y v x
def plot_signal(x,y):
  #get a figure
  fig,ax= plt.subplots()
  #set title
  ax.set_title('Poly Eval')
  #set x label
  ax.set_xlabel('Range')
  #set y label
  ax.set_ylabel('Domain')
  #turn on grid
  ax.grid()
  #plot
  ax.plot(x,y)
  #display the plot
  plt.show()

a = 0.01
b = 0.002
c = 0.0001

# Generating the x values from 0 to 1 in steps of 0.01
myX = [i * 0.01 for i in range(101)]

# Calculate y values using the polynomial formula
myY = [a * x**2 + b * x + c for x in myX]

# Ploting the results using separate lists
plot_signal(myX, myY)

# Create a list of tuples for x and y values
points = [(x, a * x**2 + b * x + c) for x in myX]

# Unpack tuples into x and y lists and plot
x_from_tuples, y_from_tuples = zip(*points)

# Ploting the results using list of tuples
plot_signal(x_from_tuples, y_from_tuples)
