from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
def makeNameAdmin(request, MyUserAdmin , queryset):
    queryset.update(first_name = "بدون نام")

class MyUserAdmin(UserAdmin):  
    list_display = ('email','username','last_login_date','signing_date','is_admin','is_staff','first_name','last_name')
    search_fields = ("email","username",)
    readonly_fields = ("signing_date",'last_login_date')
    fieldsets = (
        (None, {
            "fields": (
                'email','username','is_admin','is_staff',('first_name','last_name')
            ),
        }),
        ('Advanced options' ,{
            'classes': ('last_login','signing_date'),
            'fields': ('is_active', 'is_superuser'),
        })
    )
    actions=[makeNameAdmin]

admin.site.add_action(makeNameAdmin, name="تغییر نام")
admin.site.register(MyUser,MyUserAdmin)