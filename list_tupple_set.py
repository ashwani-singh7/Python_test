
grades_list = [78,87,65,74,96,15] #LIST
grades_tupple= (74,58,26,74,96,47) #TUPPELS  Immutable
grades_set = {45,85,97,41,63,14} #Sets Unordered List

print(len(grades_list)) 
print(sum(grades_tupple)/len(grades_tupple))
print(grades_list[4])
print(grades_tupple[2])

arry_1 = {1,2,4,6,8,15}
arry_2 = {1,3,9,7,4,14}

print(arry_1.intersection(arry_2))
print(arry_1.union(arry_2))
