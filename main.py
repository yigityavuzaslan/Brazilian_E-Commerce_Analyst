import pandas as pd
import seaborn as sns

"""
orders = pd.read_csv(r"data_file\olist_orders_dataset.csv")
print(orders.head())
print(orders.info())
print(orders.isnull().sum())

->>null verileri doldurma-silme
#delivered_customer_date kolonunda 99 bin tane değer olduğu 3 bin tanesi null değermiş,silebiliriz
#3 kolonun null verilerini sildik

orders_clean = orders.dropna(subset=['order_delivered_customer_date','order_approved_at','order_delivered_carrier_date'])
print(orders_clean.head())
print(orders_clean.isnull().sum())
"""



"""
product = pd.read_csv(r"data_file\product_category_name_translation.csv")

print(product.head())
print(product.info())
print(product.describe())

print(product.isnull().sum())
#null veri yok o yüzden temizlik yapmaya gerek yok
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

->>Veri Temizliği
order_comment_message_clean=order_reviews['review_comment_message'] = order_reviews['review_comment_message'].fillna("Yorum Yok")
print(order_comment_message_clean.isnull().sum())
#boş olan kısımları "yorum yok" şeklinde dolduruldu.

print(),print(),print()

order_comment_title_clean=order_reviews['review_comment_title'] = order_reviews['review_comment_title'].fillna("Başlık Yok")
print(order_comment_title_clean.isnull().sum())
#boş olan kısımlar "başlık yok" şelinde dolduruldu.
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