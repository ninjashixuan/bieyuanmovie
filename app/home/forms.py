# coding:utf8

from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, ValidationError
from ..models import User
from flask import session


class RegisterForm(FlaskForm):
    name = StringField(
        '昵称',
        validators=[DataRequired('请输入昵称')],
        description='昵称',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称",
            # "required": "required"
        }
    )

    pwd = PasswordField(
        '密码',
        validators=[DataRequired('请输入密码'), EqualTo('repwd', message='两次密码输入不一致')],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码",
            # "required": "required"
        }
    )

    repwd = PasswordField(
        '确认密码',
        validators=[DataRequired('请再次输入密码')],
        description='确认密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请再次输入密码",
            # "required": "required"
        }
    )

    email = StringField(
        '邮箱',
        validators=[DataRequired('请输入邮箱'), Email('邮箱格式不对')],
        description='邮箱',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱",
            # "required": "required"
        }
    )

    phone = StringField(
        '手机',
        validators=[DataRequired('请输入手机'), Regexp('1[3458]\\d{9}', message=('手机格式不正确！'))],
        description='手机',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机",
            # "required": "required"
        }
    )

    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('该昵称已被使用')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已被使用')

    def validate_phone(self, field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('该手机已被使用')


class LoginForm(FlaskForm):
    name = StringField(
        '账号',
        validators=[DataRequired('请输入账号')],
        description='昵称',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号",
            # "required": "required"
        }
    )

    pwd = PasswordField(
        '密码',
        validators=[DataRequired('请输入密码')],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码",
            # "required": "required"
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        if not User.query.filter_by(name=field.data).first():
            raise ValidationError('账号不存在！')


class UserdetailForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机！"),
            Regexp("1[3458]\\d{9}", message="手机格式不正确！")
        ],
        description="手机",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机！",
        }
    )
    face = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像！")
        ],
        description="头像",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        }
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        '旧密码',
        validators=[DataRequired('请输入密码')],
        description='旧密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码",
        }
    )

    new_pwd = PasswordField(
        '新密码',
        validators=[DataRequired('请输入密码')],
        description='新密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码",
        }
    )

    submit = SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-success",
        }
    )

    def validate_old_pwd(self, field):
        user = User.query.filter_by(name=session['user']).first()
        if not user.check_pwd(field.data):
            raise ValidationError('旧密码错误')

    def validate_new_pwd(self, field):
        user = User.query.filter_by(name=session['user']).first()
        if user.check_pwd(field.data):
            raise ValidationError('新密码与旧密码一样！')


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容！"),
        ],
        description="内容",
        render_kw={
            "id": "input_content"
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )
