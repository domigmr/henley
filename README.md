# henley
Scraped results from the [Henley Royal Regatta website]([url](https://www.hrr.co.uk/results/?result-page=1)).

[Henley Royal Regatta]([url](https://www.hrr.co.uk/)) is a multi-day rowing competition that takes place in the town of Henley, England each year. It's been running since 1839, with a few breaks for the world wars and covid.

Each race is a head-to-head, knockout-style affair. Crews will race once a day, progressing to the next day if they win. The finals are always raced on Sunday.

The files in this repository document the scraping and cleaning process.

henley_scraper.py for the scraper

scraped_results_v2.json for the raw results

cleaning_and_transformation.ipnyb for the cleaning of the data

For the results, henley_results_cleaned.csv.

I hope this leads to some interesting and enjoyable analysis!

## data dictionary

| column_name         | type    | description |
| --------            | ------- | ---------|
| winner              | string  | winning crew - differs from club in that clubs can enter multiple crews in an event|
| winning_club        | string  | club of the winning crew|
| loser               | string  | losing crew - see above|
| losing_club         | string  | club of the losing crew|
| cup                 | string  | the event in which the race took place|
| stage               | string  | what stage of the competition (heats, semi-finals, or finals)|
| boatclass           | string  | what [type of boat]([url](https://en.wikipedia.org/wiki/Rowing_(sport)#Boat_classes)) was used|
| winner_station      | string  | which of the two stations the winner began from (either Bucks or Berks)|
| time                | string  | time at which race started - note that most of the races were recorded as 2:00am, I recorded these as None|
| date                | date    | date|
| barrier_time        | float   | the time of the first boat to reach the 'barrier' checkpoint|
|barrier_loser_leading| bool    | if the eventual loser was ahead at the barrier|
|fawley_time          | float   | the time of the first boat to reach the 'fawley' checkpoint|
|fawley_loser_leading | bool    | if the eventual loser was ahead at the fawley checkpoint|
|finish_time          | float   | the winning time|
|verdict              | string  | the distance betweeen the boats at the finish - mostly done in relative boatlengths (e.g 1 boat length - which varies between classes).|
