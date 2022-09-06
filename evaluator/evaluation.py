
def single_evaluation(user_dict):
    grade = 0

    if user_dict["photo"]:
        grade += 10

    if user_dict["email"]:
        grade += 10

    if user_dict["linkedin"]:
        grade += 10

    if user_dict["readme"] != 404:
        grade += 10
        if user_dict["tags"] >= 5:
            grade += 10
            if user_dict["tags"] >= 10:
                grade += 10

    if user_dict["repos"] >= 5:
        grade += 10
        if user_dict["repos"] >= 10:
            grade += 10

    if user_dict["pinned"] >= 2:
        grade += 10
        if user_dict["pinned"] >= 4:
            grade += 10

    user_dict["grade"] = grade

    return user_dict


# def group_evaluation(general_list_of_dicts):
#     general_list_of_dicts = fetch_content(general_list_of_dicts)

#     general_list_of_dicts = populate_dicts(general_list_of_dicts)

#     statistics_dict = get_statistics(general_list_of_dicts)

#     for each_dict in general_list_of_dicts:
#         each_dict = single_evaluation(each_dict)
#         cohort = each_dict["cohort_name"]

#     write_new_csv(str(cohort), general_list_of_dicts, statistics_dict)

#     return general_list_of_dicts
