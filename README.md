# JerseyVault

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Farrell Zidane Raihandrawan (2306275600)

LINK PWS : https://farrell-zidane31-jerseyvault1.pbp.cs.ui.ac.id/
 

## TUGAS 1
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

## TUGAS 2

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan bagian yang penting karena menjadi penghubung/jembatan bagi aliran informasi antara hardware, device, dan user. Data delivery yang efisien memastikan bahwa informasi yang dibutuhkan selalu tersedia secara real-time

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik dibanding XML karena JSON memiliki 
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

8. 


