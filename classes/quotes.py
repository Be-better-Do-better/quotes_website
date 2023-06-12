import numpy as np
import codecs
import re
import random
from collections import Counter
from classes.quote import Quote

from auxiliary.utils import DEFAULT_QUOTEE, QUOTE_PATTERN, SYS_SEPERATOR  # QUOTE_WITH_TRANSLATION_PATTERN

COMPILED_QUOTE_PATTERN = re.compile(QUOTE_PATTERN)


class Quotes(object):
	def __init__(self, quotes_file_name):
		self.quotes_file_name = quotes_file_name
		self.quotes = []
		self.weights = None
		self.quotees_counter = Counter()
		self.last_quote = None

		self.load_quotes()
		constant_weights = np.ones(len(self.quotes))
		self.weights = np.expand_dims(constant_weights, axis=1)

	def load_quotes(self):
		splitting_delimiter = SYS_SEPERATOR*2  # os.linesep*2  # '\n\n'
		f = codecs.open(self.quotes_file_name, "r", "utf-8")
		all_quotes_text = f.read()
		f.close()

		all_quotes = all_quotes_text.split(splitting_delimiter)
		for full_quote in all_quotes:
			self.quotes.append(self.extract_quote(full_quote))

	def extract_quote(self, full_quote):
		full_quote_lines = full_quote.split(SYS_SEPERATOR)
		quote_lines = []
		quotee_and_source = DEFAULT_QUOTEE

		for quote_line in full_quote_lines:
			if COMPILED_QUOTE_PATTERN.match(quote_line):
				# quote, quotee_and_source = COMPILED_QUOTE_PATTERN.match(full_quote).groups()
				# quote_addition, quotee_and_source = COMPILED_QUOTE_PATTERN.match(quote_line).groups()
				m = re.match(COMPILED_QUOTE_PATTERN, quote_line)
				quote_addition = m.group(1)
				quotee_and_source = m.group(2)
				quote_lines.append(quote_addition)
			else:
				# quote_addition, quotee_and_source = COMPILED_QUOTE_PATTERN.match(quote_line).groups()
				quote_lines.append(quote_line)

		quote = SYS_SEPERATOR.join(quote_lines)

		quotee, source = self.extract_quotee_and_source(quotee_and_source)

		return Quote(quote=quote, quotee=quotee, source=source)

	@staticmethod
	def extract_quotee_and_source(quotee_and_source):
		source = None  # init value
		m = re.search(',', quotee_and_source)
		if m:
			quotee = quotee_and_source[:m.start()]
			source = quotee_and_source[m.start()+2:]
		else:
			quotee = quotee_and_source
		return quotee, source

	def pick_random_quote(self) -> Quote:
		selected_quote_as_list = random.choices(self.quotes, weights=self.weights, cum_weights=None, k=1)
		return selected_quote_as_list[0]
