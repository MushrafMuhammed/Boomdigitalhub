from django.shortcuts import redirect



# without argument 
def auth_employee(func) :
      def wrapper (request):
             if 'employee_sessionID' in request.session:
               
               return func (request)
             else:
                return redirect('employee:login')   
      return wrapper