from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

User = get_user_model()

class Livro(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    avaiable = models.IntegerField()
    cover = models.ImageField(upload_to='images/', blank=True, null=True)


    class Meta:
        ordering = ['title']

    def emprestimo(self):
        loan_date = timezone.now()
        return_date = loan_date + timedelta(days=30)
        if self.avaiable > 0: 
            loan_date = loan_date,
            return_date = return_date,
            self.avaiable -= 1
            self.save()
            return True
        return False

    def devolver(self):
        self.avaiable += 1
        self.save()

    def __str__(self):
        return f"{self.title} by {self.author}"

class Emprestimo(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
        ('refused', 'Refused'),
    ]

    person = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Livro, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS)

    class Meta:
        ordering = ['-loan_date']
    

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = self.loan_date + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Loan of {self.book.title}"
    