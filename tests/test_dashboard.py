from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage


def open_tracking_system(driver):

    wait = WebDriverWait(driver,40)

    print("Klik toggle sidebar")

    wait.until(
        EC.element_to_be_clickable(DashboardPage.menu_button)
    ).click()


    print("Klik Prod Control Hangar")

    prod_menu = wait.until(
        EC.element_to_be_clickable(DashboardPage.prod_control_hangar)
    )

    driver.execute_script("arguments[0].click();", prod_menu)


    print("Klik Tracking System BETA")

    tracking_menu = wait.until(
        EC.element_to_be_clickable(DashboardPage.tracking_system_beta)
    )

    driver.execute_script("arguments[0].click();", tracking_menu)

    print("Halaman Tracking System terbuka")


    # tunggu overlay benar-benar hilang
    wait.until(
        EC.invisibility_of_element_located(DashboardPage.loading_overlay)
    )

    print("Loading selesai")


    status_dropdown = wait.until(
        EC.presence_of_element_located(DashboardPage.status_dropdown)
    )


    # gunakan javascript untuk set dropdown
    driver.execute_script("""
        let select = arguments[0];
        select.value = 'Progress';
        select.dispatchEvent(new Event('change'));
    """, status_dropdown)


    print("Status Progress dipilih")


    # tunggu loading setelah filter
    wait.until(
        EC.invisibility_of_element_located(DashboardPage.loading_overlay)
    )

    print("Data aircraft loaded")