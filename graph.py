from matplotlib import pyplot as plt
from eqnsol import eqnsol1 

def drawgraph():
    x1, x2 = eqnsol1()
    plt.plot(x1,x2,color='r',linestyle ='dashed',linewidth = 2,marker = '*',markersize =9,label ='red line\n marker at 1 ft interval')
    plt.axis([-10,10,-10,10])
    plt.title("Roots of a Quadratic Equation")
    plt.xlabel("X Axis1")
    plt.ylabel("x Axis2")
    plt.legend(loc = 'lower right')
    plt.show()

drawgraph()