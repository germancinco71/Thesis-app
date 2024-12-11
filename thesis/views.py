from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import medpapers, itpapers, cspapers, Comment, itcomment, cscomment
from django.db.models import Q
from .forms import CommentForm, itCommentForm, csCommentForm


def home(request):
    return render (request, "home.html")

def med(request):
    query = request.GET.get('search')
    if query:
        papers = medpapers.objects.filter(
            Q(Title__icontains=query) | Q(Authors__icontains=query)
        )
    else:
        papers = medpapers.objects.all()
        
    paginator = Paginator(papers, 5)
    page_number = request.GET.get('page')
    papers = paginator.get_page(page_number)
    
    return render (request, "med.html", {"papers": papers})

def medabs(request, id):
    papers = get_object_or_404(medpapers, id=id)
    post = get_object_or_404(medpapers, pk=id)
    
    comments = Comment.objects.filter(post=post)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post  
            new_comment.save()
            return redirect('medlist', id=post.pk) 
    else:
        form = CommentForm()

    return render(request, 'medlist.html', {
        'papers': papers,
        'post': post,
        'comments': comments,
        'form': form,
    })

def it(request):
    query = request.GET.get('search')
    if query:
        papers = itpapers.objects.filter(
            Q(Title__icontains=query) | Q(Authors__icontains=query)
        )
    else:
        papers = itpapers.objects.all()
        
    paginator = Paginator(papers, 5)
    page_number = request.GET.get('page')
    papers = paginator.get_page(page_number)
    
    return render (request, "it.html", {"papers": papers})

def itabs(request, id):
    papers = get_object_or_404(itpapers, id=id)
    post = get_object_or_404(itpapers, pk=id)
    
    comments = itcomment.objects.filter(post=post)
    
    if request.method == "POST":
        form = itCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post  
            new_comment.save()
            return redirect('itlist', id=post.pk) 
    else:
        form = CommentForm()

    return render(request, 'itlist.html', {
        'papers': papers,
        'post': post,
        'comments': comments,
        'form': form,
    })

def cs(request):
    query = request.GET.get('search')
    if query:
        papers = cspapers.objects.filter(
            Q(Title__icontains=query) | Q(Authors__icontains=query)
        )
    else:
        papers = cspapers.objects.all()
        
    paginator = Paginator(papers, 5)
    page_number = request.GET.get('page')
    papers = paginator.get_page(page_number)
    
    return render (request, "cs.html", {"papers": papers})

def csabs(request, id):
    papers = get_object_or_404(cspapers, id=id)
    post = get_object_or_404(cspapers, pk=id)
    
    comments = cscomment.objects.filter(post=post)
    
    if request.method == "POST":
        form = csCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post  
            new_comment.save()
            return redirect('cslist', id=post.pk) 
    else:
        form = CommentForm()

    return render(request, 'cslist.html', {
        'papers': papers,
        'post': post,
        'comments': comments,
        'form': form,
    })




