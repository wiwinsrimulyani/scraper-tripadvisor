import csv
from selenium import webdriver
from time import sleep
from random import randint
import change_date
import sys
from datetime import datetime

import multiprocessing
multiprocessing.set_start_method('spawn')

last_scraping = change_date.change3("Jul 2021")
driver = webdriver.Chrome(executable_path= 'D:\Review\scraper_new\chromedriver.exe')

urls = []
with open('url/Bali_things_2 baris.csv', 'r', encoding = 'ISO-8859-1') as oj:
    oj_reader = csv.reader(oj, delimiter = ',')
    for row in oj_reader:
        urls.append(row[0])
urls.pop(0)

f = open('Hasil/Bali/hasil_bali_things_coba.csv', 'w', newline='', encoding="utf-8")
with f:
    writer = csv.writer(f)
    writer.writerow(['name', 'date'])
    place_count = 0
    review_count = 0
    for url in urls:
        place_count = place_count + 1
        scraped_before_count = 0
        try:
            print('trying to load webpage ' + str(url))
            driver.get(url)
        except:
           print('failed to load webpage')
        sleep(randint(2,3))

        try:
            pagenum = driver.find_elements_by_class_name('pageNum ')
            # return a list
            try:
                numiter = int(pagenum[len(pagenum) - 1].text)
            except:
                pagenum = 0
        except:
            "page num tidak ada"
        if (pagenum == 0):
            numiter = 1

        while True:
            try:
                next_page_bttn = driver.find_element_by_xpath('//a[@aria-label = "Next page"]')
            except:
                "tidak ada"

            try:
                listings_date = driver.find_elements_by_class_name('_3JxPDYSx')
            except:
                "tidak ada"

            try:
                listings_date = driver.find_elements_by_class_name('fEDvV')
            except:
                "tidak ada"

            sleep(randint(1, 2))

            for listing in listings_date:
                try:
                    date1 = listing.text
                    date = date1.split(' • ')[0]

                    if (date is None):
                        date = date1
                except:
                    "tidak ada"
                try:
                    date = change_date.change3(date)
                    if date <= last_scraping:
                        print("Review tanggal " + str(date.strftime("%m/%d/%Y")) + "    sudah pernah discraping")
                        scraped_before_count += 1
                        continue
                except:
                    print("gagal compare tanggal")

                try:
                    name_place = driver.find_element_by_class_name('_3QHreJVJ').text
                    # print(name_place)
                except:
                    "tidak ada"

                try:
                    name_place = driver.find_element_by_class_name('DrjyGw-P._1SRa-qNz.qf3QTY0F').text
                    # print(name_place)
                except:
                    "tidak ada"

                try:
                    name_place = driver.find_element_by_class_name('WlYyy.cPsXC.GeSzT').text
                    # print(name_place)
                except:
                    "tidak ada"

                detail = []
                detail.append(name_place)
                detail.append(date.strftime("%m/%d/%Y"))
                review_count += 1
                writer.writerow(detail)


            print("place count : " + str(place_count))
            print("review count : " + str(review_count))
            print("review yang sudah discraping : " + str(scraped_before_count))

            # click the next button in pagination
            try:
                sleep(randint(1, 2))
                next_page_bttn.click()
                sleep(randint(1, 2))

                try:
                    if scraped_before_count == len(listings_date):
                        print("***** All review in this page have been collected. Go to next url *****")
                        break
                    print('<---------------------next page ----------------------->')
                    scraped_before_count = 0
                    # print('/n')
                    # print('/n')
                except:
                    "tidak ada"
            except:
                if (pagenum == 0):

                    try:
                        print('only 1 page')
                        break
                    except:
                        "tidak ada"
                else:
                    try:
                        print('the end of pagination')
                        break
                    except:
                        "tidak ada"


driver.close()