// scraper1.ts

import { chromium } from 'playwright';

async function scrapeTitle(url: string) {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto(url);
    const title = await page.title();
    console.log(`Title of ${url}: ${title}`);
    await browser.close();
}

scrapeTitle('https://instagram.com');
