class DumbBar():
	"""
	A text based loading bar!

	"""
	def __init__(self, showPercent=True, start='[', end=']', fill='=', empty=' ', length=79):
		self.showPercent = showPercent
		self.start = start
		self.end = end
		self.fill = fill
		self.empty = empty
		self.length = length - len(start) - len(end)
		if self.showPercent:
			self.length = self.length-6

	def done(self):
		print()

	def drawBar(self, percent):
		bar = ""
		bar += self.drawStart()
		filled, empty = self.getBalance(percent)
		bar += self.drawFilled(filled)
		bar += self.drawEmpty(empty)
		bar += self.drawEnd()
		if self.showPercent:
			bar += self.drawPercent(percent)
		print(bar, end='')

	def drawChar(self, char, count):
		return char * count

	def drawFilled(self, count):
		output = self.drawChar(self.fill,count)
		output = output[:count] if len(output) > count else output
		return output

	def drawEmpty(self, count):
		output = self.drawChar(self.empty,count)
		output = output[::-1]
		output = output[:count] if len(output) > count else output
		output = output[::-1]
		return output

	def drawEnd(self):
		return self.end

	def drawPercent(self,percent):
		percent = str(round(percent))
		spaces = 5 - 1 - len(percent)
		return " " * spaces + percent + "%"

	def drawStart(self):
		return "\r"+self.start
	
	def getBalance(self, percent):
		realPercent = percent/100.0
		total = self.length-2
		if not percent:
			return (0,total)
		filled = round(total*realPercent)
		empty = total-filled
		return (filled,empty)