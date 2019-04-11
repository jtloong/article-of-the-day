import requests, json, random


with open('keys.json') as f:
    d = json.load(f)

key = d['airtable']

def select_article(key):
	link = "https://api.airtable.com/v0/appdpiET2lgP7D2fM/Future%20Reads?view=Grid%20view"
	authorization = "Bearer " + key
	r=requests.get(link, headers={"Authorization": authorization})

	records = r.json()

	titles, links = [], []
	for item in records['records']:
		fields = item['fields'] 

		try:
			titles.append(fields['Name'])
			links.append(fields['Link'])
			# print(fields['Name'])

		except:
			break

	selection = random.choice(range(len(titles)))

	return titles[selection], links[selection]