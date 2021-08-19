from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_chats")
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"


class Reply(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="replies"
    )
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"reply on {self.message}"

    class Meta:
        verbose_name_plural = "Replies"
