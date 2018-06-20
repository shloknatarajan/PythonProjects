import numpy
import time

count = 0
total = 0
while(True):
    number = numpy.random.randn()
    if (number > -1 and number < 1):
        count += 1 
    total += 1
    print(count / total)
    
    