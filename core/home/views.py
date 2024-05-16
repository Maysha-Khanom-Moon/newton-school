from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# one way
# def home(request):
#     return HttpResponse("""
#     <h1>Hey I am a Django Server.</h1>
#     <p>Hey this is coming from Django server</p>
#     <hr>
#     <h3 style="color:red;">Hope you are loving it :)</h3>
# """)


# efficient way
def home(request):
    
    peoples = [
        {'name': 'Abhijeet Gupta', 'age': 26},
        {'name': 'Rohan Sharma', 'age': 23},
        {'name': 'Vicky Kaushal', 'age': 14},
        {'name': 'Sandeep', 'age': 17},
        {'name': 'moon', 'age': 21}
    ]
    
    # for people in peoples:
    #     print(people)
    
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    
    vegetables = ['Pumpkin', 'Tomato', 'Potato']
    
    return render(request, "home/index.html", context={'peoples': peoples, 'text': text, 'vegetables': vegetables, 'page': 'Django Tutorial'} )
    # if index.html inside the repo then path will be "repo/index.html"



# about page
def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)


# contact page
def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)



def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page</h1>")