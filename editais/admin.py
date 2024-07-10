from django.contrib import admin

# Register your models here.
from django.contrib import admin
from unfold.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from unfold.contrib.inlines.admin import TabularInline
from rangefilter.filters import  DateRangeQuickSelectListFilterBuilder

from unfold.contrib.filters.admin import TextFilter, FieldTextFilter

from datetime import datetime

from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


# Register your models here.
from .models import Municipio, Edital, Produto, Item, Preco


class MunicipioAdmin(ModelAdmin,ImportExportModelAdmin):
    list_display = ('nome', 'view_editais')  # Include the custom method in list display

    def view_editais(self, obj):
        """Generate HTML links to the Edital objects related to this Municipio."""
        editais = Edital.objects.filter(municipio=obj)
        links = []
        for edital in editais:
            url = reverse('admin:editais_edital_change', args=[edital.id])
            link = format_html('<a href="{}">{}</a>', url, edital)
            links.append(link)
        return format_html('<br>'.join(links))

    view_editais.short_description = 'Editais'
    import_form_class = ImportForm
    export_form_class = ExportForm
    change_list_template = "admin/change_list.html"
    
class ItemInline(TabularInline,ImportExportModelAdmin):
    model = Item
    extra = 1
    import_form_class = ImportForm
    export_form_class = ExportForm 
    class Media:
        css = {
            "all":["custom_admin.css"],
        }

class EditalAdmin(ModelAdmin,ImportExportModelAdmin):
    inlines = [ItemInline]
    list_display = ('municipio', 'data_pregao','valor_total') 
    list_filter_submit = True 
    list_filter = (
        ("data_pregao", DateRangeQuickSelectListFilterBuilder()),
        ("municipio", FieldTextFilter),
        )
    import_form_class = ImportForm
    export_form_class = ExportForm 
    

class PrecoInline(TabularInline):
    model = Preco
    extra = 0
class ProdutoAdmin(ModelAdmin,ImportExportModelAdmin):
    inlines = (PrecoInline,)
    import_form_class = ImportForm
    export_form_class = ExportForm


admin.site.site_header = "Controle de Editais Nutri C"
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Edital, EditalAdmin)
admin.site.register(Produto, ProdutoAdmin)
