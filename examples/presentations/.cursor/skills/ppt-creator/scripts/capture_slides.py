"""
Playwright screenshot capture for HTML slides.

Adapt SLIDES and HTML_FILE to your project. Run from the project root:
    python capture_slides.py
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = "slides.html"
OUTPUT_DIR = "screenshots"

# Define your slides: (css_selector, total_click_steps)
# steps=0 means static (capture once with everything visible)
# steps=N means capture N+1 frames (base + one per click)
SLIDES = [
    (".s1", 0),   # static slide
    (".s2", 5),   # animated: 5 clicks = 6 frames (base through step 5)
    (".s3", 0),   # static slide
]


async def capture():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    abs_path = Path(HTML_FILE).resolve()

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
        )
        await page.goto(f"file://{abs_path}")
        await page.wait_for_timeout(1000)

        for selector, steps in SLIDES:
            el = page.locator(selector)
            name = selector.replace(".", "")

            if steps == 0:
                # Static: reveal all data-step elements then capture
                await page.evaluate(f"""() => {{
                    const el = document.querySelector('{selector}');
                    el.querySelectorAll('[data-step]').forEach(e => e.classList.add('show'));
                }}""")
                await page.wait_for_timeout(500)
                await el.screenshot(path=f"{OUTPUT_DIR}/{name}.png")
                print(f"  {name}.png (static)")
            else:
                # Animated: capture base frame then one frame per click
                # Base frame (nothing revealed yet)
                await page.evaluate(f"""() => {{
                    const el = document.querySelector('{selector}');
                    el.querySelectorAll('[data-step]').forEach(e => e.classList.remove('show'));
                }}""")
                await page.wait_for_timeout(300)
                await el.screenshot(path=f"{OUTPUT_DIR}/{name}_step0.png")
                print(f"  {name}_step0.png (base)")

                for i in range(1, steps + 1):
                    await page.evaluate(f"""() => {{
                        const el = document.querySelector('{selector}');
                        el.querySelectorAll('[data-step]').forEach(e => {{
                            if (parseInt(e.dataset.step) <= {i}) e.classList.add('show');
                            else e.classList.remove('show');
                        }});
                    }}""")
                    await page.wait_for_timeout(500)
                    await el.screenshot(path=f"{OUTPUT_DIR}/{name}_step{i}.png")
                    print(f"  {name}_step{i}.png")

        await browser.close()
    print(f"\nAll screenshots saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(capture())
