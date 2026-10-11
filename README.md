# AeroPulse — Uçuş Aksama ve Havalimanı Risk Analiz Sistemi

AeroPulse, 2024 yılı ABD uçuş verilerini analiz ederek havayolları, havalimanları ve rotalar için güvenilirlik ve risk değerlendirmeleri üreten Python tabanlı bir analiz sistemidir.

Proje; uçuş gecikmeleri, iptaller, yönlendirmeler, gecikme nedenleri, olağandışı operasyon günleri ve rota riskleri gibi konuları analiz eder.

## Projenin Amacı

AeroPulse aşağıdaki sorulara cevap vermeyi amaçlar:

* Hangi havayolları daha güvenilir?
* Hangi havalimanlarında gecikme riski daha yüksek?
* Hangi rotalar daha problemli?
* Günün hangi saatlerinde gecikmeler artıyor?
* Gecikmelerin temel nedenleri neler?
* Hangi günlerde olağandışı operasyonel durumlar yaşanıyor?

## Dataset

Projede 2024 yılına ait milyonlarca uçuş kaydı içeren bir uçuş verisi kullanılmaktadır.

Dataset içerisinde şu bilgiler bulunmaktadır:

* Havayolu
* Kalkış havalimanı
* Varış havalimanı
* Planlanan kalkış ve varış saatleri
* Gerçek kalkış ve varış saatleri
* Kalkış gecikmesi
* Varış gecikmesi
* İptal durumu
* Yönlendirme durumu
* Uçuş mesafesi
* Havayolu kaynaklı gecikme
* Hava durumu kaynaklı gecikme
* NAS kaynaklı gecikme
* Güvenlik kaynaklı gecikme
* Geç gelen uçak kaynaklı gecikme

## Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Matplotlib
* Nesne Yönelimli Programlama
* CSV veri işleme

## Proje Yapısı

```text
AeroPulse/
│
├── data/
│   └── flight_data_2024.csv
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── feature_engineer.py
│   ├── delay_analyzer.py
│   ├── airline_analyzer.py
│   ├── airport_analyzer.py
│   ├── route_analyzer.py
│   ├── risk_engine.py
│   ├── anomaly_detector.py
│   ├── search_engine.py
│   ├── visualizer.py
│   ├── report_generator.py
│   └── menu.py
│
└── main.py
```

## Temel Özellikler

### Gecikme Analizi

AeroPulse aşağıdaki gecikme metriklerini hesaplar:

* Ortalama gecikme
* Medyan gecikme
* Standart sapma
* Gecikme yüzdelikleri
* 15+ dakika gecikme oranı
* 30+ dakika gecikme oranı
* 60+ dakika gecikme oranı
* 120+ dakika gecikme oranı

## Havayolu Analizi

Her havayolu için şu metrikler hesaplanır:

* Toplam uçuş sayısı
* Ortalama gecikme
* Zamanında uçuş oranı
* Ciddi gecikme oranı
* İptal oranı
* Yönlendirme oranı

## Havalimanı Analizi

Havalimanları şu kriterlere göre değerlendirilir:

* Uçuş sayısı
* Ortalama gecikme
* Zamanında uçuş oranı
* İptal oranı
* Yönlendirme oranı
* Ciddi gecikme oranı

Çok az uçuşu bulunan havalimanlarının sonuçları yanıltmaması için minimum uçuş sayısı filtresi kullanılmaktadır.

## Rota Analizi

Rotalar şu formatta oluşturulur:

```text
Origin -> Destination
```

Örnek:

```text
JFK -> LAX
```

Her rota için şu metrikler hesaplanır:

* Toplam uçuş sayısı
* Ortalama gecikme
* Ciddi gecikme oranı
* İptal oranı
* Gecikme değişkenliği

## Airport Reliability Score

AeroPulse, havalimanları için 0–100 arasında özel bir güvenilirlik skoru üretir.

Skor ağırlıkları:

```text
Zamanında uçuş oranı       %40
Ciddi gecikme performansı  %25
İptal performansı          %20
Ortalama gecikme           %10
Yönlendirme performansı     %5
```

Yüksek skor, daha güvenilir bir operasyon anlamına gelir.

## Airline Reliability Score

Havayolları da benzer kriterlerle 0–100 arasında değerlendirilir.

Kullanılan metrikler:

* Zamanında uçuş oranı
* Ciddi gecikme oranı
* İptal oranı
* Ortalama gecikme
* Yönlendirme oranı

Yüksek skor daha güvenilir havayolu operasyonunu ifade eder.

## Route Risk Score

Rotalar için 0–100 arasında bir risk skoru hesaplanır.

Kullanılan ağırlıklar:

```text
Ortalama gecikme        %25
Ciddi gecikme oranı     %30
İptal oranı             %20
Gecikme değişkenliği    %15
Uçuş yoğunluğu          %10
```

Risk seviyeleri:

```text
0–20    LOW
21–40   MODERATE
41–60   HIGH
61–80   VERY HIGH
81–100  CRITICAL
```

Yüksek skor daha yüksek operasyonel riski ifade eder.

## Anomaly Detection

AeroPulse, NumPy ve Z-Score yöntemini kullanarak olağandışı operasyon günlerini tespit eder.

Günlük ortalama gecikmeler, normal operasyon seviyeleriyle karşılaştırılır.

Anomaly seviyeleri:

