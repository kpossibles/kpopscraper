# Kpop Scraper

## Original Plan

It would also have a browsing feature as groups and solo artists (no group associated) with a group picture, name, latest album, and associated social media accounts, which would expand with picture, name, and instagram account if they have one. Each person has an option to add to your custom list.

Once the user has chosen all the artists, it will show the most recent instagram photos on their list.

There isn't a kpop database available with an API, so this project would scrape data from a user-submitted database website with profiles using Beautiful Soup and Python. (see /python for web scraping programs). For the groups, I will be using social media information parsed from public database file CSV. 

## Reality

I overestimated how many idols there were as there's 1500+ on the list. The scraper took about 45 minutes to complete and I couldn't use parallelization because I wanted to store things in order as indexed ids for use on the website.

I ended up using Node JS and Express to create the simple website with tabs for GROUPS, IDOLS (individuals), and RANDOM.

 However, since Instagram killed off their API for viewing public data of users, I couldn't complete that part of the project and only figured out a python script to scrape all the recent 12 posts from Instagram via all 1500+ artists. It's viewable on `/python/instagram-user.py` and I don't know how to translate that into javascript.

 ![Groups](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-groups.png)

 ![Idols](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-idols.png)

 ![Profile - HyunA](https://raw.githubusercontent.com/kpossibles/kpopscraper/master/screenshot-profile.png)

 I also tried to deploy this project to Heroku but it didn't work. http://kpopscraper.heroku.com doesn't work unfortunately and I coan't figure out why.

 ### Running the site

 Clone the git, install via `npm i` and run it with `npm start` which will start it up on `http://localhost:5000/
