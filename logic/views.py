from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from . import models

def index(request):
    context = {'trailer_list': models.Trailer.objects.all()}
    return render(request, 'index.html', context)

def action_list(request, trailer_id):
    context = {'trailer': get_object_or_404(models.Trailer, id=trailer_id),'action_list': models.Action.objects.filter(trailer_id=trailer_id)}
    return render(request, 'actions.html', context)

def action(request, trailer_id, action_id):
    context = {'action': get_object_or_404(models.Action, id=action_id)}
    return render(request, 'action.html', context)

def create_action(request):
    if request.method == 'POST':

        try:
            trailer = models.Trailer.objects.get(id=request.POST['id'])
        except models.Trailer.DoesNotExist:
            return render(request, 'trailer_not_exist.html')
        
        if request.POST['delivery_date'] == '':
            delivery_date = None
        else:
            delivery_date = request.POST['delivery_date']

        action = models.Action(
            trailer_id = models.Trailer.objects.get(id=request.POST['id']),
            summary = request.POST['summary'],
            is_component_detached = 'detached' in request.POST,
            is_component_delivered = request.POST.get('delivered') == 'true',
            is_component_correct_amount = request.POST.get('correct_amount') == 'true',
            who_contacted = request.POST['who_contacted'],
            result_contact = request.POST['result_contact'],
            expected_delivery_date = delivery_date,
            location_component = request.POST['location'],
            description_of_action = request.POST['description'],
            reason_action = request.POST['reason'],
            name_creator_action = request.POST['creator'],
            extra_info_action = request.POST['info'],
        )

        action.save()

        return HttpResponseRedirect('/')

    return render(request, 'create_action.html')

def create_trailer(request):
    if request.method == 'POST':
        trailer = models.Trailer(id=request.POST['id'], description=request.POST['description'])

        trailer.save()
        
        return HttpResponseRedirect('/')

    return render(request, 'create_trailer.html')