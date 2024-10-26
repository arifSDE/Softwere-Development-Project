from django.http import HttpResponse
def home(request):
    return HttpResponse("This is home page")
def contact(request):
    return HttpResponse("This is Contact Page")
def goribs(request):
    return HttpResponse("আপাদত গরিবস আচি")

def Thanda(request):
    return HttpResponse("গরমের দিনে থান্ডা দরকার")

def Gorom(request):
    return HttpResponse("এখন শিতকাল গরম দরকার")

def OdaBaloija(request):
    return HttpResponse("কিচু কমু না Somoy Thaikte Baloija")