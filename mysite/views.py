from django.shortcuts import render

def primera(request):
  return render(request, 'primera.html')

def segunda(request):
  return render(request, 'segunda.html')

def tercera(request):
  return render(request, 'tercera.html')

def cuarta(request):
  return render(request, "cuarta.html")