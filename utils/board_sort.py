async def sort_data_by_commits(data):
    for item in data:
        item[2] = int(item[2].replace(',', ''))

    sorted_data = sorted(data, key=lambda x: x[2], reverse=True)
    return sorted_data