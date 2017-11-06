s= 'abcabcbb'
start  = 0
length = 1
dp = [0 for i in range(len(s))]
dp[0] = 1
visit = {}
visit[s[0]] = 0
lst = 1
lst_start = 0

if len(s)<=1:
	print len(s)

for i in range(1, len(s)):
	if s[i] not in visit.keys():
		visit[s[i]] = i
		dp[i] = dp[i-1] +1
	else:
		if visit[s[i]] < start:
			dp[i] = dp[i-1]+1
			visit[s[i]] = i
		else:
			start = visit[s[i]] + 1
			dp[i] = i-visit[s[i]]
		#	print dp[i]
			visit[s[i]] = i
	if dp[i] > lst:
		print i, dp[i]
		lst = dp[i]
		lst_start = i-lst+1

print lst, lst_start
		
	
