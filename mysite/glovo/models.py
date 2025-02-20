from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/')
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(100)
    ], null=True, blank=True)
    STATUS_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
        ('courier', 'courier')
    )
    status = models.CharField(max_length=53, choices=STATUS_CHOICES, default='client')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=54, unique=True)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    store_name = models.CharField(max_length=43)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_store')
    description = models.TextField()
    store_image = models.ImageField(upload_to='stores_image/')
    address = models.CharField(max_length=98)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    def count_people(self):
       ratings = self.store_rating.all()
       if ratings.exists():
           totol = ratings.count()
           if totol > 2:
                 return '2+'
           return totol


           return 0

    def get_good_rating(self):
        ratings = self.store_rating.all()
        if ratings.exists():
            totol = 0
            for i in ratings:
                if i.stars > 3:
                    totol += 1
                return f'{round((totol* 100) / ratings.count())}'





            return '0%'


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=53)
    contact_number = PhoneNumberField(null=True, blank=True)
    social_network = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.contact_number}, {self.title}'


class Product(models.Model):
    product_name = models.CharField(max_length=54)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='stores_name')

    def __str__(self):
        return f'{self.product_name}'


class Combo(models.Model):
    combo_name = models.CharField(max_length=64)
    description = models.TextField()
    combo_image = models.ImageField(upload_to='combos_image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combos_store')

    def __str__(self):
        return self.combo_name


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    ORDER_STATUS_CHOICES = (
        ('Отменен', 'Отменен'),
        ('Доставлен', 'Доставлен'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Ожидает обработки', 'Ожидает обработки')
    )
    order_status = models.CharField(max_length=98, choices=ORDER_STATUS_CHOICES)
    delivery_address = models.CharField(max_length=134)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='couriers_profile')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_status


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    current_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    COURIER_STATUS_CHOICES = (
        ('ДОСТУПЕН', 'ДОСТУПЕН'),
        ('ЗАНЯТ', 'ЗАНЯТ')
    )
    courier_status = models.CharField(max_length=42, choices=COURIER_STATUS_CHOICES)

    def __str__(self):
        return f'{self.courier}, {self.courier_status}'


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, )
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_rating')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.store}'


class CourierRating(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_ratings')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_ratings')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.courier}'












