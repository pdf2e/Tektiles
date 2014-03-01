from django.template import RequestContext
from django.shortcuts import render_to_response


def webstoreView(request):
    return render_to_response('webstore.html')
