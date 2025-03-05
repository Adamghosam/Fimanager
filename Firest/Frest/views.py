from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import User, Paket, Langganan
from .serializers import UserSerializer, PaketSerializer, LanggananSerializer


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])  # Tanpa autentikasi saat register
def register_user(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User berhasil terdaftar", "id_user": user.id_user}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PaketViewSet(viewsets.ModelViewSet):
    queryset = Paket.objects.all()
    serializer_class = PaketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LanggananViewSet(viewsets.ModelViewSet):
    queryset = Langganan.objects.all()
    serializer_class = LanggananSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
