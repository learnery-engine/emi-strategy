#!/usr/bin/env python3
"""Capture screenshots of Learneris sites using Playwright."""
import os
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "/Users/kelsienguyen/Documents/LRN/EMI/emi-strategy/assets/screenshots"

def scroll_and_trigger_animations(page):
    """Scroll through the page to trigger all scroll-based animations, then return to top."""
    page.evaluate("""
        async () => {
            const totalHeight = document.body.scrollHeight;
            const step = 400;
            for (let y = 0; y <= totalHeight; y += step) {
                window.scrollTo(0, y);
                await new Promise(r => setTimeout(r, 100));
            }
            window.scrollTo(0, 0);
            await new Promise(r => setTimeout(r, 500));
        }
    """)

def capture_site(page, url, prefix, wait_for_selector=None):
    print(f"\n--- Capturing {url} ---")
    page.goto(url, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2000)

    if wait_for_selector:
        try:
            page.wait_for_selector(wait_for_selector, timeout=5000)
        except:
            pass

    # Take initial viewport screenshot (hero/above-fold)
    hero_path = os.path.join(OUTPUT_DIR, f"{prefix}-hero.png")
    page.screenshot(path=hero_path, clip={"x": 0, "y": 0, "width": 1440, "height": 900})
    print(f"  Saved hero: {hero_path}")

    # Scroll to trigger animations
    scroll_and_trigger_animations(page)
    page.wait_for_timeout(1000)

    # Full-page screenshot
    full_path = os.path.join(OUTPUT_DIR, f"{prefix}-full.png")
    page.screenshot(path=full_path, full_page=True)
    print(f"  Saved full page: {full_path}")

    # Also take section screenshots at key scroll positions
    total_height = page.evaluate("document.body.scrollHeight")
    viewport_height = 900
    sections = ["features", "how-it-works", "programs", "testimonials"]
    for section_id in sections:
        el = page.query_selector(f"#{section_id}")
        if el:
            el.scroll_into_view_if_needed()
            page.wait_for_timeout(600)
            section_path = os.path.join(OUTPUT_DIR, f"{prefix}-section-{section_id}.png")
            page.screenshot(path=section_path, clip={"x": 0, "y": 0, "width": 1440, "height": viewport_height})
            print(f"  Saved section #{section_id}: {section_path}")

    return total_height

def extract_image_urls(page):
    """Extract all image and asset URLs from the page."""
    return page.evaluate("""
        () => {
            const results = new Set();
            // img tags
            document.querySelectorAll('img').forEach(el => {
                if (el.src) results.add(el.src);
                if (el.getAttribute('srcset')) {
                    el.getAttribute('srcset').split(',').forEach(s => {
                        const url = s.trim().split(' ')[0];
                        if (url) results.add(url);
                    });
                }
            });
            // picture/source tags
            document.querySelectorAll('source').forEach(el => {
                if (el.srcset) results.add(el.srcset);
            });
            // background-image styles
            document.querySelectorAll('*').forEach(el => {
                const bg = window.getComputedStyle(el).backgroundImage;
                if (bg && bg !== 'none' && bg.includes('url(')) {
                    const match = bg.match(/url\\(["']?([^"')]+)["']?\\)/);
                    if (match) results.add(match[1]);
                }
            });
            // data-src lazy loaded
            document.querySelectorAll('[data-src]').forEach(el => results.add(el.getAttribute('data-src')));
            return Array.from(results).filter(u => u && !u.startsWith('data:') && u.length > 5);
        }
    """)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()

    # ---- 1. learneris.com ----
    capture_site(page, "https://www.learneris.com", "learneris-com")
    imgs = extract_image_urls(page)
    print(f"\n  Image URLs found on learneris.com ({len(imgs)}):")
    for url in imgs:
        print(f"    {url}")

    # ---- 2. ai.learneris.com ----
    capture_site(page, "https://ai.learneris.com", "ai-learneris")
    ai_imgs = extract_image_urls(page)
    print(f"\n  Image URLs found on ai.learneris.com ({len(ai_imgs)}):")
    for url in ai_imgs:
        print(f"    {url}")

    # ---- 3. studio.learneris.com ----
    capture_site(page, "https://studio.learneris.com", "studio-learneris")
    studio_imgs = extract_image_urls(page)
    print(f"\n  Image URLs found on studio.learneris.com ({len(studio_imgs)}):")
    for url in studio_imgs:
        print(f"    {url}")

    browser.close()
    print("\n\nAll screenshots saved to:", OUTPUT_DIR)
    print("Files:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith('.png'):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
            print(f"  {f} ({size//1024}KB)")
