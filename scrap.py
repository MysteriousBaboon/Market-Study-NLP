from bs4 import BeautifulSoup
import requests
import pandas as pd

# for categories
domain = "https://fr.trustpilot.com"
under_domain = "/categories/"
category_urls = ["food_beverages_tobacco", "animals_pets", "money_insurance",
                 "beauty_wellbeing", "construction_manufactoring", "education_training",
                 "electronics_technology", "events_entertainment", "hobbies_crafts",
                 "home_garden","media_publishing","restaurants_bars","health_medical",
                 "utilities", "home_services", "business_services", "legal_services_government",
                 "public_local_services", "shopping_fashion", "sports", "travel_vacation",
                 "vehicles_transportation"]


def scrap_db():
    df = pd.DataFrame(columns=['company', 'category', 'date', 'review', 'note'])

    for category in category_urls:
        page = requests.get(domain + under_domain + category)
        soup = BeautifulSoup(page.text, 'lxml')

        company_urls = soup.find_all("a", {"class": "link_internal__YpiJI link_wrapper__LEdx5",
                                         "target": "_blank", "aria-label": "", "rel": ""})

        for company in company_urls:
            url = domain + company["href"]
            page_2 = requests.get(url)
            soup_2 = BeautifulSoup(page_2.text, 'lxml')

            comp_name = soup_2.find("span", {"class": "multi-size-header__big"}).text
            reviews = soup_2.find_all("div", {"class": "review-content"})

            for el in reviews:
                stars = el.find("div", {"class": "star-rating star-rating--medium"}).find('img')['alt'][0]
                text = el.find("p", {"class": "review-content__text"})

                try:

                    date = el.find("p", {"class": "review-content__dateOfExperience"}).text
                except:
                    date = "too far"
                try:
                    text = text.text
                except:
                    text = None

                df = df.append({"company": comp_name, "category": category,
                                "date": date, 'review': text, "note": stars}, ignore_index=True)
    df.to_csv("scrap.csv")


def scrap_api(field, location):
    df = pd.DataFrame(columns=['company', 'date', 'review', 'note'])

    page = requests.get(domain + under_domain + field + f"?location={location}")
    soup = BeautifulSoup(page.text, 'lxml')
    company_urls = soup.find_all("a", {"class": "link_internal__YpiJI link_wrapper__LEdx5",
                                     "target": "_blank",
                                     "aria-label": "",
                                     "rel": ""})
    for company in company_urls:
        url = domain + company["href"]
        page_2 = requests.get(url)
        soup_2 = BeautifulSoup(page_2.text, 'lxml')

        comp_name = soup_2.find("span", {"class": "multi-size-header__big"}).text
        reviews = soup_2.find_all("div", {"class": "review-content"})

        for el in reviews:
            stars = el.find("div", {"class": "star-rating star-rating--medium"}).find('img')['alt'][0]
            text = el.find("p", {"class": "review-content__text"})

            try:

                date = el.find("p", {"class": "review-content__dateOfExperience"}).text
            except:
                date = "too far"
            try:
                text = text.text
            except:
                text = None

            df = df.append({"company": comp_name,
                            "date": date, 'review': text, "note": stars}, ignore_index=True)

        #TODO df = pd.DataFrame(columns=['company', 'category', 'global_note', 'number_reviews', 'date', '])

    df.to_csv("api.csv")





scrap_api("electronics_technology", "reims")