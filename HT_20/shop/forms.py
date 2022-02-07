from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow my-2', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow my-1', 'placeholder': 'Password'}))


class EditForm(forms.Form):
    title = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                attrs={'class': 'shadow my-2',
                                       'placeholder': 'Product Title'}))
    description = forms.CharField(widget=forms.Textarea(
                                      attrs={'class': 'shadow my-2',
                                             'placeholder': 'Product Description'}))
    price = forms.DecimalField(max_digits=15,
                               decimal_places=2,
                               widget=forms.NumberInput(
                                   attrs={'class': 'shadow my-2',
                                          'placeholder': 'Product Price'}))
    image_url = forms.URLField(widget=forms.URLInput(
                                   attrs={'class': 'shadow my-2',
                                          'placeholder': 'Image Url'}))
    category = forms.CharField(widget=forms.Select(choices=[('computers', 'Computers'),
                                                            ('house', 'House and Garden'),
                                                            ('Clothing', 'Clothing'),
                                                            ('car', 'Car Products'),
                                                            ('clothing', 'Toys')],
                                                   attrs={'class': 'shadow my-2 btn btn-dark',
                                                          'placeholder': 'Image Url'}))
