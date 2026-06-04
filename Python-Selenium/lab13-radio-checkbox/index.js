import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const browser = await puppeteer.launch();
const page = await browser.newPage();

const filePath = `file:${path.join(__dirname, 'index.html')}`;
await page.goto(filePath);

// Select radio button
await page.click('input[name="fruit"][value="banana"]');
console.log('Selected radio: Banana');

// Select checkboxes
await page.click('input[name="hobbies"][value="reading"]');
await page.click('input[name="hobbies"][value="travelling"]');
console.log('Selected checkboxes');

// Get selected values
const selected = await page.evaluate(() => {
  return Array.from(document.querySelectorAll('input:checked'))
    .map(el => `${el.type}-${el.value}`);
});

console.log('Selected values:', selected);

await browser.close();
