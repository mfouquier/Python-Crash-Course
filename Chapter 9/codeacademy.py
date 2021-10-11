def middle_element(lst):
  if len(lst) % 2 == 0:
    even1 = int(((len(lst)/2) - 1))
    even2 = int(((len(lst)/2)))
    even = int((lst[even1] + lst[even2]) / 2)
    return even
  else:
    odd = int((len(lst) / 2))
    
    return lst[odd]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))