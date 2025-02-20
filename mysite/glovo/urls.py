from .views import *
from django.urls import path, include
from  rest_framework import routers

router = routers.SimpleRouter()
router.register(r'User', UserProfileView, basename='profile_list')
router.register(r'Cart', CartView, basename='Cart_list')
router.register(r'CartItem', CartItemView, basename='CartItem_list')



urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreWideAPIView.as_view(), name='store-wide'),
    path('category/',  CategoryAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategorysWideAPIView.as_view(), name='category_wide'),
    path('create_store/', StoreDataiAPIView.as_view(), name='creates_stores'),
    path('create_product/', ProductCreateAPIView.as_view(),  name='create_products'),
    path('combo/', ComboCreateAPIView.as_view(), name='combo_create'),
    path('couriers/', CourierRatingAPIView.as_view(), name='courier_rating'),
    path('product/', ProductListAPIView.as_view(),  name='product_list'),
    path('product/<int:pk>/', ProductWideAPIView.as_view(), name='product_delete'),
    path('combos/', ComboListAPIView.as_view(), name='combo_list'),
    path('combos/<int:pk>/', ComboDeleteAPIView.as_view(), name='combo_delete'),
    path('courier/', CourierAPIView.as_view(), name='courier_list'),
    path('order/', OrderAPIView.as_view(), name='order_create'),
    path('contact/', ContactAPIView.as_view(), name='contact_create'),
    path('create_review/', StoreReviewCreateAPIView.as_view(), name='store_review_create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]





