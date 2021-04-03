n, B = list(map(int, input().strip().split()))
T = 0

# your code here#

i = 1
multiplicator = 0

while i <= n:
  
  if i%2 != 0:

    multiplicator += ((3 ** i) + 1) ** (n-i)

  if i%2 == 0:

    multiplicator += ((2 ** i) + 1) ** (n-i)    

  i += 1

while (T * multiplicator) < B:

  T += 1

  if T > 10000:
    T = -1
    break

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)