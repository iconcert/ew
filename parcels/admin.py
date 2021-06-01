from django.contrib import admin
from parcels.models import Parcel, Store

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'store', 'tracking_number', 'user_client', 'user_warehouse', 'status')
    list_display_links = ('name',)
    list_editable = ('status',)
    #list_filter = ('status', 'created', 'publish', 'author')
    #search_fields = ('title', 'comment')
    #prepopulated_fields = {'slug': ('name',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ('status', 'publish')


admin.site.register(Store)