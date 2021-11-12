from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "image"]

        labels = {
            "caption": "내용",
            "image": "사진"
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption"]


class CommentForm(forms.ModelForm):
    contents = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ["contents"]
