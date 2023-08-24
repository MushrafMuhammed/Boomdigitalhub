from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


# def auth_customer(func) :
#       def wrapper (request, *args, **kwargs):
#              if 'customer_sessionId' in request.session:
               
#                return func (request, *args, **kwargs)
#              else:
#                 return redirect('common:common')   
#       return wrapper


# without argument 
def auth_customer(func) :
      def wrapper (request):
             if 'customer_sessionId' in request.session:
               
               return func (request)
             else:
                return redirect('customer:login')   
      return wrapper