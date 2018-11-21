from django.shortcuts import render

# Create your views here.
def index(request):
    test_variable = 'hello, i am a test variable'
    return render(request, 'basic_app/index.html', {'test_variable':test_variable})

def about(request):
    test_variable = 'hello, i am a test variable for the about page'
    return render(request, 'basic_app/about.html', {'test_variable':test_variable})
