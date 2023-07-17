from pprint import pprint
import pandas as pd
from scrape_page_content import ScrapePageContent
from bs4 import BeautifulSoup


def has_zl_mc(text):
    return 'zł/mc' in text or "zł/miesiąc" in text


def has_pokoje_mc(text):
    return 'pokoje' in text or 'pokój' in text


def has_m2_mc(text):
    return 'm²' in text


def parse_additional_cost(additional_cost_text):
    if additional_cost_text:
        additional_cost = ((((additional_cost_text.get_text().split(":"))[1]).split("/")[0]).split()[0])
        if additional_cost == '674,05':
            additional_cost = additional_cost.replace(',', '.')
        return int(float(additional_cost))
    return None


def scrape_listings_data(url):
    response = ScrapePageContent().pageContent(url)
    soup = BeautifulSoup(response, 'lxml')
    listings_link_body = soup.select('[data-cy="listing-item-link"]')
    listings_html = "".join([str(link) for link in listings_link_body])
    return BeautifulSoup(listings_html, 'html.parser')


def extract_listing_info(listing):
    location = listing.find('p', class_='css-14aokuk e1ualqfi4').get_text().strip()
    price_text = listing.find('span', class_='css-1on0450 ei6hyam2', string=has_zl_mc)
    price = int(price_text.get_text().strip()[:4]) if price_text else None
    room_text = listing.find("span", class_="css-1on0450 ei6hyam2", string=has_pokoje_mc)
    rooms = room_text.get_text().strip() if room_text else None
    area_text = listing.find('span', class_='css-1on0450 ei6hyam2', string=has_m2_mc)
    area = area_text.get_text().strip() if area_text else None
    additional_cost_text = listing.find('span', class_='css-5qfobm ei6hyam4', string=has_zl_mc)
    additional_cost = parse_additional_cost(additional_cost_text)

    listing_info = {
        'ADDRESS': location,
        'PRICE (zł)': price,
        'ROOMS': rooms,
        'AREA': area,
        'ADDITIONAL COST (zł)': additional_cost
    }
    return listing_info


def main():
    base_url = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/slaskie/katowice/katowice/katowice"
    params = "?distanceRadius=5&page={}&limit=36&isPromoted=true&priceMax=2000&by=LATEST&direction=DESC&viewType=listin"

    total_pages = 2  # Update this if you know the total number of pages to scrape.
    all_listing_data = []

    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}{params.format(page_num)}"
        listings_page = scrape_listings_data(page_url)

        for listing in listings_page.find_all('a', class_='css-1up0y1q e1n6ljqa3'):
            listing_info = extract_listing_info(listing)
            all_listing_data.append(listing_info)

    listings_dataframe = pd.DataFrame(all_listing_data)
    pprint(listings_dataframe)

    output_file = "Apartments_for_rent_Katowice.xlsx"
    listings_dataframe.to_excel(output_file, index=False)


if __name__ == "__main__":
    main()
