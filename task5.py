# removing duplicated from list 
# using naive methods 
test_list =     [1,2,55,1,3,2,34,55]
print ("The original list is : " + str(test_list)) 

# using naive method 
# to remove duplicated 
# from list 
res = [] 
for i in test_list: 
	if i not in res: 
		res.append(i) 

# printing list after removal 
print ("The list after removing duplicates : " + str(res)) 
