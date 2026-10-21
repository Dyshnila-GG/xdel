# Generates the static site pages with a shared header/footer.
import pathlib, re

ROOT = pathlib.Path(__file__).parent
YEAR = "2026"
NAV = [("index.html", "Home"), ("publisher.html", "xDel Publisher"), ("about.html", "About"),
       ("contact.html", "Contact")]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://dyshnila-gg.github.io/xdel/assets/icon-512.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="index.html"><img src="assets/icon-192.png" alt="xDel | SO2 logo" width="40" height="40"><span><b>xDel</b> | SO2</span></a>
<nav>{nav}</nav>
</div></header>
<main class="wrap">
"""

FOOT = """</main>
<footer class="bottom"><div class="wrap">
<div class="fcol"><a class="brand small" href="index.html"><img src="assets/icon-192.png" alt="" width="28" height="28"><span><b>xDel</b> | SO2</span></a>
<p>Standoff 2 highlights by xDel.</p></div>
<div class="fcol"><h4>Site</h4><a href="index.html">Home</a><a href="publisher.html">xDel Publisher</a><a href="about.html">About</a><a href="contact.html">Contact</a></div>
<div class="fcol"><h4>Legal</h4><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></div>
<div class="fcol"><h4>Follow</h4><a href="https://www.youtube.com/channel/UC643AM3rb8-xDpk6DF4iEvQ" rel="noopener">YouTube</a><a href="https://www.tiktok.com/@xdel_xd" rel="noopener">TikTok</a><a href="https://www.instagram.com/xdel_fun/" rel="noopener">Instagram</a></div>
</div>
<div class="wrap copy">© """ + YEAR + """ xDel | SO2 · <a href="mailto:xdelionx1401@gmail.com">xdelionx1401@gmail.com</a></div>
</footer>
</body>
</html>
"""


def page(fname, title, desc, body):
    nav = "".join(f'<a href="{h}"{" class=on" if h == fname else ""}>{t}</a>' for h, t in NAV)
    (ROOT / fname).write_text(HEAD.format(title=title, desc=desc, nav=nav) + body.strip() + "\n" + FOOT)


page("index.html", "xDel | SO2 — Standoff 2 highlights",
     "xDel | SO2: Standoff 2 gameplay highlights, shorts and a community for players.", """
<section class="hero">
<img class="hero-logo" src="assets/icon-512.png" alt="xDel | SO2" width="180" height="180">
<div>
<h1><b>xDel</b> | SO2</h1>
<p class="lead">Standoff 2 gameplay highlights: clutches, multi-kills, knife rounds and case openings — cut into short videos you can watch in a minute.</p>
<div class="btns"><a class="btn" href="https://www.youtube.com/channel/UC643AM3rb8-xDpk6DF4iEvQ" rel="noopener">Watch on YouTube</a><a class="btn ghost" href="publisher.html">About xDel Publisher</a></div>
</div>
</section>

<section>
<h2>What you'll find here</h2>
<div class="grid">
<div class="card"><h3>Short highlights</h3><p>New Standoff 2 moments every day: -2, -3 and -4 rounds with AK-47, AWP, pistols and knives, each under a minute.</p></div>
<div class="card"><h3>Real matches</h3><p>Every clip is recorded from xDel's own ranked and casual games — no edits to the gameplay, just the best part of the round.</p></div>
<div class="card"><h3>Community</h3><p>The xDel | SO2 Discord server is where viewers play together, share their own clips and talk about the game. The invite link is in our social profiles.</p></div>
</div>
</section>

<section>
<h2>Where to watch</h2>
<div class="grid">
<a class="card link" href="https://www.youtube.com/channel/UC643AM3rb8-xDpk6DF4iEvQ" rel="noopener"><h3>YouTube Shorts</h3><p>Daily shorts and longer videos.</p></a>
<a class="card link" href="https://www.tiktok.com/@xdel_xd" rel="noopener"><h3>TikTok</h3><p>The same highlights in vertical format.</p></a>
<a class="card link" href="https://www.instagram.com/xdel_fun/" rel="noopener"><h3>Instagram Reels</h3><p>Reels with the best rounds of the week.</p></a>
</div>
</section>

<section>
<h2>How the videos are made</h2>
<ol class="steps">
<li><b>Record.</b> xDel records his Standoff 2 matches on his phone.</li>
<li><b>Pick the moment.</b> Rounds with two or more kills are selected and cut into a vertical short.</li>
<li><b>Publish.</b> Shorts are scheduled and published to xDel's own channels with <a href="publisher.html">xDel Publisher</a>, our in-house publishing tool.</li>
</ol>
</section>
""")

page("publisher.html", "xDel Publisher — publishing tool for xDel | SO2",
     "xDel Publisher is the in-house tool the xDel | SO2 creator uses to schedule and publish his own short videos.", """