```text
2–3 Z-Score   HIGH
3–4 Z-Score   VERY HIGH
4+ Z-Score    CRITICAL
```

Olağandışı bir gün tespit edildiğinde sistem ayrıca şu alanlarda detaylı inceleme yapar:

* Havayolları
* Havalimanları
* Rotalar
* Kalkış saatleri

## Gecikme Nedenleri Analizi

2024 uçuş verilerinde toplam gecikme dakikalarına katkı oranları:

```text
Geç Gelen Uçak Gecikmesi     %40.44
Havayolu Kaynaklı Gecikme    %34.51
NAS Kaynaklı Gecikme         %18.90
Hava Durumu Gecikmesi         %5.97
Güvenlik Gecikmesi            %0.17
```

Bu sonuçlara göre en büyük iki gecikme kaynağı geç gelen uçaklar ve havayolu kaynaklı operasyonel sorunlardır.

## Aylık Analiz

Tüm yıl verisi üzerinde aylık karşılaştırmalar yapılır.

Her ay için:

* Toplam uçuş sayısı
* Ortalama gecikme
* İptal oranı
* Ciddi gecikme oranı

hesaplanır.

Analiz sonucunda Temmuz ayının gecikmeler açısından daha problemli aylardan biri olduğu görülmüştür.

## Saat Bazlı Analiz

Uçuşların kalkış saatlerine göre gecikme davranışları analiz edilir.

Bu sayede sabah, öğleden sonra ve akşam saatlerindeki operasyonel farklılıklar incelenebilir.

## Haftanın Günleri Analizi

Haftanın her günü için:

* Ortalama gecikme
* Medyan gecikme
* Standart sapma
* İptal oranı
* 15+ dakika gecikme oranı

hesaplanır.

## Görselleştirme

Sistem Matplotlib kullanarak otomatik grafikler üretir.

Üretilen grafiklerden bazıları:

* Havayolu güvenilirlik sıralaması
* Havalimanı güvenilirlik sıralaması
* Saatlik gecikme değişimi
* Aylık gecikme trendi
* Haftanın günlerine göre gecikme
* En riskli rotalar
* Gecikme nedenleri dağılımı
* Olağandışı operasyon günleri

Grafikler şu klasöre kaydedilir:

```text
outputs/charts/
```

## CSV Raporları

AeroPulse analiz sonuçlarını otomatik olarak CSV dosyalarına aktarır.

Üretilen raporlar:

```text
airport_rankings.csv
airline_rankings.csv
high_risk_routes.csv
anomalies.csv
```

Dosyalar şu klasöre kaydedilir:

```text
outputs/reports/
```

## Terminal Uygulaması

AeroPulse interaktif bir terminal menüsüne sahiptir.

Kullanıcı:

* Havayolu analizlerini görüntüleyebilir
* Havalimanı analizlerini görüntüleyebilir
* Rota analizlerini görüntüleyebilir
* Risk skorlarını inceleyebilir
* Anomaly sonuçlarını görebilir
* Havalimanı arayabilir
* İki havalimanını karşılaştırabilir
* İki havayolunu karşılaştırabilir

Örnek terminal menüsü:

```text
==============================
        AEROPULSE
==============================

1 - Airline Analysis
2 - Airport Analysis
3 - Route Analysis
4 - Risk Analysis
5 - Anomaly Analysis
6 - Airport Search
7 - Compare Airports
8 - Compare Airlines
9 - Exit
```

## Örnek Havayolu Karşılaştırması

```text
DL vs AA

DL
Toplam Uçuş: 25585
Ortalama Gecikme: 1.47 dk
Zamanında Uçuş: %83.81
Reliability Score: 91.83

AA
Toplam Uçuş: 29672
Ortalama Gecikme: 19.37 dk
Zamanında Uçuş: %69.31
Reliability Score: 81.23
```


## Performans Optimizasyonu

Dataset yükleme aşamasında gereksiz kolonların okunmaması ve uygun veri tiplerinin kullanılmasıyla performans iyileştirildi.

1 milyon kayıt üzerinde yapılan test:

```text
Normal yükleme:     1.19 saniye
Optimize yükleme:   0.62 saniye
```

Optimize edilmiş veri yükleme yöntemi, standart yüklemeye göre belirgin şekilde daha hızlı çalışmıştır.


## Projenin Kazandırdıkları

Bu proje yalnızca bir veri analizi notebook'u olarak tasarlanmamıştır.

Modüler ve nesne yönelimli bir mimari kullanılarak veri analizi ile yazılım geliştirme yaklaşımı bir araya getirilmiştir.

Projede:

* Büyük CSV verileriyle çalışma
* Veri temizleme
* Feature engineering
* Pandas groupby işlemleri
* NumPy istatistikleri
* Özel risk algoritmaları
* Anomaly detection
* Matplotlib görselleştirme
* OOP mimarisi
* Modüler Python geliştirme
* Terminal tabanlı kullanıcı etkileşimi
* CSV raporlama

uygulanmıştır.

## Projenin Amacı

AeroPulse, gerçek dünya uçuş verilerini kullanarak Python, veri analizi ve yazılım geliştirme becerilerini tek bir projede birleştirmek amacıyla geliştirilmiştir.

Projenin temel hedefi yalnızca veriyi analiz etmek değil, analiz sonuçlarını kullanıcıya sunabilen, risk skorları üreten ve operasyonel problemleri tespit edebilen bir sistem oluşturmaktır.
