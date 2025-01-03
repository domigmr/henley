# henley
Scraped results from the [Henley Royal Regatta website](https://www.hrr.co.uk/results/?result-page=1).

[Henley Royal Regatta](https://www.hrr.co.uk/) is a multi-day rowing competition that takes place in the town of Henley, England each year. It's been running since 1839, with a few breaks for the world wars and covid.

Each race is a head-to-head, knockout-style affair. Crews will race once a day, progressing to the next day if they win. The finals are always raced on Sunday.

The files in this repository document the scraping and cleaning process.

For the scraper programme: henley_scraper.py

For the raw scraped results: scraped_results_v2.json

For cleaning and transformation of the data: cleaning_and_transformation.ipnyb

For the results, henley_results_cleaned.csv

I hope this leads to some interesting and enjoyable analysis!

## data dictionary

| column_name         | type    | description |
| --------            | ------- | ---------|
| winner              | string  | winning crew - differs from club in that clubs can enter multiple crews in an event in a given year|
| winning_club        | string  | club of the winning crew|
| loser               | string  | losing crew - see winner above|
| losing_club         | string  | club of the losing crew|
| cup                 | string  | the [event](https://www.hrr.co.uk/events-overview/) in which the race took place|
| stage               | string  | what stage of the competition (heats, semi-finals, or finals)|
| boatclass           | string  | what [type of boat](https://en.wikipedia.org/wiki/Rowing_(sport)#Boat_classes) was used|
| winner_station      | string  | which of the two [stations](https://en.wikipedia.org/wiki/Henley_Royal_Regatta#Racing) the winner began from (either Bucks or Berks)|
| time                | string  | time at which race started - note that most of the races were recorded as 2:00am, I changed these as None|
| date                | date    | date of race|
| barrier_time        | float   | the time in seconds for the first boat to reach the ['barrier'](https://en.wikipedia.org/wiki/Henley_Royal_Regatta#Racing) checkpoint|
|barrier_loser_leading| bool    | if the eventual loser was ahead at the barrier|
|fawley_time          | float   | the time (seconds) for the first boat to reach the ['fawley'](https://en.wikipedia.org/wiki/Henley_Royal_Regatta#Racing) checkpoint|
|fawley_loser_leading | bool    | if the eventual loser was ahead at the fawley checkpoint|
|finish_time          | float   | the winning time in seconds|
|verdict              | string  | the distance betweeen the boats at the finish - mostly done in relative boatlengths (e.g 1 boat length - which varies between classes). This has been left as string as some verdicts are given as 5 feet, 1 inch etc, which are not relative measurements and are left as an exercise to the reader.|
