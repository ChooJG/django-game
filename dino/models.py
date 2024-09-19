from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Scoreboard(models.Model):
    GAME_CHOICES = [
        ('dino', 'Dino'),
        ('counting-stars', 'Counting Stars'),
        ('snake', 'Snake'),
        ('shooting', 'Shooting'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scores")  # 유저와 연결
    score = models.IntegerField()  # 게임 점수
    achievement_date = models.DateTimeField(default=timezone.now)  # 점수를 달성한 날짜
    highest_score = models.BooleanField(default=False)  # 최고 점수인지 여부
    game_type = models.CharField(max_length=20, choices=GAME_CHOICES)  # 게임 이름

    class Meta:
        ordering = ['-score', 'achievement_date']  # 점수 높은 순, 달성 날짜 순으로 정렬
        constraints = [
            models.UniqueConstraint(fields=['user', 'game_type'], name='unique_score_per_game')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.score} points - {self.get_game_type_display()}"

    def save(self, *args, **kwargs):
        # 새로 추가된 점수가 유저의 해당 게임에서의 최고 점수인지 확인
        if not self.pk:  # 새로 생성되는 경우
            highest_score_record = Scoreboard.objects.filter(user=self.user, game_type=self.game_type).order_by('-score').first()
            if not highest_score_record or self.score > highest_score_record.score:
                self.highest_score = True  # 해당 게임에서 최고 점수로 설정
                if highest_score_record:
                    highest_score_record.highest_score = False  # 이전 최고 점수 기록을 업데이트
                    highest_score_record.save()
        super().save(*args, **kwargs)
