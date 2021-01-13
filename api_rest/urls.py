from django.urls import path
from .views import ProductDetail, ProductList, CategorySave, SubCategorySave, CategoryDetail, SubCategoryList, CategoryList, ProductViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

router.register('v2/products', ProductViewSet, base_name='productos')
router.register('v3/login', ProductViewSet, base_name='login')

urlpatterns = [
    path('v1/products/', ProductList.as_view(), name='list_products'),
    path('v1/products/<int:pk>', ProductDetail.as_view(), name='detail_product'),
    # path('v1/category/', CategorySave.as_view(), name='category_save'),
    path('v1/category/', CategoryList.as_view(), name='category_list'),
    path('v1/category/<int:pk>', CategoryDetail.as_view(), name='category'),
    path('v1/category/<int:pk>/sub-category/', SubCategoryList.as_view(),name='sub_category_list' ),
    path('v1/sub-category/', SubCategorySave.as_view(), name='sub_category_save'),
    path('v3/users/', UserCreate.as_view(), name='user_create'),
    path("v4/login/", LoginView.as_view(), name="login"),
    path("v4/login-drf/", views.obtain_auth_token, name="login_drf"),
    path("coreapi-docs/", include_docs_urls(title="Documentación COREAPI"))
]
urlpatterns += router.urls