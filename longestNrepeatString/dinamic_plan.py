class sub(object):
	def __init__(self,start, length, status):
		self.start = start
		self.length = length
		self.status = status
	def set_start(self, start):
		self.start = start
	def set_length(self, length):
		self.length = length
	def set_status(self, status):
		self.status = status
	def get_status(self):
		return self.status

class detect_length(object):
	def __init__(self, s):
		self.s = s

	def damage_detection(self):
		index = []
		lgt_length = 1
		sub = sub(0,1,s[0])
		for i in range(1,len(s)):
			if s[i] not in sub:
				sub.set()
