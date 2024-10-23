import heapq

price = 0
list_of_tubes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapq.heapify(list_of_tubes)


while len(list_of_tubes) > 1:
    # Витягуємо два найменші елементи
    first_smallest_tube = heapq.heappop(list_of_tubes)
    second_smallest_tube = heapq.heappop(list_of_tubes)

    # Об'єднуємо їх, додаючи до загальних витрат
    connected_tube = first_smallest_tube + second_smallest_tube
    price += connected_tube

    # Додаємо новий об'єднаний кабель назад у чергу
    heapq.heappush(list_of_tubes, connected_tube)

print(price)
