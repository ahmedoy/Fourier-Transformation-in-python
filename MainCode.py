import matplotlib.pyplot as plt
import numpy as np

#making the wave function in radians
#change this function to be whatever wave you want
#our goal is to unpack this wave into its constituent frequencies
'''
here I am using a composite wave of three waves (1 sine wave with frequency of 0.2, 1 sine wave with frequency 5,
and a cosine wave of frequency (0.7)
'''
def wave(x):
    return(np.sin(0.2*x)+np.sin(5*x)+np.cos(0.7*x))

#step increase from least input to highest input 
# for example if step equals 1 we will keep adding 1
wave_step = 0.1

#generating inputs from 0 to 2000 by recursivley adding wave_step
inputs= np.arange(0.0,   2000.0,     wave_step,      dtype='float32')

#calculating results/outputs of the genenrated nputs and making a numpy array of them
#this is an empty array which we will sotre the outpus in
outputs = np.empty((inputs.shape[0]),dtype='float32')

#Filling the empty outputs array with our outputs
counter = 0
for x in inputs:
    outputs[counter]=wave(x)
    counter+=1

#graphing the wave
plt.plot(inputs,outputs)
plt.show()


'''
Part 2 of the code:

Now that we have the x and y plots of the graph, we want to make a vector and use it to get polar coordinates 

x= r*cos(theta)
y= r*sin(theta)
'''

centersx=[]
centersy=[]
#frequencies = []
f_step = 0.1
frequency_list = np.arange(0.1,   10,     f_step,      dtype='float32')
for frequency in frequency_list:
    fourier_x = np.empty((len(outputs)),dtype='float32')
    fourier_y = np.empty((len(outputs)),dtype='float32')
    #ppr = ((2*np.pi)/frequency)  *  (1/wave_step)         #points per rotation
    points = len(frequency_list)
    inc = (2*np.pi)/(((2*np.pi)/frequency)  *  (1/wave_step))
    theta = 0
    counter=0
    sumx = 0
    sumy = 0
    for r in outputs:
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        sumx+=x
        sumy+=y
        fourier_x[counter] = x
        fourier_y[counter] = y
        theta+=inc
        counter+=1

    centersx.append(sumx/len(outputs))
    centersy.append(sumy/len(outputs))


plt.plot(frequency_list,centersx,c='r')
plt.show()
plt.plot(frequency_list,centersy,c='g')
plt.show()



plt.plot(frequency_list,centersx,c='r')
plt.plot(frequency_list,centersy,c='g')


#method 1 (get maximum)
max_n = 5 #how many maxes to get
#maxes=[] #collected maxes #disabled for now
b_centx = centersx #equal to centers x we will use it to get maximums
b_centy = centersy #equal to centers y will be uses to get maximums
#we will substitute the minumum for all our maximums
min_x = np.min(b_centx)
min_y = np.min(b_centy)
for n in range(max_n):
  print('max number', n+1)
  max_x = np.argmax(b_centx)
  max_y = np.argmax(b_centy)
  print('frequency that gives maximum number',n+1,'for center x =',frequency_list[max_x],'max value of x = ',b_centx[max_x])
  print('frequency that gives maximum number',n+1,'for center y =',frequency_list[max_y],'max value of y = ',b_centy[max_y])
  #maxes.append((maxx,maxy))   #disabled feature for now
  #np.delete(b_centx,max_x)
  b_centx[max_x] = min_x
  b_centy[max_y] = min_y
  print('\n')


'''
print('maximum 1')
print('max x',(np.argmax(centersx)*f_step))
print('max y',(np.argmax(centersy)*f_step))
'''

#getting average
print('avgerage of x =', np.average(centersx))
print('avgerage of y =', np.average(centersy))
