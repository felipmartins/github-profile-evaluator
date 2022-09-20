from operator import itemgetter


def get_median(queryset):

    print(queryset)

    if len(queryset) % 2 != 0:
        median = queryset[len(queryset) // 2 + 1].grade
    else:
        median = (
            queryset[len(queryset) // 2 + 1].grade + queryset[len(queryset) // 2].grade
        ) // 2

    return median
