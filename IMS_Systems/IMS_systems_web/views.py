from django.shortcuts import render
from .models import Services, Products
from .serializers import ServicesSerializer,ProductsSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import MyTokenObtainPairSerializer
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from IMS_systems_web.serializers import RegisterSerializer, ChangePasswordSerializer,UpdateUserSerializer
from rest_framework.views import APIView



# Create your views here.
def Services_list(request):
    services = Services.objects.all()
    return render(request, 'Services.html', {'Services': services})

# def Products_list(request):
#     products = Products.objects.all()
#     return render(request, 'Services.html', {'Products': products})

class ServicesDetail(generics.ListCreateAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    pagination_class = LimitOffsetPagination

class ServicesList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()

class ProductsDetail(generics.ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    pagination_class = LimitOffsetPagination

class ProductsList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

""" 

Extend user and authontication


 """
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

