from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'product_image', 'price']


class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'description', 'combo_image', 'price', 'store']


class StoreSerializer(serializers.ModelSerializer):
    count_people = serializers.SerializerMethodField()
    get_good_rating = serializers.SerializerMethodField()
    class Meta:
        model = Store
        fields = ['id','store_name', 'category', 'store_image', 'count_people', 'get_good_rating']

    def count_people(self,obj):
        return obj.count_people()

    def get_good_rating(self,obj):
        return obj.get_good_rating()

class StoreReviewSerializer(serializers.ModelSerializer):
    client =UserProfileStoreSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y'))

    class Meta:
        model = StoreReview
        fields = ['client', 'store', 'text', 'stars', 'created_date']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']





class StoreWideSerializer(serializers.ModelSerializer):
    owner =UserProfileStoreSerializer()
    stores_name = ProductSerializer(many=True)
    combos_store = ComboSerializer(many=True)
    store_rating = StoreReviewSerializer(many=True, read_only=True)
    category = CategoryListSerializer()
    class Meta:
        model = Store
        fields = ['owner','address', 'store_name', 'category',
                  'store_image','stores_name', 'combos_store', 'store_rating', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']



class CategoryWideSerializer(serializers.ModelSerializer):
    category_store =StoreSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_store']

class StoreDataiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ComboCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name',  'product_image', 'price' ]


class ProductWideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'product_image', 'price']





class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class CourierRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierRating
        fields = '__all__'



class ComboListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'description', 'combo_image', 'price', 'store']



class ComboDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'



class StoreReviewCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'





