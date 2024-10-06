from pathlib import Path

path = Path('./task2/task2.txt').absolute()

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            raw_cat_data = fh.readlines()

        cats_data = []
        for item in raw_cat_data:
            cat_data = item.replace('\n', '').split(',')
            cats_data.append({
                'id': cat_data[0],
                'name': cat_data[1],
                'age': cat_data[2]
            })
    except Exception as e:
        print(e)
        return
    
    return cats_data
    

print(get_cats_info(path))