from .models import Product, Category, Store
from modeltranslation.translator import TranslationOptions,register

@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('address', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description', 'product_name')

