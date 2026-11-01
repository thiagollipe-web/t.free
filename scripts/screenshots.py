"""Capture local-only review images; never publish or deploy the website."""
import functools,http.server,os,threading,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
output=root/'screenshots';output.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as folder:
 Path(folder,'t.free').symlink_to(root,target_is_directory=True)
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=folder))
 threading.Thread(target=server.serve_forever,daemon=True).start()
 try:
  with sync_playwright() as p:
   browser=p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or None)
   for width,label in [(1440,'desktop'),(390,'mobile')]:
    page=browser.new_page(viewport={'width':width,'height':1000})
    page.goto(f'http://127.0.0.1:{server.server_port}/t.free/');page.wait_for_selector('#filters button')
    page.screenshot(path=str(output/(label+'-home.png')),full_page=True)
    page.screenshot(path=str(output/(label+'-hero.png')))
    page.locator('#grid').screenshot(path=str(output/(label+'-cards.png')))
    page.locator('#grid .compare-pick input').nth(0).check();page.locator('#grid .compare-pick input').nth(1).check();page.locator('#compare-open').click()
    page.locator('#comparison').screenshot(path=str(output/(label+'-comparison.png')))
    page.goto(f'http://127.0.0.1:{server.server_port}/t.free/ferramentas/chatgpt/')
    page.screenshot(path=str(output/(label+'-tool.png')),full_page=True);page.close()
   browser.close()
 finally:server.shutdown();server.server_close()
