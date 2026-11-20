import subprocess

# Run Chrome with --dump-dom
cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,1200',
    '--dump-dom',
    'file:///d:/wedding-card/scratch/test_metric.html'
]
res = subprocess.run(cmd, capture_output=True, text=True)
dom = res.stdout
if '<pre id="report">' in dom:
    start = dom.find('<pre id="report">') + len('<pre id="report">')
    end = dom.find('</pre>', start)
    print("REPORT JSON:\n", dom[start:end])
else:
    print("Report not found in DOM")

