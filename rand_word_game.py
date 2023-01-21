#importing required libraries
import random
import string
import time

#setting increment and score values
i = 0
score = 0

start_time = time.time()

#while loop to repeat 10 times
while i < 10:
    
    f = open("words.txt", "r")
    
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
        
        score += 1

end_time = time.time()

#calculating time taken and points depending on correctness and speed
time_taken = end_time - start_time
time_based_pts = round(150 / time_taken, 1)

#outputting total points where user score is between 1 and 9, inclusive
if score in range(1, 10):

    if time_taken < 15.0:

        print("\n--You scored %s points--" %(score* 10.0))

    else:

        print("\n--You scored %s points--" %(time_based_pts + (score - 1) * 10))

#outputting total points for a perfect score
elif score == 10:

    if time_taken < 15.0:

        print("\n--You scored 100.0 points--")

    else:

        print("\n--You scored %s points--" %(time_based_pts + (score - 1) * 10))

#outputting total points for a zero score
else:

    print("\n--You scored 0.0 points--")
