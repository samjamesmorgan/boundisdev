from django.contrib import admin
from .models import sport
# Register your models here.

class sportAdmin(admin.ModelAdmin):
	class Meta:
		model = sport

admin.site.register(sport, sportAdmin)