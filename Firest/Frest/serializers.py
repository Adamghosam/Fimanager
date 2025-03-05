from rest_framework import serializers
from .models import User, Paket, Langganan

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nama', 'alamat', 'kontak', 'email', 'role', 'password']

    def create(self, validated_data):
        # Buat ID pelanggan sesuai format U-tahun-noid
        #last_user = User.objects.filter(role='pelanggan').order_by('-id').first()
        last_user = User.objects.filter(role='pelanggan').order_by('-id_user').first()

        last_id = int(last_user.id_user.split('-')[-1]) + 1 if last_user else 1
        tahun = "2025"  # Bisa pakai datetime.now().year
        id_user = f"U-{tahun}-{last_id:04d}"

        # Simpan user dengan ID baru
        user = User.objects.create(id_user=id_user, **validated_data)
        return user




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Menampilkan semua field

class PaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paket
        fields = '__all__'

class LanggananSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    paket = PaketSerializer(read_only=True)

    class Meta:
        model = Langganan
        fields = '__all__'




