from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)