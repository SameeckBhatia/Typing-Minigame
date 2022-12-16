#importing required libraries
import random
import string
import time

#setting increment value and points
i = 0
points = 0

start_time = time.time()

#while loop to repeat 10 times
while i < 10:
    
    f = open("C:\\Users\samee\Downloads\words.txt", "r")
    
    array = []
    
    letter = random.choice(string.ascii_lowercase)
    
    #appending words from file to array
    for w in f:
        if w[0] == letter:
            array.append(w[0:-1])
            
    rand_word = array[random.randrange(len(array))]
    
    #output message
    print("\nYour mystery word is: " + rand_word)
    
    i += 1
    
    #checking if input matches output
    if input() == rand_word:
        
        points += 1
        
        if i == 9:
            
            break

end_time = time.time()

#calculating time taken depending on correctness and speed
time_taken = round(1000 / (end_time - start_time), 2)

#condition to create and control point-scoring system
if not points == 0 and time_taken + points * 10 < 100.0:
    
    print("\n--You scored %s points--" %(time_taken + points * 10))
    
else:
    
    print("\n--You scored %s points--" %(points * 10.0))