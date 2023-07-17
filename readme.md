Apartments Scraper for Rent in Katowice
=======================================

This Python project is designed to scrape apartment listings for rent in Katowice from the popular real-estate website Otodom. It uses the BeautifulSoup and Selenium libraries to extract data from the website and stores the results in an Excel file.

Requirements
------------

Before running the script, ensure you have the following installed:

-   Python 3.x
-   Selenium library
-   BeautifulSoup library
-   Pandas library
-   XlsxWriter library
-   Openpyxl library
-   Chrome WebDriver

You can install the required Python libraries using `pip`:

Copy code

`pip install selenium beautifulsoup4 pandas xlsxwriter openpyxl`

Save to grepper

Setting up Chrome WebDriver
---------------------------

1.  Download the Chrome WebDriver for your Chrome browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2.  Place the downloaded `chromedriver.exe` file in the `C:\Users\<username>\Downloads\chromedriver_win32\` directory.
3.  Make sure the `CHROME_DRIVER_PATH` variable in the script points to the correct location of `chromedriver.exe`.

How to Run
----------

1.  Clone the repository or download the script `apartments_scraper.py`.
2.  Make sure the required libraries and Chrome WebDriver are set up as mentioned above.
3.  Run the `apartments_scraper.py` script.

The script will scrape the apartment listings for rent in Katowice from the specified URL and store the data in an Excel file named `Apartments_for_rent_Katowice.xlsx` in the same directory.

Output
------

The Excel file `Apartments_for_rent_Katowice.xlsx` will contain the following columns:

-   ADDRESS: The address of the apartment.
-   PRICE (zł): The monthly rent price in Polish Złoty (PLN).
-   ROOMS: The number of rooms in the apartment.
-   AREA: The area of the apartment in square meters (m²).
-   ADDITIONAL COST (zł): Any additional costs associated with the rent in Polish Złoty (PLN).
-   LINK: The hyperlink to the original listing on the Otodom website.

Note
----

The script may take some time to complete, depending on the number of listings and your internet connection speed. Please be patient.

Disclaimer
----------

This project is intended for educational purposes only. Make sure to respect the terms and conditions of the website you are scraping data from. Always use web scraping responsibly and consider the website's policies regarding scraping and data usage.

Author
------

This project was developed by [Afeez Bolaji](https://github.com/Afeez-Ola).

Feel free to contribute, report issues, or suggest improvements via [GitHub](https://github.com/Afeez-Ola/apartment-listings-scraping).

License
-------

This project is licensed under the MIT License.