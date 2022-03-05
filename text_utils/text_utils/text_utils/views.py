# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

"""My navigator site code
def index(request):
    return HttpResponse("Hello Guys welcome to my webpage")

def about(request):
    return HttpResponse("Hello Guy its ankit.")

def site1(request):
    return HttpResponse('''<h1>Ankit</h1> <a href="https://leetcode.com/problemset/all/"> Leetcode</a><br>
    <a href="https://www.youtube.com/"> Youtube</a><br>
    <a href="https://www.hackerrank.com/dashboard"> Hackerrank</a><br>
    <a href="https://www.geeksforgeeks.org/"> Geeks for geeks</a>''')


"""


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')  # taking input text


    # check which checkbox is checked
    removepunc = request.POST.get('removepunc', "off")
    uppercase = request.POST.get('uppercase', "off")
    newlineremover = request.POST.get('newlineremover', "off")
    charcount = request.POST.get('charcount', "off")

    if removepunc == "on":
        punctuation = '''\./?{}[]()+,-*&^%$#@""!=<>:'';'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalizing', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        count = ''
        for char in djtext:
            count = len(djtext)
        char_count = {'purpose': 'No. of characters', 'analyzed_text': count}
        return render(request, 'analyze.html', char_count)

        # return render(request, 'analyze.html', params)

    if removepunc != "on" and uppercase != 'on' and newlineremover != "on" and charcount != "on":
        return HttpResponse("Error.Choose atleast one option")

    return render(request, 'analyze.html', params)


'''
def capitalizefirst(request):
    return HttpResponse("Capitalize first letter <a href='/'> Back</a>")

def newlineremove(request):
    return HttpResponse("New line remove <a href='/'> Back</a>")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'> Back</a>")

def charcount(request):
    return HttpResponse("char count <a href='/'> Back</a>")'''
