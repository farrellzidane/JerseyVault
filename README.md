# JerseyVault

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Farrell Zidane Raihandrawan (2306275600)

LINK PWS : https://farrell-zidane31-jerseyvault1.pbp.cs.ui.ac.id/
 

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