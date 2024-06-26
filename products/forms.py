from django import forms
from .models import Product, Category, ProductReview
from .widgets import CustomClearableFileInput

class ReviewForm(forms.ModelForm):
    """
    Form to add a review of a product
    """

    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')


class ProductForm(forms.ModelForm):
    """
    Form for adding/updating products
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'

