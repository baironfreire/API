from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets, status

from .models import Product, Category, SubCategory
from .serializer import ProductSerializer, CategorySerializer, SubCategorySerializer, UserSerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

#usar apiview cuando desees personalizar por completo el proceso
# class ProductList(APIView):
#     def get(self, request):
#         prod = Product.objects.all()[:20]
#         data = ProductSerializer(prod, many=True).data
#         return Response(data)

# class ProductDetail(APIView):
#     def get(self, request, pk):
#         prod = get_object_or_404(Product, pk=pk)
#         data = ProductSerializer(prod).data
#         return Response(data)

# Create your views here. genericas
#usar generics. cuando solo permitas realizar algunas operaciones en el modelo
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategorySave(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategorySave(generics.CreateAPIView):
    serializer_class = SubCategorySerializer

class SubCategoryList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategory.objects.filter(category_id = self.kwargs["pk"])
        return queryset
    serializer_class = SubCategorySerializer

# clase nos genera todas las rutas POST, GET, PUT, DELETE
#Utiliza esta vista cuando se permita realizar el crud en el modelo
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ([IsAuthenticated, IsOwner])


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user :
            return Response({"token": user.auth_token.key })
        else:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)