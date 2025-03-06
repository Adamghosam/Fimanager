from rest_framework import serializers  # type: ignore
from .models import User, Paket, Langganan

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nama', 'alamat', 'kontak', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Menyembunyikan password dari respons

    def create(self, validated_data):
        # Ambil user terakhir dengan role 'pelanggan'
        last_user = User.objects.filter(role='pelanggan').order_by('-id_user').first()

        # Tentukan ID user baru dengan format U-tahun-noid
        last_id = int(last_user.id_user.split('-')[-1]) + 1 if last_user else 1
        tahun = "2025"  # Bisa pakai datetime.now().year untuk dinamis
        id_user = f"U-{tahun}-{last_id:04d}"

        # Simpan user dengan ID baru
        user = User.objects.create(id_user=id_user, **validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Sembunyikan password di respons

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
