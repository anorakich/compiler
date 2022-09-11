from django.shortcuts import render
import os

def index(request):
    context = {}
    if request.method == "POST":
        file = open("code_file.cpp", "w")
        code = request.POST["code"]
        for i in range(int(request.POST["keywords_counter"])):
            code = code.replace(request.POST["keyword_value" + str(i + 1)], request.POST["keyword" + str(i + 1)])
        file.write(code)
        file.close()
        execute_code = "g++ code_file.cpp; ./a.out > answer.txt"
        os.system(execute_code)
        file = open("answer.txt", 'r')
        answer = file.read()
        context["answer"] = answer

    return render(request, "compiler_app/index.html", context=context)
