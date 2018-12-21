# Kpop Scraper

## Original Plan

It would also have a browsing feature as groups and solo artists (no group associated) with a group picture, name, latest album, and associated social media accounts, which would expand with picture, name, and instagram account if they have one. Each person has an option to add to your custom list.

Once the user has chosen all the artists, it will show the most recent instagram photos on their list. (However, since Instagram killed off their API for users, this isn't possible.

There isn't a kpop database available with an API, so this project would scrape data from a user-submitted database website with profiles using Beautiful Soup and Python. (see /python for web scraping programs). For the groups, I will be using social media information parsed from public database file CSV. 

## Reality

I overestimated how many idols there were as there's 1500+ on the list. The scraper took about 45 minutes to complete and I couldn't use parallelization because I wanted to store things in order as indexed ids for use on the website.

I ended up using Node JS and Express to create the simple website.
