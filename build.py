#!/usr/bin/env python3
# Builds the Maharaja London static site (shared head/header/footer).
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

IMG = {
 'thali_round':'https://images.unsplash.com/photo-1546833999-b9f581a1996d',
 'platter':    'https://images.unsplash.com/photo-1742281258189-3b933879867a',
 'silver':     'https://images.unsplash.com/photo-1680993032090-1ef7ea9b51e5',
 'thali_side': 'https://images.unsplash.com/photo-1742281257687-092746ad6021',
 'thali_var':  'https://images.unsplash.com/photo-1742281257707-0c7f7e5ca9c6',
 'spread':     'https://images.unsplash.com/photo-1659907521212-8bbdfa688aa6',
 'wooden':     'https://images.unsplash.com/photo-1725167260486-255a40ce00e3',
 'fish':       'https://images.unsplash.com/photo-1756741987051-a6a38f28838b',
 'tray_pita':  'https://images.unsplash.com/photo-1671970922492-4d2a4c7a2ffe',
 'variety':    'https://images.unsplash.com/photo-1559561724-732dbca7be1e',
 'metal_tray': 'https://images.unsplash.com/photo-1711153419402-336ee48f2138',
 'sari':       'https://images.unsplash.com/photo-1761391464085-e88d8dc5dfa6',
}
def img(key, w=900, q=80):
    return f"{IMG[key]}?auto=format&fit=crop&w={w}&q={q}"

NAV = [("index.html","Home"),("about.html","Our Story"),("menus.html","The Menus"),
       ("services.html","Services"),("gallery.html","Gallery"),("venues.html","Venues"),("journal.html","Journal")]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" type="image/png" href="assets/img/favicon.png" />
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500&family=Marcellus&family=Mukta:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="assets/css/styles.css" />
</head>
<body>
"""

def header(active):
    links = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        links += f'      <a href="{href}"{cls}>{label}</a>\n'
    mlinks = "".join(f'    <a href="{h}">{l}</a>\n' for h,l in NAV)
    return f"""<header id="hdr">
  <nav>
    <a href="index.html" class="brand">
      <span class="wm gold-text">Maharaja<small>London</small></span>
    </a>
    <div class="navlinks">
{links}      <a href="contact.html" class="btn btn-gold nav-cta">Enquire</a>
    </div>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </nav>
  <div class="mobile-menu" id="mobileMenu">
{mlinks}    <a href="contact.html">Enquire</a>
  </div>
</header>
"""

FOOTER = """<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="index.html" class="brand">
          <span class="wm gold-text">Maharaja<small>London</small></span>
        </a>
        <p>Award-winning Indian &amp; Asian wedding catering and event design, bringing the grandeur of the royal table to London's finest celebrations for over two decades.</p>
        <div class="socials">
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9V7c0-1 .5-1.5 1.5-1.5H17V2h-2.5C12 2 11 4 11 6v3H8v3h3v9h3v-9h2.5l.5-3z"/></svg></a>
          <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M5 4a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zM4 9h3v11H4zM10 9h3v1.6c.5-.9 1.7-1.8 3.4-1.8 3 0 3.6 2 3.6 4.6V20h-3v-5.2c0-1.2-.4-2.1-1.6-2.1s-1.8.9-1.8 2V20h-3z"/></svg></a>
        </div>
      </div>
      <div class="foot-col">
        <h5>Explore</h5>
        <a href="about.html">Our Story</a>
        <a href="menus.html">The Menus</a>
        <a href="services.html">Services</a>
        <a href="gallery.html">Gallery</a>
        <a href="venues.html">Venues</a>
        <a href="journal.html">Journal</a>
      </div>
      <div class="foot-col">
        <h5>Get in Touch</h5>
        <a href="tel:+442000000000">+44 (0)20 0000 0000</a>
        <a href="mailto:enquiries@maharaja.co.uk">enquiries@maharaja.co.uk</a>
        <a href="contact.html">Request a Tasting</a>
        <a href="#top">Back to top &uarr;</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="year">2026</span> Maharaja London Ltd &middot; All rights reserved</span>
      <span>Crafted with heritage &middot; London</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>"""

SEAL = '<svg class="seal" viewBox="0 0 60 60" fill="none"><circle cx="30" cy="30" r="28" stroke="#c2a14e" stroke-width="1"/><circle cx="30" cy="30" r="22" stroke="#c2a14e" stroke-width="1" opacity=".5"/><path d="M30 16l3.5 8.5L42 25l-6 6 1.5 9L30 35.5 22.5 40 24 31l-6-6 8.5-.5z" fill="#e7ce87"/></svg>'
STAMP = '<svg class="stamp" viewBox="0 0 120 120" fill="none" aria-hidden="true"><circle cx="60" cy="60" r="58" stroke="#c2a14e"/><circle cx="60" cy="60" r="44" stroke="#c2a14e" opacity=".4"/><path id="cp" d="M60 60 m-50 0 a50 50 0 1 1 100 0 a50 50 0 1 1 -100 0" fill="none"/><text fill="#c2a14e" font-size="9" letter-spacing="3.4" font-family="Marcellus"><textPath href="#cp" startOffset="0">&#183; CRAFTED WITH HERITAGE &#183; SERVED WITH PRIDE </textPath></text><path d="M60 46l3 8 8 .5-6 5 2 8-7-4.5-7 4.5 2-8-6-5 8-.5z" fill="#e7ce87"/></svg>'

def arch(key, w=900):
    return f'<div class="arch"><div class="archinner"><img src="{img(key,w)}" alt="" /></div></div>'

def trust():
    return """<div class="trust">
  <div class="wrap">
    <span class="label">Wedding Caterer of the Year &middot; UK</span>
    <div class="venues"><span>Two decades at Britain's finest venues</span></div>
    <div class="stars"><b>4.6</b><small>&#9733;&#9733;&#9733;&#9733;&#9733;<br/>583 verified reviews</small></div>
  </div>
