# 2d collections


# groceries = [
#     ["apple", "orange", "banana", "coconut"],
#     ["celery", "carrots", "potatoes"],
#     ["chicken", "fish", "turkey"],
# ]

# for list in groceries:
#     for item in list:
#         print(item, end=" ")
#     print()

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for item in num_pad:
    for number in item:
        print(number, end=" ")
    print()
