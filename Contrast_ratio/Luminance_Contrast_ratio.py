
"""
This code calculates contrast ratio of two numbers based on their red blue green luminance value.
It creates random colors then calculate their luminance value, calculate their contrast ratio and
plot the colors along with their contrast ration value
"""
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import struct
from matplotlib.colors import LogNorm

#this function takes red green blue values as parameters,calculates and returns their luminance value
def luminance(r,g,b):
#coverting values to 0-1 scale
    ro=r/255
    go=g/255
    bo=b/255
#calculating new values based on the formula for Red
    if ro<=0.03928:
        ri=ro/12.92
    else:
        ri=((ro+0.055)/1.055)**2.4
#calculating new values based on the formula for Green
    if go<=0.03928:
        gi=go/12.92
    else:
        gi=((go+0.055)/1.055)**2.4
#calculating new values based on the formula for Blue
    if bo<=0.03928:
        bi=bo/12.92
    else:
        bi=((bo+0.055)/1.055)**2.4
#calculating luminance value of the color
    L=(0.2126*ri)+(0.7152*gi)+(0.0722*bi)
    return L

#This function takes red green blue values of two colors as parameters,calculates and returns their contrastRatio
def contrastRatio(r1,g1,b1,r2,g2,b2):
#calculte the luminance of  both colors by calling luminance function
    L1=luminance(r1,g1,b1)
    L2=luminance(r2,g2,b2)
#identify and assign the lighter and darker colors using luminance value
    if L1>L2:
        L_light=L1
        L_dark=L2
    else:
        L_light=L2
        L_dark=L1
#calculate contrast ratio
    Ck=round((L_light+0.05)/(L_dark+0.05),2)
    return Ck

#This function takes one parameter n (number of colors),generate n random red green blue values(0-255) and plot the colours
#and their respective contrast ratio
def randomColors(n):
#generating n random numbers between 0 and 255 for red,green and blue
    red = [random.randint(0, 255) for iter in range(n)]
    green = [random.randint(0, 255) for iter in range(n)]
    blue =[random.randint(0, 255) for iter in range(n)]
#changing the red,green and blue values to hexadecimal number using 'struct' library and put in an array(clr_hexa)
    clr_hexa=[]
    for i in range(n):
#making a tupul of each color containing red green blue values
        rgb=(red[i],green[i],blue[i])
#changing color to hexadecimal number and add '#' as a suffix and put in the array
        clr_hexa.append("#"+bytes.hex(struct.pack('BBB',*rgb)))
#creating an array of the contrast ratio of the numbers
    contrast=[]
    for i in range(n-1):
        contrast.append(contrastRatio(red[i],green[i],blue[i],red[i+1],green[i+1],blue[i+1]))
#scatter plotting
#creating a list of n multipled by 2 consecutive numbers to use for plotting
    x_list = list(range(n*2))
# a list of values for scatter plot x-axis
    x=[a for a in x_list if a % 2 == 0]
# a list of values for scatter plot y-axis and annotation
    y = [0] * n
# a list of values for x-axis for annotation of scatter plot
    a_x=[a for a in x_list if a % 2 != 0]
#ploting
    plt.figure(figsize=(20, 3))
    plt.scatter(x,y,c=clr_hexa,s=1500)
#for loop to add annotations to each point in plot
    for i, txt in enumerate(contrast):
        plt.annotate(txt, (a_x[i], y[i]))
    plt.title('Contrast ratio of random colors',fontsize= 20)
    plt.show()

randomColor(10)
