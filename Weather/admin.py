from django.contrib import admin
from Weather.models import City,UserData

class CityAdmin(admin.ModelAdmin):

    search_fields = ['name']

    list_filter = ['name' ]

    list_display = ['name']

class UserDataAdmin(admin.ModelAdmin):
    search_fields = ['Name','Age','Email','Feedback' , 'Date']

    list_filter = ['Date','Feedback' ]

    list_display = ['Name','Email','Age','Feedback' , 'Date']

admin.site.register(City, CityAdmin)
admin.site.register(UserData,UserDataAdmin)
