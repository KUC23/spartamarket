from django import forms
from .models import Product


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = [
            'created_at', 
            'updated_at',
            'liked_by',
            'owner',
            
            ]