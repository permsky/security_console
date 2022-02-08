from datacenter.models import Visit
from django.shortcuts import render

from datacenter.passcard_info_view import format_duration


def storage_information_view(request):
    non_closed_visits = list()
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': (format_duration(visit.get_duration())),
                'is_strange': visit.is_long()
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
