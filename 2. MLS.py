# Motor Learning Sequence
# This program is for helping you perform MLS Tasks so that you may train
# your brain and increase sleep spindles for better sleep

# How to use program: 
# Align your non-dominant hand with the numbers 1, 2, 3, 4
# on your keyboard. Do not use your thumb.

# Program instructions-------------------------------------------------------
# When you run program:
# you will be shown a BLOCK which consists of 5 numbers at random from in the range 1-4
# For example: 1 - 4 - 3 - 1 - 2 
# There will be a total of 12 BLOCKs, where users are given 30 seconds to complete as many
# sequences as they can. A sequence is when the user inputs the 5 numbers show from the block

# Users will input 5 numbers, they have to press 'enter' to submit it everytime

#There will be a 30 seconds break in-between each block


# After you finish 12 blocks you should see your results which contain:
# - total completions per block
# - number of perfect completions per block (no mistakes)
# - number of imperfect completions per block where you made a mistake
# - accuracy % per block
# - total score accuracy 

# Here's an example final output:
# [Block1] Stats:
# Total No. of completions: 50
# No. of perfect completions: 38
# No. of imperfect completions: 12
# Accuracy by matching Numbers: xx%
from threading import Thread
import time
from random import *

block = 0
def main():
    global block
    while block < 3:
        Thread(target=userInputs).start()
        Thread(target=countTime(5)).start()
        block += 1

block_list = []
timeOut = True
def userInputs():
    while timeOut == True:
        num_inputs = int(input("Input 5 numbers and then press 'enter': "))
        block_list.append(num_inputs)
    print(block_list)


start_time = time.time()
num_list = [1,2,3,4]
block_list = []
def countTime(seconds):
    global timeOut
    global start_time
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= seconds:
            print()
            print("Time spent:")
            print(time.time()-start_time)
            timeOut = False
            break
    timeOut = True
    start_time = time.time()
    print(start_time)

main()

# if __name__ == '__main__':
#     Thread(target=userInputs).start()
#     Thread(target=countTime(10)).start()
# for i in range(5):
#     x = sample(num_list, 1)
#     block_list.append(x[0])
#     y = print(x[0],'- ', end='')




