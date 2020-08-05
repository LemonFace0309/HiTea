from django.contrib import admin
from .models import *

admin.site.site_header = 'Hi Tea Admin Dashboard'


class FoodAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_price')
    list_filter = ('product__price',)

    def get_price(self, obj):
        return obj.product.price

    get_price.admin_order_field = 'product__price'  # Allows column order sorting
    get_price.short_description = 'Product Price'  # Renames column head


# Register your models here.
admin.site.register(Product)
admin.site.register(FreshFruit, FoodAdmin)
admin.site.register(HotMilkTea, FoodAdmin)
admin.site.register(IcedMilkTea, FoodAdmin)
admin.site.register(HotLemonTea, FoodAdmin)
admin.site.register(IcedLemonTea, FoodAdmin)
admin.site.register(HotCheeseFoam, FoodAdmin)
admin.site.register(IcedCheeseFoam, FoodAdmin)
