from django.contrib import admin

from KFLProduct.models import UserProfile, DVDProduct, downloadProduct, Language, ProductBundle, ProductCategory



class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)


class DVDProductAdmin(admin.ModelAdmin):
	list_display = ('name',
					'title_CN',)
	filter_horizontal = ('online_download',)
admin.site.register(DVDProduct, DVDProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ('name_en',)
					
admin.site.register(ProductCategory, ProductCategoryAdmin)



class downloadProductAdmin(admin.ModelAdmin):
	list_display = ('name',
					'section_no',)
admin.site.register(downloadProduct, downloadProductAdmin)


class LanguageAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Language, LanguageAdmin)	


class ProductBundleAdmin(admin.ModelAdmin):
	list_display = ('title_EN',)
admin.site.register(ProductBundle, ProductBundleAdmin)	