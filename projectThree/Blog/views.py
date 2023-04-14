from django.shortcuts import render

posts = [
    {
    'author': "Gary Chapman",
    'title': 'Post 1',
    'date_posted': 'March 28, 2023'
},
    {
    'author': "Robert Greene",
    'title': 'Post 2',
    'date_posted': 'March 28, 2023'
},
    {
    'author': "Joyce Meyer",
    'title': 'Post 3',
    'date_posted': 'March 28, 2023'
}
]
contacts = {
    'location': 'Nigeria',
    'city': 'Abuja',
    'phone': +2348023410223
}
blog_news = {
    'title': 'Election',
    'description': '2023 Presidential Election',
    'date_posted': 'March 30, 2023'
}

groups = [
    {
        'category': 'fashion',
        'id': 1
    },
    {
        'category': 'accessories',
        'id': 2
    },
    {
        'category': 'electronics',
        'id': 3
    }
]

# Create your views here.
def blog(request):
    post = {"posts": posts}
    return render(request, 'blog/blog.html', post)

def contact(request):
    contact = {"contacts": contacts}
    return render(request, 'blog/contact.html', contact)

def news(request):
    news = {"news": blog_news}
    return render(request, 'blog/news.html', news)

def categories(request):
    group = {
        'groups': groups
    }
    return render(request, 'blog/categories.html', group)