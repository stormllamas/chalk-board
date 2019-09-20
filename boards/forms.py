from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':1, 'placeholder': 'Write a Subject'}
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':9, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='4000 characters allowed')

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message',]