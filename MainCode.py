#I know there's a much more easier way to do this which is the integral of e^pi*i*f or something like that but I just wanted to - 
#make a code that manually calculates it

# I highly suggest you watch 3blue 1 brown's youtube video about fourier transformations to get an idea of what I'm trying to do here
#here's the link : https://www.youtube.com/watch?v=spUNpyF58BY

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

Now that we have the x and y plots of the graph, we want to make a vector and use it to graph the wave in that circular almost polar 
coordinates fashion

The law of polar coordianates tell us that 
x = r*cos(theta)
y = r*sin(theta)

So:
the x coordinate of any point  will equal the output of the wave multiplied by cosine(the angle)
the y coordinate of any point  will equal the output of the wave multiplied by sine(the angle)

then once we've graphed the entire graph we will get the average of all x coordinates and y coordinates giving us the
x and y coordinates of the center of mass 

now we get those x and y coordinates for the center of mass for different frequencies/speeds of the rotating vector and 
then graph them 

'''
#those will store the x and y coordinates of all centers of mass for different speeds/frequencies of the vector
centersx=[]
centersy=[]

#Here we generate all the rotating vector frequencies for which we will calcualte the x and y coordinates of center of mass
#Here we will test frequencies from 0.1 to 10 by adding 0.1 each time so were testing a total of 
f_step = 0.1
frequency_list = np.arange(0.1,   10,     f_step,      dtype='float32')


#here we plot the graph of the rotating  vector and calculate center of mass c
for frequency in frequency_list:
    #Xs and Ys will store the x and y coordinate for each point on the rotating vector graph
    #We will later take the average of all those points to get x and y of c
    Xs = np.empty((len(outputs)),dtype='float32')
    Ys = np.empty((len(outputs)),dtype='float32')
    
    #PPR is points per rotation, to get this, we divide 2pi by the vector frequency and multiply by 1 over the wave step
    PPR = ((2*np.pi)/frequency)  *  (1/wave_step)         
    points = len(frequency_list)
    inc = (2*np.pi)/PPR  *  (1/wave_step))
    theta = 0
    counter=0
    for r in outputs:
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        sumx+=x
        sumy+=y
        Xs[counter] = x
        Ys[counter] = y
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
