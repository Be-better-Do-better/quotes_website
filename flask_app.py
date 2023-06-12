from flask import Flask, render_template
from classes.quotes import Quotes

app = Flask(__name__,
            static_folder='./assets/',
            template_folder='./assets/templates/')


quotes = Quotes('./assets/data/quotes.txt')

@app.route('/', methods=['GET'])
def home():
	selected_quote = quotes.pick_random_quote()
	quote_text = str(selected_quote)
	quote_lines = quote_text.split('\n')
	return render_template('index.html', quote_lines=quote_lines)


if __name__ == '__main__':
	print('len(Quotes):')
	print(len(quotes.quotes))
	app.run()
