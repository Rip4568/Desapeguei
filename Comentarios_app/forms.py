from django import forms

class ComentarioManualForm(forms.Form):
    comentario = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Deixe sua avaliação aqui...",
                "id":"message",
                "cols":30,
                "rows":5,
            }))