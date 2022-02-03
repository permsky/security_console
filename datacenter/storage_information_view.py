from datacenter.models import Visit
from django.shortcuts import render

from passcard_info_view import format_duration


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = list()
    for visit in current_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': (format_duration(visit.get_duration())),
                'is_strange': visit.is_long()
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
