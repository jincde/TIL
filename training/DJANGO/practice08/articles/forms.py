from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=21, error_messages={"required": "제목을 입력해주세요."}, label="제목")
  content = forms.CharField(max_length=21, error_messages={"required": "내용을 입력해주세요."}, label="내용", widget=forms.Textarea) 