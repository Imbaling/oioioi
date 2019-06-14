import oioioi.base.utils.permissions

from oioioi.base.utils.permissions import is_regular_user as old_is_regular_user

oioioi.base.utils.permissions.is_regular_user = \
    lambda user: old_is_regular_user(user) and not user.has_perm('teachers.teacher')
