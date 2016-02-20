from django.shortcuts import render
from django.views.generic import ListView

from board.models import Board


class IndexView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'index/index.html'