</div>"""

# Reusable logo wall. Each item is (label, sublabel-or-None).
# To use a REAL logo later, swap the <span> for: <img src="assets/img/logos/NAME.png" alt="NAME" />
def logo_wall(eyebrow, heading, items, darker=False):
    cells = ""
    for label, sub in items:
        subhtml = f"<small>{sub}</small>" if sub else ""
        cells += f'<div class="logo-cell"><div><span>{label}</span>{subhtml}</div></div>'
    sec = "darker" if darker else "dark"
    return f"""<section class="{sec} pad-sm">
  <div class="wrap">
    <div class="wall-head reveal"><span class="eyebrow c">{eyebrow}</span><h3>{heading}</h3></div>
    <div class="logo-wall reveal">{cells}</div>
  </div>
</section>"""

LAUREL = '<svg class="laurel" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M24 6v30"/><path d="M24 12c-5-4-10-3-12-1 1 4 5 7 12 7M24 12c5-4 10-3 12-1-1 4-5 7-12 7"/><path d="M24 22c-5-4-10-3-12-1 1 4 5 7 12 7M24 22c5-4 10-3 12-1-1 4-5 7-12 7"/><path d="M18 40h12"/></svg>'

def awards():
    rows = [("Wedding Caterer of the Year","Britain's Asian Wedding Awards","2018"),
            ("4.6 / 5","From 583 Verified Reviews","Ongoing"),
            ("Recommended Caterer","At Britain's Finest Venues","Trusted"),
            ("Highly Recommended","By Couples &amp; Planners","Word of Mouth")]
    cards = "".join(f'<div class="award reveal">{LAUREL}<div class="org">{o}</div><h4>{t}</h4><div class="year">{y}</div></div>' for t,o,y in rows)
    return f"""<section class="darker pad">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow c">Awards &amp; Accolades</span><h2>Recognised for the work.</h2></div>
    <div class="awards-row">{cards}</div>
  </div>
</section>"""

# --- Journal posts (migrated & polished from the original Maharaja site) -----
POSTS = [
 {"slug":"wedding-caterer-of-the-year.html","title":"Maharaja Named Wedding Caterer of the Year",
  "date":"February 2018","cat":"Maharaja News","img":"https://maharaja.co.uk/wp-content/uploads/2018/02/Sam-Patel-Maharaja-820x820.jpg",
  "excerpt":"Recognised on a national stage at Britain's Asian Wedding Awards &mdash; a night celebrating the very best of the UK's Asian wedding industry.",
  "body":"""<p>Maharaja London has been named <strong>Wedding Caterer of the Year</strong> at Britain's Asian Wedding Awards &mdash; a recognition our whole team were thrilled to receive on a national stage.</p>
<p>The black-tie ceremony, only the second of its kind in Britain, was held at the Sheraton in London in February 2018. The evening brought together some of the industry's biggest names to celebrate the craft, progress and innovation of the UK's Asian wedding sector, with more than fifty awards presented across the night.</p>
<blockquote>It's a rarity for us to be on the other side of the kitchen. None of this would be within reach without our chefs, waiters and hosts &mdash; and our customers, for letting us play a part in their big day.<cite>Sam Patel, Maharaja London</cite></blockquote>
<p>To us, an award like this was never a trophy for the shelf. It's a reflection of every plate sent out, every late night in the kitchen, and every couple who trusted us with the most important day of their lives &mdash; and it's the standard we've held ourselves to at every event since.</p>
<p>To talk to us about catering your celebration, <a href="contact.html">request a private tasting</a>.</p>"""},

 {"slug":"unforgettable-weddings.html","title":"Five Ways to Make Your Wedding Unforgettable",
  "date":"July 2019","cat":"Weddings","img":"https://maharaja.co.uk/wp-content/uploads/2017/11/Maharaja-Highgate-201710-LR-24-580x400.jpg",
  "excerpt":"From destination celebrations to statement venues &mdash; inspiration for couples who want their day to feel like no one else's.",
  "body":"""<p>No matter how you celebrate, a wedding is always a special occasion. But for guests who attend several a year, the familiar rhythm can begin to feel the same. Here are five ways couples are making their day feel entirely their own.</p>
<h3>The destination wedding</h3>
<p>A celebration abroad gives your guests something they'll never forget &mdash; a wedding wrapped inside a holiday. Whether it's white sand and palm trees or somewhere closer to home, it buys you precious, unhurried time with the people you love. The art is choosing somewhere your guests can comfortably reach, so no one is left behind.</p>
<h3>The weekend wedding</h3>
<p>Why let the celebration end at midnight? A weekend wedding &mdash; often at a country house taken over for the occasion &mdash; lets everyone truly unwind, free of the clock-watching that single-day events demand. The atmosphere is softer, the memories deeper.</p>
<h3>The statement venue</h3>
<p>Galleries, museums and the country's most dramatic spaces increasingly open their doors for weddings. Think about the rooms in your city that take the breath away, and ask what they can offer &mdash; a remarkable setting does half the storytelling for you.</p>
<h3>The festival wedding</h3>
<p>For couples who love a party, a festival-style celebration brings entertainment, food and a relaxed, open-air spirit all at once. Handle the legalities the traditional way, and let the day itself be pure joy.</p>
<h3>The intimate gathering</h3>
<p>Sometimes the most memorable weddings are the smallest &mdash; a marquee in the garden, a handful of the people who matter most, and food made with real care. Less spectacle, more feeling.</p>
<p>We've catered destination and out-of-the-ordinary weddings of every kind. <a href="contact.html">Tell us what you're dreaming of</a> and we'll help bring it to the table.</p>"""},

 {"slug":"why-indian-food.html","title":"Why Indian Food Is Good for the Soul",
  "date":"August 2017","cat":"Foody Stuff","img":"https://maharaja.co.uk/wp-content/uploads/2015/11/4-FoodProductShots09-580x400.jpg",
  "excerpt":"The aromas, the spice, the warmth &mdash; there's a reason a good Indian meal makes you feel cared for. A few of them, actually.",
  "body":"""<p>Anyone who has enjoyed a meal made with love and care knows how special this food can be. The aromas, the layered flavours, the textures of Indian cooking do far more than excite the palate &mdash; many of them carry quiet, time-honoured benefits too.</p>
<h3>Built on more than taste</h3>
<p>Researchers studying traditional Indian recipes have found that the way ingredients are combined may have roots in centuries of medicinal wisdom &mdash; which might explain why certain dishes feel genuinely soothing, clearing the head and settling the stomach.</p>
<h3>The power of spice</h3>
<p>Spice sits at the very heart of Indian cooking, and it's no accident. Turmeric, coriander, cumin and chilli don't just define the flavour &mdash; many double as some of nature's most celebrated superfoods.</p>
<h3>Warmth in a bowl</h3>
<p>A good homemade curry is built from warming ingredients &mdash; slow-cooked spice and depth that hits exactly the right spot on a cold or weary day. Comfort, in the most literal sense.</p>
<h3>A natural lift</h3>
<p>The fiery chillies in many curries have long been linked to a release of endorphins &mdash; a small, delicious boost to your mood and energy.</p>
<p>Great food, of any kind, begins with great ingredients and an honest hand &mdash; the two things our kitchen has always insisted on. <a href="menus.html">Explore our menus</a> to see where that takes us.</p>"""},
]

