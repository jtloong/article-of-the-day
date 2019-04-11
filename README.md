# article-of-the-day

I use [Airtable](https://airtable.com/) to record what I've been reading / listening to (books, papers, articles, podcasts, lectures). I also use it to record things I want to read in the future, except I found I would never read it.

This script is meant to run on CRON to send me one random paper/article from my to-read list on Airtable everyday via [Pushbullet](https://www.pushbullet.com/). 

## Instructions

If you want to run this yourself you'll need to modify this to fit your Airtable set up. Major things are authentication, I have a private `.json` file with the following format:

```json
{
	"airtable": "AIRTABLE-API-KEY",
	"pushbullet": "PUSHBULLET-API-KEY"
}
```

You'll also need to change your Airtable link to point to the specific table you have in your account. Check out the [Airtable](https://airtable.com/api) and [Pushbullet](https://docs.pushbullet.com/) API docs for more info.

