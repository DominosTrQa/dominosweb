All Test Staging
===================


Üye Girişi
---------------------------------
tags:staging_uyeGirisi

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Giriş - Başarısız giriş 2
-------------------------------
tags:staging_uyeGirisiBasarisizGiris

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "test" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Başarısız giriş 2
------------------------------
tags:staging_uyeGirisiBasarisizGiris2

* Dominos - Staging ortamına gidilir
* "test@gmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Giriş yaparken E-Posta veya Şifre yanlış uyarısının geldiği kontrol edilir


Üye Girişi - Ekran kontrolü
------------------------------
tags:staging_uyeGirisiEkranKontrolu

* Dominos - Staging ortamına gidilir
* Giriş Yap butonuna basılır
* Giriş Yap sayfasındaki elementlerin geldiği kontrol edilir


Üye Girişi - Parolamı Unuttum
-------------------------------
tags:staging_uyeGirisiParolamiUnuttum

* Dominos - Staging ortamına gidilir
* Giriş Yap butonuna basılır
* Parolamı Unuttum butonuna basılır ve textboxa mail adresi yazılır
* Şifremi Hatırlat butonunun çalıştığı kontrol edilir


Üye Olma
-------------------------------
tags:staging_uyeOlma

* Dominos - Staging ortamına gidilir
* Üye olmak için bilgiler girilir
* Mesafeli satış sözleşmesi işaretlenir
* KVKK ve Ye Kazan E-Posta seçilir ve üye olunur


Üye Olma - Ekran Kontrolü
----------------------------------------
tags:staging_uyeOlmaEkrankontrolu

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Üye ol sayfasının elementlerinin geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma
----------------------------------------------
tags:staging_uyeOlmaBasariliUyeOlma

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olma - Başarısız Üye Olma
-------------------------------
tags:staging_uyeOlmaBasarisizUyeOlma

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Üye olurken bilgiler boş bırakıldığında uyarıların geldiği kontrol edilir


Üye Olma - Başarılı Üye Olma 2
---------------------------------
tags:staging_uyeOlmaBasariliUyeOlma2

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Random mail ve telefon ile üye olunur ve iletişim kanalları seçilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir


Üye Olmadan Devam Et - Button Kontrol
-------------------------------------------------
tags:staging_uyeOlmadanDevamEtButtonKontrol

* Dominos - Staging ortamına gidilir
* Giriş Yap butonuna basılır
* Element var mı kontrol et "uyeOlmadanDevamEtButon"


Üye Olmadan Devam Et - Ekran Kontrolü
-------------------------------------------
tags:staging_uyeOlmadanDevamEtEkranKontrolu

* Dominos - Staging ortamına gidilir
* Giriş Yap butonuna basılır
* Üye olmadan devam edilir
* Adrese teslim ve gel al butonlarının geldiği kontrol edilir
* Element var mı kontrol et "loginButton"
* Element var mı kontrol et "uyeOlButon"


Üye Adres Ekleme - Adrese Teslim - Üye
-----------------------------------------------------
 tags:staging_uyeAdresEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Profilim popup eklenen adres silinir


Üye Adres Ekleme - Adrese Teslim - Yeni Üye
----------------------------------------------------------
 tags:staging_uyeAdresEklemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)


Üye Adres Ekleme - Gel Al - Üye
-------------------------------------------------------------
 tags:staging_uyeAdresEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)
* Profilim popup eklenen adres silinir

Üye Adres Ekleme - Gel Al - Yeni Üye
-------------------------------------------------------------
 tags:staging_uyeAdresEklemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Yeni adres ekle (Gel Al)


Üye Adres Düzenleme - Adrese Teslim - Üye
------------------------------------------
 tags:staging_uyeAdresDuzenlemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır
* Profilim popup eklenen adres silinir


Üye Adres Düzenleme - Adrese Teslim - Yeni Üye
------------------------------------------
 tags:staging_uyeAdresDuzenlemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır ve popup açıldığı kontrol edilir
* Profilim popup Yeni Adres Ekle butonuna tıklanır
* Adres bilgileri tamamlanır(Liste - üye)
* Profilim popup eklenen  adres düzenlenir ve eski adresin değiştiği doğrulanır


