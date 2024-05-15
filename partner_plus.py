import asyncio, os
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from logger import setup_logger
import socket, http.client as hc
from dotenv import load_dotenv

load_dotenv()

CURRENT_DIRECTORY = os.getcwd()
FILE_PATH = os.path.join(CURRENT_DIRECTORY, 'goal.txt')

CHANNEL = os.getenv('CHANNEL')
GOAL_POINTS = 100

log = setup_logger('partner-tracker')

async def check_internet():
    conn = hc.HTTPSConnection('google.com')
    try:
        conn.request('GET', '/generate_204')
        response = conn.getresponse()
        conn.close()
        return bool(response.status == 204)
    except (hc.HTTPException, socket.timeout, socket.error):
        conn.close()
        return False

async def partner_plus_tracker():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            f.write(f'partner+: 0/{GOAL_POINTS}')

    try:        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                if page is None or not page:
                    return
                
                await page.goto(f'https://www.twitch.tv/{CHANNEL}')
                await page.wait_for_load_state('domcontentloaded')
                await asyncio.sleep(3)

                goal_text = await page.locator('//h3[contains(@title,"Plus Goal")]/../../div[2]/div/div/div/div/div[2]/div[2]/p').all_text_contents()
                if len(goal_text) == 0:
                    return

                goal_text = goal_text[0].split(' ')[0]
                goal_text = f'partner+: {goal_text}/{GOAL_POINTS}'

                with open(FILE_PATH, 'w+') as f:
                    f.write(goal_text)
                    #print(goal_text)
            except PlaywrightTimeoutError as ex:
                print(str(ex))
                pass
            except Exception as ex:
                print(str(ex))
                pass
                        
            await browser.close()
    except Exception as ex:
        pass