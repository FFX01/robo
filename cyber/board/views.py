from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from .models import Board
from thread.models import Thread
from post.models import Post


class SingleBoard(View):

    def get(self, request, slug):

        board = get_object_or_404(Board, slug=slug)

        context = {
            'board': board
        }

        return render(
            request,
            'board/single_board.html',
            context,
        )

    def post(self, request, slug):

        board = get_object_or_404(Board, slug=slug)

        new_thread = Thread(
            title=request.POST['thread_title'],
            board=board
        )

        new_thread.save()

        initial_post = Post(
            image=request.FILES['image'],
            body=request.POST['body'],
            parent_thread=Thread.objects.get(id=new_thread.id)
        )

        initial_post.save()

        return HttpResponseRedirect(
            reverse(
                'thread:single_thread',
                kwargs={
                    'id': Thread.objects.get(id=new_thread.id).id
                }
            )
        )
