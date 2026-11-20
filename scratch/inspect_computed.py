import subprocess

script = '''
window.onload = function() {
  const knot = document.querySelector('.fam-knot');
  const card = document.querySelector('.fam-card');
  const amp = document.querySelector('.fam-knot__amp');
  const l1 = document.querySelectorAll('.fam-knot__line')[0];
  const l2 = document.querySelectorAll('.fam-knot__line')[1];
  
  const csKnot = window.getComputedStyle(knot);
  const csCard = window.getComputedStyle(card);
  const csAmp = window.getComputedStyle(amp);
  
  const report = {
    card_rect: card.getBoundingClientRect(),
    knot_rect: knot.getBoundingClientRect(),
    amp_rect: amp.getBoundingClientRect(),
    l1_rect: l1.getBoundingClientRect(),
    l2_rect: l2.getBoundingClientRect(),
    knot_flex_dir: csKnot.flexDirection,
    knot_justify: csKnot.justifyContent,
    knot_align: csKnot.alignItems,
    knot_margin: csKnot.margin,
    card_display: csCard.display,
    card_grid_cols: csCard.gridTemplateColumns,
    card_padding: csCard.padding
  };
  
  const pre = document.createElement('pre');
  pre.id = 'report';
  pre.textContent = JSON.stringify(report, null, 2);
  document.body.appendChild(pre);
};
'''

with open(r'd:\wedding-card\scratch\test_metric.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace script
idx1 = c.find('<script>')
idx2 = c.find('</script>') + 9
c = c[:idx1] + f'<script>{script}</script>' + c[idx2:]

with open(r'd:\wedding-card\scratch\test_metric.html', 'w', encoding='utf-8') as f:
    f.write(c)

cmd = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    '--headless=new',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=412,1200',
    '--screenshot=d:/wedding-card/scratch/test_report.png',
    'file:///d:/wedding-card/scratch/test_metric.html'
]
subprocess.run(cmd, check=True)
print("Rendered test_report.png")

