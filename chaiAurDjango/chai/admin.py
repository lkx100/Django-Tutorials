from django.contrib import admin
from .models import chaiVariety, chaiReviews, chaiCertificate, Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaiReviews
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chaiType', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variety',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_id', 'issue_date', 'valid_until')

admin.site.register(chaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(chaiCertificate, ChaiCertificateAdmin)