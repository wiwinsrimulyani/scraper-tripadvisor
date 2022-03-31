import csv
from selenium import webdriver
from time import sleep
from random import randint
import multiprocessing
import sys
from datetime import datetime
import change_date
multiprocessing.set_start_method('spawn')
sys.stdout = open("Log\log_review_bali_resto.txt", "w")

########### Yang perlu diubah tiap nge run ##################
last_scraping = change_date.change2("31 Juli 2021")
f = open('Hasil/Bali/hasil_bali_resto_oktober21.csv', 'w', newline='', encoding="utf-8")
#############################################################

driver = webdriver.Chrome(executable_path= 'D:\Review\scraper_new\chromedriver.exe')
print('Latest activity from filename : review_bali_resto.py, in ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

urls = []
with open('url\Bali_resto_noduplicates.csv', 'r', encoding = 'ISO-8859-1') as oj:
    oj_reader = csv.reader(oj, delimiter = ',')
    for row in oj_reader:
        urls.append(row[0])
urls.pop(0)

with f:
    writer = csv.writer(f)
    writer.writerow(['name', 'title', 'date', 'review_text' ])
    place_count = 0
    review_count = 0

    for url in urls:
        place_count = place_count +1
        scraped_before_count = 0
        try:
            print('trying to load webpage ' + str(url))
            driver.get(url)
        except:
            print('failed to load webpage')
        sleep(randint(2,3))

        try:
            radio_bttn = driver.find_element_by_xpath('//*[@id="filters_detail_language_filterLang_ALL"]')
            driver.execute_script('arguments[0].click();', radio_bttn)
            sleep(2)
            print('page is ready')
        except:
            print('failed to click radio button')

        try:
            selengkapnya_bttn = driver.find_element_by_xpath("//span[contains(@class,'taLnk ulBlueLinks')]")
            driver.execute_script('arguments[0].click();', selengkapnya_bttn)
            sleep(2)
            print("'selengkapnya' button has been clicked!")
        except:
            print("there is no 'selengkapnya' button or failed to click")

        try:
            pagenum = driver.find_elements_by_class_name('pageNum ')
            # return a list
            try:
                numiter = int(pagenum[len(pagenum) - 1].text)

            except:
                try:
                    pagenum = 0
                    # print("[~~~~~~~~~~no contains page number~~~~~~~~~~]")
                except:
                    "tidak ada"
        except:
            "page num tidak ada"
        if (pagenum == 0):
            numiter = 1

        while True:
            try:
                next_page_bttn = driver.find_element_by_xpath('//a[@class = "nav next ui_button primary"]')
            except:
                "tidak ada"
            sleep(randint(1, 2))

            try:
                listings = driver.find_elements_by_class_name('review-container')
            except:
                "tidak ada"

                # get all review in that page
            #ini perulangan untuk tiap review per page
            for listing in listings:
                detail = []
                name_place = ""
                title = ""
                date1 = ""
                review_text = ""
                try:
                    date1 = listing.find_element_by_class_name('ratingDate').get_attribute("title")
                    # date = date1.split(': ')[1]
                except:
                    "tidak ada"

                try:
                    date1 = change_date.change2(date1)
                    if date1 <= last_scraping:
                        print("Review tanggal " + str(date1) + "    sudah pernah discraping")
                        scraped_before_count += 1
                        continue
                except:
                    print("gagal compare tanggal")
                    continue

                try:
                    name_place = driver.find_element_by_class_name('fHibz').text
                    # print(name_place)
                except:
                    "tidak ada"
                try:
                    name_place = driver.find_element_by_class_name('_3QHreJVJ').text
                    # print(name_place)
                except:
                    "tidak ada"
                try:
                    name_place = driver.find_element_by_class_name('_1mTlpMC3').text
                    # print(name_place)
                except:
                    "tidak ada"
                try:
                    name_place = driver.find_element_by_class_name('_3a1XQ88S').text
                    print(name_place)
                except:
                    "tidak ada"
                try:
                    name_place = driver.find_element_by_class_name('ui_header.h1').text
                    # print(name_place)
                except:
                    "tidak ada"


                try:
                    title = listing.find_element_by_class_name('noQuotes').text
                    # print(title)
                except:
                    "tidak ada"

                try:
                    review_text = listing.find_element_by_class_name('partial_entry').text
                    # print(review_text)
                except:
                    "tidak ada"


                detail.append(name_place)
                detail.append(title)
                detail.append(date1.strftime("%m/%d/%Y"))
                detail.append(review_text)
                # print(detail[1])
                review_count += 1
                writer.writerow(detail)

            print("place count : " + str(place_count))
            print("review count : " + str(review_count))
            print("review yang sudah discraping : " + str(scraped_before_count))

            try:
                next_page_bttn.click()
                sleep(randint(1,2))
                if(next_page_bttn is not None):
                    try:
                        if scraped_before_count >= 10:
                            print("***** All review in this page have been collected. Go to next url *****")
                            break
                        print('<---------------------next page ----------------------->')
                        scraped_before_count = 0
                        #print('/n')
                        #print('/n')
                    except:
                        "tidak ada"
            except:

                if(pagenum == 0):
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

            try:
                selengkapnya_bttn = driver.find_element_by_xpath("//span[contains(@class,'taLnk ulBlueLinks')]")
                driver.execute_script('arguments[0].click();', selengkapnya_bttn)
                sleep(2)
                try:
                    print("'selengkapnya' button has been clicked!")
                except:
                    "tidak ada"
            except:
                try:
                    print("there is no 'selengkapnya' button or failed to click")
                except:
                    "tidak ada"

print('Process finished at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
sys.stdout.close()
driver.close()