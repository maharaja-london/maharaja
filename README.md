# Maharaja London — Website

Award-winning Indian & Asian wedding catering and event design, London.
A fast, fully static website — no build step, no framework, no database.

**Palette:** bone · royal emerald green · gold · black
**Type:** Cormorant Garamond (display) · Marcellus (wordmark) · Mukta (body)

---

## What's inside

```
maharaja/
├── index.html          Home
├── about.html          Our Story
├── menus.html          The Menus (4 signature tables)
├── services.html       Services (weddings, corporate, private, bespoke)
├── gallery.html        Gallery
├── venues.html         Venues
├── contact.html        Enquire (Netlify form)
├── 404.html            Not-found page
├── netlify.toml        Netlify config (publish dir + caching headers)
├── build.py            Regenerates the HTML pages (optional — see below)
└── assets/
    ├── css/styles.css  All styling (one file)
    ├── js/main.js      Sticky nav, mobile menu, scroll reveal
    └── img/            Logo, crest and favicons
```

There is **no build command**. The HTML is ready to serve as-is, so Netlify
deploys are near-instant and use effectively zero build minutes.

---

## Deploying (GitHub → Netlify)

You've already connected the repo, so:

1. Copy these files into your `maharaja` repo (keep the folder structure).
2. Commit and push to your default branch:
   ```bash
   git add .
   git commit -m "New Maharaja site"
   git push
   ```
3. Netlify auto-deploys. In **Site settings → Build & deploy**, make sure:
   - **Build command:** *(leave empty)*
   - **Publish directory:** `.` (the repo root — already set in `netlify.toml`)

### Preview locally before pushing (optional)
```bash
cd maharaja
python3 -m http.server 8080      # then open http://localhost:8080
# or:  npx serve
```

---

## The enquiry form

`contact.html` uses **Netlify Forms** — no backend needed. Once deployed,
submissions appear in **Netlify → Forms → "enquiry"**. To get email alerts,
go to **Forms → Settings → Form notifications** and add your email.

The form already includes the hidden `form-name` field and a honeypot for
spam, which is all Netlify needs to detect it on deploy.

---

## Things to change before going live

| What | Where | Notes |
|------|-------|-------|
| **Phone number** | `assets`/footer + `contact.html` | Currently a placeholder `+44 (0)20 0000 0000`. Search & replace `+442000000000` and the display number. |
| **Email** | footer + `contact.html` | Set to `enquiries@maharaja.co.uk` — change if needed. |
| **Social links** | footer (`socials`) | The `#` links go to Instagram / Facebook / LinkedIn — drop in real URLs. |
| **Photography** | `build.py` `IMG` dict | Images are licensed Unsplash stock standing in for *your own* food/wedding photos. Replacing these with real Maharaja photography is the single biggest upgrade. See below. |
| **Stats & copy** | any page | Years/weddings figures are sensible placeholders — adjust to the real numbers. |

### Swapping in real photography (recommended)
Right now images are hot-linked from Unsplash (so they don't count against your
Netlify bandwidth). To use your own photos instead:

1. Drop your images into `assets/img/` (e.g. `hero.jpg`, `royal-table.jpg`).
2. In `build.py`, change the URLs in the `IMG` dictionary to local paths
   like `assets/img/royal-table.jpg`, then run `python3 build.py`.
   *(Or just find-and-replace the image URLs directly in the HTML.)*

---

## Editing content

- **Styling / colours:** everything lives in `assets/css/styles.css` under the
  `:root` variables at the top — change `--emerald`, `--gold`, `--bone` etc.
  once and it updates site-wide.
- **Page text & structure:** edit the `.html` files directly, **or** edit the
  matching section in `build.py` and re-run `python3 build.py` to regenerate
  all pages with a consistent header/footer. (Python 3 + Pillow only needed if
  you also want to regenerate the logo/favicons.)

---

© Maharaja London Ltd. Built with heritage.
