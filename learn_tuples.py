def learn_tuples():
  print("learn_tuples")
     ################################Tuples##################################

  # Tuples Practice #1
  # Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:
   
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

hi = my_tuple.count(2)
print(hi)

  # Tuples Practice #2
  # Convert the following tuple to a list, and store it in a variable called my_list.
  
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
my_list = my_tuple
print(my_list)

  # Tuples Practice #3
  # Extract the elements of the following tuple into four variables: a, b, c, d
a, b, c, d, e, f, g, h = my_tuple
print(a)

my_tuple = {1, 2, 3, 2, 3, 1, 3, 2}
a, b, c = my_tuple
print(a, b, c)