## Kurulum ve Çalıştırma

### Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki araçların sistemde kurulu olması gerekmektedir:

* Qt Creator
* Qt 5 veya Qt 6
* C++ derleyici (MinGW / MSVC / GCC)
* MySQL Server
* Git

---

### Projeyi Klonlama

```bash
git clone https://github.com/mermean/hastane-randevu-sistemi.git
cd hastane-randevu-sistemi
```

---

### Veritabanı Ayarı

* MySQL servisinin çalışır durumda olması gerekmektedir
* Uygulama ilk çalıştırıldığında gerekli veritabanı ve tablolar otomatik olarak oluşturulur




* Varsayılan veritabanı bilgileri kullanıcının şifre ve kullanıcı adına göre değişebilir. Proje içerisinden değiştirilmelidir.
---

### Projenin Açılması

1. Qt Creator açılır
2. "Open Project" seçeneği ile proje klasörü seçilir
3. `.pro` veya `CMakeLists.txt` dosyası açılır
4. Uygun kit (Desktop Qt) seçilir

---

### Derleme ve Çalıştırma

1. Proje açıldıktan sonra "Build" işlemi yapılır
2. Ardından "Run" butonu ile uygulama çalıştırılır

---

### Notlar

* MySQL çalışmadan uygulama veritabanına bağlanamaz
* Gerekli Qt kitleri yüklü değilse proje derlenmez
* Veritabanı bağlantı bilgileri güvenlik açısından değiştirilmesi önerilir
* İlk çalıştırmada tablolar otomatik oluşturulduğu için manuel SQL kurulumu gerekmez
