#!/bin/bash
# ---------------------------------------------------------------------------
# Saves the original Maharaja photos (food, prep, events, award) from the live
# old site into assets/img/gallery/ so you own local copies.
#
# Run this ON YOUR MAC (it can reach maharaja.co.uk). Either double-click this
# file in Finder, or in Terminal:   bash scripts/get-photos.command
#
# The site currently hot-links these photos so they work right away. Once you
# have local copies, tell me and I'll repoint the site at them — important
# before you ever switch the maharaja.co.uk domain over to this new site.
# ---------------------------------------------------------------------------
cd "$(dirname "$0")/.." || exit 1
mkdir -p assets/img/gallery
base="https://maharaja.co.uk/wp-content/uploads"
paths=(
  "2015/11/4-FoodProductShots09-580x400.jpg"
  "2015/11/4-FoodProductShots11-580x400.jpg"
  "2015/11/4-FoodProductShots13-580x400.jpg"
  "2015/11/4-FoodProductShots16-580x400.jpg"
  "2015/11/4-FoodProductShots20-580x400.jpg"
  "2015/11/4-FoodProductShots22-580x400.jpg"
  "2015/11/4-FoodProductShots02-580x400.jpg"
  "2015/11/2-FoodPreparation-07-580x400.jpg"
  "2015/11/2-FoodPreparation-13-580x400.jpg"
  "2017/11/Maharaja-Highgate-201710-LR-18-580x400.jpg"
  "2017/11/Maharaja-Highgate-201710-LR-24-580x400.jpg"
  "2017/11/Maharaja-Highgate-201710-LR-47-580x400.jpg"
  "2018/02/Sam-Patel-Maharaja-820x820.jpg"
)
echo "Saving original Maharaja photos..."
for p in "${paths[@]}"; do
  fn=$(basename "$p")
  printf "  downloading %s ... " "$fn"
  if curl -fsSL "$base/$p" -o "assets/img/gallery/$fn"; then echo "ok"; else echo "FAILED"; fi
done
echo "Done. Saved into assets/img/gallery/"
