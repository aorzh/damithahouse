from django.shortcuts import render
from room.models import Room, RoomImage
from house.models import House, HouseImage
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    context_dict = {}
    items = Room.objects.all()
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict['items'] = items
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    if items.count() != 0:
        return render_to_response('index.html', context_dict, context)
    else:
        return render_to_response('nothing.html', context_dict, context)


def single_room(request, item_id):
    context_dict = {}
    context = RequestContext(request)
    item = Room.objects.get(pk=item_id)
    context_dict['item'] = item

    return render_to_response('room/single_room.html', context_dict, context)

