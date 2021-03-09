n, B = list(map(int, input().strip().split()))
T = 0

# your code here

i = 1 
multiplicator = 0

while i <= n:
  
  if i%2 != 0:

    multiplicator += ((3 ** i) + 1) ** (n-i)

  if i%2 == 0:

    multiplicator += ((2 ** i) + 1) ** (n-i)    

  i += 1

step_counter = 0
T = 10000
low = B / multiplicator
high = T
guess = (low + high) / 2.0

while (T * multiplicator) > B:

  if guess * multiplicator < B:
    low = guess
  if guess * multiplicator > B:
    high = guess

  guess = (low + high) / 2.0
  T = guess
  prev_guess = guess
  step_counter += 1
  if step_counter > 10000:
    break

  if T > 10000: 
    T = -1
    break

if T > int(T):
  T = int(T)
  T += 1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)