from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# admin.site.register(Book)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def display_genre(self):
        """Create a string for the genre. This is required to diplay genre in admin."""
        return ", ".join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

    list_display = ("title", "author", display_genre)
    inlines = [BookInstanceInline]


# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name",  ("date_of_birth", "date_of_death")]
# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)