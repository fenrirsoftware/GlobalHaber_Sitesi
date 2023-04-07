Ulak | Global Teknoloji Haber Sitesi

## Ulak Nedir ?

Ulak, Türk devletlerinde haber götürüp getiren kişilere verilen bir isimdir. Biz de yabancı teknoloji haber sitelerinde paylaşılan içerikleri tek çatı altında toplamayı ve özellikle gündemi yakından takip edenlerin haberlere daha kolay bir şekilde ulaşmasını sağlamak için bu projeyi hayata geçirdik.

Projenin özellikleri arasında, toplam 10 adet siteden içeriklerin çekilmesi, içeriklerin otomatik olarak Türkçeye çevrilmesi ve tarih, metinlerin Türkçe ve İngilizce kelime sayıları, orijinal link gibi istatistiklerin sitede gösterilmesi yer almaktadır.
  Ulak | Global Haber Sitesi
Ulak | Global Haber Sitesi
Ulak | Global Haber Sitesi

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki değişkenleri config.json adında ki dosyaya eklemeniz gerekmektedir.

`postgre username`

`postgre password`

`postgre database name`

  
## Kullanılan Teknolojiler

**Front-End :** Html, Css, JavaScript

**Back-End:** Python-Flask


  
  
## Özellikler

- 10 Adet yabancı haber sitesi kazılmıştır.
- İçerikler otomatik olarak Türkçe'ye çevrilmektedir.
- Tarih, orjinal metin, çevrilmiş metin, orjinal link, tarih gibi bilgiler alınmıştır.



  
## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/pjnzyu3.jpg)

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/s16l4h7.jpg)

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/evcpcuy.jpg)


![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/1do8mge.jpg)

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/1ud9rxw.jpg)

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/2ww7r9q.jpg)

## Yükleme 

PostgreSQL Üzerinden Ulak adında bir veritabanı oluşturun, buna news adında bir tablo ekleyin en son da resimde bulunan isimlerde sütunlar ekleyin. 

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/gllm9m5.jpg)

Main dosyası scraping işlemlerin yapıldığı dosyadır, bu dosya haberleri veritabanına kayıt eder.

```bash 
python main.py
```

App dosyası, web sitenin çalıştığı dosyadır. Bu dosya çalıştığında http://127.0.0.1:5000/ adresinde web sitesi açılacak.

```bash 
python app.py
```


![Logo](https://res.cloudinary.com/practicaldev/image/fetch/s--yfF3_q8k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/f0i5oszdj3gwk686xuc0.JPG)

    
