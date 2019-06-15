# This functions are located here instead of base/permissions because of import
# problems during initialization of teachers app.
def is_regular_user(user):
    return not user.is_superuser

def can_create_contest(user):
    return user.is_superuser
