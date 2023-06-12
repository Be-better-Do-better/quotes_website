import codecs

FIRST_LINE_TO_INCLUDE = 14

#RAW_TEXT_FILE = './assets/data/raw_text.txt'
# RAW_TEXT_FILE = './assets/data/sample2.txt'
RAW_TEXT_FILE = './assets/data/ציטוטים שימושיים.txt'
TARGET_FILE = './assets/data/quotes2.txt'


text_to_write = ''
i = 0
f = codecs.open(RAW_TEXT_FILE, "r", "utf-8")
for line in f.readlines():
	if (i < FIRST_LINE_TO_INCLUDE) or line.startswith('<'):
		pass
	else:
		text_to_write += line
	i += 1
f.close()

f = codecs.open(TARGET_FILE, "w", "utf-8")
f.write(text_to_write[:-2])
f.close()
