from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    purpose = ""
    analyzed = ""
    # params = {'purpose': purpose, 'analyzed_text': analyzed}
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "|Removed Punctuations"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose += "|Capitalized"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "|Removed New lines"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if extraspaceremover == "on":
        analyzed = ""
        for num, char in enumerate(djtext):
            if not (djtext[num] == " " and djtext[num + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "|Removed extra spaces"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if charcount == "on":
        analyzed = ""
        djtext = djtext.replace(" ", "")
        counted_text = "The number of character in your text is " + str(len(djtext))
        purpose += "|Character counted"
        # analyzed = djtext
        params = {'purpose': purpose, 'analyzed_text': djtext, "counted_text": counted_text}


    return render(request, 'analyze.html', params)

# def about(request):
#     return HttpResponse("about harry")
