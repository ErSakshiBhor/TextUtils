# i have created this file...........sakshu
from django.http import HttpResponse
from django.shortcuts import render

#playing the pipeline
def index(request):
    return render(request, 'index.html')                 #request,(second element) template name, (3rd element)dictionary.
    # return HttpResponse( "home ")

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')     #it returns the values how name is text which we have enterd and if not entered then it will take default value
    # check chackbox values 
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    
    print(removepunc) 
    print(djtext) 


# check with checkbox is on
    analyzed = djtext  # Always work on the latest result

    if removepunc == "on":
        punctuations = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
        analyzed = "".join(char for char in analyzed if char not in punctuations)

    if fullcaps == "on":
        analyzed = analyzed.upper()

    if newlineremover == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", "")

    if extraspaceremover == "on":
        new_text = ""
        for index, char in enumerate(analyzed):
            if index == len(analyzed) - 1 or not (analyzed[index] == " " and analyzed[index + 1] == " "):
                new_text += char
        analyzed = new_text

    if charcounter == "on":
        count = len(analyzed)
        analyzed += f"\n\nTotal Characters: {count}"

    if (
        removepunc != "on" and
        fullcaps != "on" and
        newlineremover != "on" and
        extraspaceremover != "on" and
        charcounter != "on"
    ):
        return HttpResponse("Please select at least one operation!")

    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
