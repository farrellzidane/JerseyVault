# JerseyVault

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Farrell Zidane Raihandrawan (2306275600)

LINK PWS : https://farrell-zidane31-jerseyvault.pbp.cs.ui.ac.id/
 

## TUGAS 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. membuat _repository_ bernama ```Jerseyvault```
2. meng-_clone repository_ kosong ke dalam komputer
3. Di direktori asal Membuat _virtual environment_ Python baru dengan command:
    ```bash
    python -m venv env
    ```
4. Menyalakan _virtual environment_ Python baru dengan command:
    ```bash
    source env/bin/activate
    ```

5.  Menyiapkan  Dependencies dan Membuat Proyek Django dengan membuat file ```requirements.txt``` yang berisi
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
6. Meng-_install requirements_ dengan pip
    ```bash
    Python -m pip install -r requirements.txt
    ```

7. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject jerseyvault .
    ```

8. Konfigurasi Proyek untuk menjalankan server dengan menambahkan kedua string berikut pada ```ALLOWED_HOSTS``` di ```settings.py``` untuk keperluan deployment:
    ```bash
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
9. Membuat aplikasi ```main``` dengan command:
    ```bash
    python manage.py startapp main
    ```

10. Menambahkan nama aplikasi ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```JerseyVault``` 

11. Me-_routing_ url pada file ```urls.py``` di direktori ```JerseyVault``` sehingga isi file ```urls.py``` menjadi:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls),
    ]
    
    ```
12.  Mengubah Berkas ```models.py``` dalam Aplikasi main menjadi :
```python
    from django.db import models

    class MoodEntry(models.Model):
        mood = models.CharField(max_length=255)
        time = models.DateField(auto_now_add=True)
        feelings = models.TextField()
        mood_intensity = models.IntegerField()

        @property
        def is_mood_strong(self):
            return self.mood_intensity > 5
```

13. Melakukan migrasi dengan command :
```
    python manage.py makemigrations
    python manage.py migrate
```

14. Membuat direktori template dan template ```html``` untuk laman ```main```:

    ```html
    <h1>{{ app_name }} Page</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```

15. Menambahkan fungsi untuk me-_render_ laman main pada file ```views.py```:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app name': 'JerseyVault',
            'name': 'Farrell Zidane Raihandrawan',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)
    ```

16. Melakukan routing pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

17. Mengetest aplikasi pada localhost dengan command:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_

18. Melakukan deploy app ke situs _Adaptable_



### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```
+----------------+        +------------+       +-------------+       +------------+      +----------------+
|     Client     |------->|  urls.py   |------>|   views.py  |------>|  models.py |      |    Template    |
|    (Browser)   |        | (Routing)  |       |   (Logic)   |  R/W  | (Database) |      |     (HTML)     |
| (HTTP Request) |        |            |       |             |<------|            |      |   (Response)   |
+----------------+        +------------+       +-------------+       +------------+      +----------------+
        ^                                          |      ^                                       |
        |                                          |      |                                       |
        -----------------(response)-----------------      -----------------------------------------
```

- Client (browser) : mulainya proses saat client (user) mengirimkan permintaan HTTP ke aplikasi Django, misalnya untuk mengakses halaman tertentu seperti /products/

- urls.py (Routing) : Django menerima request dan urls.py bertugas untuk mencocokkan URL request dengan pola yang ada. Jika cocok, maka Django akan mengarahkan request ke views.py yang sesuai

- views.py (Logic) : setelah diarahkan ke views.py, Django menjalankan fungsi view atau class-based view terkait. fungsi di dalam views.py biasanya berisi logic yang mengatur bagaimana data diambil dan dikirimkan ke template HTML dan bisa berinteraksi dengan models.py

- models.py (Database) : models.py ini berisi struktur data yang digunakan untuk berinteraksi dengan database

- Template (HTML) : Setelah data diperoleh dari models.py, view akan me-render template HTML dan mengirimkan data tersebut ke template yang akan ditampilkan di halaman web.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
## Fungsi Git :
Git adalah salah satu alat terpenting dalam pengembangan perangkat lunak saat ini. Secara sederhana, Git membantu kita mengelola perubahan yang terjadi pada kode, terutama ketika bekerja dalam tim.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
## Django sering dijadikan pilihan untuk pembelajaran pengembangan perangkat lunak karena:

- Batteries Included yaitu banyak fitur bawaan seperti autentikasi, admin panel, dan ORM, memudahkan pengembangan tanpa alat tambahan.
- Full-Stack yaitu menangani backend hingga frontend, sehingga pemula memahami alur lengkap pengembangan web.
- Struktur Terorganisir (MTV) yaitu Arsitektur Model-Template-View memisahkan data, logika bisnis, dan tampilan dengan jelas.
- Dokumentasi Baik yaitu Dokumentasi lengkap dan mudah dipahami memudahkan pemula belajar.
- Komunitas Besar yaitu Banyak tutorial dan dukungan komunitas membantu pemecahan masalah.
- Keamanan Bawaan yaitu Django secara otomatis menangani keamanan dasar seperti SQL injection dan CSRF.
- Skalabilitas yaitu Cocok untuk proyek kecil hingga besar, memungkinkan pemula tetap menggunakannya saat lebih berpengalaman.

### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena memungkinkan pengembang bekerja dengan database menggunakan objek Python, tanpa harus menulis SQL. Django memetakan objek Python ke tabel di database secara otomatis. ORM menyederhanakan operasi database seperti `SELECT`, `INSERT`, dan `UPDATE`, serta menyediakan keamanan dari SQL injection. Dengan ORM, pengelolaan data menjadi lebih mudah, abstraksi SQL terjamin, dan mendukung berbagai jenis database tanpa mengubah kode.

## TUGAS 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan bagian yang penting karena menjadi penghubung/jembatan bagi aliran informasi antara hardware, device, dan user. Data delivery yang efisien memastikan bahwa informasi yang dibutuhkan selalu tersedia secara real-time

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik dibanding XML karena JSON memiliki :
- struktur yang lebih sederhana dibandingkan dengan XML karena menggunakan struktur berbasis objek dengan key-values. 
- JSON lebih mudah untuk diparsing langsung oleh browser
- Sebagian besar REST API modern menggunakan JSON sebagai format standar untuk pertukaran data
- JSON mendukung validasi data dengan format yang lebih fleksibel melalui JSON Schema. Ini lebih ringan dan lebih mudah dipahami oleh developer.

### 3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 Fungsi `is_valid()` digunakan untuk
- Memeriksa Validasi Form untuk semua aturan validasi yang diterapkan pada form, baik itu validasi bawaan dari Django (seperti format email yang benar, panjang minimum/maximum, dll.) maupun validasi kustom yang dibuat oleh developer

- Membersihkan Data yang Valid : membersihkan data input dan menyimpannya dalam properti cleaned_data, yang kemudian dapat digunakan untuk memproses data lebih lanjut, seperti menyimpannya ke database

is_valid() berfungsi sebagai alat pengaman untuk memastikan bahwa semua input dari pengguna sudah sesuai dengan aturan yang ditentukan, sehingga aplikasi dapat berjalan dengan lancar dan aman.

### 4.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token diperlukan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana penyerang mencoba mengelabui pengguna yang sudah terotentikasi untuk melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka. Tanpa csrf_token ini penyerang dapat menyalahgunakan form Django seperti mengubah-ubah data pengguna, penghapusan data sensitif, dan lainnya 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat folder ```templates``` pada root folder dan buat ```base.html``` dengan isi
```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
```

2. membuka ```settings.py``` dan masukkan kode ini untuk mendeteksi berkas base.html sebagai berkas template

```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
...
```
3. Ubah kode ```main.html``` dengan menambahkan untuk untuk mewarisi template lain (`base.html`) dan mengganti isi blok `content` dengan konten spesifik halaman.:
```html
    {% extends 'base.html' %}
    {% block content %}
    ...
    {% endblock content %}
 ```

4. Menambahkan kode berikut pada ```models.py``` :
 ```python
    import uuid
    from django.db import models

    class Product(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
        jersey_name = models.CharField(max_length=255)
        time = models.DateField(auto_now_add=True)
        description = models.TextField()
        price = models.IntegerField()
        quantity = models.IntegerField()


        @property
        def is_mood_strong(self):
            return self.price > 5
```

dan lakukan migrasi model
```
    python manage.py makemigrations
    python manage.py migrate
```

5. Membuat file ```forms.py``` untuk membuat struktur form yang dapat menerima data Jersey Baru dengan memasukkan kode berikut:
``` python
    from django.forms import ModelForm
    from main.models import Product

    class ProductEntryForm(ModelForm):
        class Meta:
            model = Product
            fields = ["jersey_name", "description", "price", "quantity"]
```

6. Menambahkan import dan fungsi baru pada file ```views.py```  untuk menghasilkan form yang dapat menambahkan data Jersey Entry secara otomatis ketika data di-submit dari form.
```python
    from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
    from main.forms import ProductEntryForm
    from main.models import Product

    def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

7. Mengubah fungsi `show_main`dengan menambahkan kode beriku tuntuk mengambil seluruh objek product yang tersimpan pada database.
```python
    def show_main(request):
    product_entries = Product.objects.all()
    context = {
        ...
        'product_entries': product_entries
    }

    return render(request, "main.html", context)
```

8. Tambahkan import ```create_product_entry``` dan path URL ke dalam variabel ```urlpatterns``` pada ```urls.py``` di main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
```python
urlpatterns = [
   ...
    path('create_product_entry', create_product_entry, name='create_product_entry'),
]
```

9. Buat berkas HTML baru dengan nama ```create_product_entry.html``` pada direktori main/templates dan isi dengan kode berikut.
```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Jersey</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Jersey Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
```
10. Tambahkan kode ini ke dalam ```main.html``` untuk menampilkan data jersey dalam bentuk tabel yang akan redirect ke halaman form.
```html
    ...
    {% if not product_entries %}
        <p>Belum ada data jersey pada JerseyVault.</p>
    {% else %}
        <table>
        <tr>
            <th>Jersey name</th>
            <th>Time</th>
            <th>Description</th>
            <th>Price</th>
            <th>Quantity</th>

        </tr>
        {% for product_entry in product_entries %}
        <tr>
            <td>{{product_entry.jersey_name}}</td>
            <td>{{product_entry.time}}</td>
            <td>{{product_entry.description}}</td>
            <td>Rp.{{product_entry.price}}</td>
            <td>{{product_entry.quantity}}</td>
        </tr>
        {% endfor %}
        </table>
    {% endif %}
```
Screenshot POSTMAN : https://docs.google.com/document/d/16JmIt-wZpMgFIVi2bI5hJfzVgQuXsNG7B0p_BoDDfcE/edit?usp=sharing


## TUGAS 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
```HttpResponseRedirect()``` dan ```redirect()``` keduanya digunakan untuk mengarahkan user ke URL lain dalam Django, tetapi ada beberapa perbedaan antara keduanya. 

- ```HttpResponseRedirect()``` digunakan untuk mengembalikan respons HTTP yang menunjukkan bahwa browser harus diarahkan (redirect) ke URL yang ditentukan.  ```HttpResponseRedirect()``` memerlukan satu parameter yaitu URL tujuan. Biasanya digunakan  ketika ingin melakukan pengalihan manual dan secara eksplisit menulis URL sebagai string.

- ```redirect()``` merupakan fungsi utilitas Django yang lebih fleksibel untuk melakukan pengalihan. ```redirect()```lebih disukai karena lebih fleksibel. Ini memungkinkan pengalihan berdasarkan URL, nama view, atau objek, membuat kode lebih bersih dan mudah dipahami.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!

untuk menghubungkan model Product dengan User di Django dilakukan dengan menggunakan *ForeignKey* untuk mengaitkan setiap produk dengan pengguna tertentu. Pertama, impor model `User` dari `django.contrib.auth.models`. Kemudian, tambahkan ForeignKey pada model Product yang menunjuk ke User. Dengan begitu, setiap produk dapat dikaitkan dengan pengguna yang menambahkannya. Atribut `on_delete=models.CASCADE` digunakan untuk memastikan bahwa jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus. Saat membuat atau menyimpan produk, kaitkan produk dengan pengguna yang sedang login melalui request.user. Berikut ini adalah contoh kode yang diperlukan:

- pada `models.py`
```python    
    from django.db import models
    from django.contrib.auth.models import User

    class Product(models.Model):
        ...
        user = models.ForeignKey(User, on_delete=models.CASCADE)  # Hubungan dengan User
```

- pada `views.py` dan tambahkan kode pada function `show_main` :
```python
    def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
...
```

dan function `create_product_entry` :
```python
    def create_product_entry(request):
        form = ProductEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)
```
### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Authentication** adalah proses memverifikasi identitas pengguna (misalnya melalui login), sementara **Authorization** menentukan hak akses pengguna setelah mereka terautentikasi. Saat pengguna login, Django memverifikasi kredensial menggunakan `authenticate()` dan memulai sesi dengan `login()`. Setelah itu, otorisasi memastikan pengguna hanya bisa mengakses fitur sesuai izin mereka, yang diatur dengan sistem permissions dan groups.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan **session cookies**. Saat pengguna berhasil login, Django membuat sesi dan menyimpan informasi pengguna dalam bentuk **cookie** di browser pengguna. Setiap kali user mengirimkan permintaan, cookie ini dikirim kembali ke server, sehingga Django dapat mengidentifikasi pengguna yang login dan menjaga sesi tetap aktif.

1. Kegunaan lain dari cookies :
- Melacak preferensi pengguna: Seperti pengaturan bahasa, tema, atau barang yang ditambahkan ke keranjang belanja.
- Menyimpan data sementara: Seperti form yang diisi sebagian atau aktivitas browsing.
- Mengumpulkan data analitik: Seperti mengukur kunjungan atau perilaku pengguna di situs web.

2. Keamanan cookies :
Umumnya cookie tidak berbahaya bagi aktivitas online. Kemungkinannya sangat kecil bahwa malware dapat masuk ke komputer atau data-data rahasia hilang melalui cookie.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Proses Implementasi Login Page

1. **Membuat Fungsi Registrasi**:
- Modifikasi `views.py` untuk membuat fungsi registrasi yang meng*import* formulir bawaan Django. Tambahkan fungsi `register` untuk menangani pendaftaran pengguna baru.
- Buat file `register.html` sebagai template untuk tampilan halaman registrasi dan tambahkan path URL ke dalam `urlpatterns`.

2. **Implementasi Fungsi Login**:
- Di `views.py`, import fungsi bawaan Django seperti `authenticate`, `login`, dan `AuthenticationForm`. Tambahkan fungsi `login_user` untuk menangani proses login.
- Buat file `login.html` untuk tampilan halaman login dan atur URL path untuk akses halaman tersebut.

3. **Membuat Fungsi Logout**:
- Di `views.py`, impor fungsi `logout` dan tambahkan fungsi `logout_user` untuk menangani proses logout.
- Modifikasi file `main.html` dengan menambahkan hyperlink untuk logout dan tambahkan path URL untuk logout di `urlpatterns`.

4. **Restriksi Akses Halaman Utama**:
- Import `login_required` untuk membatasi akses ke halaman utama. 
- Gunakan decorator `@login_required(login_url='/login')` agar hanya pengguna yang sudah login yang dapat mengakses halaman tersebut.

5. **Mengelola Cookies**:
- Tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` di` views.py`. 
- Modifikasi fungsi `login_user` untuk membuat cookie `last_login` saat pengguna berhasil login.
- Tambahkan informasi cookie `last_login` ke dalam konteks, sehingga dapat ditampilkan di halaman `main.html`. 
- Modifikasi fungsi `logout_user` untuk menghapus cookie tersebut saat pengguna logout.
- Tampilkan informasi cookie di `main.html`.

6. **Menghubungkan Model Product dengan User**:

- Di `models.py`, import model `User` dan tambahkan field user pada model `Product` dengan menggunakan kode dibawah ini
```python
    models.ForeignKey(User, on_delete=models.CASCADE)
``` 
Ini akan mengaitkan setiap produk dengan pengguna yang membuatnya.

- Modifikasi fungsi `create_product_entry` di `views.py` agar menyimpan objek produk terkait dengan pengguna yang sedang login. Ubah query `product_entries` untuk menampilkan hanya produk yang terasosiasi dengan pengguna yang sedang login, serta tampilkan nama pengguna di konteks.

7. **Melakukan Migrasi Database**:
- Jalankan perintah `python manage .py makemigrations` dan `python manage.py migrate` untuk memperbarui skema database sesuai dengan perubahan yang dilakukan.

8. **Pengaturan Konfigurasi Proyek**:
- Buka berkas `settings.py`, `import os`, dan ubah variabel `DEBUG` menjadi kode berikut :

```python
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION 
```
untuk mengatur mode produksi.

9. **Membuat Aplikasi Baru**:
- Buat aplikasi baru bernama login yang akan mencakup halaman `registrasi`, `login`, dan `logout` (meskipun logout tidak memerlukan tampilan dan hanya mengarahkan kembali ke halaman login).

10.**Routing URL**:
- Atur routing URL untuk memastikan alur tampilan halaman berjalan dengan baik.

## TUGAS 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, ketika ada beberapa selector yang diterapkan pada elemen yang sama, prioritas atau urutan spesifisitas digunakan untuk menentukan gaya mana yang akan dipakai. Semakin tinggi urutan atau spesifisitas, semakin besar kemungkinannya untuk diterapkan pada elemen tersebut. Berikut adalah urutan prioritas selector CSS dari yang paling tinggi hingga paling rendah:

#### 1. Inline Styles (Gaya yang Didefinisikan Langsung di Elemen)
*Style* ini diterapkan langsung pada elemen HTML melalui atribut *style*. Karena diterapkan langsung di *element*, gaya ini memiliki prioritas tertinggi.
- **Contoh** : ```<div style="color: red;">Teks ini berwarna merah</div>```
- **Prioritas** : *Inline Style* akan mengabaikan semua *style* yang ditentukan oleh ```ID Selector```, ```class```, atau ```elemen```.

#### 2. ID Selectors (Selector Berdasarkan ID)
Selector yang menggunakan atribut id dari elemen HTML. Karena id harus unik untuk setiap *element* di halaman, selector ini memiliki prioritas yang tinggi.
- **Contoh** : ```#judul { color: blue; }``` akan mempengaruhi *element* dengan ID judul.
- **Prioritas** : ID memiliki prioritas lebih tinggi dibandingkan selector class dan elemen.

#### 3. Class Selectors (Selector Berdasarkan Class)
Selector yang menggunakan atribut class dari elemen. Class dapat diterapkan ke beberapa elemen, sehingga memiliki prioritas di bawah ID.
- **Contoh**: ```.konten { margin: 20px; }``` akan mempengaruhi semua *element* dengan class konten.
- **Prioritas**: Class memiliki prioritas lebih tinggi daripada selector elemen, tetapi lebih rendah dari ID.

#### 4. Element Selectors (Selector Berdasarkan Elemen)
Selector yang hanya berdasarkan elemen HTML seperti div, p, atau h1. Ini adalah selector dengan prioritas terendah.
- **Contoh**: ```p { color: green; }``` akan mempengaruhi semua *element* paragraf ```(<p>)```.
- **Prioritas:** Ini memiliki prioritas paling rendah dibandingkan selector ID dan class.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
**Responsive design** penting dalam pengembangan aplikasi web karena memungkinkan web atau aplikasi menyesuaikan tata letaknya secara otomatis agar **tampilan optimal** di berbagai perangkat dengan ukuran layar yang berbeda, seperti desktop, tablet, dan smartphone. 

#### Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- **Twitter**:
Twitter menggunakan desain responsif yang sangat baik. Baik di desktop maupun *mobile*, tata letak aplikasi tetap nyaman untuk diakses, dengan penyesuaian yang mulus berdasarkan ukuran layar. Teks, gambar, dan elemen interaktif semua berubah sesuai dengan perangkat yang digunakan pengguna.

#### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- **Situs Web Lama**:
Banyak situs web lama atau yang tidak di-update sering kali masih menggunakan layout statis yang tidak menyesuaikan dengan perangkat pengguna. Pengguna mungkin harus melakukan zoom atau scroll secara horizontal, terutama di layar yang lebih kecil.
- **Contoh**: Beberapa situs institusi pemerintah atau situs lama dari universitas yang belum dioptimalkan untuk perangkat seluler cenderung memiliki layout yang tidak responsif.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
#### Margin
**Margin** adalah ruang di luar border elemen, yang digunakan untuk memberi jarak antara elemen dan elemen lain di sekitarnya.

- **Cara Kerja**
**Margin** tidak mempengaruhi ukuran konten atau elemen itu sendiri, tetapi mengatur jarak antara elemen tersebut dengan elemen lain.

- **Properti** 
    - ```margin-top```
    - ```margin-right```
    - ```margin-bottom```
    - ```margin-left```
    - ```margin``` (shorthand untuk semua sisi)

- **Contoh Syntax** :
```css
    .box {
    margin: 10px; /* Margin 10px di semua sisi */
    }
```
#### Border
**Border** adalah garis yang mengelilingi elemen di antara padding dan margin. Border menambah batas visual di sekitar elemen dan dapat dikustomisasi dengan berbagai gaya, ketebalan, dan warna.

- **Cara Kerja** :
Border dapat memiliki lebar, warna, dan gaya yang berbeda. Border mempengaruhi ukuran total elemen karena menambah lebar di luar padding.

- **Properti**

- **Contoh Syntax**
```css
    .box {
        border: 2px solid #000; /* Border dengan ketebalan 2px, gaya solid, dan warna hitam */
    }
```
#### Padding
**Padding** adalah ruang antara konten elemen dan batas elemen (border). Padding menciptakan jarak di dalam elemen, sehingga konten elemen tidak menempel langsung pada tepi border.

- **Cara Kerja** :
**Padding** mempengaruhi ukuran elemen, menambah ruang di dalam elemen tersebut.

- **Properti**:
    - ```padding-top```
    - ```padding-right```
    - ```padding-bottom```
    - ```padding-left```
    - ```padding``` (shorthand untuk semua sisi)

- **Contoh Syntax**
```css
    .box {
        padding: 20px; /* Memberi padding 20px di semua sisi */
    }
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

#### Flex Box
**Flex Box** adalah *method layout* yang bertujuan untuk memberikan kontrol yang lebih baik terhadap *alignment* di dalam container, terutama ketika ukuran *element* anak tidak diketahui atau dinamis. Flexbox bekerja dalam satu dimensi, baik secara horizontal (baris) atau vertikal (kolom).

- **Kegunaan**: Mengatur alignment dan space antar elemen dalam satu arah.
- **Properti Utama**: `flex-direction`, `justify-content`, `align-items`, `flex-grow`, `flex-shrink`.
- **Cocok untuk**: Navbar, tombol, atau elemen baris/kolom fleksibel.

**Contoh** :
```css
.flex-container { display: flex; justify-content: space-between; }
```

#### Grid Layout
**Grid layout** adalah *method layout* dengan tata letak dua dimensi, yang memungkinkan kontrol penuh untuk mendefinisikan baris dan kolom. Berbeda dengan flexbox yang berfokus pada satu dimensi (baris atau kolom), grid bekerja pada **dua dimensi (baris dan kolom)** secara bersamaan.

- **Kegunaan**: Mengatur tata letak yang kompleks dengan baris dan kolom.
- **Properti Utama**: `grid-template-columns`, `grid-template-rows`, `grid-gap`, `grid-area`.
- **Cocok untuk**: Layout halaman penuh, galeri, dashboard.

**Contoh** :
```css
.grid-container { display: grid; grid-template-columns: 1fr 2fr; gap: 20px; }
```
#### Perbandingan Flexbox vs Grid Layout:
- **Flexbox** lebih cocok untuk tata letak satu dimensi (baris atau kolom) di mana elemen-elemen secara fleksibel diatur dalam satu arah.
- **Grid Layout** lebih cocok untuk tata letak dua dimensi di mana kita ingin mengatur elemen di baris dan kolom sekaligus, dengan kontrol yang lebih kompleks.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Kustomisasi halaman login, register, dan tambah product semenarik mungkin. ###
- implementasi styling menggunakan tailwind css , dengan tipe inline css dan internal css
    1. Menambahkan kode berikut pada base.html untuk menyambungkan template django dengan taiwind
    ```html
    <head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
    </head>
    ```
2. menambahkan warna, font, dan ukuran yang sesuai pada tiap page
3. menambahkan animasi dan transisi untuk membuat tampilan lebih menarik
4. menyesuaikan layout dan posisi elemen agar terlihat rapi dan mudah dibaca

 - **Contoh** : pada bagian ```card_product.html``` untuk menampilkan produk yang ada sebagai berikut :

 ```html
 <div class="w-full max-w-xs bg-white border border-gray-200 rounded-lg shadow-lg hover:shadow-2xl transition duration-300 ">
    
    <!-- Product Info Section -->
    <div class="px-4 pb-4">
        <!-- Edit and Delete Buttons -->
        <div class="flex justify-end mt-3 mb-3 space-x-2">
            <a href="{% url 'main:edit_product' product.pk %}" class="text-white bg-yellow-500 hover:bg-yellow-600 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm px-3 py-1.5 text-center">
                Edit
            </a>
            <a href="{% url 'main:delete_product' product.pk %}" class="text-white bg-red-500 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3 py-1.5 text-center">
                Delete
            </a>
        </div>
        <!-- Product Image Section -->
        <a href="#">
            {% if product.image_url %}
                <!-- Display the product image from the URL -->
                <img class="p-6 rounded-t-lg" src="{{ product.image_url }}" alt="{{ product.jersey_name }}" />
            {% else %}
                <!-- Fallback image if no image_url is provided -->
                <img class="p-6 rounded-t-lg" src="/static/images/placeholder.png" alt="Placeholder image" />
            {% endif %}
        </a>

        <a href="#">
            <h5 class="text-lg font-semibold tracking-tight text-gray-900">{{ product.jersey_name }}</h5>
        </a>

        <!-- Product Description Section -->
        <div class="mt-2.5 mb-4">
            <p class="text-gray-700 text-sm">{{ product.description }}</p>
        </div>

        <!-- Price and Button Section -->
        <div class="flex items-center justify-between">
            <span class="text-2xl font-bold text-gray-900">Rp {{ product.price }}</span>
            <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center">Add to cart</a>
        </div>
    </div>
</div>

 ```

## TUGAS 6
### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
**JavaScript** adalah bahasa pemrograman yang memungkinkan kita untuk membuat konten, mengontrol multimedia, animasi gambar, dan elemen dinamis lainnya di web.
Beberapa manfaat JavaScript dalam pengembangan aplikasi web meliputi:
- **Kemampuan untuk melakukan permintaan HTTP secara asinkron (AJAX)**: Ini memungkinkan aplikasi web untuk mengambil atau mengirim data di latar belakang tanpa harus memuat ulang seluruh halaman, meningkatkan interaktivitas aplikasi bagi pengguna.
- **User Interface yang interaktif**: Dengan adanya framework seperti React, Vue, dan Angular, JavaScript memungkinkan pengembang membuat antarmuka yang dinamis dan menarik bagi pengguna.
- **Dukungan luas pada browser**: JavaScript telah menjadi standar di hampir semua browser modern, membuatnya menjadi pilihan populer untuk mengembangkan fitur aplikasi web yang dapat diakses di berbagai platform.
-** Manipulasi DOM (Document Object Model)**: JavaScript dapat mengubah elemen pada halaman web secara real-time berdasarkan interaksi pengguna, memberikan pengalaman yang lebih responsif.
- **Full Stack Development**: JavaScript dapat digunakan di sisi front-end maupun back-end, misalnya dengan Node.js. Ini memudahkan proses pengembangan dan penyebaran aplikasi karena satu bahasa dapat digunakan di kedua sisi.
Secara keseluruhan, **JavaScript** menjadi komponen penting dalam pengembangan aplikasi web modern. Bahasa ini membantu menghadirkan fungsionalitas yang lebih kompleks, seperti yang digunakan di search engine, e-commerce, dan platform media sosial.

### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Dalam JavaScript, fungsi `fetch()` digunakan untuk melakukan permintaan HTTP (seperti GET, POST) ke server dan mengembalikan promise yang merepresentasikan proses asinkron dari permintaan tersebut. Penggunaan `await` dalam konteks `fetch()` berfungsi untuk menunggu hingga promise dari `fetch()` selesai diproses, sehingga hasilnya dapat digunakan seperti data sinkron.

#### Fungsi Penggunaan `await` dengan `fetch()`:
1. **Menunggu Penyelesaian Promise**: `await` digunakan untuk membuat eksekusi kode "menunggu" sampai permintaan `fetch()` selesai dan promise dikembalikan. Artinya, JavaScript akan menunggu respons dari server sebelum melanjutkan ke baris kode berikutnya.

2. **Mengubah Promise Menjadi Hasil Nilai** : Ketika menggunakan `await` pada `fetch()`, JavaScript mengekstrak nilai yang dihasilkan oleh promise tersebut, yang biasanya berupa respons dari server (seperti data JSON atau status HTTP). Ini membuat kode lebih mudah dibaca dan lebih mirip dengan alur sinkron.

### 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
`@csrf_exempt` digunakan untuk menonaktifkan perlindungan **Cross-Site Request Forgery (CSRF)** pada view tertentu. Ini akan membuat Django tidak memeriksa keberadaan `csrf_token` pada **POST request** yang dikirimkan ke view tersebut, seperti pada fungsi `create_product_entry_ajax`. Biasanya, `@csrf_exempt` digunakan jika view memproses data dari layanan eksternal yang tidak memiliki akses ke token CSRF, sehingga POST request dapat dilakukan tanpa validasi CSRF. Penggunaan `@csrf_exempt` juga diperlukan saat menerima **AJAX POST request** yang tidak menyertakan token CSRF, karena tanpa itu, Django akan menolak permintaan dengan **error 403**.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input harus tetap dilakukan di sisi backend demi menjaga keamanan data. Pengguna dapat menonaktifkan JavaScript atau memodifikasi validasi yang dilakukan di frontend, sehingga validasi di sisi klien saja tidak cukup. Oleh karena itu, perlu dilakukan pembersihan di sisi backend (server) untuk memastikan data yang diterima aman dan tidak mengandung serangan seperti `XSS (Cross-Site Scripting)`.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### Pengimplementasian AJAX dan Javascript
1. Membuat Fungsi untuk Menambahkan produk dengan AJAX dengan menambahkan potongan kode berikut pada `views.py`
```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
...
@csrf_exempt
@require_POST
def create_product_entry_ajax(request):
    jersey_name = strip_tags(request.POST.get("jersey_name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    image_url = request.POST.get("image_url")
    user = request.user

    new_jersey = Product(
        jersey_name=jersey_name, description=description,
        price=price, quantity=quantity, image_url=image_url,
        user=user
    )
    new_jersey.save()

    return HttpResponse(b"CREATED", status=201)
```

2. Menambahkan Routing Untuk Fungsi `create_product_entry_ajax` pada `urls.py` dengan potongan kode berikut :
```python
from main.views import ..., create_product_entry_ajax
...
urlpatterns = [
    ...
    path('create_product_entry_ajax/', create_product_entry_ajax, name='create_product_entry_ajax'),
]
```
3. Menampilkan Data product Entry dengan `fetch()` API dengan memodifikasi `views.py` dan `main.html` :
- `views.py`
```python
    data = Product.objects.filter(user=request.user)
    # ubah pada baris pertama sho_json dan show_xml
```
- `main.html`
```html
<script>
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');
  
  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
  
  async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  function addProductEntry() {
    fetch("{% url 'main:create_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#ProductEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("ProductEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  function showModal() {
      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    const productEntries = await getProductEntries();
    let htmlString = "";

    if (productEntries.length === 0) {
      htmlString = `
          <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
              <p class="text-center text-gray-600 mt-4">Belum ada jersey pada JerseyVault.</p>
          </div>`;
    } else {
      productEntries.forEach((item) => {
        htmlString += `
          <div class="w-full max-w-xs bg-white border border-gray-200 rounded-lg shadow-lg hover:shadow-2xl transition duration-300">
            <div class="px-4 pb-4">
              <div class="flex justify-end mt-3 mb-3 space-x-2">
                <a href="/edit-product/${item.pk}" class="text-white bg-yellow-500 hover:bg-yellow-600 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm px-3 py-1.5 text-center">Edit</a>
                <a href="/delete/${item.pk}" class="text-white bg-red-500 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3 py-1.5 text-center">Delete</a>
              </div>
              <a href="#">
                ${item.fields.image_url ? `<img class="p-6 rounded-t-lg" src="${DOMPurify.sanitize(item.fields.image_url)}" alt="${DOMPurify.sanitize(item.fields.jersey_name)}" />` : `<img class="p-6 rounded-t-lg" src="/static/images/placeholder.png" alt="Placeholder image" />`}
              </a>
              <a href="#"><h5 class="text-lg font-semibold tracking-tight text-gray-900">${DOMPurify.sanitize(item.fields.jersey_name)}</h5></a>
              <div class="mt-2.5 mb-4"><p class="text-gray-700 text-sm">${DOMPurify.sanitize(item.fields.description)}</p></div>
              <!-- Quantity Section -->
              <div class="mb-2">
                <p class="text-gray-500 text-sm">Available Quantity: <span class="font-bold">${DOMPurify.sanitize(item.fields.quantity)}</span></p>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-2xl font-bold text-gray-900">Rp ${DOMPurify.sanitize(item.fields.price)}</span>
                <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center">Add to cart</a>
              </div>
            </div>
          </div>`;
      });
    }

    document.getElementById("product_entry_cards").innerHTML = htmlString;
  }

  refreshProductEntries();
  document.getElementById("ProductEntryForm").addEventListener("submit", (e) => {
      e.preventDefault();
      addProductEntry();
  });
</script>
```

4. Melindungi Aplikasi dari **Cross Site Scripting (XSS)** dengan menambahkan `strip_tags` untuk membersihkan data baru pada `views.py`,`forms.py`
- `views.py`
```python
from django.utils.html import strip_tags
...

@csrf_exempt
@require_POST
def create_product_entry_ajax(request):
    jersey_name = strip_tags(request.POST.get("jersey_name"))
    description = strip_tags(request.POST.get("description"))
...
```
- `forms.py`
```python
from django.utils.html import strip_tags
...
class ProductEntryForm(forms.ModelForm):
    class Meta:
        ...
    def clean_jersey_name(self):
        jersey_name = self.cleaned_data.get("jersey_name")
        # Check if the field is empty
        if not jersey_name:
            raise ValidationError("This field cannot be blank.")
        # Strip HTML tags for XSS protection
        return strip_tags(jersey_name)

    def clean_description(self):
        description = self.cleaned_data.get("description")
        # Check if the field is empty
        if not description:
            raise ValidationError("This field cannot be blank.")
        # Strip HTML tags for XSS protection
        return strip_tags(description)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            raise ValidationError("This field cannot be blank.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            raise ValidationError("This field cannot be blank.")
        return quantity

    def clean_image_url(self):
        image_url = self.cleaned_data.get("image_url")
        if not image_url:
            raise ValidationError("This field cannot be blank.")
        return strip_tags(image_url)
```

5. Melakukan pembersihan data dengan DOMPurify dengan memodifikasi kode pada `main.html`
```html
{% block meta %}
...
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
...
{% endblock meta %}
```
```javascript
...
    async function refreshProductEntries() {
        ...
        moodEntries.forEach((item) => {
            const jersey_name = DOMPurify.sanitize(item.fields.jersey_name);
            const description = DOMPurify.sanitize(item.fields.description);
            const price = DOMPurify.sanitize(item.fields.price);
            const quantity = DOMPurify.sanitize(item.fields.quantity);
            const image_url = DOMPurify.sanitize(item.fields.image_url);
    });
        ...
    }
    ...
```