Üye Adres Düzenleme - Gel Al - Üye
------------------------------------------
 tags:staging_uyeAdresDuzenlemeGelAlUye

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
 tags:staging_uyeAdresDuzenlemeGelAlYeniUye

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
 tags:staging_sepeteKampanyaEklemeAdreseTeslimUyeKampanya1

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 3 Al 1 öde kampanyası seçilir (Stg)
* 3 Al 1 öde kampanyası için sipariş oluşturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Yeni Üye - Kampanya 2
--------------------------------------------------------------------------
 tags:staging_sepeteKampanyaEklemeAdreseTeslimYeniUyeKampanya2

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 3 Al 1 öde kampanyası seçilir (Stg)
* 3 Al 1 öde kampanyası için sipariş oluşturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Adrese Teslim - Üyeliksiz - Kampanya 3
-----------------------------------------------------------------------------------------------------------------------
 tags:staging_sepeteKampanyaEklemeAdreseTeslimUyeliksizKampanya3

* Dominos - Staging ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* 3 Al 1 öde kampanyası seçilir (Stg)
* 3 Al 1 öde kampanyası için sipariş oluşturulur
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üye - Kampanya 4
-----------------------------------------------------------------------------------------------------------
 tags:staging_sepeteKampanyaEklemeGelAlUyeKampanya4

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Kampanyalar Butonuna tıklanır
* Dilediğin büyük boy pizza kampanyası secilir (Stg)
* İlk ürün düzenlemeye tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Yeni Üye - Kampanya 5
--------------------------------------------------------------------------------
 tags:staging_sepeteKampanyaEklemeGelAlYeniUyeKampanya5

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Kampanyalar Butonuna tıklanır
* Dilediğin büyük boy pizza kampanyası secilir (Stg)
* İlk ürün düzenlemeye tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Kampanya Ekleme - Gel Al - Üyeliksiz -  Kampanya 6
----------------------------------------------------------------------------------------
 tags:staging_sepeteKampanyaEklemeGelAlUyeliksizKampanya6

* Dominos - Staging ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Kampanyalar Butonuna tıklanır
* Dilediğin büyük boy pizza kampanyası secilir (Stg)
* İlk ürün düzenlemeye tıklanır
* Sucuk ve mısır malzemeleri çıkarılır
* Ekstra Malzeme Ekle butonuna tıklanır
* Cheddar ve Mozarella eklenir
* Ekstra Malzeme Ekle butonuna tıklanır
* Güncelle butonuna tıklanır(özel kampanyalar için)
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üye
------------------------------------------------
 tags:staging_pizzaEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Yeni Üye
------------------------------------------------
 tags:staging_pizzaEklemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Adrese Teslim - Üyeliksiz
------------------------------------------------
 tags:staging_pizzaEklemeAdreseTeslimUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üye
------------------------------------------------
 tags:staging_pizzaEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Yeni Üye
------------------------------------------------
 tags:staging_pizzaEklemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Pizza Ekleme - Gel Al - Üyeliksiz
------------------------------------------------
 tags:staging_pizzaEklemeGelAlUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Tüm Pizzalar butonuna tıklanır
* Tüm pizzalarda ilk pizza kategorisi seçilir
* Pizza kategorisindeki ilk pizza seçilir
* Pizza boyutunda ilk boyut seçilir
* Kenar tipinde ilk kenar seçilir
* Pizza sepete eklenir
* Sepetimde ürün var mı kontrol edilir


Sepete Yan Ürün Ekleme - Adrese Teslim - Üye
----------------------------------------------
 tags:staging_sepeteYanUrunEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, adrese teslim servis tipi seçilir ve anasayfaya gidilir (Staging)
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Adrese Teslim - Yeni Üye
--------------------------------------------------
 tags:staging_sepeteYanUrunEklemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:staging_sepeteYanUrunEklemeAdreseTeslimUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, adrese teslim servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)

Sepete Yan Ürün Ekleme - Gel Al - Üye
----------------------------------------------
 tags:staging_sepeteYanUrunEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Kullanıcı ile giriş yapılır, gel al servis tipi seçilir ve anasayfaya gidilir (Staging)
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Gel Al - Yeni Üye
----------------------------------------------
 tags:staging_sepeteYanUrunEklemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepete Yan Ürün Ekleme - Gel Al - Üyeliksiz