<section class="hero">
<img class="hero-logo" src="assets/icon-512.png" alt="xDel Publisher" width="150" height="150">
<div>
<h1>xDel Publisher</h1>
<p class="lead">The in-house tool the xDel | SO2 creator uses to prepare, schedule and publish his own short gaming videos to YouTube, TikTok and Instagram from one place.</p>
</div>
</section>

<section>
<h2>Features</h2>
<div class="grid">
<div class="card"><h3>One upload, every platform</h3><p>Pick a finished short once and publish it to YouTube Shorts, TikTok and Instagram Reels together.</p></div>
<div class="card"><h3>Scheduling</h3><p>Choose "publish now", an exact date and time, or the next free daily time slot.</p></div>
<div class="card"><h3>Captions per platform</h3><p>Titles, descriptions and hashtags are prepared separately for each platform and can be edited before publishing.</p></div>
<div class="card"><h3>First comment</h3><p>A first comment with a question for viewers is added under each new video.</p></div>
<div class="card"><h3>Discord announcement</h3><p>When a new YouTube video goes live, an announcement is posted on the creator's own Discord server.</p></div>
<div class="card"><h3>History</h3><p>Every publication is logged with its status on each platform, so nothing is posted twice.</p></div>
</div>
</section>

<section>
<h2>How it works with TikTok</h2>
<ol class="steps">
<li><b>Connect.</b> The creator signs in with TikTok (Login Kit) and authorizes his own account. The app reads only basic profile info (name, avatar) to show which account is connected.</li>
<li><b>Prepare.</b> He selects a finished short, edits the caption and hashtags and chooses the privacy setting.</li>
<li><b>Publish.</b> The video is sent to his TikTok profile with the Content Posting API — either posted directly or uploaded to TikTok drafts for final editing in the TikTok app.</li>
<li><b>Track.</b> The app shows the post status and the creator's own public videos and basic stats so he can see how each short performs.</li>
</ol>
<p class="muted">xDel Publisher is used only by the owner of the xDel | SO2 channels for his own accounts. It is not offered to other users and never posts to anyone else's account.</p>
</section>

<section>
<h2>Data and privacy</h2>
<p>Access tokens and settings are stored on the creator's own computer. Nothing is sold or shared with third parties. Read the full <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms of Service</a>.</p>
</section>
""")

page("about.html", "About — xDel | SO2", "About xDel, the Standoff 2 player behind the xDel | SO2 channels.", """
<h1>About xDel | SO2</h1>
<p class="lead">xDel is a Standoff 2 player and content creator. The channel started as a way to save the best rounds from everyday matches — now it is a daily stream of short highlights and a growing community of players.</p>

<h2>The channel</h2>
<p>Every video comes from real matches played by xDel. Each short shows one round from start to finish: the entry, the kills and the result, without cuts inside the action. Videos are published on YouTube, TikTok and Instagram several times a day.</p>

<h2>The community</h2>
<p>The xDel | SO2 Discord server brings viewers together: team up for matches, post your own clips, take part in weekly games with xDel and get help with your account progress.</p>

<h2>Plans</h2>
<ul>
<li>Longer videos: case openings, skin collections and full matches with commentary.</li>
<li>Live streams with the community.</li>
<li>Viewer clip of the week — the best moment sent by a subscriber gets featured on the channel.</li>
</ul>
""")

page("contact.html", "Contact — xDel | SO2", "How to contact xDel | SO2.", """
<h1>Contact</h1>
<p class="lead">Questions, collaboration offers or problems with the site — write to us.</p>
<div class="grid">
<div class="card"><h3>Email</h3><p><a href="mailto:xdelionx1401@gmail.com">xdelionx1401@gmail.com</a></p><p class="muted">We usually reply within 1–2 days.</p></div>
<div class="card"><h3>Social</h3><p><a href="https://www.youtube.com/channel/UC643AM3rb8-xDpk6DF4iEvQ" rel="noopener">YouTube</a> · <a href="https://www.tiktok.com/@xdel_xd" rel="noopener">TikTok</a> · <a href="https://www.instagram.com/xdel_fun/" rel="noopener">Instagram</a></p><p class="muted">Direct messages are open on all platforms.</p></div>
<div class="card"><h3>Data requests</h3><p>To ask about data handled by xDel Publisher, see the <a href="privacy.html">Privacy Policy</a> or email us.</p></div>
</div>
""")

for f, title, desc in (("privacy.html", "Privacy Policy — xDel Publisher", "Privacy Policy of xDel Publisher."),
                       ("terms.html", "Terms of Service — xDel Publisher", "Terms of Service of xDel Publisher.")):
    body = (ROOT / "legal" / (f + ".body")).read_text()
    page(f, title, desc, '<article class="legal">' + body + "</article>")
