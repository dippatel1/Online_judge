from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Submissions,user_score,TestCases

admin.site.register(Question)
admin.site.register(user_score)
admin.site.register(TestCases)
admin.site.register(Submissions)