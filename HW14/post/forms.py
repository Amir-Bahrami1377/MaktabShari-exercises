from django import forms


class CreatePostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(required=False)
    detail = forms.CharField(required=False, widget=forms.Textarea)
    author = forms.CharField(required=False)
    image_path = forms.CharField(required=False)
    link_url = forms.CharField(required=False)
    tags = forms.CharField(required=False)


class UpdatePostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(required=False)
    detail = forms.CharField(required=False, widget=forms.Textarea)
    author = forms.CharField(required=False)
    image_path = forms.CharField(required=False)
    link_url = forms.CharField(required=False)
    tags = forms.CharField(required=False)
