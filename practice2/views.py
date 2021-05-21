from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def results(request):
    user_input = request.GET['user_input']
    user_input=user_input.lower()
    return render(request, 'results.html', {'user_input_value': user_input})