#!/usr/bin/python3

class Cores:
	name = 'none'
	leg = 0.0
	def __init__(self, name, leg):
		self.name = name
		self.leg = leg
  
	def __repr__(self):
		return self.name + " => " + str(self.leg) + " mm"
  
	@staticmethod
	def lookupCoreBySize(len, cores):
		for c in cores:
			if c.leg >= len:
				return c
		return "unknown"

dbcores = []

dbcores.append(Cores("4HS-190", 19.0))
dbcores.append(Cores("4HS-200", 20.0))
dbcores.append(Cores("4HS-220", 22.0))
dbcores.append(Cores("4HS-222", 22.2))
dbcores.append(Cores("4HS-250", 25.0))
dbcores.append(Cores("4HS-254", 25.4))
dbcores.append(Cores("4HS-280", 28.0))
dbcores.append(Cores("4HS-286", 28.6))
dbcores.append(Cores("4HS-318", 31.8))
dbcores.append(Cores("4HS-320", 32.0))
dbcores.append(Cores("4HS-350", 35.0))
dbcores.append(Cores("4HS-360", 36.0))
dbcores.append(Cores("4HS-380", 38.0))
dbcores.append(Cores("4HS-400", 40.0))
dbcores.append(Cores("4HS-444", 44.4))
dbcores.append(Cores("4HS-500", 50.0))
dbcores.append(Cores("4HS-508", 50.8))
dbcores.append(Cores("4HS-600", 60.0))
dbcores.append(Cores("4HS-635", 63.5))

print(Cores.lookupCoreBySize(10, dbcores))
print(Cores.lookupCoreBySize(20, dbcores))
print(Cores.lookupCoreBySize(30, dbcores))