def journal_teaser():
    cards = ""
    for p in POSTS:
        cards += f"""<a href="{p['slug']}" class="post-card reveal"><div class="thumb"><img src="{p['img']}" alt="{p['title']}" /></div>
        <div class="pc-body"><span class="cat">{p['cat']}</span><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="more">Read More</span></div></a>"""
    return f"""<section class="dark pad" id="journal">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow c">The Journal</span><h2>Stories from the kitchen.</h2><p>News, ideas and a little inspiration from the Maharaja table.</p></div>
    <div class="journal-grid">{cards}</div>
  </div>
</section>"""

def cta():
    return """<section class="cta-band">
  <div class="wrap reveal">
    <span class="eyebrow c">Begin the Conversation</span>
    <h2 style="margin-top:22px">Let us set your table.</h2>
    <p>Tell us about your celebration and we'll arrange a private tasting with our chefs &mdash; no obligation, simply a conversation about the day you have in mind.</p>
    <a href="contact.html" class="btn btn-gold">Request a Tasting</a>
  </div>
</section>"""

# service icons
ICONS = {
 'wedding':'<svg class="ico" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="18" cy="28" r="11"/><circle cx="30" cy="28" r="11"/><path d="M14 16l4-6 4 6M26 16l4-6 4 6"/></svg>',
 'corp':'<svg class="ico" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="8" y="16" width="32" height="24" rx="2"/><path d="M18 16v-4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v4M8 26h32"/></svg>',
 'private':'<svg class="ico" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M24 6c4 6 8 9 8 15a8 8 0 0 1-16 0c0-6 4-9 8-15z"/><path d="M16 40h16M20 40v-4h8v4"/></svg>',
 'bespoke':'<svg class="ico" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M24 8l3 10 10 3-10 3-3 10-3-10-10-3 10-3z"/><path d="M37 9l1.5 4 4 1.5-4 1.5L37 21l-1.5-4-4-1.5 4-1.5z"/></svg>',
}

def write(name, body):
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(body)
    print("wrote", name)

# ============================ HOME ============================
# --- Logo wall data ---------------------------------------------------------
# VENUES are real (from the original site). Partners are honest CATEGORY
# placeholders — swap each <span> for a real <img> logo when you have them.
VENUE_LOGOS = [("The Mayfair Hotel","London"),("Hilton London Bankside","London"),("Grand Connaught Rooms","London"),
 ("Mercedes-Benz World","Surrey"),("Hilton London Metropole","London"),("Radisson Blu Edwardian","Heathrow"),
 ("Novotel London West","Hammersmith"),("Newbury Racecourse","Berkshire"),("The Garden Room","Syon Park"),("Vale Resort","Cardiff")]

PARTNER_LOGOS = [("Champagne &amp; Wine",None),("Premium Spirits",None),("Fine Beverages",None),("Luxury Travel",None),
 ("Asian Media",None),("Floristry",None),("Photography &amp; Film",None),("Rice &amp; Grains",None),
 ("Event Production",None),("D&eacute;cor &amp; Staging",None)]

# Real Maharaja photography pulled from the live original site (food, prep & events).
# NOTE: these are hot-linked from maharaja.co.uk. Before pointing that domain at this
# new site, run scripts/get-photos.command to download them locally (see README).
_R = "https://maharaja.co.uk/wp-content/uploads/2015/11/"
_H = "https://maharaja.co.uk/wp-content/uploads/2017/11/"
REAL_GALLERY = [
 (_R+"4-FoodProductShots09-580x400.jpg","g-big"),
 (_H+"Maharaja-Highgate-201710-LR-18-580x400.jpg","g-tall"),
 (_R+"4-FoodProductShots11-580x400.jpg",""),
 (_R+"2-FoodPreparation-07-580x400.jpg",""),
 (_R+"4-FoodProductShots20-580x400.jpg","g-wide"),
 (_H+"Maharaja-Highgate-201710-LR-47-580x400.jpg",""),
 (_R+"4-FoodProductShots13-580x400.jpg","g-wide"),
 (_R+"2-FoodPreparation-13-580x400.jpg","g-tall"),
 (_R+"4-FoodProductShots16-580x400.jpg",""),
 (_H+"Maharaja-Highgate-201710-LR-24-580x400.jpg","g-wide"),
 (_R+"4-FoodProductShots22-580x400.jpg",""),
 (_R+"4-FoodProductShots02-580x400.jpg",""),
]

