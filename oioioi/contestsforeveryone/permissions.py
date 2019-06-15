from django.conf import settings

import oioioi.base.utils.permissions

oioioi.base.utils.permissions.can_create_contest = \
    lambda user: not settings.ARCHIVE_CONTESTS_FOR_REGULAR_USERS
