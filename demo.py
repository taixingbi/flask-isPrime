
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

class Prime():
  def __init__(self, n):
    self.n= n

  # time complexity: O(m) m= ( int(n**0.5) )/2
  def isPrime(self, n):
    if n<=1: return False
    if n==2 or n==3: return True

    if n%2==0: return False  # <=3 or even number

    max_n= int(n**0.5)+1
    for i in range(3, max_n, 2):   # only odd numbers
      if n%i==0: return False
    return True

  def ans(self):
    n= self.n
    if n <=1 or int(n)!=n: return n, "Error: input number less than 1 or not an integer"
    if self.isPrime(n): return n, "\n Prime Number"
    else: return n, "\n Composite Number"


if __name__ == '__main__':

  #test cases
  num= 9

  for n in range(9):
    print ( Prime(n).ans() )


  print ( Prime(-1).ans() )
  print ( Prime(2.3).ans() )




  


  
  



