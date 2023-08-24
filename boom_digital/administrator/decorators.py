from django.shortcuts import redirect

# without argument 
def auth_admin(func) :
      def wrapper (request):
             if 'admin_sessionID' in request.session:
               
               return func (request)
             else:
                return redirect('admin:login')   
      return wrapper