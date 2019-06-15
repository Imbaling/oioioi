from django.utils.translation import ugettext_lazy as _

from oioioi.programs.controllers import ProgrammingContestController


class RegularUserContestController(ProgrammingContestController):
    description = _("Contest for regular user")
