from requests import get

response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
print(response.json()['quoteText'])
print(response.json()['quoteAuthor'])