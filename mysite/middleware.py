from datetime import datetime
from django.http import HttpResponseRedirect


class SessionExpiredMiddleware:
    def process_request(request):
        last_activity = request.session['last_activity']
        now = datetime.datetime.now()

        if (now - last_activity).minutes > 10:
            # Do logout / expire session
            # and then...
            return HttpResponseRedirect('/accounts/login')

        if not request.is_ajax():
            # don't set this for ajax requests or else your
            # expired session checks will keep the session from
            # expiring :)
            request.session['last_activity'] = now    