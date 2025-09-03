import pandas as pd
import seaborn as sns
import os

"""
orders = pd.read_csv(r"data_file\olist_orders_dataset.csv")
print(orders.head())
print(orders.info())
print(orders.isnull().sum())

#->>null verileri doldurma-silme
#delivered_customer_date kolonunda 99 bin tane değer olduğu 3 bin tanesi null değermiş,silebiliriz
#3 kolonun null verilerini sildik

orders_clean = orders.dropna(subset=['order_delivered_customer_date','order_approved_at','order_delivered_carrier_date'])
print(orders_clean.head())
print(orders_clean.isnull().sum())

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'orders_clean.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
orders_clean.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""



"""
product = pd.read_csv(r"data_file\product_category_name_translation.csv")

print(product.head())
print(product.info())
print(product.describe())

print(product.isnull().sum())
#null veri yok o yüzden temizlik yapmaya gerek yok

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'product.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
product.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")

"""


"""
customers = pd.read_csv(r"data_file\olist_customers_dataset.csv")
print(customers.head())
print(),print(),print()

print(customers.info())
print(),print(),print()

print(customers.describe())
print(),print(),print()

print(customers.isnull().sum())
#temizliğe gerek yok null veri yok

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'customers.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
customers.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""




"""
geolocation = pd.read_csv(r"data_file\olist_geolocation_dataset.csv")
print(geolocation.head())
print(),print(),print()

print(geolocation.info())
print(),print(),print()

print(geolocation.isnull().sum())
print(),print(),print()
##veri temiz 

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'geolocation.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
geolocation.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""




"""
order_items = pd.read_csv(r"data_file\olist_order_items_dataset.csv")
print(order_items.head())
print(),print(),print()

print(order_items.info())
print(),print(),print()

print(order_items.isnull().sum())
print(),print(),print()

print(order_items.describe())
#veri temiz

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'order_items.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
order_items.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""






"""
order_payments=pd.read_csv(r"data_file\olist_order_payments_dataset.csv")
print(order_payments.head())
print(),print(),print()

print(order_payments.info())
print(),print(),print()

print(order_payments.isnull().sum())
print(),print(),print()

print(order_payments.describe())
#veri temiz

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'order_payments.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
order_payments.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""



"""
order_reviews = pd.read_csv(r"data_file\olist_order_reviews_dataset.csv")

print(order_reviews.head())
print(),print(),print()

print(order_reviews.info())
print(),print(),print()

print(order_reviews.isnull().sum())
print(),print(),print()

print(order_reviews.describe())
print(),print(),print()

#->>Veri Temizliği
order_comment_message_clean=order_reviews['review_comment_message'] = order_reviews['review_comment_message'].fillna("Yorum Yok")
print(order_comment_message_clean.isnull().sum())
#boş olan kısımları "yorum yok" şeklinde dolduruldu.

print(),print(),print()

order_comment_title_clean=order_reviews['review_comment_title'] = order_reviews['review_comment_title'].fillna("Başlık Yok")
print(order_comment_title_clean.isnull().sum())
#boş olan kısımlar "başlık yok" şelinde dolduruldu.
#1.kaydetme
klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'order_comment_message_clean.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
order_comment_message_clean.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")

#2.kaydetme
klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'order_comment_title_clean.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
order_comment_title_clean.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")
"""



sellers_dataset=pd.read_csv(r"data_file\olist_sellers_dataset.csv")
print(sellers_dataset.head())
print(),print(),print()

print(sellers_dataset.info())
print(),print(),print()

print(sellers_dataset.isnull().sum())
print(),print(),print()

#->>Anlaşılır olması için kısaltmalar uzatıldı.
state_mapping = {
    "SP": "São Paulo",
    "RJ": "Rio de Janeiro",
    "MG": "Minas Gerais",
    "RS": "Rio Grande do Sul",
    "PR": "Paraná"
}

sellers_dataset['seller_state_long'] = sellers_dataset['seller_state'].map(state_mapping)

print(sellers_dataset["seller_state_long"].head())
##null veri yok, temiz veri

klasor_yolu = 'temiz veriler'
dosya_yolu = os.path.join(klasor_yolu, 'sellers_dataset.csv')

#veri klasörü oluşturma
os.makedirs(klasor_yolu, exist_ok=True)
#veriyi csv dosyasına kaydetme
sellers_dataset.to_csv(dosya_yolu, index=False, header=False)

print(f"Veri, '{dosya_yolu}' klasörüne kaydedildi.")