import json
import requests

req = False
try:
    req = requests.get('https://codeforces.com/api/problemset.problems')
except:
    print('Error requesting CF API')

if req.status_code == 200 and 'json' in req.headers['content-type']:
    problems = req.json()["result"]["problems"]
    problem_statistics = req.json()["result"]["problemStatistics"]

    # Словарь для хранения статистики по сложности задач
    rating_count = {}
    # Словарь для хранения статистики по тегам
    tags_count = {}

    for problem in problems:
        rating = problem.get("rating")
        tags = problem.get("tags", [])

        # Статистика по сложности
        if rating:
            if rating in rating_count:
                rating_count[rating] += 1
            else:
                rating_count[rating] = 1

        # Статистика по тегам
        for tag in tags:
            if tag in tags_count:
                tags_count[tag] += 1
            else:
                tags_count[tag] = 1

    # Сортировка статистики по сложности
    sorted_ratings = dict(sorted(rating_count.items(), key=lambda x: x[0]))
    # Сортировка статистики по тегам
    sorted_tags = dict(reversed(sorted(tags_count.items(), key=lambda x: x[1])))

    # Вывод статистики по сложности
    print("Статистика по сложности задач:")
    for rating in sorted_ratings.keys():
        print(f"Рейтинг {rating}: {sorted_ratings[rating]} задач")

    # Вывод статистики по тегам
    print("\nСтатистика по тегам:")
    for tag in sorted_tags.keys():
        print(f"Тег '{tag}': {sorted_tags[tag]} задач")
else:
    print('Not a JSON response requesting CF API')