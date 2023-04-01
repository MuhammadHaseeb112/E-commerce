from django.contrib import admin
from .models import bikes
from .models import cars
from .models import laptops
from .models import mobiles
from .models import User_info,Rating
from django.utils.timezone import now
# Register your models here.
@admin.register(bikes)
class bikesAdmin(admin.ModelAdmin):
    list_display = ('catagory','name','model','new','city','price','discription','img','username')

@admin.register(cars)
class carsAdmin(admin.ModelAdmin):
    list_display = ('catagory','name','model','new','city','price','discription','img','username')

@admin.register(laptops)
class carsAdmin(admin.ModelAdmin):
    list_display = ('catagory','name','model','new','city','price','discription','img','username')

@admin.register(mobiles)
class carsAdmin(admin.ModelAdmin):
    list_display = ('catagory','name','model','new','city','price','discription','img','username')

@admin.register(User_info)
class carsAdmin(admin.ModelAdmin):
    list_display = ('User_name','user_contact','user_address','user_email')


@admin.register(Rating)
class carsAdmin(admin.ModelAdmin):
    list_display = ('Buyer_name','Product_catagory','product_id','time','rate','comment')
