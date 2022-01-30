from django import forms


class CategorySelector(forms.Form):
    category_dropdown = forms.ChoiceField(choices=(('newstories', 'newstories'),
                                                   ('jobstories', 'jobstories'),
                                                   ('askstories', 'askstories'),
                                                   ('showstories', 'showstories'),))
