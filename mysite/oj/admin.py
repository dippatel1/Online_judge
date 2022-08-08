from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question,user_score,TestCases,submissions1

admin.site.register(Question)
admin.site.register(user_score)
admin.site.register(TestCases)

admin.site.register(submissions1)