---------------------------------------------
 tags:staging_sepeteYanUrunEklemeGelAlUyeliksiz

* Dominos - Staging ortamına gidilir
* Üyeliksiz, gel al servis tipi seçilir ve anasayfaya devam edilir
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır (Stg)
* Sepete coca cola eklenir (Stg)
* Sepette coca cola var mı kontrol edilir (Stg)


Sepetten Upsell Ekleme - Adrese Teslim - Üye
---------------------------------------------
 tags:staging_sepettenUpsellEklemeAdreseTeslimUye

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sepetten Upsell Ekleme - Adrese Teslim - Yeni Üye
---------------------------------------------
 tags:staging_sepettenUpsellEklemeAdreseTeslimYeniUye

* Dominos - Staging ortamına gidilir
* Üye olunur, adrese teslim servis tipi seçilir ve anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Adrese Teslim - Üyeliksiz
--------------------------------------------------
 tags:staging_sepettenUpsellEklemeAdreseTeslimUyeliksiz

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir


Sepetten Upcell Ekleme - Gel Al - Üye
------------------------------------------
 tags:staging_sepettenUpsellEklemeGelAlUye

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında giriş yap butonuna tıklanır
* E-posta "dominostest1@hotmail.com" ve "a1w2d3r4D" şifre girilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Gel Al - Yeni Üye
---------------------------------------
 tags:staging_sepettenUpsellEklemeGelAlYeniUye

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir
* Sepetim ikonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ye kazan popupında üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında dürüm yazısının geldiği kontrol edilir(Stg)


Sepetten Upcell Ekleme - Gel Al - Üyeliksiz
--------------------------------------------------
 tags:staging_sepettenUpsellEklemeGelAlUyeliksiz

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sepete dürüm eklenir(Stg)
* Sepetim ikonuna tıklanır
* Sepetteki dürümün eklendiği kontrol edilir


Servis Tipi Seçimi - Adrese Teslim
-----------------------------------
 tags:staging_servisTipiSecimiAdreseTeslim

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al
----------------------------
 tags:staging_servisTipiSecimiGelAl

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
 tags:staging_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
-----------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlUyeliksizSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
----------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Varolan Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlVarOlanUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Adrese teslim butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Gel Al - Yeni Üye Sepette Servis Tipinin Değiştirilememesi
------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlYeniUyeSepetteServisTipininDegistirilememesi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Gel al butonuna tıklanamadığı görülür


Servis Tipi Seçimi - Adrese Teslim - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Üyeliksiz Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlUyeliksizSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Varolan Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlVarOlanUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Servis Tipi Seçimi - Adrese Teslim - Yeni Üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
-------------------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiAdreseTeslimYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Gel Al olduğu kontrol edilir


Servis Tipi Seçimi - Gel Al - Yeni üye Sepette Ürün varken Servis Tipinin Değiştirilmesi
----------------------------------------------------------------------------------------
 tags:staging_servisTipiSecimiGelAlYeniUyeSepetteUrunVarkenServisTipininDegistirilmesi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Anasayfadaki dominos logosuna tıklanır
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısı geldiği doğrulanır
* Teslimat tipini değiştirmek sepetteki ürünün silinmesine neden olur uyarısına evet denir
* Servis tipinin Adrese Teslim olduğu kontrol edilir


Adres Seçimi - Varolan Üye - Adres Teslim - Manuel - Adres Seçimi
------------------------------------------------------------------
 tags:staging_adresSecimiVarOlanUyeAdresTeslimManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Gel Al - Manuel - Adres Seçimi
------------------------------------------------------------
 tags:staging_adresSecimiVarOlanUyeGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Adres Teslim - Manuel - Adres Seçimi
---------------------------------------------------------------
 tags:staging_adresSecimiYeniUyeAdresTeslimManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:staging_adresSecimiYeniUyeGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Adres Teslim - Manuel - Adres Seçimi
