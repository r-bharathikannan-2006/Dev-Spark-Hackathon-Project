from django.shortcuts import redirect, render
from . import apis
from . models import Profiles
# Create your views here.
def login(request):
    if request.method == 'POST':
        # Handle login logic here
        print("Login POST request received")
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user
        profile = Profiles.objects.filter(email=email, password=password).first()
        dictionary = {}
        if profile:
            # Login successful
            dictionary['profile'] = profile
            dictionary['username'] = profile.user_name
            return render(request, 'index.html', context=dictionary)
        else:
            # Login failed
            dictionary['error'] = "Invalid email or password. Please try again."
            return render(request, 'login.html', context=dictionary)
    else:
        return render(request, 'login.html', context={})
     

def signup(request):
    if request.method == 'POST':
        print("Signup POST request received")
        # Handle signup logic here
        status = True
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user_name = request.POST.get('username')
        error = ""
        if email and password and user_name and password1:
            if password == password1:
                Profiles.objects.create(email=email, password=password, user_name=user_name)
                print("A")
                return redirect('login')
            else:
                print("B")
                return render(request, 'register.html', context={'error': "Passwords do not match. Please try again."})
                
        else:
            print("C")
            return render(request, 'register.html', context={'error': "All fields are required. Please fill in all details."})
    return render(request, "register.html")

def search_template(request):
    if request.method == 'GET':
        return render(request, "search_template.html")
    elif request.method == 'POST':
        query = request.POST.get('query')
        videos_list = apis.search_video(query=query, maxResults=20)
        if type(videos_list) == str:
            return render(request, 'error.html', context={'message': videos_list})
        dictionary = {
            'videos_list':videos_list
        }
        return render(request, 'search_results.html', context=dictionary)
    
# All done - Open video player
def search(request, query):
    videos_list = apis.search_video(query=query, maxResults=20)
    if type(videos_list) == str:
        return render(request, 'error.html', context={'message': videos_list})
    dictionary = {
        'videos_list':videos_list
    }
    return render(request, 'search_results.html', context=dictionary)


def open_player(request, video_id):
    summary_text, chat_prompt = apis.get_video_summary(video_id)
    #summary_text = "Example summary text."
    #chat_prompt = "Example chat prompt."
    dictionary = {
        'video_id': video_id,
        'summary': summary_text,
        'chat_prompt': chat_prompt,
    }
    return render(request, 'video_player.html', context=dictionary)

def intro(request):
    return render(request, 'intro.html', context={})

def about_us(request):
    return render(request, 'about_us.html', context={})

    