home = head("Maharaja &mdash; Royal Indian Wedding Catering &amp; Events, London",
            "Award-winning Indian &amp; Asian wedding catering and event design in London. A feast fit for royalty, served at Britain's finest venues.")
home += header("index.html")
home += f"""<main id="top">
<section class="hero">
  <div class="jali"></div>
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">Award-Winning Indian &amp; Asian Wedding Catering &middot; London</span>
      <h1>A Feast Fit<br/>For <em>Royalty.</em></h1>
      <p class="lead">For over two decades, Maharaja has brought the grandeur of the Indian table to Britain's most celebrated weddings &mdash; menus crafted with heritage, served with the kind of care reserved for kings and queens.</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-gold">Request a Tasting</a>
        <a href="menus.html" class="btn btn-ghost">Explore the Menus</a>
      </div>
      <div class="hero-badge">{SEAL}<div><b>Wedding Caterer of the Year</b><small>National industry award &mdash; UK</small></div></div>
    </div>
    <div class="hero-visual reveal">
      {arch('thali_round',1100)}
      <div class="hero-float"><div class="num">4.6<span style="font-size:1rem;color:var(--gold)">&#9733;</span></div><div class="lbl">583 reviews</div></div>
    </div>
  </div>
  <div class="scrollcue">Scroll<i></i></div>
</section>

{trust()}

<section class="dark pad" id="story">
  <div class="wrap"><div class="split reveal">
    <div class="split-visual">{arch('platter',1000)}{STAMP}</div>
    <div class="split-body">
      <span class="eyebrow">Our Story</span>
      <h2>Three generations of<br/>the royal kitchen.</h2>
      <!-- TODO: drop in the REAL heritage line here, e.g. "Since 19XX, from <place>, the <family> family..." — this dated origin story is the single strongest credibility signal. -->
      <p>Maharaja was born from a simple belief: the food at the heart of a celebration should be worthy of the moment. What began as a family kitchen has grown into one of London's most decorated Asian catering houses &mdash; without ever losing the hand of the home cook.</p>
      <p>Every menu is composed, never copied; every event tasted, refined and tasted again until it is unmistakably yours.</p>
      <a href="about.html" class="btn btn-ghost" style="margin-top:10px">Read Our Story</a>
    </div>
  </div></div>
</section>

{logo_wall("The Houses That Trust Us", "Welcomed at Britain's most distinguished venues.", VENUE_LOGOS)}

<section class="darker pad" id="menus">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow c">The Menus</span><h2>Composed like a banquet,<br/>tasted like a memory.</h2><p>Four signature tables, each a world of its own &mdash; and every one shaped entirely around your day, your guests and your traditions.</p></div>
    <div class="menu-grid">
      <div class="dish reveal">{arch('silver',800)}<span class="kicker">North &middot; Mughlai</span><h3>The Royal Table</h3><p>Slow-cooked biryanis, velvet kormas and tandoor-charred kebabs from the imperial courts.</p></div>
      <div class="dish reveal">{arch('thali_side',800)}<span class="kicker">South &middot; Coastal</span><h3>The Coastal Feast</h3><p>Coconut, curry leaf and tamarind; dosas, appams and fragrant seafood of the Malabar shore.</p></div>
      <div class="dish reveal">{arch('spread',800)}<span class="kicker">Live &middot; Street</span><h3>The Chaat Bazaar</h3><p>Theatre on the plate &mdash; live chaat counters, golgappa and a roaming street-food carnival.</p></div>
      <div class="dish reveal">{arch('tray_pita',800)}<span class="kicker">Modern &middot; Fusion</span><h3>The Grand Fusion</h3><p>Heritage flavours, contemporary plating &mdash; canap&eacute;s and tasting courses for the modern celebration.</p></div>
    </div>
    <div class="center" style="margin-top:54px"><a href="menus.html" class="btn btn-gold reveal">View Full Menus</a></div>
  </div>
</section>

<section class="light pad" id="services">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow dark c">What We Do</span><h2>From the first guest to the last.</h2><p>More than caterers &mdash; a single house to design, cook and run your entire celebration with calm and grace.</p></div>
    <div class="svc-grid reveal">
      <div class="svc">{ICONS['wedding']}<h3>Weddings</h3><p>Multi-day Asian weddings catered end to end &mdash; mehndi, ceremony and reception, each with its own menu.</p></div>
      <div class="svc">{ICONS['corp']}<h3>Corporate</h3><p>Galas, launches and award dinners delivered to the standard your brand and clients expect.</p></div>
      <div class="svc">{ICONS['private']}<h3>Private &amp; Intimate</h3><p>Milestone birthdays, anniversaries and home dinners &mdash; the same kitchen, a closer table.</p></div>
      <div class="svc">{ICONS['bespoke']}<h3>Bespoke Design</h3><p>D&eacute;cor, mandap styling and planning woven seamlessly around the food for one effortless day.</p></div>
    </div>
  </div>
</section>

{awards()}

<section class="dark pad" id="gallery">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow c">The Gallery</span><h2>Tables we've been proud to set.</h2></div>
    <div class="gal-grid reveal">
      <figure class="g-big"><img src="{REAL_GALLERY[0][0]}" alt="Maharaja plated dish" /></figure>
      <figure class="g-tall"><img src="{REAL_GALLERY[1][0]}" alt="Maharaja event" /></figure>
      <figure><img src="{REAL_GALLERY[2][0]}" alt="Maharaja dish" /></figure>
      <figure><img src="{REAL_GALLERY[3][0]}" alt="Food preparation" /></figure>
      <figure class="g-wide"><img src="{REAL_GALLERY[4][0]}" alt="Maharaja dish" /></figure>
      <figure><img src="{REAL_GALLERY[5][0]}" alt="Maharaja event" /></figure>
      <figure class="g-wide"><img src="{REAL_GALLERY[6][0]}" alt="Maharaja dish" /></figure>
    </div>
    <div class="center" style="margin-top:46px"><a href="gallery.html" class="btn btn-ghost reveal">See the Full Gallery</a></div>
  </div>
</section>

<section class="darker pad" id="reviews">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow c">Kind Words</span><h2>Loved by couples &amp; planners alike.</h2></div>
    <div class="rev-grid">
      <div class="review reveal"><span class="qm">&ldquo;</span><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><h4>5-star service</h4><p>Thank you so much, Maharaja, for the fantastic service. All our guests absolutely loved the experience.</p><div class="who">Pooja Sharma &mdash; Bride</div></div>
      <div class="review reveal"><span class="qm">&ldquo;</span><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><h4>The best I've worked with</h4><p>I'm an event planner, and recently planned a reception for a VIP client with many fine details. Maharaja made everything possible &mdash; my clients have asked me to book them again.</p><div class="who">Charlotte North &mdash; Event Planner</div></div>
      <div class="review reveal"><span class="qm">&ldquo;</span><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><h4>A job well done</h4><p>We were highly recommended Maharaja by a close friend &mdash; now I know why. Great food, great service, great company, from start to finish.</p><div class="who">Surinder Sandhu &mdash; Father of the Bride</div></div>
    </div>
  </div>
</section>

{journal_teaser()}

{cta()}
</main>
"""
home += FOOTER
write("index.html", home)

