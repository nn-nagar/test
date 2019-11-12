# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency(my_list): 
	# Creating an empty dictionary 
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1

	for key, value in freq.items(): 
		print ("% s : % s"%(key, value)) 

# Driver function 
if __name__ == "__main__": 
	my_list =    ['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']
	CountFrequency(my_list) 
