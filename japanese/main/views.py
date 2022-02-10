from django.shortcuts import render

# Create your views here.
def main_menu(req):
    slovo = [x for x in range(1,5)]
    digit = [y for y in range(5,1,-1)]

    tmp = list(zip(slovo , digit))
    print(tmp)
    firs = [1,2,3]
    contex = {'first':firs,'tmp':tmp}

    return render(req,'index.html',contex)