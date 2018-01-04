#!/usr/bin/python
def fizzbuzz(num):
  if num % 15 == 0:
    return 'FizzBuzz'
  elif num % 3 == 0:
    return 'Fizz'
  elif num % 5 == 0:
    return 'Buzz'
  else:
    return num

if __name__ == '__main__':
  for i in range(1,31):
    print(fizzbuzz(i))