# ============================ ABOUT ============================
about = head("Our Story &mdash; Maharaja London", "The heritage, craft and family behind Maharaja, London's award-winning Indian wedding caterer.")
about += header("about.html")
about += f"""<main id="top">
<section class="banner">
  <div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">Our Story</span><h1>Heritage on every plate.</h1><p>Three generations, one kitchen, and an unwavering belief that great food is the truest form of hospitality.</p><div class="crumbs"><a href="index.html">Home</a> &middot; Our Story</div></div>
</section>

<section class="dark pad">
  <div class="wrap"><div class="split reveal">
    <div class="split-visual">{arch('platter',1000)}{STAMP}</div>
    <div class="split-body">
      <span class="eyebrow">The Beginning</span>
      <h2>From a family table to<br/>Britain's finest rooms.</h2>
      <p>Maharaja began the way the best food always does &mdash; at home, among family, cooking for the people we love. Word travelled, tables grew, and a home kitchen became a catering house entrusted with the most important days of people's lives.</p>
      <p>Two decades on, we have catered thousands of weddings across London and beyond. Yet the principle has never moved: cook as though you are feeding your own family, because to us, every couple is.</p>
      <div class="stats">
        <div><div class="num">20+</div><div class="lbl">Years of service</div></div>
        <div><div class="num">2,000+</div><div class="lbl">Weddings catered</div></div>
        <div><div class="num">11</div><div class="lbl">Recommended venues</div></div>
      </div>
    </div>
  </div></div>
</section>

<section class="darker pad" id="founder">
  <div class="wrap"><div class="split reveal">
    <div class="split-visual" style="aspect-ratio:3/4">
      <div class="arch"><div class="archinner"><img src="assets/img/lak-banwait.jpg" alt="Lak Banwait, Founder of Maharaja London" /></div></div>
    </div>
    <div class="split-body">
      <span class="eyebrow">The Founder</span>
      <h2>Lak Banwait</h2>
      <div style="font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:-10px 0 22px">Founder &amp; Director</div>
      <p>Maharaja London is the vision of its founder, Lak Banwait &mdash; a name that has become synonymous with grand-scale Asian weddings and unforgettable celebrations across the UK. What began as an ambitious idea, he has built into one of the most respected names in the British Asian wedding industry.</p>
      <p>His approach is simple to describe and hard to match: create experiences, not merely events. Lak pairs the warmth of traditional South Asian hospitality with the polish of modern luxury production &mdash; authentic cuisine, flawless coordination and immersive design that feels cinematic in scale yet remains deeply personal to every client.</p>
      <p>Known for a sharp eye for detail and a calm hand over hundreds of moving parts, he is trusted to orchestrate some of the most important days in people's lives. Under his leadership Maharaja has grown from a catering company into a full event-experience brand &mdash; modern in its ambition, traditional in its heart.</p>
    </div>
  </div></div>
</section>

<section class="light pad">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow dark c">What We Stand For</span><h2>Care you can taste.</h2></div>
    <div class="svc-grid reveal">
      <div class="svc"><h3>Heritage</h3><p>Recipes carried through generations, honouring the regions, rituals and flavours they come from.</p></div>
      <div class="svc"><h3>Craft</h3><p>Spices ground in-house, breads pulled to order, every dish tasted and refined before it reaches your guests.</p></div>
      <div class="svc"><h3>Service</h3><p>A dedicated event manager and a team that moves quietly and gracefully through your celebration.</p></div>
      <div class="svc"><h3>Trust</h3><p>Recommended by Britain's leading venues and returned to, year after year, by the planners who know us.</p></div>
    </div>
  </div>
</section>

<section class="darker pad">
  <div class="wrap"><div class="split rev reveal">
    <div class="split-body">
      <span class="eyebrow">In The Kitchen</span>
      <h2>The hand of the<br/>home cook.</h2>
      <p>Our chefs balance the bold, slow-cooked richness of the north with the bright, coastal cooking of the south. Nothing arrives from a packet; masalas are blended in our own kitchen, and the menu you taste is the menu you are served.</p>
      <p>It is this insistence on doing things the long way that earned us the industry's &lsquo;Wedding Caterer of the Year&rsquo; and the loyalty of the couples we cook for.</p>
    </div>
    <div class="split-visual">{arch('wooden',1000)}</div>
  </div></div>
</section>

<section class="dark pad-sm">
  <div class="wrap center reveal" style="max-width:46em">
    <div style="font-family:var(--serif);font-size:clamp(1.8rem,4vw,2.8rem);line-height:1.3;color:var(--bone)">&ldquo;The food at a wedding is the one thing every guest remembers. We treat that responsibility as the honour it is.&rdquo;</div>
    <div class="divider"><span></span><svg class="lotus" viewBox="0 0 24 24" fill="#c2a14e"><path d="M12 2c1 3 1 5 0 7-1-2-1-4 0-7zM5 7c2 1 3 3 3 5-2 0-4-1-5-3 0 0 1-1 2-2zm14 0c1 1 2 2 2 2-1 2-3 3-5 3 0-2 1-4 3-5zM3 13c3-1 6 0 9 3-3 1-7 0-9-3zm18 0c-2 3-6 4-9 3 3-3 6-4 9-3z"/></svg><span></span></div>
    <div style="margin-top:20px;font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)">The Maharaja Kitchen</div>
  </div>
</section>

{cta()}
</main>
"""
about += FOOTER
write("about.html", about)

