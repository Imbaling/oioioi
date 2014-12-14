from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from oioioi.base.utils.user_selection import UserSelectionField


class FilterUsersInRankingForm(forms.Form):
    user = UserSelectionField(label=_("Username"), required=False)

    def __init__(self, request, *args, **kwargs):
        super(FilterUsersInRankingForm, self).__init__(*args, **kwargs)
        self.fields['user'].hints_url = reverse('get_users_in_ranking',
            kwargs={'contest_id': request.contest.id})
        self.fields['user'].widget.attrs['placeholder'] = \
                _('Search for user...')
