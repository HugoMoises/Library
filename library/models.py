from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name

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
        if self.avaiable > 0:
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
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]

    person = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    book = models.ForeignKey(Livro, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return f"Loan of {self.book.title} to {self.person.name}"
    