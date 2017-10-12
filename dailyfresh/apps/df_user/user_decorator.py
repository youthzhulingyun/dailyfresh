from django.http import HttpResponseRedirect

def login(func):
    def inner(request,*args,**kwargs):
        if request.session.get("username") != None and request.session.get("username") != "":
            return func(request,*args,**kwargs)
        elif request.get_full_path().startswith("/cart/add/"):
            red = HttpResponseRedirect("/user/login/")
            red.set_cookie('url', "/cart/")
            return red
        else:
            red = HttpResponseRedirect("/user/login/")
            red.set_cookie('url',request.get_full_path())
            return red
    return inner