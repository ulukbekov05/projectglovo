from drf_yasg.openapi import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *
from rest_framework import viewsets, generics, permissions, status
from django_filters .rest_framework import DjangoFilterBackend
from rest_framework .filters import OrderingFilter, SearchFilter
from .paginations import StorePagination

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class StoreAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['store_name']
    search_fields = ['category']
    pagination_class = StorePagination


class StoreWideAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreWideSerializer



class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategorysWideAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWideSerializer






class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers


class ComboCreateAPIView(generics.CreateAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboCreateSerializer


class ComboListAPIView(generics.ListAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboListSerializer


class ComboDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboDeleteSerializer



class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CourierAPIView(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class CourierRatingAPIView(generics.CreateAPIView):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializer


class StoreDataiAPIView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDataiSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductWideAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWideSerializer


class StoreReviewCreateAPIView(generics.CreateAPIView):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewCreateSerializers


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

