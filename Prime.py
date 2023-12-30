def primt(a):
  assert a not in [0,1],"Prime is not Defined"
  assert a>0 , "Error : Negative Number"
  count = 0
  for i in range(2,int((a**0.5) +1)):
      if a%i == 0:
          count+=1
  if count <2:
      return "Prime Number"
  else:
      return "Not a Prime"

b = int(intput("Enter a number"))
print(prime(b))
