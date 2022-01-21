'''
Prog Challange: Temp Variation in Day
'''

import matplotlib.pyplot as plt

def time_axes():
    # create a list for time of day
    x_numbers = list(range(0,25))
    #convert list to string
    print(list(map(str,list(range(0,25)))))

    return x_numbers

#def temp_axes():

def timeaxes():
    time = ['00:00 am','01:00 am','02:00 am','03:00 am','04:00 am','05:00 am','06:00 am','07:00 am','08:00 am','09:00 am','10:00 am','11:00 am','12:00 pm','01:00 pm','02:00 pm','03:00 pm','04:00 pm','05:00 pm','06:00 pm','07:00 pm','08:00 pm','09:00 pm','10:00 pm','11:00 pm']
    

def draw_graph():

    y_numbers = [8,8,8,8,8,8,7,7,7,7,8,9,9,9,9,9,8,8,7,6,6,6,6,6,5]
    z_numbers = [6,6,6,6,7,8,9,8,7,6,5,6,7,9,9,9,8,7,7,8,8,8,6,5,7]
    x_numbers = time_axes()
    time = ['00:00 am','01:00 am','02:00 am','03:00 am','04:00 am','05:00 am','06:00 am','07:00 am','08:00 am','09:00 am','10:00 am','11:00 am','12:00 pm','01:00 pm','02:00 pm','03:00 pm','04:00 pm','05:00 pm','06:00 pm','07:00 pm','08:00 pm','09:00 pm','10:00 pm','11:00 pm','000:0 am']
    
    #plt.plot(x_numbers, y_numbers, x_numbers, z_numbers)
    plt.plot(time,y_numbers)
    plt.xlabel('Time of day')
    plt.ylabel('Temperature in Degrees Centigrade')
    plt.title('Temperature During The Day')
    plt.legend(['Harrow','Somewhere'])
    plt.axis(ymin=0)
    plt.show()
                     
    





if __name__ == '__main__':
    draw_graph()
    
