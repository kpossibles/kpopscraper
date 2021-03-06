# Kpop Scraper

## Original Plan

It would also have a browsing feature as groups and solo artists (no group associated) with a group picture, name, latest album, and associated social media accounts, which would expand with picture, name, and instagram account if they have one. Each person has an option to add to your custom list.

Once the user has chosen all the artists, it will show the most recent instagram photos on their list.

There isn't a kpop database available with an API, so this project would scrape data from a user-submitted database website with profiles using Beautiful Soup and Python. (see /python for web scraping programs). For the groups, I will be using social media information parsed from public database file CSV. 

## Reality

I overestimated how many idols there were as there's 1500+ on the list. The scraper took about 45 minutes to complete and I couldn't use parallelization because I wanted to store things in order as indexed ids for use on the website.

I ended up using Node JS and Express to create the simple website with tabs for GROUPS, IDOLS (individuals), and RANDOM.

However, since Instagram killed off their API for viewing public data of users, I couldn't complete that part of the project and only figured out a python script to scrape all the recent 12 posts from Instagram via all 1500+ artists. It's viewable on `/python/instagram-user.py` and I don't know how to translate that into javascript.

Something else I learned during this project was deploying to Heroku. After following the steps, you must include `Procfile` and make sure the [port on your server](https://stackoverflow.com/questions/30787451/deploy-node-js-app-on-heroku-succeeds-but-doesnt-work) is 

```
var port = process.env.PORT || 3000;
app.listen(port);
```

### Website

You can view the live site on https://kpopscraper.herokuapp.com/

![Groups](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-groups.png)

![Idols](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-idols.png)

![Profile - HyunA](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-profile.png)

 ### Running the site

 Clone the git, install via `npm i` and run it with `npm start` which will start it up on http://localhost:5000/
