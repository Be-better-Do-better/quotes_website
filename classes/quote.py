class Quote(object):
	def __init__(self, quote, quotee=None, source=None):
		self.quote = quote
		self.quotee = quotee
		self.source = source

	def __str__(self):
		s = self.quote
		if self.source is None:
			s += '(' + self.quotee + ')'
		else:
			s += '(' + self.quotee + ' ,' + self.source + ')'
		return s
