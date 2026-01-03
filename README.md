# Mergen
Turkic myht powered crypt program
# Biruni - Nucleus - Biyolojik Tabanlı Şifreleme Algoritması
Nucleus, metinsel verileri DNA replikasyonu ve protein sentezi süreçlerinden (transkripsiyon/translasyon) esinlenerek şifreleyen deneysel bir Python kütüphanesidir.
Bu algoritma, veriyi önce ikili (binary) sisteme, ardından sanal DNA nükleotitlerine (A, T, G, C), sonra üçlü kodonlara ve son olarak özel Unicode sembollerine dönüştürür. Ayrıca katmanlı (loop) şifreleme desteği ile veriyi birden fazla kez bu süreçten geçirerek güvenliği artırır.
🚀 Özellikler
 * Biyolojik Benzetim: Binary veriyi Adenin (A), Timin (T), Guanin (G) ve Sitozin (C) bazlarına dönüştürür.
 * Kodon Haritalama: 3'lü nükleotit dizilerini (Örn: GCT) özel sembollere (Örn: ܧ) dönüştürür.
 * UTF-8 Desteği: Türkçe karakterler ve emojiler dahil tüm metinleri destekler.
 * Döngüsel (Looped) Şifreleme: Şifrelenmiş veriyi tekrar girdi olarak alıp n-kez şifreleyerek karmaşıklığı artırır.
 * Tam Geri Dönüştürülebilirlik: Şifrelenen veri kayıpsız bir şekilde orijinal haline döndürülebilir.
📋 Gereksinimler
 * Python 3.x
 * Herhangi bir ek kütüphane kurulumu gerektirmez (Standart kütüphaneler kullanılır).
🛠️ Kurulum
Proje dosyasını (nucleus.py olarak varsayılmıştır) projenize dahil etmeniz yeterlidir.
from nucleus import Nucleus

📖 Kullanım
1. Sınıfı Başlatma
Öncelikle Nucleus sınıfından bir nesne oluşturun:
oxi = Nucleus()

2. Basit Şifreleme ve Çözme (Tek Katman)
Veriyi bir kez şifrelemek ve çözmek için:
metin = "Merhaba Dünya"

# Şifreleme
sifreli_veri = oxi.engine_runner_oneline(metin)
print(f"Şifreli: {sifreli_veri}")

# Çözme
cozulen_metin = oxi.decode_engine_runner(sifreli_veri)
print(f"Çözülen: {cozulen_metin}")

3. Döngüsel (Looped) Şifreleme ve Çözme
Veriyi daha karmaşık hale getirmek için loop parametresini kullanın. Dikkat: Şifrelerken kullandığınız loop sayısı ile çözerken kullandığınız sayı aynı olmalıdır.
metin = "Gizli Mesaj!"
dongu_sayisi = 3

# Döngüsel Şifreleme
sifreli_veri = oxi.looped_engine_runner(text=metin, loop=dongu_sayisi)
print(f"3 Katmanlı Şifre: {sifreli_veri}")

# Döngüsel Çözme
orijinal_veri = oxi.looped_decode_engine_runner(crypted_text=sifreli_veri, loop=dongu_sayisi)
print(f"Orijinal: {orijinal_veri}")

🧬 Algoritma Mantığı (Nasıl Çalışır?)
Sistem veriyi şu adımlarla işler:
 * Metin -> Binary: Girdi metni UTF-8 formatında binary (0 ve 1) dizisine çevrilir.
 * Binary -> Nükleotit: Her 2 bitlik veri bir nükleotite karşılık gelir:
   * 00 -> A
   * 11 -> T
   * 01 -> G
   * 10 -> C
 * DNA -> Kodon: Nükleotitler üçerli gruplara ayrılır (Örn: ATG, CGC). Eğer uzunluk 3'e bölünmüyorsa sonuna 'N' (Belirsiz) eklenir.
 * Kodon -> Sembol: Her kodon, crypted_codon haritasındaki özel bir Unicode karaktere dönüştürülür (Örn: GCT -> ܧ).
Döngüsel Mod:
Eğer loop > 1 ise, elde edilen sembol listesi tekrar metin olarak kabul edilir, binary'ye çevrilir ve süreç baştan başlar.
⚠️ Hata Ayıklama ve İpuçları
 * Veri Tipi: Şifreleme fonksiyonları genellikle list (liste) formatında çıktı verir. Çıktıyı veritabanına kaydetmeden önce join işlemi yapmanız gerekebilir, ancak çözme fonksiyonuna geri verirken tekrar listeye çevirmeyi veya fonksiyonun bunu halletmesini beklemeyi unutmayın (Kod içinde string gelirse listeye çeviren mekanizma mevcuttur).
 * Loop Sayısı: Bir veriyi loop=5 ile şifreleyip loop=4 ile çözmeye çalışırsanız anlamsız bir binary verisi veya hata alırsınız.
🤝 Katkıda Bulunma
Hataları düzeltmek veya yeni kodon haritaları eklemek için Pull Request gönderebilirsiniz. Özellikle codon_map içerisindeki eksik veya 'N' içeren durdurucu kodonların geliştirilmesi şifreleme çeşitliliğini artırabilir.
📄 Lisans
Bu proje açık kaynaklıdır ve eğitim/hobi amaçlı geliştirilmiştir.
