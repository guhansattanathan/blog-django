from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.utils.text import slugify

# Create your views here.
blog_posts = [
    {"title": "Getting Started with Python", "author": "Alex Morgan", "content": "An introduction to Python basics and setup.", "slug": "getting-started-with-python"},
    {"title": "Why Data Structures Matter", "author": "Priya Patel", "content": "Understanding how data structures improve performance.", "slug": "why-data-structures-matter"},
    {"title": "My Journey into Computer Science", "author": "Daniel Kim", "content": "How I discovered my passion for programming.", "slug": "my-journey-into-computer-science"},
    {"title": "Debugging Tips for Beginners", "author": "Sofia Ramirez", "content": "Common debugging strategies every developer should know.", "slug": "debugging-tips-for-beginners"},
    {"title": "Web Development Basics", "author": "Jordan Lee", "content": "An overview of HTML, CSS, and JavaScript.", "slug": "web-development-basics"},
    {"title": "How APIs Work", "author": "Emily Chen", "content": "A simple explanation of REST APIs and JSON.", "slug": "how-apis-work"},
    {"title": "Learning Java as a C++ Developer", "author": "Michael Brown", "content": "Key differences between Java and C++ for beginners.", "slug": "learning-java-as-a-c-developer"},
    {"title": "Productivity Tips for Students", "author": "Aisha Khan", "content": "How to manage time effectively while studying.", "slug": "productivity-tips-for-students"},
    {"title": "Building Your First Project", "author": "Lucas Nguyen", "content": "Steps to go from idea to a working application.", "slug": "building-your-first-project"},
    {"title": "Preparing for Software Internships", "author": "Natalie Wilson", "content": "What to focus on when applying for internships.", "slug": "preparing-for-software-internships"}
]


def index(request):
    total_blogs = len(blog_posts)
    blogs = blog_posts[total_blogs - 3: total_blogs]
    return render(request, "blogsite/home.html", {
        "blogs": blogs
    })

def posts(request):
    return render(request, "blogsite/posts.html", {
        "blogs": blog_posts
    })

def each_post(request, slug):
    blog = None
    for item in blog_posts:
        if item["slug"] == slug:
            blog = item
    return render(request,  "blogsite/blog.html", {
        "blog": blog
    })