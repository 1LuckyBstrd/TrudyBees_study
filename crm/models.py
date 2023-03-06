from django.db import models


class Order(models.Model):  # класс Order наследует класс Model
    order_dt = models.DateTimeField(auto_now=True)  # поле даты заявки
    order_name = models.CharField(max_length=200, verbose_name='Имя')  # поле имени длина 200
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return self.order_name


    # class Meta:
    #    verbose_name='заказ'
    #    verbose_name_plural = 'заказы'
