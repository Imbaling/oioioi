from django.conf import settings
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from oioioi.base.menu import personal_menu_registry
from oioioi.base.utils.permissions import is_regular_user

if 'oioioi.simpleui' not in settings.INSTALLED_APPS:
    personal_menu_registry.register('create_contest', _("New contest"),
        lambda request: reverse('oioioiadmin:contests_contest_add'),
        lambda request: is_regular_user(request.user),
        order=10)
