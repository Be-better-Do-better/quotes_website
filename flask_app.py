import os
from flask import Flask, render_template, send_from_directory
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


@app.route("/favicon.ico")
def fav():
	return send_from_directory(os.path.join(app.root_path, 'images'), 'favicon.ico')


if __name__ == '__main__':
	print(f"We have {len(quotes.quotes)} Quotes in total.")
	app.run()
