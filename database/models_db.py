from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    Модель для сохранения пользователей.
    Поля: никнейм, имя, фамилия, id, роль, дата регистрации, последняя активность с ботом, статус(active\block)
    """
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, null=True)
    first_name = fields.CharField(max_length=100, null=True)
    telegram_id = fields.BigIntField(unique=True)
    registration_date = fields.DatetimeField(auto_now_add=True)
    last_activity = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'users'


class Role(Model):
    """
    Модель для создания ролей
    """
    id = fields.IntField(pk=True)
    role = fields.CharField(max_length=30, default='user')


class UserRole(Model):
    """
    Связь пользователя и роли
    """
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='roles')
    role = fields.ForeignKeyField('models.Role', related_name='users')


class Status(Model):
    """
    Статус пользователя.
    banned - 0 активен, 1 - забанен
    """
    id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField('models.User', related_name='block_list')
    banned = fields.IntField(pk=False, default=0)
