from django.contrib import admin

from .models import User
from .models import ServiceProvider
from .models import Event
from .models import Wedding
from .models import Note

# class OwnerInline(admin.StackedInline):
#     model = User
#     extra = 2
#      
# class WeddingAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['name']}),
#         ('Owner information', {'fields': ['owner'], 'classes': ['collapse']}),
#     ]
#     inlines = [OwnerInline]


admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Event)
admin.site.register(Wedding)
admin.site.register(Note)

