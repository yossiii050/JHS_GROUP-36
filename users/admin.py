from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Candidate , CVFormModel,User,UserProfile,CandidateProfile,MyUser
from .forms import CreateEmployerForm,CreateCandidateForm
# django.contrib.auth.models import User 
admin.site.register(MyUser)
admin.site.register(CVFormModel)
admin.site.register(User)


admin.site.register(UserProfile)
admin.site.register(CandidateProfile)


class ProfileInline1(admin.StackedInline):
    model = UserProfile
    can_delete = False
class ProfileInline2(admin.StackedInline):
    model = UserProfile
    can_delete = False
class UserAdmin(UserAdmin):
    inlines = (ProfileInline1,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

