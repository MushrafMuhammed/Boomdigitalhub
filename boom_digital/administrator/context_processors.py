from django.shortcuts import render
from administrator.models import Admin_users


def admin_name(request):
    admin_id = request.session.get('admin_sessionID')
    if admin_id is not None:
        admin = Admin_users.objects.get(id=admin_id)
        return {'admin_name': admin.username}
    else:
        return {'admin_name': None}  # default value if no customer is found

