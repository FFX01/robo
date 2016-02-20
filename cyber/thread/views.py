from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Thread


class SingleThread(View):

    def get(self, request, id):
        thread = get_object_or_404(Thread, id=id)
        context = {
            'thread': thread,
        }
        return render(
            request,
            'thread/single_thread.html',
            context,
        )
