from django.contrib import admin
#username = readit_name
#Email address: readit_team@gmail.com
#password = readit_name
# Register your models here.
from .models import User,Question,Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)