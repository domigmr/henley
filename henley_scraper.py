import requests
from requests_html import HTMLSession
import bs4
import json
import logging


def main():

    all_results = []

    pages_not_scraped = []

    for page_number in range(1, 379):

        print(page_number)

        url = "https://www.hrr.co.uk/results/?result-page="

        session = HTMLSession()
        r = session.get(url + str(page_number))
        try:
            r.html.render(timeout = 10)
        except:
            pages_not_scraped.append(page_number)
            continue

        result_cards = get_all_cards(r)

        r.session.close()

        for result in result_cards:
            result_info = get_info_in_card(result, page_number)

            all_results.append(result_info)

    with open("scraped_results_v2.json", "w") as f:
        json.dump(all_results, f)

    with open("page-numbers-not-scraped_v2.json", "w") as f:
        json.dump(pages_not_scraped, f)




def get_all_cards(r) -> list:

    soup = bs4.BeautifulSoup(r.html.raw_html, "html.parser")

    table = soup.find("div", {"class" : "results-table-wrapper"})

    result_cards = table.find_all("div", {"class" : "results-card__wrapper"})

    return result_cards




def get_info_in_card(result, page_number) -> dict:

    first_extra_info_line = result.find("div", {"class" : "results-card__row event-details desktop-only"})
    second_extra_info_line = first_extra_info_line.find("ul", {"class" : "inline-details"})
    barrier_info = result.find("div", {"class" : "record barrier"})
    fawley_info = result.find("div", {"class" : "record fawley"})
    finish_info = result.find("div", {"class" : "record finish"})
    verdict_info = result.find("div", {"class" : "record verdict"})

    info = {"page_number" : page_number,
            "winner" : result.find("div", {"class" : "club club--winning"}).get_text(),
             "loser" : result.find("div", {"class" : "club club--losing"}).get_text(),
             "cup" : first_extra_info_line.find("div").get_text(),
             "stage" : second_extra_info_line.find("li").get_text(),
             "boatclass" : second_extra_info_line.find_all("li")[1].get_text(),
             "winner_station" : second_extra_info_line.find_all("li")[2].get_text(),
             "time" : second_extra_info_line.find_all("li")[3].get_text(),
             "date" : second_extra_info_line.find_all("li")[4].get_text().strip().replace(" ", "").replace("\n", " "),
             "barrier_time" : barrier_info.find("div", {"class" : "stat split"}).get_text().strip(),
             "barrier_loser_leading" : True if barrier_info.find("div", {"class": "stat loser-leading active"}) else False,
             "fawley_time" : fawley_info.find("div", {"class" : "stat split"}).get_text().strip(),
             "fawley_loser_leading" : False,
             "finish_time" : finish_info.find("div", {"class" : "stat split"}).get_text().strip(),
             "verdict" : verdict_info.find("div", {"class" : "stat"}).get_text()}
    
    return info


if __name__ == '__main__':
    main()
