import logging

from django.contrib import admin
from django.db.models import Count

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from catalog.models import Category, Example, Option, ProductClass, ProductAttributeClass, ProductRecommendation, \
    Product, ProductImage, ProductAttributeValue


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, CategoryAdmin)

admin.site.register(Option)


class ProductRecommendationInline(admin.StackedInline):
    model = ProductRecommendation
    extra = 2
    fk_name = 'primary'


class ProductCategoryInline(admin.StackedInline):
    model = Product.categories.through
    extra = 2


class ProductAttributeValueInLine(admin.TabularInline):
    model = ProductAttributeValue
    extra = 2


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [ProductAttributeValueInLine, ProductImageInline, ProductRecommendationInline]

    prepopulated_fields = {"slug": ("title",)}


class ProductAttributeInLine(admin.TabularInline):
    model = ProductAttributeClass
    extra = 2


class AttributesCountFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attr_count'

    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More Than 5'),
            ('lower_5', 'lower Than 5'),
        ]

    def queryset(self, request, queryset):

        if self.value() == 'more_5':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__gt=2)
        if self.value() == 'lower_5':
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__lte=2)


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'track_stock', 'require_shipping', 'attribute_count')
    list_filter = ('track_stock', 'require_shipping', AttributesCountFilter)

    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductAttributeInLine, ]
    actions = ['enable_track_stock', ]

    def attribute_count(self, obj):
        return obj.attributes.count()

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)

    # def enableTrackStock
