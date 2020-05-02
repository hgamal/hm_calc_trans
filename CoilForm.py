import csv

class CoilForm:
	supplier = ""
	model = ""
	type = ""
	obs = ""
	leg = 0.0
	stack = 0.0
	length = 0.0
	thickness = 0.0

	def __init__(self, supplier, model, leg, stack, lenght, thickness, type, obs):
		self.supplier = supplier
		self.model = model
		self.type = type
		self.obs = obs
		self.leg = float(leg)
		self.stack = float(stack)
		self.length = float(lenght)
		self.thickness = float(thickness)

	def __repr__(self):
		rc =  "model=\"" + self.supplier + ":" + self.model + "\", type=\"" + self.type + "\", leg=" + str(self.leg)
		rc = rc + " mm, stack=" + str(self.stack) + " mm, thickness=" + str(self.thickness) + " mm"
		return rc
    
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
					bob = CoilForm(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
					table.append(bob)
					# print(f'\t{row[0]}: code="{row[1]}"", leg={row[2]} mm')
					line_count += 1
			# print(f'Processed {line_count} lines.')
			return table

	@staticmethod
	def lookupCoilForms(table, sizemin, sizemax):
		resp = []
		for c in table:
			carea = c.leg * c.stack
			# print(carea, sizemin, sizemax)
			if sizemin <= carea and sizemax >= carea:
				resp.append(c)
		return resp
