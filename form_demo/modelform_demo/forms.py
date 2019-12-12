from django import forms

from modelform_demo.models import BookDemo, UserDemo


class BaseForm(forms.ModelForm):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            print(message_dicts)
            message = []
            for message_dict in message_dicts:
                print(message_dict['message'])
                message.append(message_dict['message'])
                new_errors[key] = message
        return new_errors


# 模型表单继承与ModelForm
class AddBookForm(BaseForm):
    class Meta:
        model = BookDemo
        fields = "__all__"   # 拿到模型中所有的字段
        # fields = ['title', 'price']  # 拿到给定的字段
        # exclude = ['price']  # 拿到除price以外的所有字段


class AddUserDemo(BaseForm):
    class Meta:
        model = UserDemo
        fields = '__all__'
