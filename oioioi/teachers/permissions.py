import oioioi.base.utils.permissions

from oioioi.base.utils.permissions import (is_regular_user as old_is_regular_user,
                                           can_create_contest as old_can_create_contest)

oioioi.base.utils.permissions.is_regular_user = \
    lambda user: old_is_regular_user(user) and not user.has_perm('teachers.teacher')

oioioi.base.utils.permissions.can_create_contest = \
    lambda user: old_can_create_contest(user) or user.has_perm('teachers.teacher')

