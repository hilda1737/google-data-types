# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  
  if count<10:   
        
        print("number of donoughts is:" ,count)
  else:
      count >=10 
      print("number of donnoughts many")
donuts((1))   


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# def test(got, expected):
#   if got == expected:
#     prefix = ' OK '
#   else:
#     prefix = '  X '
#   print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
# test(1,10)

            