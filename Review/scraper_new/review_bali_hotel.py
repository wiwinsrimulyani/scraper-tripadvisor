import csv
from selenium import webdriver
from time import sleep
from random import randint
import multiprocessing
import sys
from datetime import datetime
import change_date

multiprocessing.set_start_method('spawn')
sys.stdout = open("Log\log_review_bali_hotel.txt", "w")

########### Yang perlu diubah tiap nge run ##################
last_scraping = change_date.change1("Juli 2021")
f = open('Hasil/Bali/hasil_bali_hotel_oktober21.csv', 'w', newline='', encoding="utf-8")
#############################################################

driver = webdriver.Chrome(executable_path= 'D:\Review\scraper_new\chromedriver.exe')
print('Latest activity from filename : review_bali_hotel.py, in ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

urls = []
with open('url\Bali_hotel_noduplicates.csv', 'r', encoding = 'ISO-8859-1') as oj:
    oj_reader = csv.reader(oj, delimiter = ',')
    for row in oj_reader:
        urls.append(row[0])
urls.pop(0)

with f:
    writer = csv.writer(f)
    writer.writerow(['name', 'title', 'date', 'review_text'])

    place_count = 0
    review_count = 0

    for url in urls:
        place_count = place_count + 1
        scraped_before_count = 0

        #trying to load page
        try:
            print('trying to load webpage ' + str(url))
            driver.get(url)
        except:
            print('failed to load webpage '+ str(url))
        sleep(randint(2, 3))

        #trying to click radio button
        try:
            radio_bttn = driver.find_element_by_id('LanguageFilter_0')
            driver.execute_script('arguments[0].click();', radio_bttn)
            sleep(2)
            print('page is ready')
        except:
            print('failed to click radio button')

        #check page number
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

        #extract the data
        while True:
            try:
                next_page_bttn = driver.find_element_by_xpath('//a[@class = "ui_button nav next primary "]')
            except:
                "tidak ada"
            sleep(randint(1, 2))

            try:
                listings = driver.find_elements_by_class_name('cqoFv._T')
            except:
                "tidak ada"

            for listing in listings:

                try:
                    date1 = listing.find_element_by_class_name('_34Xs-BQm').text
                    date = date1.split(': ')[1]
                except:
                    "tidak ada"
                try:
                    date1 = listing.find_element_by_class_name('euPKI._R.Me.S4.H3').text
                    date = date1.split(': ')[1]
                except:
                    "tidak ada"
                try:
                    date = change_date.change1(date)
                    if date <= last_scraping:
                        print("Review tanggal " + str(date) + "    sudah pernah discraping")
                        scraped_before_count += 1
                        continue
                except:
                    print("gagal compare tanggal")


                try:
                    name_place =  driver.find_element_by_class_name('_3QHreJVJ').text
                except:
                    "tidak ada"
                try:
                    name_place =  driver.find_element_by_class_name('fkWsC.b.d.Pn').text
                except:
                    "tidak ada"
                try:
                    name_place =  driver.find_element_by_class_name('_1mTlpMC3').text
                except:
                    "tidak ada"
                try:
                    name_place =  driver.find_element_by_class_name('ui_header.h1').text
                except :
                    "tidak ada"

                try:
                    title = listing.find_element_by_class_name('ocfR3SKN').text
                    # print(title)
                except:
                    "tidak ada"
                try:
                    title = listing.find_element_by_class_name('fCitC').text
                    # print(title)
                except:
                    "tidak ada"

                try:
                    review_text = listing.find_element_by_class_name('IRsGHoPm').text
                    # print(review_text)
                except:
                    "tidak ada"
                try:
                    review_text = listing.find_element_by_class_name('XllAv.H4._a').text
                    # print(review_text)
                except:
                    "tidak ada"

                detail = []
                detail.append(name_place)
                detail.append(title)
                detail.append(date.strftime("%m/%d/%Y"))
                detail.append(review_text)
                writer.writerow(detail)
                review_count += 1

            print("place count : " + str(place_count))
            print("review count : " + str(review_count))



            try:
                next_page_bttn.click()
                sleep(randint(1, 2))
                if (next_page_bttn is not None):
                    try:
                        if scraped_before_count >= 5:
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
print('Process finished at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
sys.stdout.close()
driver.close()