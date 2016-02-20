from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Board


class SingleBoard(View):

    def get(self, request, slug):
        board = get_object_or_404(Board, slug=slug)
        context = {
            'board': board,
        }
        return render(
            request,
            'board/single_board.html',
            context,
        )
