from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin  # change
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin

from .models import BlogPost, BlogPostImage, Author, BlogPostImageDescription
from .resources import BlogPostResource, AuthorResource


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    actions = ['export_selected']
    list_display = ('full_name', 'age')

    def export_selected(self, request, queryset):
        """Custom export action"""
        resource = AuthorResource()
        dataset = resource.export(queryset)
        response = HttpResponse(
            dataset.export('xlsx'),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="books.xlsx"'
        return response


# class BlogPostImageInline(SortableInlineAdminMixin, admin.TabularInline): # remove
#     model = BlogPostImage # remove
#     extra = 1 # remove


# class BlogPostAdmin(SortableAdminMixin, admin.ModelAdmin): # remove
#     inlines = [BlogPostImageInline] # remove
#     list_display = ('title', 'is_active', 'created_at') # remove
#     list_filter = ('is_active', 'authors') # remove
#     search_fields = ('title',) # remove
#     date_hierarchy = 'created_at' # remove
#     filter_horizontal = ('authors',) # remove
#     prepopulated_fields = {'slug': ('title',)} # remove
#     # list_per_page = 2 # remove
#     # fields = ('title', 'is_active', 'text') # remove
#     # exclude = ('text',) # remove
#     # filter_vertical = ('authors',) # remove
#     # fieldsets = ( # remove
#     #     ("Basic Information", { # remove
#     #         "fields": ("title", "text", "website") # remove
#     #     }), # remove
#     #     ("Many to Many", { # remove
#     #         "fields": ("authors",) # remove
#     #     }) # remove
#     # ) # remove


class BlogPostImageDescriptionInline(NestedTabularInline):
    model = BlogPostImageDescription
    extra = 1


class BlogPostImageInline(NestedTabularInline):
    model = BlogPostImage
    inlines = [BlogPostImageDescriptionInline]
    extra = 1


@admin.register(BlogPost)  # change
class BlogPostAdmin(ImportExportModelAdmin, NestedModelAdmin):
    resource_class = BlogPostResource
    inlines = [BlogPostImageInline]
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)  # add
    search_fields = ('title',)  # add

# class BlogPostAdmin(ImportExportModelAdmin, NestedModelAdmin): # remove
#     resource_class = BlogPostResource # remove
#     inlines = [BlogPostImageInline] # remove
#     list_display = ('title', 'is_active', 'created_at') # remove

# admin.site.register(BlogPost, BlogPostAdmin) # remove
