import requests
from collections import Counter
import json

def get_unique_key(lst, number=None):
	if number == None:
		return get_unique_key(lst, number=1)
	elif number in lst:
		number+=1
		return get_unique_key(lst, number)
	else:
		return number

def get_key(dictionary, value):
	for key, val in dictionary.items():
		if val == value:
			return key

class Puzzle:

	def __init__(self, quote=None, quoteAuthor=None,legend=None):
		if quote==None:
			self.quote = self.get_quote()['quoteText'].upper()
		else:
			self.quote = quote.upper()
		if quoteAuthor==None:
			self.quoteAuthor = self.get_quote()['quoteAuthor']
		else:
			self.quoteAuthor = quoteAuthor
		if legend == None:
			legend = self.get_legend()
		self.legend = legend
		self.puzzle = list()

	@property
	def answer_key(self):
		answer_key = {}
		if hasattr(self, 'legend'):
			answer_key.update(self.legend)
		for character in list(self.quote):
			number_keys = list(answer_key.keys())
			value_keys = list(answer_key.values())
			if character.isalpha():
				new_key = get_unique_key(number_keys)
				if character not in value_keys:
					answer_key[new_key] = character
		return answer_key

	def get_legend(self):
		legend = {}
		new_quote = ''.join([i for i in self.quote if i.isalpha()])
		counter_list = Counter(new_quote).most_common(3)
		top_letters = [letter for letter, number in counter_list]
		for letter in top_letters:
			key = get_key(self.answer_key, letter)
			legend[key] = letter
		print(counter_list)
		return legend

	def get_puzzle(self):
		for word in self.quote.split(" "):
			word = list(word)
			for index, character in enumerate(word):
				if character.isalpha():
					number = get_key(self.answer_key, character)
					word[index] = number
				else:
					word[index] = character
			self.puzzle.append(word)
		return self.puzzle

	def new(self, quote=None, legend=None):
		self.__init__()

	def get_quote(self):
		params = {
		'method':'getQuote',
		'lang':'en',
		'format':'json'
		}
		response = requests.get('http://api.forismatic.com/api/1.0/',params)
		jsonText = None
		while jsonText is None:
		    try:
		    	jsonText = json.loads(response.text)
		    except:
		         pass
		return jsonText