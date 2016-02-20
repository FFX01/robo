from django import template
from django.shortcuts import render

from board.models import Board


register = template.Library()


@register.inclusion_tag('board/tag_board_list.html')
def list_boards():
    boards = Board.objects.all()
    return {'boards': boards}