----------------------------------------------------------------
 tags:staging_adresSecimiUyeliksizAdresTeslimManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Kalem ikonuna tıklanır
* Adrese teslim adres düzenleye tıklanır
* Adrese teslim servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Üyeliksiz - Gel Al - Manuel - Adres Seçimi
---------------------------------------------------------
 tags:staging_adresSecimiUyeliksizGelAlManuelAdresSecimi

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Kalem ikonuna tıklanır
* Gel al adres ekleme ekranında düzenle butonuna tıklanır
* Gel Al servis tipi için Sarıyer / Ayazaga  mah. adresi eklenir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Adres Teslim - Adreslerim - Adres Seçimi
----------------------------------------------------------------------
 tags:staging_adresSecimiVarOlanUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Seçili ilk adrese tıklanır
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Varolan Üye - Gel Al - Adreslerim - Adres Seçimi
----------------------------------------------------------------
 tags:staging_adresSecimiVarOlanUyeGelAlAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Adreslerim kısmından Sarıyer adresi seçilir
* Seçili adres ile devam edilir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Adres Teslim - Adreslerim - Adres Seçimi
-------------------------------------------------------------------
 tags:staging_adresSecimiYeniUyeAdreseTeslimAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Anasayfa İstanbul/Sarıyer/Ayazağa adresinin doğru geldiği kontrol edilir(Stg)


Adres Seçimi - Yeni Üye - Gel Al - Adreslerim - Adres Seçimi
-------------------------------------------------------------
 tags:staging_adresSecimiYeniUyeGelAlAdreslerimAdresSecimi

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Anasayfa Test Pulse adresinin doğru geldiği kontrol edilir(Stg)
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Yeni adres ekle butonuna tıklanır
* Gel al olarak devam edilip adreslerime girilerek adrese teslim için İstanbul/Adalar/Burgazada eklenir
* Kullanıcıya yeni adres eklenir,tamamlanır(İstanbul/Sarıyer/Ayazaga mah)
* Seçili adres ile devam edilir
* Anasayfa İstanbul/Sarıyer/Ayazaga adresinin doğru geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Nakit
-----------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimNakit

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Nakit
----------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlNakit

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Nakit
----------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimNakit

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Nakit
-------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlNakit

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Nakit
------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimNakit

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Nakit
-----------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlNakit

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Nakit yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Kredi Kartı
-----------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Kredi Kartı
----------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlKrediKartı

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Kredi Kartı
--------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Kredi Kartı
-------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlKrediKartı

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Kredi Kartı
------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimKrediKartı

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Kredi Kartı
------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlKrediKartı

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Kredi Kartı seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında Kredi Kartı yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Sodexo Kart
-------------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Sodexo Kart
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Sodexo Kart
--------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlSmartSodexoKart

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Smart Sodexo Kart seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smart sodexho kart yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Sodexo Yemek Çeki
----------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir

Ödeme Tipi Secimi - Yeni Üye - Gel Al - Sodexo Yemek Çeki
----------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Sodexo Yemek Çeki
-------------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Sodexo Yemek Çeki
-------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Sodexo Yemek Çeki
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlSodexoYemekCeki

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Sodexo Yemek Çeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında sodexho yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Smart Ticket Yemek Çeki
-----------------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Smart Ticket Yemek Çeki
--------------------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Smart Ticket Yemek Çeki
-------------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme SmartTicket Yemek Çeki seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Smart Ticket Yemek Çeki
------------------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme smartTicket YemekÇeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Smart Ticket Yemek Çeki
-----------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlSmartTicketYemekÇeki

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme smartTicket YemekÇeki seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında smartTicket yemek çeki yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Multinet
--------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Multinet
-------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlMultinet

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Multinet
-----------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Multinet
----------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlMultinet

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Multinet
---------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimMultinet

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Multinet seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Multinet
--------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlMultinet

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Multinet seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında multinet yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Setcard
-------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimSetCard

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Setcard
------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlSetCard

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Setcard
---------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimSetCard

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Setcard
----------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlSetCard

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Setcard
----------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimSetCard

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme setCard seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Üyeliksiz - Gel Al - Setcard
--------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlSetCard

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme setCard seçeneği ile devam edilir(guest)
* Onay sayfasında ödeme aracı kısmında setCard yazısının geldiği kontrol edilir(guest)


