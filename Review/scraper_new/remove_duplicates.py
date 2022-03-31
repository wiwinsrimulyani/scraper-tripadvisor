import pandas
bali_hotel = pandas.read_csv('hasil_bali_hotel2.csv')
bali_resto = pandas.read_csv('hasil_bali_resto2.csv')

new_bali_hotel = bali_hotel.drop_duplicates(subset = None, keep = 'first', inplace = False)
new_bali_resto = bali_resto.drop_duplicates(subset= None, keep = 'first', inplace = False)


print(bali_hotel.shape)
print(new_bali_hotel.shape)
print(bali_resto.shape)
print(new_bali_resto.shape)
print(jogja_hotel.shape)
print(new_jogja_hotel.shape)
print(jogja_resto.shape)
print(new_jogja_resto.shape)

new_bali_hotel.to_csv('bali_hotel_noduplicates.csv', index = False)
new_bali_resto.to_csv('bali_resto_noduplicates.csv', index = False)


def replace_month(df):
    df['date'] = df['date'].replace(to_replace = ['Januari', 'Februari', 'Maret', 'Mei', 'Juni', 'Juli', 'Agustus', 'Oktober', 'Desember'], value = ['January', 'February', 'March', 'May', 'June', 'July', 'August', 'October', 'December'], regex = True)
    return df

replace_month(bali_hotel)
replace_month(bali_resto)
replace_month(jogja_hotel)
replace_month(jogja_resto)

import os
#to create new folder
os.mkdir('./changed_date')

bali_hotel.to_csv('./changed_date/bali_hotel.csv', index = False)
bali_resto.to_csv('./changed_date/bali_resto.csv', index = False)
jogja_hotel.to_csv('./changed_date/jogja_hotel.csv', index = False)
jogja_resto.to_csv('./changed_date/jogja_resto.csv', index = False)