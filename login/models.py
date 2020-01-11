from django.db import models
# from rest_framework.authtoken.models import Token


# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)
    # token = models.CharField(max_length=128)
    # token = models.OneToOneField('Token',max_length=128,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# class Article(models.Model):
#     title = models.CharField(u'标题', max_length=256)
#     content = models.TextField(u'备注')
#     ph = models.ImageField(u'图片',upload_to=settings.STATICFILES_DIRS[0])
#     # ph = models.ImageField(u'图片',upload_to='static/login/image/%Y/%m/%d')
#     pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
#     update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)


# class Images(models.Model):
#     image = models.ImageField(upload_to="static/",default='null.jpg')
#
#     def file_link(self):
#         if self.image:
#             return u"%s" % (self.image.url,)
#         else:
#             return "No attachment"
#
#     file_link.allow_tags = True


# from django.utils.html import format_html
from django.utils.html import mark_safe
class Images(models.Model):
    image = models.ImageField(upload_to='',default='null.jpg')
    image_url = models.CharField(verbose_name='别名',max_length=100)

    # def image_data(self):
    #     # pass
    #     return format_html(
    #         '<img src="{}" width="100px"/>', self.image_url,
    #     )
    # image_data.short_description = u'图片'

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" width="128" height="64" />' % (self.image))
    image_tag.short_description = '预览'

    class Meta:
        ordering = ["-image"]
        verbose_name = "图像管理"
        verbose_name_plural = "图像管理"



from django.conf import settings


class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    details = models.TextField()

    class Meta:
        verbose_name = '资产添加(带图片附件形式)'
        verbose_name_plural = "资产添加(带图片附件形式)"


class VideoDetails(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videos')
    images = models.ImageField(upload_to='images/%Y/%m/%d')

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.images.url)



import os
def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename) # 系统路径分隔符差异，增强代码重用性

class Photo(models.Model):
    # upload_to 参数接收一个回调函数 user_directory_path，
    # 该函数返回具体的路径字符串，图片会自动上传到指定路径下，即 MEDIA_ROOT + upload_to .
    # user_directory_path 函数必须接收 instace 和 filename 两个参数,
    # 参数 instace 代表一个定义了 ImageField 的模型的实例，说白了就是当前数据记录；filename 是原本的文件名
    # null 是针对数据库而言，如果 null = True, 表示数据库的该字段可以为空；blank 是针对表单的，如果 blank = True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    photo = models.ImageField('照片', upload_to = user_directory_path, blank = True, null = True)

    # 这里定义一个方法，作用是当用户注册时没有上传照片，模板中调用 [ModelName].[ImageFieldName].url 时赋予一个默认路径
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/media/null.jpg'


class Car(models.Model):
    title = models.CharField(max_length=128,verbose_name=u'标题')


class Photos(models.Model):
    # title = models.CharField(max_length=128,default='',verbose_name=u'标题')
    name =  models.ForeignKey(Car,on_delete=models.CASCADE,max_length=1024,related_name=u'备注')
    images = models.ImageField(upload_to='images/%Y/%m/%d/',verbose_name=u'图片')




