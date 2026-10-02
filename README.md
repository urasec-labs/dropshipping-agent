# 🚀 Autonomous Dropshipping Agent v3 (ReAct Mimarisi)

Bu proje; sosyal medya trendlerini analiz eden, ürün tedarik süreçlerini yöneten, dinamik fiyatlandırma yapan ve sipariş otomasyonu sağlayan **ReAct (Reasoning + Acting)** döngüsüne sahip otonom bir yapay zeka ajanı altyapısıdır. 

Proje, modüler kod yapısı (**Clean Code**) ve gevşek bağlı (**Loose Coupling**) asenkron olay mimarisi dikkate alınarak üretime hazır (production-ready) standartlarda geliştirilmiştir.

---

## 🛠️ Öne Çıkan Özellikler & Teknolojiler
- **🧠 ReAct Karar Döngüsü:** Kararlarını (Düşünce -> Aksiyon -> Gözlem) adımlarıyla otonom yürüten LLM kontrolcü yapısı.
- **👁️ LLM & Vision Motoru:** Google Gemini API tabanlı görsel pazar trendi analizleri ve otonom reklam metni (creative) üretimi.
- **📈 Dinamik Fiyatlandırma Motoru:** Ürün maliyetleri (COGS), hedef kâr marjları ve anlık rakip fiyat kırılımlarına göre değişken fiyatlandırma algoritmaları.
- **🗄️ Hibrit Bellek Katmanı:** İlişkisel veri takibi için `SQLAlchemy ORM`, pazar istihbaratları ve RAG (Retrieval-Augmented Generation) hafızası için `ChromaDB` vektör veritabanı.
- **🚨 HITL (Human-in-the-Loop):** Kritik finansal ve operasyonel aksiyonlar öncesinde Telegram/Discord entegrasyonlu insan doğrulama ve onay mekanizması.
- **🔄 Asenkron Event Bus:** Modüller arası haberleşmeyi arka planda asenkron yürüten, sistem genişletilebilirliğini artıran olay havuzu.
- **🛡️ Dayanıklı Kazıyıcı (Scraper):** `tenacity` ile ağ hatalarına karşı otomatik yeniden deneme (retry) mekanizmalı, esnek pazar kazıma motoru.

---

## 📂 Proje Dosya Yapısı
```text
dropshipping_agent_v3/
├── database/         # İlişkisel (SQLite/PostgreSQL) ve Vektör (ChromaDB) veri katmanı
├── modules/          # İş mantığı motorları (Fiyatlandırma, Kargo, Reklam, Trend)
├── utils/            # Loglama, Bildirim (HITL) ve Asenkron Event Bus araçları
├── config.py         # Pydantic v2 tabanlı çevre ve API değişkenleri yönetimi
├── gemini_client.py  # Gemini API LLM entegrasyon katmanı
├── scraper.py        # Hata toleranslı veri kazıma modülü
├── store_sync.py      # E-ticaret platformu (Shopify vb.) senkronizasyon motoru
├── main.py           # Ajanın ana ReAct karar ve çalışma döngüsü
├── .gitignore        # GitHub'a hassas veri sızmasını önleyen filtre dosyası
└── requirements.txt  # Projenin çalışması için gerekli kütüphaneler listesi
```

---

## 🚀 Kurulum ve Başlatma Talimatları

### 1. Depoyu Klonlayın veya İndirin
```bash
git clone https://github.com
cd dropshipping-agent
```

### 2. Sanal Ortam Oluşturun ve Bağımlılıkları Yükleyin
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Çevre Değişkenlerini Tanımlayın
Kök dizinde bulunan `.env.example` dosyasının adını `.env` olarak değiştirin ve gerekli API anahtarlarınızı girin:
```env
GEMINI_API_KEY=AIzaSyYourActualKeyHere...
DATABASE_URL=sqlite:///./dropshipping.db
MIN_PROFIT_MARGIN=0.35
```

### 4. Ajanı Çalıştırın
```bash
python main.py
```

---

## 🔒 Güvenlik Uyarıları
Bu depoda **kesinlikle ham şifreler veya canlı API anahtarları saklanmaz**. Hassas tüm veriler `.env` dosyası üzerinden okunur ve bu dosya `.gitignore` kuralları doğrultusunda GitHub'a yüklenmekten korunur. Dağıtım yaparken `.env.example` şablonunu referans alınız.
