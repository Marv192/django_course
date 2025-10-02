from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

# здесь продолжайте программу
pages = Paginator(lst, 3)

print(*pages.page_range)