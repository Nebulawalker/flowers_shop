from django.contrib import admin
from .models import Bouquet, Tag, Order, Consultation

class BouquetInline(admin.TabularInline):
    model = Bouquet.tags.through
    extra = 0

@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'price']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [BouquetInline, ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    pass
