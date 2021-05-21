from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserEditForm
from .models import CustomUser, Profile, ContactPhone

User = get_user_model()

admin.site.register(ContactPhone)


class ProfileInlines(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ['image', 'logo', 'brand', 'city',
              'address', 'subscribed_to']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserEditForm
    model = CustomUser
    list_display = ('email', 'first_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email',
                           'first_name',
                           'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'password1',
                       'password2',
                       'is_staff',
                       'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = [ProfileInlines, ]
