from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

if __name__ == "__main__":
	with sync_playwright() as sp:
		browser = sp.chromium.launch(headless=True)
		katabump = browser.new_page()
		katabump.goto("https://dashboard.katabump.com/auth/login")

		# Login page
		katabump.fill("input[name='username']", ID)
		katabump.fill("input[name='password']", PASSWORD)
		katabump.click("text=Login")

		# Dashboard
		katabump.click("text=Manage server")