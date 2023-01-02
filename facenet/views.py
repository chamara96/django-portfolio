from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from time import sleep
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

process_image_url = settings.FACENET_BACKEND + settings.FACENET_PROCESS_IMAGE_PATH
train_face_url = settings.FACENET_BACKEND + settings.FACENET_TRAIN_FACE_PATH


def index(request):

    context = {
        "view": "run_model",
        "process_image_url": process_image_url,
        "train_face_url": train_face_url,
    }
    return render(request, "facenet/index.html", context=context)


def train_face(request):

    context = {
        "view": "train_face",
        "process_image_url": process_image_url,
        "train_face_url": train_face_url,
    }
    return render(request, "facenet/index.html", context=context)
