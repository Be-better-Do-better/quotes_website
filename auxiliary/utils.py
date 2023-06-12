import os
import re

SYS_SEPERATOR = '\r\n'

QUOTES_FILE_NAME = 'quotes.txt'
DEFAULT_QUOTEE = 'Anonymous'

QUOTE_PATTERN = '(.*)\((.*)\)$'
# QUOTE_WITH_TRANSLATION_PATTERN = '(.*\n)(.*)\((.*)\)$'
#QUOTE_WITH_TRANSLATION_PATTERN = '(.*)'+os.linesep+'(.*)\((.*)\)$'

COMPILED_QUOTE_PATTERN = re.compile(QUOTE_PATTERN)
# COMPILED_QUOTE_WITH_TRANSLATION_PATTERN = re.compile(QUOTE_WITH_TRANSLATION_PATTERN)