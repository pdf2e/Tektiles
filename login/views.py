from django.template import RequestContext
from django.shortcuts import render_to_response
from login.forms import PersonForm


def add_user(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = PersonForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # the user to the database
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return registration(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PersonForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('login/../templates/registration.html', {'form': form}, context)


def registration(request):
    return render_to_response('registration.html')