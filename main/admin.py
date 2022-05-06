from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('author', 'category')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['author', 'category']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('author', 'description', 'author_text',)

    # list_filter -> Фильтр для отображения
    list_filter = ('category',)

    # list_per_page -> Бир страницада канча запись болуш керек
    list_per_page = 10

    # actions -> Кайсы дествиялар болуш керек
    '''
    actions = ['set_category_man',
               'set_category_woman',
               'set_category_sport',
               'set_category_electric',
               'set_clone_model',
               ]
    
    
    # Добавление дествии
    @admin.action(description='Установить категорию Sport')
    def set_category_sport(self, request, qs: QuerySet):
        count_updates = qs.update(category=3)
        # self.message_user -> Функция болгондо кандай сообщение чыгарына жооп берет.
        self.message_user(request,
                          f'Было обновлено {count_updates} записей',
                          # level -> INFO Записьти жашыл кылат, ERROR кызыл
                          level=messages.INFO
                          )

    @admin.action(description='Установить категорию Man')
    def set_category_man(self, request, qs: QuerySet):
        qs.update(category=1)

    @admin.action(description='Установить категорию Woman')
    def set_category_woman(self, request, qs: QuerySet):
        qs.update(category=2)

    @admin.action(description='Установить категорию Electric')
    def set_category_electric(self, request, qs: QuerySet):
        qs.update(category=4)

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()
    '''


admin.site.register(Post, PostAdmin)
