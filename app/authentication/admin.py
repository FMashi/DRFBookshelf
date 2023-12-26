from django.contrib import admin
from .models import CustomUser,Profile

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)
    


admin.site.register(Profile)
admin.site.register(CustomUser,CustomerAdmin)