# prime number count

n = int(input("Enter number upto addition of prime number "))
count = 0
m = 0
for i in range(1,n+1):
    if  n%i == 0:
        count= count+i
if count ==2:
    m = m+i


print(m)

n = int(input("Enter number up to addition of prime number: "))
prime_sum = 0

# Outer loop to check every number from 2 up to n
for i in range(2, n + 1):
    is_prime = True  # Assume the number is prime initially
    
    # Inner loop to look for factors
    for j in range(2, i):
        if i % j == 0:
            is_prime = False  # Found a factor, so it's not prime
            break  # No need to check further, exit inner loop
            
    # If no factors were found, add it to the sum
    if is_prime:
        prime_sum += i

print("The sum of prime numbers is:", prime_sum)
