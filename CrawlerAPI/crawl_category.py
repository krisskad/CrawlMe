# !pip install kora -q
import sys
import requests
from bs4 import BeautifulSoup
import time

# from kora.selenium import wd as webdriver


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def platform():
    if sys.platform == 'linux':
        from kora.selenium import wd

        return wd

    elif sys.platform == 'win32':
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        try:
            browser = webdriver.Chrome(executable_path='src/drivers/chromedriver.exe', options=chrome_options)
        except:
            from webdriver_manager.chrome import ChromeDriverManager
            browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        return browser


# Extract All categories from websites
def get_all_categories(base_url):
    webpage = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # print(soup.prettify())
    category_data = dict()
    cat_temp = soup.findAll('div', class_='SMSubCat')
    for link in cat_temp:
        a = link.find_all("a")
        for i in a:
            if i.string is not None:
                key = i.string.split()
                key = " ".join(key)
                category_data[key.lower()] = i.get('href').replace(" ", "")
    return category_data


# Extract user requested categories from all categories
def get_required_categories(required_category, all_category):
    required_category = required_category.lower()
    required_category = required_category.split(" ")

    req_category_links = dict()
    for key in all_category.keys():
        # print(key)
        if all(cat in str(key).lower() for cat in required_category):
            # print(key)
            req_category_links[key] = all_category[key]

    return req_category_links


# Get all products from requested category
def get_all_products(browser, requested_categories):
    product_list = dict()
    for each_link in requested_categories.values():
        # print(each_link)

        # I used Firefox; you can use whichever browser you like.

        # Tell Selenium to get the URL you're interested in.
        browser.get(each_link)

        # Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
        lenOfPage = browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while match == False:
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True

        # Now that the page is fully scrolled, grab the source code.
        source_data = browser.page_source
        bs_data = BeautifulSoup(source_data, "html.parser")
        # print(bs_data.prettify())
        all_product_source = bs_data.find_all('div', class_='product-tuple-description ')
        # print(all_product_source)
        if all_product_source == None or all_product_source == "" or len(all_product_source) == 0:
            all_product_source = bs_data.find_all('div', class_='product-tuple-description')

        for data in all_product_source:
            for a in data.find_all('a'):
                product_name = a.find('p', class_='product-title')
                product_href = a.get('href')
                if product_name is not None and product_href is not None:
                    product_name = product_name.string

                    product_list[product_name] = product_href

    # print(len(product_list))
    # product_list["total_products"] = len(product_list)
    return product_list


def crawler(category):
    base_url = 'https://www.snapdeal.com/page/sitemap'

    all_cat = get_all_categories(base_url)

    req_cat = get_required_categories(category, all_cat)

    browser = platform()

    all_products = get_all_products(browser, req_cat)

    return all_products

# if __name__ == '__main__':
#     base_url = 'https://www.snapdeal.com/page/sitemap'
#     category = "tablet"
#
#     all_cat = get_all_categories(base_url)
#
#     req_cat = get_required_categories(category, all_cat)
#
#     browser = platform()
#
#     all_products = get_all_products(browser, req_cat)
#
#     print(all_products)

