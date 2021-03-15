def is_admin_user(request):
    # Check - requested user is admin user or not. if yes return true else false.
    user_obj = request.user
    print(user_obj.groups.filter(name="Admin").exists())
    if user_obj.groups.filter(name="Admin").exists():
        return True
    return False
