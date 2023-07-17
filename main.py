from pprint import pprint
import pandas as pd
from scrape_page_content import ScrapePageContent
from bs4 import BeautifulSoup

url = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/slaskie/katowice/katowice/katowice?distanceRadius=5&page=1&limit=36&isPromoted=true&priceMax=2000&by=LATEST&direction=DESC&viewType=listin"

response = ScrapePageContent().pageContent(url)
soup = BeautifulSoup(response, 'lxml')
listings_link_body1 = soup.select('[data-cy="listing-item-link"]')

second_page_url = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/slaskie/katowice/katowice/katowice?distanceRadius=5&page=2&limit=36&isPromoted=true&priceMax=2000&by=LATEST&direction=DESC&viewType=listin"

response = ScrapePageContent().pageContent(second_page_url)
soup = BeautifulSoup(response, 'lxml')
listings_link_body2 = soup.select('[data-cy="listing-item-link"]')
total_listings_body = listings_link_body1 + listings_link_body2
listings_link_body = [str(link) for link in total_listings_body]

def has_zl_mc(text):
    return 'zł/mc' in text or "zł/miesiąc" in text
def has_pokoje_mc(text):
    return 'pokoje' in text or 'pokój' in text

def has_m2_mc(text):
    return 'm²' in text


listings = BeautifulSoup("".join(listings_link_body), 'html.parser')

listing_data = []
for listing in listings.find_all('a', class_='css-1up0y1q e1n6ljqa3'):
    location = listing.find('p', class_='css-14aokuk e1ualqfi4').get_text().strip()
    link = listing.get('href')
    link = "https://otodom" + link
    price_text = listing.find('span', class_='css-1on0450 ei6hyam2', string=has_zl_mc)
    price = int(price_text.get_text().strip()[:4]) if price_text else None
    room_text = listing.find("span", class_="css-1on0450 ei6hyam2", string=has_pokoje_mc)
    rooms = room_text.get_text().strip() if room_text else None
    area_text = listing.find('span', class_='css-1on0450 ei6hyam2', string=has_m2_mc)
    area = area_text.get_text().strip() if area_text else None
    additional_cost_text = listing.find('span', class_='css-5qfobm ei6hyam4', string=has_zl_mc)

    if additional_cost_text:
        additional_cost = ((((additional_cost_text.get_text().split(":"))[1]).split("/")[0]).split()[0])
        if additional_cost == '674,05':
            additional_cost = additional_cost.replace(',', '.')
        additional_cost = int(float(additional_cost))

    listing_info = {
        'ADDRESS': location,
        'PRICE (zł)': price,
        'ROOMS': rooms,
        'AREA': area,
        'ADDITIONAL COST (zł)': additional_cost,
        "LINK": link
    }
    listing_data.append(listing_info)

listings_dataframe = pd.DataFrame(listing_data)
pprint(listings_dataframe)
output_file = "Apartments_for_rent_Katowice.xlsx"
writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

listings_dataframe.to_excel(writer, index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

hyperlink_format = workbook.add_format({'color': 'blue', 'underline': 1})

worksheet.set_column('A:A', None, hyperlink_format)
for row_num, address in enumerate(listings_dataframe['ADDRESS'], start=1):
    worksheet.write_url(row_num, 0, address)

writer._save()