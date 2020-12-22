from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
# Create your views here.
def blog(request):
    return render(request,"blog.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article =form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Başarıyla Makale Kaydedildi")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,title):
    #article = Article.objects.filter(id = id).first() 
    article = get_object_or_404(Article,title = title)
    comments = article.comments.all()
    return render(request,"detail.html",{"article" : article,"comments":comments})
def updateArticle(request,title):
    article = get_object_or_404(Article,title=title)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article =form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("index")
    return render(request,"update.html",{"form":form})    
def deleteArticle(request,title):
    article = get_object_or_404(Article,title = title)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("article:dashboard")
def blog(request):
    articles = Article.objects.all()
    return render(request,"blog.html",{"articles": articles})
def addComment(request,title):
    article = get_object_or_404(Article,title =title)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect("/articles/article/" + str(title))