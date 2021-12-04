from django.contrib import admin
#username = readit_team
#Email address: readit_team@gmail.com
#password = readit_team
# Register your models here.
from .models import User,Question,Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)