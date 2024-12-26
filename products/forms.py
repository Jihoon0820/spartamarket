from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '상품 제목을 입력하세요'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '상품 설명을 입력하세요'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '가격을 입력하세요'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }