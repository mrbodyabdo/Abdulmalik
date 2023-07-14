
import requests
from bs4 import BeautifulSoup

# رابط الموقع الذي ترغب في فحصه
url = 'https://offical-site.github.io/abdulmalek/'

# إرسال طلب GET للحصول على صفحة الويب
response = requests.get(url)

# تحقق من نجاح الطلب
if response.status_code == 200:
    # استخدام BeautifulSoup لتحليل صفحة HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # العثور على جميع النصوص داخل عناصر HTML وطباعتها
    for text in soup.find_all(text=True):
        print(text)
else:
    print('Failed to retrieve the webpage.')


