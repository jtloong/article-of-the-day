import requests, json, random
from pushbullet import Pushbullet


with open('keys.json') as f:
    d = json.load(f)

airtable_key = d['airtable']
pushbullet_key = d['pushbullet']

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


article_title, article_link = select_article(airtable_key)

print(article_title)
print(article_link)

pb = Pushbullet(pushbullet_key)

push = pb.push_link(article_title, article_link)