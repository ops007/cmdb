def check_auth(request, data):
    if request.user.is_superuser or request.session["fun_auth"].get(data, False):
        return True
    else:
        return False
