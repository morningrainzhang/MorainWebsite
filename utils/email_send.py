from random import choice
from django.core.mail import send_mail
from apps.users.models import EmailVerifyRecord
from MorainWebsite.settings import EMAIL_HOST_USER


# def random_str(randomlength=4):
#     str = ''
#     chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#     length = len(chars) - 1
#     random = Random()
#     for i in range(randomlength):
#         str += chars[random.randint(0, length)]
#     return str
def random_str(randomlength):
    """
    生成四位数字的验证码字符串
    """
    seeds = "1234567890"
    random_str = []
    for i in range(randomlength):
        random_str.append(choice(seeds))

    return "".join(random_str)

def send_email(email, send_type):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(4)
        email_record.code = code
        email_record.email = email
        email_record.send_type = send_type
        email_record.save()

        email_title = ''
        email_body = ''
    if send_type == 'register':
        email_title = '注册验证码'
        email_body = '验证码: \n{0}'.format(code)
        # email_title = '注册激活链接'
        # email_body = '请点击下面的链接激活你的账号: http://www.morain.top/novel/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [email], fail_silently=False)
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '密码重置链接'
        email_body = '请点击下面的链接重置你的密码: http://www.morain.top/novel/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, ['17858935980@163.com'])
        if send_status:
            pass

