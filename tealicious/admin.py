from django.contrib import admin

from .models import categories,AddItem,Event,Franchise

class addmenuitems(admin.ModelAdmin):
    list_display=('title','category','updated_on','created_at')


class addevent(admin.ModelAdmin):
    list_display=('Fullname','email','number','venue','Date')


class addFranchise(admin.ModelAdmin):
    list_display=('Fullname','email','number','Location','created_at')


admin.site.register(categories)
admin.site.register(AddItem,addmenuitems)
admin.site.register(Event,addevent)
admin.site.register(Franchise,addFranchise)



# Register your models here.
