from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Похоже на сайт, вроде работает</h1>' \
           f'<h3>{title}</h3>' \
           f'<p>{text}</p>'

def general(request):
    title = 'Главная '
    body_text = 'Привет, учусь.'
    logger.info(f'Page "general" is open')
    return HttpResponse(text(title, body_text))

def about(request):
    title = 'О себе'
    body_text = 'Пытаюсь научиться Django<br>' \
                'Пока не получается, стараюсь(((<br>' \
                'вот, что получилось...'
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
