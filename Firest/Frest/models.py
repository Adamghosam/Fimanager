from django.db import models
from django.utils.timezone import now
import uuid

# Fungsi untuk generate ID pelanggan/admin/teknisi
def generate_user_id(role):
    year = now().year
    unique_id = str(uuid.uuid4().int)[:4]  # Menggunakan 4 digit unik
    prefix = {'pelanggan': 'U', 'admin': 'A', 'teknisi': 'T'}.get(role, 'U')
    return f"{prefix}-{year}-{unique_id}"

# Model User
class User(models.Model):
    ROLE_CHOICES = [
        ('pelanggan', 'Pelanggan'),
        ('admin', 'Admin'),
        ('teknisi', 'Teknisi'),
    ]

    id_user = models.CharField(max_length=20, primary_key=True, editable=False)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    kontak = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='pelanggan')
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.id_user:
            self.id_user = generate_user_id(self.role)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama} ({self.role})"

# Model Paket Internet
class Paket(models.Model):
    nama_paket = models.CharField(max_length=20, unique=True)
    kecepatan = models.CharField(max_length=10)  # Contoh: "3 Mbps"
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nama_paket} - {self.kecepatan} - Rp {self.harga}"

# Model Langganan Pelanggan
class Langganan(models.Model):
    STATUS_CHOICES = [
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'pelanggan'})
    paket = models.ForeignKey(Paket, on_delete=models.CASCADE)
    tanggal_mulai = models.DateField(default=now)
    tanggal_berakhir = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aktif')

    def __str__(self):
        return f"{self.user.nama} - {self.paket.nama_paket} ({self.status})"
