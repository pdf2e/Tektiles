from django.template import RequestContext
from django.shortcuts import render_to_response


def companionView(request):
    return render_to_response('companion.html')
