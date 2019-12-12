from django import forms
from django.core import validators

from front.models import User


class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            # print(message_dicts)
            message = []
            for message_dict in message_dicts:
                # print(message_dict['message'])
                message.append(message_dict['message'])
                new_errors[key] = message
        return errors


class MessageBoardForm(BaseForm):
    title = forms.CharField(max_length=20, label='标题', min_length=6, error_messages={"max_length": "长度太长", "min_length": "长度太短"})
    content = forms.CharField(widget=forms.Textarea, label="内容")
    email = forms.EmailField(label="邮箱")
    reply = forms.BooleanField(required=False, label="回复")


class MyForm(BaseForm):
    #email = forms.EmailField(error_messages={"invalid": "请输入正确邮箱"})
    #price = forms.FloatField(error_messages={"invalid": "请输入正确的价格"})
    personal_website = forms.URLField(error_messages={"invalid": "请输入正确的邮箱", "required": "请输入个人网站"})
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确的邮箱")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}', message="请输入正确的手机号")])


class RegisterForm(BaseForm):
    username = forms.CharField(label="用户名", max_length=20, min_length=6, error_messages={"invalid": "请输入正确的用户名", "required": "请输入用户名"})
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}', message="请输入正确的手机号")])
    password1 = forms.CharField(label="密码", max_length=30, min_length=6, error_messages={"required": "请输入密码", "max_length": "长度过长", "min_length": "长度太短"})
    password2 = forms.CharField(label="重复密码", max_length=30, min_length=6, error_messages={"required": "请输入密码", "max_length": "长度过长", "min_length": "长度太短"})

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError("phone number exit")
        return telephone

    def clean(self):
        clean_data = super(RegisterForm, self).clean()
        password1 = clean_data.get("password1")
        password2 = clean_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("not equals")
        return clean_data   # 一定要返回这个结果







