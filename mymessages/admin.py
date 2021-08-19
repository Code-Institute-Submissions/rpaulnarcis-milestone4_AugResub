from django.contrib import admin
from django.utils.html import format_html
from .models import Message, Reply

admin.site.register(Reply)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'reply']

    def reply(self, obj):
        return format_html('<a href="/admin/mymessages/reply/add/?message=%s" class="button">Reply</a>' % (obj.id))
    reply.allow_tags = True