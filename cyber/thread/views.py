from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from .models import Thread
from post.models import Post
from .forms import PostForm


class SingleThread(View):

    def get(self, request, id):
        thread = get_object_or_404(Thread, id=id)
        form = PostForm()
        context = {
            'thread': thread,
            'post_form': form
        }
        return render(
            request,
            'thread/single_thread.html',
            context,
        )

    def post(self, request, id):

        form = PostForm(
            data=request.POST,
            files=request.FILES
        )

        form.save()

        return HttpResponseRedirect('#')
