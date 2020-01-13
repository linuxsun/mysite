# import os
# from django.core.mail import send_mail
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#
# if __name__ == '__main__':
#
#     send_mail(
#         '来自测试邮件', # 邮件主题subject
#         '欢迎访问!', # 邮件具体内容
#         'source@mail.com', # 邮件发送方,需要和settings中的一致
#         ['dest@mail.com'], # 接受方的邮件地址列表
#     )

import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if __name__ == '__main__':

    subject, from_email, to = '来自测试邮件', 'usernameFrom@mail.com', 'usernameTo@mail.com'
    text_content = '欢迎访问!'
    html_content = '<p>欢迎访问<a href="http://www.web.com" target=blank>www.web.com</a>，这是演示站点!</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
