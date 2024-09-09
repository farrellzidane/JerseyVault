# JerseyVault

LINK PWS : 
 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

+----------------+        +------------+       +-------------+       +------------+      +----------------+
|     Client     |------->|  urls.py   |------>|   views.py  |------>|  models.py |----->|    Template    |
|    (Browser)   |        | (Routing)  |       |   (Logic)   |       | (Database) |      |     (HTML)     |
| (HTTP Request) |        |            |       |             |       |            |      |   (Response)   |
+----------------+        +------------+       +-------------+       +------------+      +----------------+

- Client (browser) : mulainya proses saat client (user) mengirimkan permintaan HTTP ke aplikasi Django, misalnya untuk mengakses halaman tertentu seperti /products/

- urls.py (Routing) : Django menerima request dan urls.py bertugas untuk mencocokkan URL request dengan pola yang ada. Jika cocok, maka Django akan mengarahkan request ke views.py yang sesuai

- views.py (Logic) : setelah diarahkan ke views.py, Django menjalankan fungsi view atau class-based view terkait. fungsi di dalam views.py biasanya berisi logic yang mengatur bagaimana data diambil dan dikirimkan ke template HTML dan bisa berinteraksi dengan models.py

- models.py (Database) : models.py ini berisi struktur data yang digunakan untuk berinteraksi dengan database

- Template (HTML) : Setelah data diperoleh dari models.py, view akan me-render template HTML dan mengirimkan data tersebut ke template yang akan ditampilkan di halaman web.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi Git :
Git adalah salah satu alat terpenting dalam pengembangan perangkat lunak saat ini. Secara sederhana, Git membantu kita mengelola perubahan yang terjadi pada kode, terutama ketika bekerja dalam tim.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan pilihan untuk pembelajaran pengembangan perangkat lunak karena:

- Batteries Included yaitu banyak fitur bawaan seperti autentikasi, admin panel, dan ORM, memudahkan pengembangan tanpa alat tambahan.

- Full-Stack yaitu menangani backend hingga frontend, sehingga pemula memahami alur lengkap pengembangan web.
- Struktur Terorganisir (MTV) yaitu Arsitektur Model-Template-View memisahkan data, logika bisnis, dan tampilan dengan jelas.
- Dokumentasi Baik yaitu Dokumentasi lengkap dan mudah dipahami memudahkan pemula belajar.
- Komunitas Besar yaitu Banyak tutorial dan dukungan komunitas membantu pemecahan masalah.
- Keamanan Bawaan yaitu Django secara otomatis menangani keamanan dasar seperti SQL injection dan CSRF.
- Skalabilitas yaitu Cocok untuk proyek kecil hingga besar, memungkinkan pemula tetap menggunakannya saat lebih berpengalaman.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena memungkinkan pengembang bekerja dengan database menggunakan objek Python, tanpa harus menulis SQL. Django memetakan objek Python ke tabel di database secara otomatis. ORM menyederhanakan operasi database seperti `SELECT`, `INSERT`, dan `UPDATE`, serta menyediakan keamanan dari SQL injection. Dengan ORM, pengelolaan data menjadi lebih mudah, abstraksi SQL terjamin, dan mendukung berbagai jenis database tanpa mengubah kode.