import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook


# ==========================
# COMMON FUNCTIONS
# ==========================

def wait_loading(driver):
    WebDriverWait(driver, 40).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "vld-background"))
    )


def change_dropdown(driver, dropdown, value):
    driver.execute_script("""
        let select = arguments[0];
        select.value = arguments[1];
        select.dispatchEvent(new Event('change'));
    """, dropdown, value)


def wait_table_rows(driver):
    return WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//table/tbody/tr")
        )
    )


def check_data(driver, aircraft, page):

    time.sleep(2)  # 🔥 penting untuk UI async

    page_text = driver.page_source.lower()

    if "data not found" in page_text or "no data" in page_text:

        filename = f"screenshots/{aircraft}_{page}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(filename)

        print(f"⚠ {page} kosong")
        return "No Data", filename

    try:
        rows = wait_table_rows(driver)
        print(f"✔ {page} tampil ({len(rows)} rows)")
        return "Data OK", ""
    except:
        print(f"❌ {page} gagal load")
        return "Error", ""


# ==========================
# MAIN TEST
# ==========================

def test_tracking_pages(driver):

    from tests.test_login import login
    from tests.test_dashboard import open_tracking_system

    login(driver)
    open_tracking_system(driver)

    wait = WebDriverWait(driver, 40)

    aircraft_dropdowns = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//select[contains(@id,'select-tracking')]")
        )
    )

    print("Total aircraft:", len(aircraft_dropdowns))

    # 🔥 MODE
    MODE = "SMOKE"  # FULL / SMOKE

    if MODE == "SMOKE":
        aircraft_dropdowns = aircraft_dropdowns[:5]

    # ==========================
    # EXCEL REPORT
    # ==========================

    os.makedirs("report", exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Automation Result"

    ws.append([
        "Aircraft",
        "Dashboard",
        "Jobcard",
        "MDR",
        "Screenshot"
    ])

    failed_cases = []

    for i, dropdown in enumerate(aircraft_dropdowns):

        aircraft_name = f"Aircraft_{i+1}"

        print(f"\n===== {aircraft_name} =====")

        driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        wait_loading(driver)

        # DASHBOARD
        change_dropdown(driver, dropdown, "dashboard_summary")
        wait_loading(driver)
        dashboard_result, dash_ss = check_data(driver, aircraft_name, "dashboard")

        # JOBCARD
        change_dropdown(driver, dropdown, "jobcard")
        wait_loading(driver)
        jobcard_result, job_ss = check_data(driver, aircraft_name, "jobcard")

        # MDR
        change_dropdown(driver, dropdown, "mdr")
        wait_loading(driver)
        mdr_result, mdr_ss = check_data(driver, aircraft_name, "mdr")

        screenshot = dash_ss or job_ss or mdr_ss

        ws.append([
            aircraft_name,
            dashboard_result,
            jobcard_result,
            mdr_result,
            screenshot
        ])

        if "No Data" in [dashboard_result, jobcard_result, mdr_result]:
            failed_cases.append(aircraft_name)

        # balik ke tracking
        change_dropdown(driver, dropdown, "Tracking")
        wait_loading(driver)

    wb.save("report/tracking_system_report.xlsx")

    print("\nReport berhasil dibuat:")
    print("report/tracking_system_report.xlsx")

    if failed_cases:
        print("\n⚠ Data kosong ditemukan di:")
        for f in failed_cases:
            print("-", f)