# ============================ MENUS ============================
def course(kicker, title, desc, dishes, key, rev=False):
    items = "".join(f"<li>{d[0]}<span>{d[1]}</span></li>" for d in dishes)
    cls = "course rev" if rev else "course"
    return f"""<div class="{cls} reveal">
  <div class="course-visual">{arch(key,900)}</div>
  <div class="course-body"><span class="kicker">{kicker}</span><h3>{title}</h3><p>{desc}</p>
    <ul class="dishlist">{items}</ul>
  </div>
</div>"""

menus = head("The Menus &mdash; Maharaja London", "Four signature Indian wedding menus &mdash; Mughlai, coastal South Indian, live street food and modern fusion. Every menu fully bespoke.")
menus += header("menus.html")
menus += f"""<main id="top">
<section class="banner"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">The Menus</span><h1>The royal table,<br/>composed for you.</h1><p>Begin with one of our four signature tables, then shape it freely &mdash; regional dishes, family recipes, dietary needs and all.</p><div class="crumbs"><a href="index.html">Home</a> &middot; The Menus</div></div>
</section>

<section class="dark pad">
  <div class="wrap">
"""
menus += course("North &middot; Mughlai","The Royal Table",
  "The opulent, slow-cooked cuisine of the imperial courts &mdash; deep gravies, smoke from the tandoor and biryani sealed under pastry.",
  [("Hyderabadi Lamb Biryani","sealed dum, saffron, fried onion"),("Murgh Makhani","butter chicken, fenugreek cream"),
   ("Dal Makhani","black lentils, slow-cooked overnight"),("Paneer Lababdar","tomato &amp; cashew velvet"),
   ("Seekh &amp; Boti Kebabs","charcoal tandoor"),("Tandoori Salmon","ajwain, lime"),
   ("Subz Miloni","seasonal vegetables"),("Naan &amp; Roomali Roti","pulled to order")],
  "silver")
menus += course("South &middot; Coastal","The Coastal Feast",
  "Bright, fragrant cooking from the Malabar shore &mdash; coconut, curry leaf, tamarind and the gentle sourness of the south.",
  [("Malabar Fish Curry","coconut, kokum"),("Chettinad Chicken","roasted spice, peppercorn"),
   ("Appam &amp; Vegetable Stew","lace pancakes"),("Masala Dosa Station","live, to order"),
   ("Coconut Prawn Moilee","turmeric, green chilli"),("Avial","mixed veg, coconut, yoghurt"),
   ("Lemon &amp; Tamarind Rice","tempered"),("Sambar &amp; Rasam","accompaniments")],
  "thali_side", rev=True)
menus += course("Live &middot; Street","The Chaat Bazaar",
  "Theatre and nostalgia &mdash; a roaming carnival of live counters that gets every guest out of their seat and talking.",
  [("Pani Puri / Golgappa","live filling"),("Dahi Bhalla","yoghurt, tamarind, pomegranate"),
   ("Aloo Tikki Chaat","crisp potato cake"),("Pav Bhaji Counter","griddle &amp; butter"),
   ("Live Dosa Station","crisp &amp; folded"),("Chilli Paneer","Indo-Chinese"),
   ("Hara Bhara Kebab","spinach &amp; pea"),("Kulfi &amp; Falooda Cart","rose, pistachio")],
  "spread")
menus += course("Modern &middot; Fusion","The Grand Fusion",
  "Heritage flavour with contemporary plating &mdash; for couples who want their day to feel both rooted and entirely now.",
  [("Tandoori Canap&eacute;s","passed on arrival"),("Truffle Khichdi","aged basmati"),
   ("Lamb Chop Lollipops","mint, pomegranate glaze"),("Saffron Risotto","parmesan, gold leaf"),
   ("Tasting Thali","chef's selection"),("Deconstructed Gulab Jamun","cardamom, rose"),
   ("Chai Cr&egrave;me Br&ucirc;l&eacute;e","masala spiced"),("Signature Mocktail Bar","saffron, rose, mango")],
  "tray_pita", rev=True)
menus += f"""  </div>
</section>

<section class="light pad-sm">
  <div class="wrap center reveal" style="max-width:44em">
    <span class="eyebrow dark c">Every Detail Considered</span>
    <h2 style="margin:20px 0 16px;font-size:clamp(2rem,4vw,2.8rem)">Fully bespoke. Always.</h2>
    <p style="color:var(--t-dark-mute);font-size:1.08rem">Vegetarian, vegan, Jain, halal, nut-free and allergen-conscious menus are all part of how we work &mdash; never an afterthought. We'll build your menu together at a private tasting.</p>
    <a href="contact.html" class="btn btn-gold" style="margin-top:30px">Book a Tasting</a>
  </div>
</section>

{cta()}
</main>
"""
menus += FOOTER
write("menus.html", menus)

# ============================ SERVICES ============================
def svcrow(num, kicker, title, desc, tags, key, rev=False):
    cls = "svc-row rev" if rev else "svc-row"
    tagspan = "".join(f"<span>{t}</span>" for t in tags)
    return f"""<div class="{cls} reveal">
  <div class="svc-row-visual">{arch(key,1000)}</div>
  <div class="svc-row-body"><div class="num-lg">{num}</div><span class="kicker" style="color:var(--gold);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;display:block;margin-bottom:6px">{kicker}</span><h3>{title}</h3><p>{desc}</p><div class="tags">{tagspan}</div></div>
</div>"""

services = head("Services &mdash; Maharaja London", "Indian wedding catering, corporate events, private dining and full bespoke event design across London and the South of England.")
services += header("services.html")
services += f"""<main id="top">
<section class="banner"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">Services</span><h1>One house, the<br/>whole celebration.</h1><p>From a single dinner to a three-day wedding, we cook, design and run the day so you can simply enjoy it.</p><div class="crumbs"><a href="index.html">Home</a> &middot; Services</div></div>
</section>

<section class="dark pad">
  <div class="wrap">
"""
services += svcrow("01","Our Speciality","Asian &amp; Indian Weddings",
  "Multi-day weddings catered from mehndi to reception, each function with its own considered menu. We coordinate timings with your planner and venue so the food lands exactly when the moment calls for it.",
  ["Mehndi &amp; Sangeet","Ceremony","Reception","Live Stations","500+ guests"],"thali_var")
services += svcrow("02","For Business","Corporate &amp; Galas",
  "Award dinners, product launches and corporate galas delivered with precision and polish. Discreet, punctual and brand-aware &mdash; the standard your clients expect, every time.",
  ["Galas","Launches","Conferences","Canap&eacute; Receptions"],"metal_tray", rev=True)
services += svcrow("03","Closer Tables","Private &amp; Intimate Dining",
  "Milestone birthdays, anniversaries and dinners at home. The same kitchen and the same care, scaled to a more intimate gathering &mdash; with an optional private chef on site.",
  ["Home Dining","Anniversaries","Birthdays","Private Chef"],"wooden")
services += svcrow("04","Beyond the Plate","Bespoke Event Design",
  "Mandap and stage styling, floristry, tableware and full event planning, designed hand-in-hand with the menu so the whole day feels of a piece. One team, one vision, no loose ends.",
  ["Mandap Styling","Florals","Tablescapes","Full Planning"],"sari", rev=True)
services += f"""  </div>
</section>

<section class="light pad">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow dark c">How We Work</span><h2>Effortless, by design.</h2></div>
    <div class="svc-grid reveal">
      <div class="svc"><div class="num-lg" style="color:var(--gold);font-family:var(--serif);font-size:2.4rem">1</div><h3>Enquire</h3><p>Tell us about your day &mdash; date, guests, venue and the feeling you're after.</p></div>
      <div class="svc"><div class="num-lg" style="color:var(--gold);font-family:var(--serif);font-size:2.4rem">2</div><h3>Taste</h3><p>Join us for a private tasting and shape your menu with our chefs.</p></div>
      <div class="svc"><div class="num-lg" style="color:var(--gold);font-family:var(--serif);font-size:2.4rem">3</div><h3>Plan</h3><p>Your event manager handles timings, staffing and every fine detail.</p></div>
      <div class="svc"><div class="num-lg" style="color:var(--gold);font-family:var(--serif);font-size:2.4rem">4</div><h3>Celebrate</h3><p>On the day, we serve quietly and beautifully &mdash; you simply enjoy it.</p></div>
    </div>
  </div>
</section>

{cta()}
</main>
"""
services += FOOTER
write("services.html", services)

# ============================ GALLERY ============================
gal_imgs = REAL_GALLERY
figs = "".join(f'<figure class="{c}"><img src="{u}" alt="Maharaja catering" /></figure>' for u,c in gal_imgs)
gallery = head("Gallery &mdash; Maharaja London", "A gallery of Maharaja's Indian wedding and event catering &mdash; thalis, live stations, plated courses and celebration tables.")
gallery += header("gallery.html")
gallery += f"""<main id="top">
<section class="banner"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">The Gallery</span><h1>Tables we've been<br/>proud to set.</h1><p>A glimpse of the food, the colour and the celebrations we've had the honour of feeding.</p><div class="crumbs"><a href="index.html">Home</a> &middot; Gallery</div></div>
</section>
<section class="dark pad">
  <div class="wrap"><div class="gal-grid reveal">{figs}</div>
  <div class="center" style="margin-top:54px"><a href="contact.html" class="btn btn-gold reveal">Enquire About Your Day</a></div>
  </div>
</section>
</main>
"""
gallery += FOOTER
write("gallery.html", gallery)

# ============================ VENUES ============================
VENUES = [("The Mayfair Hotel","London"),("Hilton London Bankside","London"),("Grand Connaught Rooms","London"),
 ("Mercedes-Benz World","Surrey"),("Hilton London Metropole","London"),("Novotel London West","Hammersmith"),
 ("Radisson Blu Edwardian","Heathrow"),("Newbury Racecourse","Berkshire"),("The Garden Room","Syon Park"),
 ("Vale Resort","Cardiff"),("Thistle Hotel","Heathrow"),("&amp; many more","Enquire")]
venrows = "".join(f'<div class="ven"><span class="vn">{n}</span><span class="vl">{l}</span></div>' for n,l in VENUES)
venues = head("Venues &mdash; Maharaja London", "Hand-picked London and UK wedding venues where Maharaja is a trusted, recommended Indian caterer.")
venues += header("venues.html")
venues += f"""<main id="top">
<section class="banner"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">Approved &amp; Recommended</span><h1>At home in the<br/>finest rooms.</h1><p>We are a trusted, recommended caterer at venues across London and beyond &mdash; and happy to cater at a venue of your own choosing.</p><div class="crumbs"><a href="index.html">Home</a> &middot; Venues</div></div>
</section>
<section class="dark pad">
  <div class="wrap"><div class="ven-list reveal">{venrows}</div>
  <div class="center" style="margin-top:54px;color:var(--t-light-mute);max-width:40em;margin-left:auto;margin-right:auto">
    <p>Don't see your venue? We regularly cater at private estates, marquees and homes across the South of England. If you can dream the setting, we can bring the feast.</p>
    <a href="contact.html" class="btn btn-gold" style="margin-top:26px">Ask About Your Venue</a>
  </div></div>
</section>
</main>
"""
venues += FOOTER
write("venues.html", venues)

