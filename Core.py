import csv

class Core:
	model = 'none'
	leg = 0.0
 
	def __init__(self, supplier, model, a, b, leg, d, e, f, g):
		self.supplier = supplier
		self.model = model
		self.leg = float(leg)
		self.a = float(a)
		self.b = float(b)
		self.c = float(leg)
		self.d = float(d)
		self.e = float(e)
		self.f = float(f)
		self.g = float(g)
  
	def __repr__(self):
		return self.supplier + ":" + self.model + ": leg=" + str(self.leg) + " mm"

	@staticmethod
	def load(file):
		table = []
		with open(file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					# print(f'Column names: {", ".join(row)}')
					line_count += 1
				else:
					bob = Core(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
					table.append(bob)
					# print(f'\t{row[0]}: code="{row[1]}"", leg={row[2]} mm')
					line_count += 1
			# print(f'Processed {line_count} lines.')
			return table

	@staticmethod
	def lookupCoresBySize(cores, lmin, lmax):
		resp = []
		for c in cores:
			if c.leg >= lmin and c.leg <= lmax:
				resp.append(c)
		return resp
