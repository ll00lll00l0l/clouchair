from django import forms
from .models import CartItem

class ImageForm(forms.ModelForm):
  class Meta:
    model=CartItem
    fields=("name","image")
    
   

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data['image']
        # Add any custom validation or processing for the image field if needed
        return image
