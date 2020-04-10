import csv

class Core:
	name = 'none'
	leg = 0.0
	def __init__(self, supplier, name, leg):
		self.supplier = supplier
		self.name = name
		self.leg = float(leg)
  
	def __repr__(self):
		return self.supplier + ":" + self.name + ": leg=" + str(self.leg) + " mm"

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
					bob = Core(row[0], row[1], row[4])
					table.append(bob);
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
