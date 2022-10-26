import sys
import modules.veritabani_kontrol.veritabani_kontrol as VeritabaniKontrol

if len(sys.argv) == 1:
    print("""
    
    [-] Yanlış kullanım. Komutlar için: RestoranVeritabaniSistemi.py -h
    
    """)
else:
    if sys.argv[1] == "-h":
        if len(sys.argv) != 2:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -h
            
            """)
        else:
            print("""
            
            [+] Komut listesi:

            -h: Yardım komutu. Komutları listeler.
            -g <Randevu kodu> <Masa numarası> <Başlangıç saati> <Bitiş saati> <Kişi sayısı>: İşletme tarafından kullanıcıya verilecek özelbir randevu koduyla yeni randevu oluşturur, ekrana yeni oluşan randevunun sıra numarasıyla kodunu basar. İki bilgi de önemlidir, saklanmalıdır ve KİMSEYLE PAYLAŞILMAMALIDIR.
            -s <Randevu kodu>: Randevuyu siler. İptal edilmiş veya gerçekleştirilmiş randevular için kullanılmalıdır.
            -c <Randevu sıra numarası>: Sıra numarası girilen randevunun detaylarını ekrana basar.
            -b: Bütün randevuların blgilerini sırayla ekrana basar.
            -d <Randevu kodu> <Masa numarası> <Başlangıç saati> <Bitiş saati> <Kişi sayısı>: Randevu bilgilerini parametrelere girilen değerlerle değiştirir (Randevu kodu hariç, randevu kodu değişemez, Tam aksine bilgileri değiştirilecek randevuyu bulmak için kullanılır.)
            -y: Veritabanını yeniler, içindeki tüm bilgileri siler ve sıfırlanır.

            """)

    elif sys.argv[1] == "-g":
        if len(sys.argv) != 7:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -g <Randevu kodu> <Masa numarası> <Başlangıç saati> <Bitiş saati> <Kişi sayısı>
            
            """)
        else:
            bilgiler = VeritabaniKontrol.VeriGir(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            print("""
            
            [+] İşlem başarılı!

            Randevu sıra numarası: {d1}
            Randevu kodu: {d2}
            
            """.format(d1 = bilgiler[0], d2 = bilgiler[1]))

    elif sys.argv[1] == "-s":
        if len(sys.argv) != 3:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -s <Randevu kodu>

            """)
        else:
            VeritabaniKontrol.VeriSil(sys.argv[2])
            print("""
            
            [+] Randevu başarıyla silindi!

            """)
    
    elif sys.argv[1] == "-c":
        if len(sys.argv) != 3:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -c <Randevu sıra numarası>
            
            """)
        else:
            bilgiler = VeritabaniKontrol.VeriCek(int(sys.argv[2]))
            print("""
            
            [+] Bilgiler:

            Randevu sırası: {d1}
            Randevu kodu: {d2}
            Masa numarası: {d3}
            Başlangıç saati: {d4}
            Bitiş saati: {d5}
            Kişi sayısı: {d6}

            """. format(d1 = sys.argv[2], d2 = bilgiler[0], d3 = bilgiler[1], d4 = bilgiler[2], d5 = bilgiler[3], d6 = bilgiler[4]))

    elif sys.argv[1] == "-b":
        if len(sys.argv) != 2:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -b
            
            """)
        else:
            bilgiler = VeritabaniKontrol.ButunRandevular()
            print("""

            [+] Randevuların listesi:
            """)
            for bilgi in bilgiler:
                print(bilgi)
            print("")
            print("")
    elif sys.argv[1] == "-d":
        if len(sys.argv) != 7:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -d <Randevu kodu> <Masa numarası> <Başlangıç saati> <Bitiş saati> <Kişi sayısı>
            
            """)
        else:
            bilgiler = VeritabaniKontrol.VeriDegistir(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            print("""
            
            [+] Yeni bilgiler:

            Randevu kodu: {d1}
            Masa numarası: {d2}
            Başlangıç saati: {d3}
            Bitiş saati: {d4}
            Kişi saati: {d5}

            """.format(d1 = bilgiler[0], d2 = bilgiler[1], d3 = bilgiler[2], d4 = bilgiler[3], d5 = bilgiler[4]))

    elif sys.argv[1] == "-y":
        if len(sys.argv) != 2:
            print("""
            
            [-] Doğru kullanım: RestoranVeritabaniSistemi.py -y
            
            """)
        else:
            VeritabaniKontrol.Yenile()
            print("""
            
            [+] Veritabanı başarıyla yenilendi!

            """)
    else:
        print("""
    
        [-] Yanlış kullanım. Komutlar için: RestoranVeritabaniSistemi.py -h
    
        """)