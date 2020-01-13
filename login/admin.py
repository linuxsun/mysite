from django.contrib import admin
from . import models

class ShowUserInf(admin.ModelAdmin):
    list_display = ('name','email','sex','c_time')

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title','pub_date')


# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ['file_link']


from django.utils.safestring import mark_safe
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image','image_url','image_tag')
    readonly_fields = ('image_data',)
    def image_data(self, obj):
        # return mark_safe(u"<a>路径: %s </a>" % obj.image.url)
        return mark_safe('<img src="{%s}" width="128" height="64" />' % (obj.image.url))
    ##页面显示的字段名称
    image_data.short_description = u'预览'

    # fields = ( 'image_tag', )
    # readonly_fields = ('image_tag',)

    # readonly_fields = [ "image_data"]
    # def image_data(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.image.url,
    #         width=obj.image.width,
    #         height=obj.image.height,
    #     ))


class VideoDetailsInline(admin.TabularInline):
    model = models.VideoDetails

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoDetailsInline]


from .models import Car
from .models import Photos

class PhotoInline(admin.StackedInline):
    model = Photos
    fk_name = "name" # 如果Photos类只有一个ForeignKey,fk_name可以不指定；如果有多个ForeignKey则需要指定fk_name。
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)


# admin.site.register(Images, Model1Admin)
# from rest_framework.authtoken.admin import TokenAdmin
# TokenAdmin.raw_id_fields = ['user']

# Register your models here.
admin.site.register(models.User,ShowUserInf)
admin.site.register(models.ConfirmString)
# admin.site.register(models.Images,ImagesAdmin)
admin.site.register(models.Images,ImagesAdmin)
admin.site.register(models.Video, VideoAdmin)
admin.site.register(Car, CarAdmin)





