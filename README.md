# ragwi


Python'u kurarken Miniconda bizlere çok güzel araçlar sağlayabilir.

### Miniconda İndirme ve Kurulum

Öncelikle Windows ortamı için Miniconda'yı şu şekilde kuruyoruz:

* [anaconda.com/download](https://anaconda.com/download) adresine git, kayıt ol ve Windows 64-bit Graphical Installer seçeneğini seç.
* İndirilen .exe dosyasına çift tıkla.
* Just Me (Recommended) seç.
* "Add Miniconda3 to my PATH" seçeneğini işaretleme.
* Install'a bas, bitir.

Ortamı oluşturmak için aşağıdaki komutu terminalde kullanacağız:

```bash
conda create -n rag/ragwi python=3.11

```

Ancak fark etmemiz gerek şey, artık terminalde yolun yanında `(base)` kelimesinin çıktığını. İndirmek istenilen kütüphanelere `y` yazarak kabul ederiz. Son olarak bu ortamı aktifleştirmemiz gerek, bu yüzden terminale `conda activate rag/ragwi` yazıyoruz. Doğru bir şekilde aktifleştirildiği takdirde `(base)` yerine ortamın adını görmeniz gerekecektir.

---

### WSL (Windows Subsystem for Linux) Kurulumu

Biz linux ortamını kullanmak zorundayız ondan dolayı linux işletim sistemini kurmak yerine ki kurarsan daha iyi ancak kurmak istemezsen wsl terminali kullanabiliriz bu yüzden aşağıdaki adımları takip et.

**Gereksinim:** Windows 10 (2004+) veya Windows 11.

1. PowerShell'i **Yönetici** olarak aç ve `wsl --install` yaz.
2. Bilgisayarı **yeniden başlat**.
3. **Ubuntu**'yu aç.
4. **Kullanıcı adı + şifre** belirle.
5. `sudo apt update` komutunu çalıştır.

---

### WSL Terminalinde Miniconda ve VS Code Kurulumu

Şimdi wsl terminalini kullanarak ve vs code ile bağlamak için bu adımları takip etmemiz gerek:

1. Ubuntu aç.
2. `cd /mnt/g/rag/ragwi` komutunu çalıştırarak kendi projenin yoluna git.
3. VS code açmak için `code .` komutunu kullan.
4. Sonra WSL terminalinde Miniconda indirmemiz gerek, bu yüzden Miniconda resmi sayfasından linux sürümünün wget komutunu alarak terminalde çalıştırmamız gerek: `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`.
5. Modunu değiştirmek için `chmod +x Miniconda3-latest-Linux-x86_64.sh` komutunu kullanırız.
6. Sonra da `./Miniconda3-latest-Linux-x86_64.sh` yazarak kurulumu başlatırız.
7. Sırasıyla `q`, `yes` ve `Enter` yazarak indirmesini bekleriz.
8. Sonra path'a eklememi ister misin diye sorar, `Yes` yazarak bitiriz.
9. Sonra `bash ~/.profile` komutunu yazarız. Şimdi WSL terminalinde `(base)` görmemiz gerek.

Şimdi yeni ortamı olutşurma zamanı geldi, şu komutu çalıştır:

```bash
conda create -n ragwi python=3.11

```

Yukarıdaki komutu çalıştırdıktan sonra terminali kapatıp yenisini açarız ki projenin bulunduğu klasöre yönlendirsin direkt. Ondan sonra aktifleştiriz ortamı (`conda activate ragwi`).

**Olası Hatalar ve Çözümleri:**
Eğer `EnvironmentNameNotFound: Could not find conda environment: rag/ragwi` gibi bir hata ile karşılaşırsan eğer çözümü kolay.
Önce terminalde `conda info --envs` yaz. Çıkan sonuçlarda fark edeceğiz ki rag/ragwi ortamına isim vermemişiz ondan dolayı tam yolu vererek şu şekilde aktifleştireceğiz: `conda activate /home/yasirubuntu/miniconda3/envs/rag/ragwi` (Kendi kullanıcı adına göre yolu düzenlemeyi unutma).