Ödeme Tipi Secimi - Yeni Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Yeni Üye - Gel Al - Online Ödeme
------------------------------------------------------
 tags:staging_odemeTipiSecimiYeniUyeGelAlOnlineOdeme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Varolan Üye - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Ödeme Tipi Secimi - Varolan Üye - Gel Al - Online Ödeme
--------------------------------------------------------
 tags:staging_odemeTipiSecimiVarolanUyeGelAlOnlineOdeme

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Online ödeme seçeneği ile devam edilir
* Online ödeme seçiminde kayıtlı kartlarınızdan birini seçmeli veya kart ile ödemek İstiyorum seçeneğini seçmelisiniz uyarısıyla karşılaşılır
* Tamam butonuna tıklanır


Ödeme Tipi Secimi - Üyeliksiz - Adrese Teslim - Online Ödeme
------------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizAdreseTeslimOnlineOdeme

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Online ödeme seçeneği ile devam edilir(guest)
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Ödeme Tipi Secimi - Üyeliksiz - Gel AL - Online Ödeme
------------------------------------------------------
 tags:staging_odemeTipiSecimiUyeliksizGelAlOnlineOdeme

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Online ödeme seçeneği ile devam edilir(guest)
* Geçerli bir telefon giriniz hatası görülür
* Çarpıya basılıp çıkılır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Temassız Teslimat
-------------------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
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
 tags:staging_siparisNotuEklemeUyeliksizAdreseTeslimtemassizTeslimat

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Temassız teslimat seçeneği seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında temassız teslimat yazısının geldiği kontrol edilir(guest)


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Lütfen Zile Basmayınız
-------------------------------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Lütfen Zile Basmayınız
---------------------------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
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
 tags:staging_siparisNotuEklemeUyeliksizAdreseTeslimLutfenZileBasmayiniz

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Lütfen zile basmayınız seçilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Not alanında lütfen zile basmayınız yazısının geldiği kontrol edilir


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Not Ekleme
-----------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeGelAlNotEkleme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Not Ekleme
------------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Not Ekleme
--------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeGelAlNotEkleme

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Sipariş notu eklenir
* Sipariş tamamlanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Adrese Teslim - Not Ekleme
-------------------------------------------------------------
 tags:staging_siparisNotuEklemeUyeliksizAdreseTeslimNotEkleme

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Üyeliksiz - Gel Al - Not Ekleme
------------------------------------------------------
 tags:staging_siparisNotuEklemeUyeliksizGelAlNotEkleme

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir(guest)
* Sipariş notu eklenir(guest)
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Tekrar sipariş ver butonuna tıklanır
* Sipariş sayfasında sipariş notunun eklenen olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Adrese Teslim - Varolan Notu Ekleme
-----------------------------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeAdreseTeslimVarolanNotuEkleme

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
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır


Sipariş Notu Ekleme - Yeni Üye - Gel Al - Varolan Notu Ekleme
--------------------------------------------------------------
 tags:staging_siparisNotuEklemeYeniUyeGelAlVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* Üye olunur, Gel Al servis tipi seçilir ve Anasayfaya gidilir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır


Sipariş Notu Ekleme - Varolan Üye - Adrese Teslim - Varolan Notu Ekleme
-------------------------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeAdreseTeslimVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir
* Anasayfadaki dominos logosuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Adreslerim butonuna tıklanır
* Profilimden adreslerime giderek kayıtlı adres silinir


Sipariş Notu Ekleme - Varolan Üye - Gel Al - Varolan Notu Ekleme
-----------------------------------------------------------------
 tags:staging_siparisNotuEklemeVarolanUyeGelAlVarolanNotuEkleme

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Not ekle butonuna tıklanır
* Not eklenir
* Notlarım alanında Test Not Başlığı yazısının geldiği görülür
* Header tabından tüm pizzalara tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Not alanında var olan notlar combobox'ından Test Not Başlığı olan seçilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır
* Sipariş sayfasında sipariş notunun Test Not İçeriği olduğu doğrulanır
* Profilim butonuna tıklanır
* Profilim popup Notlarım butonuna tıklanır
* Varolan notum silinir


Sipariş İşlemleri(Canlı) - Test adresi - Manuel
------------------------------------------------
 tags:staging_siparisIslemleriCanliTestAdresiManuel

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada adres bilgileri tamamlanır(Kapı No Manuel)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Ödeme şekli seçilir


Sipariş İşlemleri(Canlı) - Test adresi - Dropdown
------------------------------------------
 tags:staging_siparisIslemleriCanliTestAdresiDropdown

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(Kapı No Dropdown)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Ödeme şekli seçilir


Şube atama - Varolan Üye - Adrese Teslim - Yalnızca İl
------------------------------------------------------
 tags:staging_subeAtamaVarolanUyeAdreseTeslimYalnizcaIl

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:staging_subeAtamaVarolanUyeGelAlYalnizcaIl

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
 tags:staging_subeAtamaYeniUyeAdreseTeslimYalnizcaIl

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - Yalnızca İl
------------------------------------------------
 tags:staging_subeAtamaYeniUye_gelAlYalnizcaIl

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
 tags:staging_subeAtamaUyeliksizAdreseTeslimYalnizcaIl

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adıyaman ili seçilir
* Anasayfada Adıyaman ili adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - Yalnızca İl
----------------------------------------------
 tags:staging_subeAtamaUyeliksizGelAlYalnizcaIl

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adıyaman adresi eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfadaki şubenin Adıyaman Şubesi olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe
----------------------------------------------------
 tags:staging_subeAtamaVarolanUyeAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - İl İlçe
---------------------------------------------
 tags:staging_subeAtamaVarolanUyeGelAlIlIlce

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Merkez eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfada şubenin Düzce Şubesi olduğu kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe
-------------------------------------------------
 tags:staging_subeAtamaYeniUyeAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe
------------------------------------------
 tags:staging_subeAtamaYeniUyeGelAlIlIlce

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
 tags:staging_subeAtamaUyeliksizAdreseTeslimIlIlce

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Sakarya/Adapazarı eklenir
* Anasayfada Sakarya/Adapazarı adresinin geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe
----------------------------------------------
 tags:staging_subeAtamaUyeliksizGelAlIlIlce

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Düzce/Merkez eklenir
* Gel Al da Şubeleri Göster butonuna tıklanır
* Gel Al çıkan ilk şube seçilir
* Seçili Şube ile Devam Et butonuna basılır
* Anasayfada şubenin Düzce Şubesi olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle
-----------------------------------------------------------
 tags:staging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Varolan Üye - Gel Al - İl İlçe Mahalle
----------------------------------------------------
 tags:staging_subeAtamaVarolanUyeGelAlIlIlceMahalle

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin Test Pulse Şubesi olduğu kontrol edilir


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:staging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Yeni Üye - Gel Al - İl İlçe Mahalle
--------------------------------------------------------
 tags:staging_subeAtamaYeniUyeGelAlIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin Test Pulse Şubesi olduğu kontrol edilir


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle
--------------------------------------------------------
 tags:staging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir


Şube atama - Üyeliksiz - Gel Al - İl İlçe Mahalle
--------------------------------------------------
 tags:staging_subeAtamaUyeliksizGelAlIlIlceMahalle

* Dominos - Staging ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfadaki şubenin Test Pulse Şubesi olduğu kontrol edilir


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak
-----------------------------------------------------------------
 tags:staging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak
----------------------------------------------------------
 tags:staging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak
---------------------------------------------------------------
 tags:staging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokak

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Ahu sk seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Varolan Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:staging_subeAtamaVarolanUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Yeni Üye - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:staging_subeAtamaYeniUyeAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Şube atama - Üyeliksiz - Adrese Teslim - İl İlçe Mahalle Sokak Kapı No
-------------------------------------------------------------------------
 tags:staging_subeAtamaUyeliksizAdreseTeslimIlIlceMahalleSokakKapiNo

* Dominos - Staging ortamına gidilir
* Adrese Teslim servis tipi seçilir
* İstanbul, Beşiktaş, Etiler mh, Bahtiyar sk, Apartman No 2 seçilir
* Anasayfada İstanbul/Beşiktaş/Etiler Mah. geldiği doğrulanır


Üye KVKK İzni Güncelleme - Varolan Üye - Ayrılmaktan Vazgeç
-----------------------------------------------------------
tags:staging_uyeKVKKIzniGuncellemeVarolanUyeAyrilmaktanVazgec
//blocked:Düzelince testiniuma eklenecek

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgec

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
tags:staging_uyeKVKKIzniGuncellemevarolanUyeAyrilmayiOnayla

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnayla

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
tags:staging_uyeKVKKIzniGuncellemeYeniUyeAyrilmaktanVazgecGiris

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* Kvkk checkboxının işaretli olmadığı gözlemlenir


Üye KVKK İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş
---------------------------------------------------------------
tags:staging_uyeKVKKIzniGuncellemeYeniUyeAyrilmayiOnaylaGiris

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Açık rıza metni KVKK işaretlenir
* Üye olurken KVKK sözleşmesi için eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime tıkladıktan sonra KVKK checkboxı işaretlenir
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Vazgeç butonuna tıklanır
* KVKK checkboxı için değişikleri kaydet butonuna basılır
* Onaylıyorum butonuna tıklanır


Üye Ye Kazan İzni Güncelleme - Varolan Üye - Ayrılmayı Onayla - Üyelik Bilgilerim
--------------------------------------------------------------------------------
tags:staging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecUyelikBilgilerim

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
tags:staging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecUyelikBilgilerim

//Bug OLOTR-1480 çözüldükten sonra Testinium suiteine eklenecek
* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaUyelikBilgilerim

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
tags:staging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmaktanVazgecProfilim

* Dominos - Staging ortamına gidilir
* "dominostest2@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecProfilim

* Dominos - Staging ortamına gidilir
* Adrese teslim servis tipi için üye olunur, Adalar/Burgazada mah. adresi ile devam edilir
* Anasayfa İstanbul/Adalar/Burgazada adresinin doğru geldiği kontrol edilir
* Cookie onaylıyorum butonuna tıklanır
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
tags:staging_uyeYeKazanIzniGuncellemeVarolanUyeAyrilmayiOnaylaProfilim

* Dominos - Staging ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
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
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaProfilim

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
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Üyelik Bilgilerim
---------------------------------------------------------------------------------------
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisUyelikBilgilerim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısı kontrol edilir
* Üyelik bilgilerim butonuna tıklanır
* Üyelik bilgilerime girildikten sonraki sayfada Domino's ye kazan işaretlenir
* Ye kazan checkboxı için değişikler kaydet butonuna basılır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Profilim butonuna tıklanır
* Bedava pizza kazanmana 5 pizza kaldı yazısının gelmediği kontrol edilir


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmaktan Vazgeç - Giris - Profilim
--------------------------------------------------------------------------------
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmaktanVazgecGirisProfilim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmaktan vazgeç butonuna tıklanılır
* Hediye pizza kazanmana 5 dilim kaldı yazısının olduğu görülür


Üye Ye Kazan İzni Güncelleme - Yeni Üye - Ayrılmayı Onayla - Giriş - Profilim
-------------------------------------------------------------------------
tags:staging_uyeYeKazanIzniGuncellemeYeniUyeAyrilmayiOnaylaGirisProfilim

* Dominos - Staging ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi işaretlenir
* Ye kazan checkbox işaretlenir
* Üye olurken ye kazan seçildikten sonra eposta işaretlenir
* Elementi bekle ve sonra tıkla "uyeOlSayfasiUyeOlButon"
* Adrese Teslim servis tipi seçilir
* İl ilçe mahalle seçilir
* Seçili Adres ile Devam Et butonuna basılır
* Profilim butonuna tıklanır
* Ye kazana üye olan kullanıcı için profilimden ye kazan sayfasına gidilir
* Ye kazandan ayrıl butonuna tıklanır
* Ye kazan ayrılmayı onaylıyorum butonuna tıklanılır
* Ye kazan uyarı butonundan çıkılır
* Ye kazandan ayrıldıktan sonra ye-kazan checkbox geldiği kontrol edilir