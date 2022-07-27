from django.contrib import admin
from TeachApp.models import alwin,Cobra,signup,score
from .models import Image,master
# Register your models here.

admin.site.register(Cobra)
admin.site.register(signup)
admin.site.register(Image)
admin.site.register(master)
admin.site.register(score)