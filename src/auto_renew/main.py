from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import time

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

if __name__ == "__main__":
	with sync_playwright() as sp:
		browser = sp.chromium.launch(headless=False)
		katabump = browser.new_page()
		katabump.goto("https://dashboard.katabump.com/auth/login", wait_until="domcontentloaded")

		# Login page
		katabump.fill("input[name='email']", EMAIL)
		katabump.fill("input[name='password']", PASSWORD)
		katabump.click("button#submit")

		# Dashboard
		with katabump.expect_navigation(wait_until="domcontentloaded"):
			katabump.click("a:has-text('See')")

		# Server
		with katabump.expect_navigation(wait_until="domcontentloaded"):
			katabump.click("button[data-bs-target='#renew-modal']:has-text('Renew')")
		with katabump.expect_navigation(wait_until="domcontentloaded"):
			katabump.click("button:has-text('Renew')")

		