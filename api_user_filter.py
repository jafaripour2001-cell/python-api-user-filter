
import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print("خطا در اتصال به API:", error)
        return []


def show_all_users(users):
    print("\n--- فهرست کاربران ---\n")

    for user in users:
        print("نام:", user["name"])
        print("شهر:", user["address"]["city"])
        print("ایمیل:", user["email"])
        print("-" * 30)


def search_by_city(users):
    city = input("\nنام شهر را وارد کنید: ").strip().lower()

    found = False

    for user in users:
        user_city = user["address"]["city"]

        if user_city.lower() == city:
            print("\n✅ کاربر پیدا شد!")
            print("نام:", user["name"])
            print("شهر:", user_city)
            print("ایمیل:", user["email"])
            found = True

    if not found:
        print("\n❌ کاربری در این شهر پیدا نشد.")


def main():
    users = get_users()

    if not users:
        return

    while True:
        print("\n========== منوی برنامه ==========")
        print("1. نمایش همه کاربران")
        print("2. جست‌وجو بر اساس شهر")
        print("3. خروج")

        choice = input("\nگزینه موردنظر را انتخاب کنید: ")

        if choice == "1":
            show_all_users(users)

        elif choice == "2":
            search_by_city(users)

        elif choice == "3":
            print("\nبرنامه بسته شد. موفق باشی! 🌷")
            break

        else:
            print("\n❌ گزینه نامعتبر است.")


if __name__ == "__main__":
    main()
