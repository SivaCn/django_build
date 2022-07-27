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
from django.urls import path
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.views import test
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]

urlpatterns = [
    path('test/', test),
]
