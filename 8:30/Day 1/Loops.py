# 1. FOR LOOP (Counting loop)
# range(5) means count from 0 to 4
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4


# 2. WHILE LOOP (Conditional loop)
count = 0
# Keep going as long as count is less than 5
while count < 5:
    print(count)
    count += 1  # Adds 1 so the loop can eventually stop!


# 3. NESTED LOOP (Loop inside a loop)
# For every 1 turn of the outer loop, the inner loop runs completely
for i in range(3):        # Outer loop
    for j in range(2):    # Inner loop
        print(f'i: {i}, j: {j}')




# 5. LOOP WITH BREAK (Stop everything)
for i in range(5):
    if i == 3:
        break  # Emergency exit! Stops the whole loop right now
    print(i)   # This will only print 0, 1, and 2


for i in range(5):
    if i == 3:
        continue  # Skip button! Jumps straight to the next number
    print(i)      # This prints 0, 1, 2, 4 (skips 3)


# * * * * *
# * * * * 
# * * *
# * *
# * 

