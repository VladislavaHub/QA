from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")

    assert "Example" in driver.title, "Заголовок не содержит 'Example'"

    link = driver.find_element(By.CSS_SELECTOR, 'a[href^="https://www.iana.org"]')
    assert "More information" in link.text, "Ссылка не содержит текст 'More information'"
    link.click()

    time.sleep(2)

    expected_url = "https://www.iana.org/help/example-domains"
    current_url = driver.current_url
    assert current_url == expected_url, f"Ожидался URL '{expected_url}', но получен '{current_url}'"

    print("Все проверки пройдены успешно.")

finally:
    driver.quit()