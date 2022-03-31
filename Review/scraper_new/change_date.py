from datetime import datetime
def change1(date_to_change):
    date_new = date_to_change.replace("Januari ", "01/").replace("Februari ", "02/").replace("Maret ", "03/")\
        .replace("April ", "04/").replace("Mei ", "05/").replace("Juni ", "06/")\
        .replace("Juli ", "07/").replace("Agustus ", "08/").replace("September ", "09/")\
        .replace("Oktober ", "10/").replace("November ", "11/").replace("Desember ", "12/")
    date_new = datetime.strptime(date_new, '%m/%Y')
    return date_new

def change2(date_to_change):
    date_new = date_to_change.replace(" Januari ", "/01/").replace(" Februari ", "/02/").replace(" Maret ", "/03/")\
        .replace(" April ", "/04/").replace(" Mei ", "/05/").replace(" Juni ", "/06/")\
        .replace(" Juli ", "/07/").replace(" Agustus ", "/08/").replace(" September ", "/09/")\
        .replace(" Oktober ", "/10/").replace(" November ", "/11/").replace(" Desember ", "/12/")
    date_new = datetime.strptime(date_new, '%d/%m/%Y')
    return date_new

def change3(date_to_change):
    date_new = date_to_change.replace("Jan ", "01/").replace("Feb ", "02/").replace("Mar ", "03/")\
        .replace("Apr ", "04/").replace("Mei ", "05/").replace("Jun ", "06/")\
        .replace("Jul ", "07/").replace("Agt ", "08/").replace("Sep ", "09/")\
        .replace("Okt ", "10/").replace("Nov ", "11/").replace("Des ", "12/")
    date_new = datetime.strptime(date_new, '%m/%Y')
    return date_new

# tanggal = "Des 2019"
#
# d = ["11 Oktober 2021", "11 Oktober 2021", "27 Agustus 2021", "11 November 2021", "1 Agustus 2021", "2 Desember 2020", "21 November 2021"]
# tanggal = change2(tanggal)
# for month in d:
#     month = change2(month)
#     if month >= tanggal:
#         print(str(month))
#     else:
#         print(str(month) + " melewati tanggal terakhir")