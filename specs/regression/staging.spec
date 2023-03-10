Regression Staging
===================


Üye Girişi - Ekran kontrolü
------------------------------
tags:regressionStaging_uyeGirisiEkranKontrolu

* Dominos - Staging ortamına gidilir
* Giris Yap butonuna tiklanir
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:regressionStaging_uyeGirisiParolamiUnuttum

* Dominos - Staging ortamına gidilir
* Giris Yap butonuna tiklanir
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:regressionStaging_uyeOlmaEkrankontrolu

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:regressionStaging_uyeOlmaBasariliUyeOlma

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:regressionStaging_uyeOlmaBasariliUyeOlma2

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:regressionStaging_uyeOlmadanDevamEtButtonKontrol

* Dominos - Staging ortamına gidilir
* Giris Yap butonuna tiklanir
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:regressionStaging_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Staging ortamına gidilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Giris Yap butonuna tiklanir
* Element var mı kontrol et "girisYapButon"
* Elementi bekle ve sonra tıkla "uyeOlTabButon"
* Element var mı kontrol et "uyeOlSayfasiUyeOlButon"
* Üye olmadan devam edilir


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
 tags:regressionStaging_uyeAdresEklemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Adalar/Burgazada mah)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Gel Al - Yeni Üye
------------------------------------------
 tags:regressionStaging_uyeAdresDuzenlemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Sepete Kampanya Ekleme - Adrese Teslim - Üye - Kampanya 1
-----------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeAdreseTeslimUyeKampanya1

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Kampanya 3
-----------------------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeAdreseTeslimUyeliksizKampanya3

* Dominos - Staging ortamına gidilir
* Uyeliksiz, adrese teslim servis tipi secilir ve anasayfaya devam edilir (Stg)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye - Kampanya 4
-----------------------------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeGelAlUyeKampanya4

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz -  Kampanya 6
----------------------------------------------------------------------------------------
 tags:regressionStaging_sepeteKampanyaEklemeGelAlUyeliksizKampanya6

* Dominos - Staging ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
 İlk ürün düzenlemeye tıklanır
 Sucuk ve mısır malzemeleri çıkarılır
 Ekstra Malzeme Ekle butonuna tıklanır
 Cheddar ve Mozarella eklenir
 Ekstra Malzeme Ekle butonuna tıklanır
 Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
 tags:regressionStaging_pizzaEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Stg)
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üyeliksiz
------------------------------------------------
 tags:regressionStaging_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Stg)
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üye
------------------------------------------------
 tags:regressionStaging_pizzaEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Stg)
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üyeliksiz
------------------------------------------------
 tags:regressionStaging_pizzaEklemeGelAlUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir (Stg)
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki içecek eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında icecek yazısının geldigi kontrol edilir (Stg)
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Upsell popup varsa kapatilir
* Sepetim ikonuna tıklanır
* Sepetteki içecek eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında icecek yazısının geldigi kontrol edilir (Stg)


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Upsell popup varsa kapatilir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki içecek eklendiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki içecek eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest1@hotmail.com" ve "a1w2d3r4D" şifre girilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında icecek yazısının geldigi kontrol edilir (Stg)


Sepetten Upcell Ekleme - Gel Al - Üyeliksiz
--------------------------------------------------
 tags:regressionStaging_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki içecek eklendiği kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir



Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Yeni üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:regressionStaging_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
 tags:regressionStaging_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Cookie varsa kapat butonuna tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:regressionStaging_adresSecimiUyeliksizGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
 Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
 tags:regressionStaging_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Seçili adres ile devam edilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
 tags:regressionStaging_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Nakit
----------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Nakit
----------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Nakit
-------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlNakit

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Nakit
------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Nakit
-----------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Kredi Kartı
-----------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Kredi Kartı
--------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Kredi Kartı
-------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Kredi Kartı
------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Kredi Kartı
------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Sodexo Kart
-------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Sodexo Yemek Çeki
----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir

Ödeme Tipi Secimi - Yeni Üye - Gel Al - Sodexo Yemek Çeki
----------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Sodexo Yemek Çeki
-------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Sodexo Yemek Çeki
-------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Yemek Çeki
-----------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Yemek Çeki
-------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Multinet
--------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Multinet
-------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Multinet
-----------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Multinet
--------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme Multinet seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Setcard
-------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Setcard
------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Setcard
---------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Setcard
----------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlSetCard

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Setcard
--------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Yemek cekleri ve kartlari odeme tipi secilir
* Kapıda ödeme setCard seçeneği ile devam edilir (Stg)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir (Stg)
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Online Ödeme
------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Online ödeme seçeneği ile devam edilir (Stg)
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Online ödeme seçeneği ile devam edilir (Stg)
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Online Ödeme
--------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Online ödeme seçeneği ile devam edilir (Stg)
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:regressionStaging_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir (Stg)
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Sipariş notu eklenir (Stg)
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* "adresEkleKontrolText" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Sipariş notu eklenir (Stg)
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie varsa kapat butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Varolan Notu Ekleme
--------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Varolan Notu Ekleme
-----------------------------------------------------------------
 tags:regressionStaging_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir veya kampanyayali ürün sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır (Stg)
* Kapıda ödeme Nakit seçeneği ile devam edilir (Stg)
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Şube atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeGelAlYalnizcaIl

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUye_gelAlYalnizcaIl

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - Yalnızca İl
----------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Sube duzenlemeye tiklanir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeGelAlIlIlce

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Merkez eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfada şubenin Düzce Şubesi olduğu kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Merkez eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfada şubenin Düzce Şubesi olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir (Stg)
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Sube duzenlemeye tiklanir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
 tags:regressionStaging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionStaging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:regressionStaging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemeVarolanUyeAyrilmaktanVazgec

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgec

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla
----------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemevarolanUyeAyrilmayiOnayla

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla
-------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnayla

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Kvkk sözleşmesi için sms, telefon, eposta checkboxları işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giriş
-----------------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgecGiris

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş
---------------------------------------------------------------
tags:regressionStaging_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnaylaGiris

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Üyelik Bilgilerim
-------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç - Üyelik Bilgilerim
-------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Aşağıdaki seçeneklerden en az bir iletişim kanalı seçmeniz gerekmektedir, hatası geldiği kontrol edilir
* Ye kazan için telefon, sms, e-mail seçilir ve kaydedilir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç - Profilim
--------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecProfilim

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Profilim
-------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecProfilim

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Profilim
--------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaProfilim

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Profilim
-----------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaProfilim

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıl butonuna tıklanır
* Sana özel hediyeler kazanmak için ye-kazana katıldıktan sonra ye-kazan checkboxına tıklanır
* Tercih ettiğiniz iletişim kanalını seçiniz yazısının geldiği görülür
* Ye kazan üyelik koşulları kabul etmek için telefon, sms, e-mail seçilir
* Ye kazana katıl butonuna tıklanır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Profilim butonuna tıklanır
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir


Üye Ye Kazan İzni güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giriş - Üyelik Bilgilerim
-----------------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Üyelik Bilgilerim
---------------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Cookie varsa kapat butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giris - Profilim
--------------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisProfilim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Profilim
-------------------------------------------------------------------------
tags:regressionStaging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisProfilim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir
