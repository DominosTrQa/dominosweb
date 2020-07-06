Smoke Kubernetes
=====================
     
     
K8s - Kullanıcı ilk kez geliyor - Adrese Teslim
-------------------------------------------------------
tags:smokeK8s_kullaniciIlkkezGeliyorAdreseTeslim

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Cookie onaylıyorum butonuna tıklanır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Adalar - Burgazada adres bilgileri tamamlanır(Kapı No Manuel)
* Adresi seçilir ve Seçili Adres ile Devam Et butonuna basılır
* Ödeme şekli seçilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır


Live - Kullanıcı ilk kez geliyor - Gel Al
------------------------------------------------
tags:smokeK8s_kullaniciIlkKezGeliyorGelAlServisTipiSecti

* Dominos - Kubernetes ortamına gidilir
* Üye ol butonuna tıklanır
* Ad Soyad Random mail telefon ve sifre girilir
* Mesafeli satış sözleşmesi onaylanır ve üye ol butonuna basılır
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ödeme şekli seçilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır


Live - Servis Tipi Seçimi - Adrese Teslimden Gel Al Geçişi
----------------------------------------------------
tags:smokeK8s_servisTipiSecimiAdreseTeslimdenGelAlGecisi

* Dominos - Kubernetes ortamına gidilir
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Anasayfadaki adres teslim butonuna tıklanır
* Gel Al servis tipi seçilir
* Servis tipinin Gel Al olduğu kontrol edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Kampanyalar Butonuna tıklanır
* Cookie onaylıyorum butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Siparis tamamlanir(guest) 2
* Ye kazan uyarı butonundan çıkılır


Live - Servis Tipi Seçimi - Gel Aldan Adrese Teslim Geçişi
----------------------------------------------------
tags:smokeK8s_servisTipiSecimiGelAldanAdreseTeslimGecisi

* Dominos - Kubernetes ortamına gidilir
* Gel Al servis tipi seçilir
* Gel al servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Gel Al olduğu kontrol edilir
* Anasayfadaki gel al butonuna tıklanır
* Adrese Teslim servis tipi seçilir
* Adrese Teslim servis tipi için Adalar / Burgazada mah. adresi eklenir
* Servis tipinin Adrese Teslim olduğu kontrol edilir
* Tüm pizzalar alanına kaydırılır
* Tüm Pizzalar butonuna tıklanır
* Pizza kategorisindeki ilk pizza seçilir
* Pizza sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Üye olmadan devam edilir butonuna tıklanır
* Adalar - Burgazada mah. adres bilgileri tamamlanır(giris yapılmadan)
* Seçili adres ile devam edilir
* Kapıda ödeme Nakit seçeneği ile devam edilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Sipariş tamamlanır(guest)
* Kullanıcı bilgileri girilir(Ad,soyad,eposta,telefon)
* Siparis tamamlanir(guest) 2
* Ye kazan uyarı butonundan çıkılır


Live - Kullanıcı ikinci kez geliyor - Adrese Teslim - Adresi var (üst menü)
---------------------------------------------------------------------------------
tags:smokeK8s_kullaniciIkincikezGeliyorAdreseTeslimAdresiVar

* Dominos - Kubernetes ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "adreseTeslimButon" servis tipi seçilir ve adres seçimi yapılır
* "AdreseTeslim" servis tipi kontrolü yapılır
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Çıkış Yap butonuna basılır
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "adreseTeslimButon" servis tipi seçilir ve adres seçimi yapılır
* "AdreseTeslim" servis tipi kontrolü yapılır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Ödeme şekli seçilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır


Live - Kullanıcı ikinci kez geliyor - Gel Al - Adresi var (üst menü)
--------------------------------------------------------------
tags:smokeK8s_kullaniciIkinciKezGeliyorGelAlAdresiVar

* Dominos - Kubernetes ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "gelAlButon" servis tipi seçilir ve adres seçimi yapılır
* "GelAl" servis tipi kontrolü yapılır
* Cookie varsa kapat butonuna tıklanır
* Profilim butonuna tıklanır
* Profilim popup Çıkış Yap butonuna basılır
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "adreseTeslimButon" servis tipi seçilir ve adres seçimi yapılır
* "AdreseTeslim" servis tipi kontrolü yapılır
* Ekstra Lezzetlere gidilir
* İçecekler tabına tıklanır
* Sepete coca cola eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepetteki ürün iki kez arttırılır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Ödeme şekli seçilir
* Onay sayfası şubenin 99362 - Siparişe Kapalı Şube olduğu kontrol edilir
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır


Live - Servis tipi değiştiren kullanıcı - Adresime Teslim > Gel Al (üst menü)
----------------------------------------------------------------------
tags:smokeK8s_servisTipiDegistirenKullaniciAdresimeTeslimGelAl

* Dominos - Kubernetes ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "adreseTeslimButon" servis tipi seçilir ve adres seçimi yapılır
* "AdreseTeslim" servis tipi kontrolü yapılır
* "gelAlButon" servis tipi seçilir ve adres seçimi yapılır
* "GelAl" servis tipi kontrolü yapılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* Odeme sekli secilir (k8s)
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Onay sayfası şubenin Test Pulse Şubesi olduğu kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır


Live - Servis tipi değiştiren kullanıcı - Gel Al > Adresime Teslim (üst menü)
-----------------------------------------------------------------------
tags:smokeK8s_servisTipiDegistirenKullaniciGelAlAdreseTeslim

* Dominos - Kubernetes ortamına gidilir
* "dominostest1@hotmail.com" kullanıcısı ve "a1w2d3r4D" şifresi ile üye girişi yapılır
* "gelAlButon" servis tipi seçilir ve adres seçimi yapılır
* "GelAl" servis tipi kontrolü yapılır
* Cookie varsa kapat butonuna tıklanır
* "adreseTeslimButon" servis tipi seçilir ve adres seçimi yapılır
* "AdreseTeslim" servis tipi kontrolü yapılır
* Tüm Kampanyalar Butonuna tıklanır
* Kampanya sayfasındaki ilk kampanya secilir
* Kampanya urun secimi yapılır
* Kampanya sepete eklenir
* Sepetimde ürün var mı kontrol edilir
* Sepetim ikonuna tıklanır
* Sepete git butonuna tıklanır
* Sipariş ver butonuna tıklanır
* "caddeDropdown" Varsa adres bilgileri tamamlanır (Kapı No Manuel)
* Odeme sekli secilir (k8s)
* Onay sayfası şubenin Test Pulse Şubesi olduğu kontrol edilir
* Ödemeyi tamamla butonu geldiği kontrol edilir
* Sipariş tamamlanır
* Ye kazan uyarı butonundan çıkılır