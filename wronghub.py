import random

def answer():
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
    return answer[random.randint(0, len(answers))]