# ============================ CONTACT ============================
contact = head("Enquire &mdash; Maharaja London", "Request a private tasting with Maharaja, London's award-winning Indian wedding caterer. We reply within one working day.")
contact += header("contact.html")
contact += f"""<main id="top">
<section class="banner" style="padding-bottom:60px"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">Begin the Conversation</span><h1>Reserve your<br/>private tasting.</h1><div class="crumbs"><a href="index.html">Home</a> &middot; Enquire</div></div>
</section>
<section class="dark pad-sm">
  <div class="wrap"><div class="enq-grid">
    <div class="enq-left reveal">
      <span class="eyebrow">We'd Love to Hear From You</span>
      <h2>Tell us about<br/>your celebration.</h2>
      <p>Share a few details and we'll be in touch within one working day to arrange a tasting with our chefs &mdash; with no obligation, simply a conversation about the day you have in mind.</p>
      <div class="enq-contact">
        <a href="tel:+442000000000"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>+44 (0)20 0000 0000</a>
        <a href="mailto:enquiries@maharaja.co.uk"><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>enquiries@maharaja.co.uk</a>
        <div><svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>Serving London &amp; the South of England</div>
      </div>
    </div>
    <form name="enquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/contact.html?sent=1" class="reveal">
      <input type="hidden" name="form-name" value="enquiry" />
      <p style="display:none"><label>Don't fill this out: <input name="bot-field" /></label></p>
      <div class="frow">
        <div><label>Your name</label><input type="text" name="name" placeholder="Full name" required /></div>
        <div><label>Phone</label><input type="tel" name="phone" placeholder="Mobile number" /></div>
      </div>
      <div class="frow">
        <div><label>Email</label><input type="email" name="email" placeholder="you@email.com" required /></div>
        <div><label>Event date</label><input type="date" name="date" /></div>
      </div>
      <div class="frow">
        <div><label>Event type</label><select name="type"><option>Wedding</option><option>Corporate event</option><option>Private party</option><option>Other</option></select></div>
        <div><label>Approx. guests</label><input type="number" name="guests" placeholder="e.g. 250" min="1" /></div>
      </div>
      <div><label>Tell us about your day</label><textarea name="message" placeholder="Traditions, dietary needs, the feeling you're after&hellip;"></textarea></div>
      <button type="submit" class="btn btn-gold">Send Enquiry</button>
      <p class="formnote">We reply within one working day. Your details are never shared.</p>
    </form>
  </div></div>
</section>
</main>
"""
contact += FOOTER
write("contact.html", contact)

# ============================ JOURNAL ============================
# Index
cards = ""
for p in POSTS:
    cards += f"""<a href="{p['slug']}" class="post-card reveal"><div class="thumb"><img src="{p['img']}" alt="{p['title']}" /></div>
    <div class="pc-body"><span class="cat">{p['cat']} &middot; {p['date']}</span><h3>{p['title']}</h3><p>{p['excerpt']}</p><span class="more">Read More</span></div></a>"""
journal = head("Journal &mdash; Maharaja London", "News, ideas and inspiration from Maharaja, London's award-winning Indian wedding caterer.")
journal += header("journal.html")
journal += f"""<main id="top">
<section class="banner"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">The Journal</span><h1>Stories from<br/>the kitchen.</h1><p>News, ideas and a little inspiration from the Maharaja table.</p><div class="crumbs"><a href="index.html">Home</a> &middot; Journal</div></div>
</section>
<section class="dark pad">
  <div class="wrap"><div class="journal-grid">{cards}</div></div>
</section>
{cta()}
</main>
"""
journal += FOOTER
write("journal.html", journal)

# Individual posts
for i, p in enumerate(POSTS):
    others = [q for q in POSTS if q['slug'] != p['slug']][:2]
    nextlinks = " &middot; ".join(f'<a href="{q["slug"]}">{q["title"]}</a>' for q in others)
    art = head(f"{p['title']} &mdash; Maharaja London", p['excerpt'].replace('&mdash;','-'))
    art += header("journal.html")
    art += f"""<main id="top">
<section class="banner" style="padding-bottom:60px"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">{p['cat']} &middot; {p['date']}</span><h1 style="font-size:clamp(2.2rem,5vw,3.8rem)">{p['title']}</h1><div class="crumbs"><a href="index.html">Home</a> &middot; <a href="journal.html">Journal</a></div></div>
</section>
<section class="dark pad-sm">
  <div class="wrap">
    <div class="article reveal">
      <div class="lead-img arch"><div class="archinner"><img src="{p['img']}" alt="{p['title']}" /></div></div>
      {p['body']}
    </div>
    <div class="article-foot">
      <a href="journal.html" class="btn btn-ghost">&larr; All Stories</a>
      <div style="font-size:.8rem;color:var(--t-light-mute)">Read next: {nextlinks}</div>
    </div>
  </div>
</section>
{cta()}
</main>
"""
    art += FOOTER
    write(p['slug'], art)

# ============================ 404 ============================
nf = head("Page Not Found &mdash; Maharaja London", "The page you are looking for could not be found.")
nf += header("")
nf += f"""<main id="top">
<section class="banner" style="min-height:70vh;display:flex;align-items:center"><div class="jali"></div>
  <div class="wrap reveal"><span class="eyebrow c">Lost the thread</span><h1 style="font-size:clamp(3rem,9vw,7rem)">404</h1><p>This table isn't set. Let's get you back to the feast.</p><div style="margin-top:30px"><a href="index.html" class="btn btn-gold">Return Home</a></div></div>
</section>
</main>
"""
nf += FOOTER
write("404.html", nf)

print("\\nAll pages built.")
