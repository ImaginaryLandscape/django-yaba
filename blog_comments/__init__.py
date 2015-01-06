import socket

from django.db.models.signals import post_save
from django_comments.models import Comment
from .forms import CommentFormNoEmail

def get_form():
    return CommentFormNoEmail

def httpbl_check(sender, instance, created, **kwargs):
    if not created:
        suspicious_array = ['1', '4', '5', '6', '7']
        is_spam = False
        ip_addy = instance.ip_address
        ip_sectioned = ip_addy.split('.')
        ip_swapped = reversed(ip_sectioned)
        ip_octect_swap = ''
        for x in ip_swapped:
            ip_octect_swap += '%s.' % x
        ip_octect_swap = ip_octect_swap.rstrip('.')
        try:
            ip_to_query = "%s.%s.dnsbl.httpbl.org" % (settings.HTTPBLKEY, 
                ip_octect_swap)
            httpbl_result = socket.gethostbyname_ex(ip_to_query)[-1][0]
        except:
            httpbl_result = None

        if httpbl_result is not None:
            activity_octet = httpbl_result.split('.')[1]
            threat_octet = httpbl_result.split('.')[2]
            visitor_octect = httpbl_result.split('.')[-3]
            if int(activity_octet) < 30 and threat_octet in suspicious_array:
                instance.is_public = False
                instance.save()

post_save.connect(httpbl_check, sender=Comment)
