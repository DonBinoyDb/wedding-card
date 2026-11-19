import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
opts.add_argument("--headless=new")
opts.add_argument("--window-size=430,932")
opts.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=opts)
try:
    driver.get("http://localhost:8000/index.html")
    time.sleep(1)

    # Scroll to reveal section
    reveal_sec = driver.find_element(By.ID, "reveal")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", reveal_sec)
    time.sleep(0.5)

    # Save unscratched state
    driver.save_screenshot("scratch/reveal_test_unscratched.png")
    print("Saved unscratched screenshot")

    canvas = driver.find_element(By.ID, "revealCanvas")
    
    # Perform scratching action
    actions = ActionChains(driver)
    actions.move_to_element(canvas)
    actions.click_and_hold()
    
    # Zig-zag scratch motions
    for dx, dy in [(-60, -30), (60, -20), (-70, 0), (70, 20), (-60, 40), (50, -40), (0, 0)]:
        actions.move_by_offset(dx, dy)
        actions.pause(0.05)
        
    actions.release()
    actions.perform()
    time.sleep(0.5)

    # Save scratched state
    driver.save_screenshot("scratch/reveal_test_scratching.png")
    print("Saved scratching screenshot")

    # Now scratch more to trigger full reveal
    actions2 = ActionChains(driver)
    actions2.move_to_element(canvas)
    actions2.click_and_hold()
    for _ in range(5):
        for dx, dy in [(-80, -40), (160, 20), (-160, 30), (160, -50), (-100, 40)]:
            actions2.move_by_offset(dx, dy)
            actions2.pause(0.03)
    actions2.release()
    actions2.perform()
    time.sleep(1.2)

    # Save fully revealed state
    driver.save_screenshot("scratch/reveal_test_revealed.png")
    print("Saved revealed screenshot")

finally:
    driver.quit()

