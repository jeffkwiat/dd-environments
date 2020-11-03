import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.info("Processing GET /api")
    return HttpResponse("Hello, world. You're at the polls index.")

def warning(request):
    logger.warning("Processing GET /api/warning")
    return HttpResponseNotFound('<h1>Page not found</h1>')
