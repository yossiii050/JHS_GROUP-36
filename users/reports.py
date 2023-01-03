from django.contrib.auth.models import User

def registered_users_report():
    # Get the total number of registered users
    total_users = User.objects.count()

    # Get the number of active users
    active_users = User.objects.filter(is_active=True).count()

    # Get the number of inactive users
    inactive_users = User.objects.filter(is_active=False).count()

    # Generate the report data
    data = {
        'total_users': total_users,
        'active_users': active_users,
        'inactive_users': inactive_users,
    }

    return data