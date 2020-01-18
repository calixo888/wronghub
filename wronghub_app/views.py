from django.shortcuts import render
from django.http import HttpResponseRedirect

answers = ["George Washington is the 1st president of the United States",
           "69",
           "321 Students",
           "5",
           "f(x) = e^x",
           "Scout Finch lives with her brother, Jem, and their widowed father, Atticus, in the sleepy Alabama town of Maycomb. Maycomb is suffering through the Great Depression, but Atticus is a prominent lawyer and the Finch family is reasonably well off in comparison to the rest of society.",
           "The mitochondria is the powerhouse of the cell",
           "Tu eres muy tonto",
           "Kc = 1.692420 E -6",
           "Abraham Lincoln",
           "420",
           "I don't know bruh"]

def index(request):
    return render(request, "wronghub_app/index.html")


def ask(request):
    if request.method == "GET":
        question = request.GET.get("q")
        answer = question
        return render(request, "wronghub_app/ask.html", context={
            "answer": answer[random.randint(0, len(answers))]
        })

    if request.method == "POST":
        question = request.POST.get("question")

        joined_question = "+".join(question.split())

        return HttpResponseRedirect("/ask/?q=" + joined_question)

    return render(request, "wronghub_app/ask.html")
