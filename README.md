RESTORAN VERITABANI SISTEMI
 
Ad: Rüzgar
Soyad: Şepçi
Sınıf: 10/D
Numara: 409 

Yapmış olduğum projede, bir restoranda yapılan rezervasyonlar bir veritabanı aracılığıyla kayıt altına alınabilir. Program, komut isteminden "RestoranVeritabaniSistemi.py" girilerek çalıştırılabilir. Programda veritabanı sistemi için "sqlite3" modülü kullanılmıştır. Veritabanında "rezervasyon kodu, rezervasyon numarası, masa numarası, randevu başlangıç saati, randevu bitiş saati, kişi sayısı" olmak üzere 6 değer bulunmaktadır. Veritabanında işlemler rezervasyon kodu ve numarası kullanılarak gerçekleştirilmektedir. Programda veriler girilebilir, değiştirilebilir, silinebilir, okunabilir veya tablo sıfırlanabilir.
Program yazılırken “veritabani_kontrol.py” isminde bir modül oluşturulmuş olup bu modüle veritabanını kontrol etmek için fonksiyonlar eklenmiştir. Ana dosya olan “RestoranVeritabaniSistemi.py” dosyasında bu modül çağrılır ve veritabanını manipüle etmek için içindeki fonksiyonlar kullanılır.
Asıl program çağrıldığında önce içindeki fonksiyonlara erişebilmek için “veritabani_kontrol.py” modülü çağrılır. Modül ise çağrıldığında eğer bulunduğu dizin olan “veritabani_kontrol”de “db.sqlite” diye bir veritabanı dosyası yoksa bu dosya oluşturulur. Ondan sonra komut isteminden girilen argümanlara göre işlem yapılır.
Programın çalıştırılabilmesi için “Sistem Özellikeri > Gelişmiş > Ortam Değişkenleri…” denilip, sonrasında “Path”in seçilip, ardından “Düzenle > Yeni” denilerek “RestoranVeritabaniSistemi.py”nin bulunduğu dizinin yazılıp kaydedilmesi vesilesiyle PATHe eklenmesi gerekmektedir.
