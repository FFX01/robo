from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .models import Thread
from post.models import Post


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

    def post(self, request):
        # TODO: Save new Post
        # TODO: Create Post model form.
        print(request.FILES)
        return HttpResponse('Thanks')
