# Tulis solusi untuk Prime

def isPrime(n):
  if n == 1:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
    
  return True

def nearestPrime(n):
  if isPrime(n):
    return n
  
  else:
    while True:
      n += 1
      if isPrime(n):
        return n

a = int(input())

myList = []
for i in range(a):
  inp = int(input())
  myList.append(inp)

print(a)
for num in myList:
  print(nearestPrime(num))
  