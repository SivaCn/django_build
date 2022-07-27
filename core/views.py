# -*- coding: utf-8 -*-

"""

    Module :mod:``


    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Namespace Imports ---------- #
# ----------- END: Namespace Imports ---------- #

# ----------- START: Native Imports ---------- #
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
from django.http import HttpResponse
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


def test(request):
    # fetch date and time
    # convert to string
    html = "Test is Successful"
    # return response
    return HttpResponse(html)
