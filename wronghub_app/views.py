from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, "wronghub_app/index.html")


def ask(request):
    if request.GET.get("q"):
        question = request.GET.get("q")


        response = requests.get("http://jservice.io/api/random")
        json = response.json()

        answer = json[0]["question"]


        return render(request, "wronghub_app/ask.html", context={
            "answer": answer
        })

    if request.method == "POST":
        question = request.POST.get("question")

        joined_question = "+".join(question.split())

        return HttpResponseRedirect("/ask/?q=" + joined_question)

    return render(request, "wronghub_app/ask.html")


def answer(request):
    response = requests.get("https://opentdb.com/api.php?amount=1")
    json = response.json()
    question = json["results"][0]["question"]

    if request.method == "POST":
        return render(request, "wronghub_app/answer.html", context={
            "question": question,
            "answered": True,
        })

    return render(request, "wronghub_app/answer.html", context={
        "question": question,
    })
