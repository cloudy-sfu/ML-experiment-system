from django.db import models
from task_manager.models import Step
from library.models import Paper


class LinearRegression(models.Model):
    step = models.ForeignKey(Step, models.CASCADE, blank=True, null=True)
    dataframe = models.ForeignKey(Paper, models.SET_NULL, blank=True, null=True, related_name="lr_dataframe")

    matrix = models.ForeignKey(Paper, models.SET_NULL, blank=True, null=True, related_name="lr_matrix")
    model = models.ForeignKey(Paper, models.SET_NULL, blank=True, null=True, related_name="lr_model")
    evaluate = models.ForeignKey(Paper, models.SET_NULL, blank=True, null=True, related_name="lr_evaluate")
    predict = models.ForeignKey(Paper, models.SET_NULL, blank=True, null=True, related_name="lr_predict")

    note = models.TextField(blank=True)
    error_message = models.TextField(blank=True)

    def open_permission(self, user):
        return any([x.user == user for x in self.step.task.openedtask_set.all()])


class Column(models.Model):
    algorithm = models.ForeignKey(LinearRegression, models.CASCADE)
    name = models.TextField()
    x_column = models.BooleanField(default=False)
    y_column = models.BooleanField(default=False)

    def __str__(self):
        return self.name