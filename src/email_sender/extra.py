from django.contrib.auth.models import User


def create_user_(request):

    user = User(
        username    = request.POST.get('username'),
        first_name  = request.POST.get('first_name'),
        last_name   = request.POST.get('last_name'),
        email       = request.POST.get('email'),
        password    = request.POST.get('password'),  
    )
        
    user.save()

    pass


# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
