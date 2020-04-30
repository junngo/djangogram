from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms as django_forms

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        # labels = {
        #     'email': '이메일 주소',
        #     'name': '성명',
        #     'username': '사용자 이름',
        #     'password': '비밀번호'
        # }

        widgets = {
            'email': django_forms.TextInput(attrs={'placeholder': '이메일 주소'}),
            'name': django_forms.TextInput(attrs={'placeholder': '성명'}),
            'username': django_forms.TextInput(attrs={'placeholder': '사용자 이름'}),
            'password': django_forms.PasswordInput(attrs={'placeholder': '비밀번호'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
