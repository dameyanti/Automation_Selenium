import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.test_tracking import change_dropdown, wait_loading, wait_table_rows


def test_jobcard_table(driver):

    from tests.test_login import login
    from tests.test_dashboard import open_tracking_system

    login(driver)
    open_tracking_system(driver)

    wait = WebDriverWait(driver, 40)

    dropdowns = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//select[contains(@id,'select-tracking')]")
        )
    )

    dropdowns = dropdowns[:3]

    for i, dropdown in enumerate(dropdowns):

        aircraft = f"Aircraft_{i+1}"

        print(f"\n[JOBCARD] {aircraft}")

        driver.execute_script("arguments[0].scrollIntoView();", dropdown)

        change_dropdown(driver, dropdown, "jobcard")
        wait_loading(driver)

        time.sleep(2)

        rows = wait_table_rows(driver)

        print("Row count:", len(rows))

        assert len(rows) > 0, f"{aircraft} jobcard kosong"