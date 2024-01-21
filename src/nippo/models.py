#モデルクラスで必要なライブラリはひとつだけ。modelsをインポートします。
from django.db import models

#Modelクラスを継承したクラスを作成
class NippoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
