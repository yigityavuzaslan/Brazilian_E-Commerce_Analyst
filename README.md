### Veri Sözlüğü (Data Dictionary)

Bu bölümde, projemizde kullanılan tüm veri dosyaları ve içerdiği kolonların açıklamaları yer almaktadır.
İsminde "clean" yazısı içeren csv dosyaları temizlenmiştir.

#### `customers.csv`
* **Açıklama:** E-ticaret platformundaki müşteriler hakkında benzersiz kimlik bilgileri içerir.
* **Kolonlar:**
    * `customer_id`: Müşterinin benzersiz kimliği.
    * `customer_unique_id`: Aynı müşterinin farklı siparişlerdeki tekil kimliği.
    * `customer_zip_code_prefix`: Müşterinin posta kodunun ilk beş hanesi.
    * `customer_city`: Müşterinin bulunduğu şehir.
    * `customer_state`: Müşterinin bulunduğu eyalet.

#### `geolocation.csv`
* **Açıklama:** Brezilya posta kodlarına karşılık gelen enlem ve boylam (coğrafi) bilgileri içerir.
* **Kolonlar:**
    * `geolocation_zip_code_prefix`: Posta kodunun ilk beş hanesi.
    * `geolocation_lat`: Enlem (latitude).
    * `geolocation_lng`: Boylam (longitude).
    * `geolocation_city`: Şehir adı.
    * `geolocation_state`: Eyalet adı.

#### `order_comment_message_clean.csv`
* **Açıklama:** Müşterilerin siparişler hakkında yaptığı yorumların temizlenmiş mesaj içeriklerini gösterir.

#### `order_comment_title_clean.csv`
* **Açıklama:** Müşterilerin siparişler hakkında yaptığı yorumların temizlenmiş başlık içeriklerini gösterir.

#### `order_items.csv`
* **Açıklama:** Siparişlerin içinde yer alan ürünler hakkında bilgiler içerir. (Bir siparişte birden fazla ürün olabilir.)
* **Kolonları:**
    * `order_id`: Siparişin kimliği.
    * `order_item_id`: Siparişteki ürünün sıra numarası.
    * `product_id`: Satılan ürünün kimliği.
    * `seller_id`: Ürünü satan satıcının kimliği.
    * `shipping_limit_date`: Kargonun son gönderim tarihi.
    * `price`: Ürünün fiyatı.
    * `freight_value`: Ürünün kargo ücreti.

#### `order_payments.csv`
* **Açıklama:** Siparişlerin ödeme bilgileri hakkında detaylar içerir. (Bir sipariş için birden fazla ödeme kaydı olabilir.)
* **Kolonları:**
    * `order_id`: Siparişin kimliği.
    * `payment_sequential`: Ödemenin sıra numarası.
    * `payment_type`: Ödeme türü (kredi kartı,kupon,vb.).
    * `payment_installments`: Taksit sayısı.
    * `payment_value`: Ödemenin toplam değeri.

#### `orderss_clean.csv`
* **Açıklama:** Platformdaki tüm siparişlerin ana bilgilerini içerir.
* **UYARI:** orders_clean.csv dosyası hatalıdır!!!
* **Kolonları:**
    * `order_id`: Siparişin benzersiz kimliği.
    * `customer_id`: Siparişi veren müşterinin kimliği.
    * `order_status`: Siparişin durumu (teslim edildi, kargoda, iptal edildi, vb.).
    * `order_purchase_timestamp`: Siparişin satın alınma tarihi ve saati.
    * `order_approved_at`: Ödemenin onaylandığı tarih ve saati.
    * `order_delivered_carrier_date`: Siparişin kargoya verildiği tarih.
    * `order_delivered_customer_date`: Siparişin müşteriye teslim edildiği tarih.
    * `order_estimated_delivery_date`: Siparişin tahmini teslimat tarihi.

#### `product.csv`
* **Açıklama:** E-ticaret platformunda listelenen ürünlerin ana özelliklerini içerir.
* **Kolonlar:**
    * `product_id`: Ürünün benzersiz kimliği.

    * `product_category_name`: Ürünün kategorisi.

    * `product_name_lenght`: Ürün adının uzunluğu.

    * `product_description_lenght`: Ürün açıklamasının uzunluğu.

    * `product_photos_qty`: Ürünün fotoğraf sayısı.

    * `product_weight_g`: Ürünün ağırlığı (gram).

    * `product_length_cm`: Ürünün uzunluğu (cm).

    * `product_height_cm`: Ürünün yüksekliği (cm).

    * `product_width_cm`: Ürünün genişliği (cm).
 
#### `sellers_dataset.csv`
* **Açıklama:** Platformdaki satıcılar hakkında bilgiler içerir.
* **Kolonları:**
    * `seller_id`: Satıcının benzersiz kimliği.

    * `seller_zip_code_prefix`: Satıcının posta kodunun ilk beş hanesi.

    * `seller_city`: Satıcının bulunduğu şehir.

    * `seller_state`: Satıcının bulunduğu eyalet. 

















