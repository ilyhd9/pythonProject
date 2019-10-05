from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """

    return render(request, "index1.html")

    rooms = Room.objects.order_by("title")

    return render(request, "index.html", {
        "rooms": rooms,
    })
