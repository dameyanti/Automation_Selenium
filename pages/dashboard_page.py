from selenium.webdriver.common.by import By


class DashboardPage:

    # sidebar toggle
    menu_button = (By.CLASS_NAME, "toggle-sidebar")

    # menu prod control hangar
    prod_control_hangar = (
        By.XPATH,
        "//span[@class='text' and text()='Prod. Control Hangar']/parent::a"
    )

    # tracking system beta
    tracking_system_beta = (
        By.XPATH,
        "//a[@href='/production_control_hangar_beta/tracking']"
    )

    # status dropdown
    status_dropdown = (By.ID, "single-status")

    # loading overlay
    loading_overlay = (By.CLASS_NAME, "vld-background")

    # tracking dropdown aircraft
    tracking_dropdown = (
        By.XPATH,
        "(//select[contains(@id,'select-tracking')])[1]"
    )

    data_not_found = (
        By.XPATH,
        "//*[contains(text(),'Data Not Found')]"
    )

    # tabel jobcard
    jobcard_table = (By.XPATH, "//table[contains(@class,'jobcard')]//tbody/tr")

    # tabel mdr
    mdr_table = (By.XPATH, "//table[contains(@class,'mdr')]//tbody/tr")