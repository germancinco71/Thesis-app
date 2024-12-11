from django import forms
from .models import Comment, itcomment, cscomment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        
class itCommentForm(forms.ModelForm):
    class Meta:
        model = itcomment
        fields = ['name', 'body']
        
class csCommentForm(forms.ModelForm):
    class Meta:
        model = cscomment
        fields = ['name', 'body']
        
