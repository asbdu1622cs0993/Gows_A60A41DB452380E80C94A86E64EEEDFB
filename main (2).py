def fact_rec(n):
  if n==1:
    return 1
  else:
    return n*fact_rec(n-1)
    

number=int (input("enter a value:"))
rec=fact_rec(number)
print ("the factorial of {} is {}.".format (number,rec))
