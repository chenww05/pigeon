from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
#from django.urls import reverse
from django.core.urlresolvers import reverse


from .models import Wedding
from .models import Event


def index(request):
    latest_wedding_list = Wedding.objects.order_by('-start_date')[:5]
    context = {
        'latest_wedding_list': latest_wedding_list,
    }
    return render(request, 'planner/index.html', context)

def detail(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)
    return render(request, 'planner/detail.html', {'wedding': wedding})

def results(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)
    return render(request, 'planner/result.html', {'wedding': wedding})

def vote(request, wedding_id):
    wedding = get_object_or_404(Wedding, pk=wedding_id)
    try:
        selected_event = wedding.event_set.get(pk=request.POST['event'])
    except (KeyError, Event.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'planner/detail.html', {
            'wedding': wedding,
            'error_message': "You didn't select an event.",
        })
    else:
        selected_event.budget += 1
        selected_event.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('planner:results', args=(wedding.id,)))