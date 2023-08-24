from administrator.models import Employee


def employee_name(request):
    admin_id = request.session.get('employee_sessionID')
    if admin_id is not None:
        employee = Employee.objects.get(id=admin_id)
        return {'employee_name': employee.second_name}
    else:
        return {'employee_name': None}  # default value if no customer is found

