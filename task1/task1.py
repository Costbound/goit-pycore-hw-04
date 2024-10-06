from pathlib import Path

path = Path('./task1/task1.txt').absolute()


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            raw_data = fh.readlines()

    
        salaries = []
        for item in raw_data:
            item = int(item.split(',')[1].replace('\n', ''))
            salaries.append(item)

        sum_salaries = sum(salaries)
        avg_salary = sum_salaries // len(salaries)
    except Exception as e:
        print(e)
        return

    return {
        'avg_salary': avg_salary,
        'sum_salaries': sum_salaries
    }


salary_data = total_salary(path)

if salary_data:
    print(f"Загальна сума заробітної плати: {salary_data['sum_salaries']}, Середня заробітна плата: {salary_data['avg_salary']}")
