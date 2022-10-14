from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Add the la class & list and view function below the imports
class La:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, location, description, rating):
    self.name = name
    self.location = location
    self.description = description
    self.rating = rating

las = [
  La('Runyon Canyon', 'HollyWood Hills', 'Beautful views', 10),
  La('Culver City Steps', '360 view of LA', '5 min drive to the beach', 0),
  La('Hollywood Hills Homes', 'Beautiful homes', 'Amazing Views', 4)
]



def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')


def las_index(request):
    return render(request, 'las/index.html', {'las': las}) 