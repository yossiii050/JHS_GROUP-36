from django.contrib import admin
from .models import Candidate , CVForm
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib.auth.models import User 
admin.site.register(Candidate)
admin.site.register(CVForm)
#admin.site.register(CreateCandidateForm)

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Get the content type for the User model
content_type = ContentType.objects.get(app_label='auth', model='user')
# Get the permission object
permission = Permission.objects.create(
    codename='can_update_user_status',
    name='Can update user status',
    content_type=content_type
)

# Get the admin user
admin_user = User.objects.get(is_staff=True)

# Add the permission to the user
admin_user.user_permissions.add(permission)