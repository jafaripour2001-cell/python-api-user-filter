"""
API Data Fetcher
-----------------
یک برنامه ساده که از یک API عمومی اطلاعات کاربران را دریافت می‌کند،
بر اساس شهر فیلتر می‌کند و نتیجه را نمایش می‌دهد.
"""

import requests


def get_data(url):
    """
    یک درخواست GET به آدرس url می‌فرستد و در صورت موفقیت،
    داده را به صورت JSON برمی‌گرداند. در صورت بروز خطا (قطعی
    اینترنت، آدرس اشتباه، timeout و ...) پیام خطا چاپ کرده و
    None برمی‌گرداند.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print("خطا:", e)
        return None


def filter_users(users, city):
    """
    از بین لیست کاربران، فقط کاربرانی که شهرشان برابر با
    مقدار city است را در یک لیست جدید برمی‌گرداند.
    """
    result = []

    for user in users:
        if user["address"]["city"] == city:
            result.append(user)

    return result


def main():
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = get_data(users_url)

    if not users:
        print("دریافت اطلاعات کاربران با مشکل مواجه شد.")
        return

    city_name = input("نام شهر را وارد کنید: ")

    filtered_users = filter_users(users, city_name)

    if filtered_users:
        for user in filtered_users:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("-" * 20)
    else:
        print("کاربری در این شهر پیدا نشد.")


if __name__ == "__main__":
    main()