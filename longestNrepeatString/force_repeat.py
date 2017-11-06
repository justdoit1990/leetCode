test_string = "jbpnbwwd"
longest = 1
longest_start = 0
start = 0

for i in range(len(test_string)):
	visit = []
	length_i = 1
	start = i
	visit.append(test_string[i])
	for j  in range(i+1,len(test_string)):
		if test_string[j] not in visit:
			visit.append(test_string[j])
			length_i+=1
		else:
			# start = test_string[i+1]
			if length_i>longest:
				print "length_i %d" %length_i
				print "start %d" %start
				print j,test_string[j] 
				longest=length_i
				longest_start = start
			break
	if length_i > longest :
		longest = length_i

print longest, longest_start	
