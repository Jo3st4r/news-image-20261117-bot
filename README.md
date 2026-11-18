# news-image-20261117-bot

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Jo3st4r/news-image-20261117-bot/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Jo3st4r/news-image-20261117-bot/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A front-page poster that sums up Tuesday 17 November 2026 in one image
(1024×1024 PNG, built with Pillow from flat-vector shapes and real text):

- **Lead — Kerch Bridge collapses after a Ukrainian strike.** A road span
  falls into the strait; the Kremlin vows to rebuild the link to Crimea.
- **Trump lands in Manila** for the ASEAN summit: a trade pact with
  Thailand signed, with Xi–Putin talks next in China.
- **Tankers hit by mines in the Strait of Hormuz.** Two tankers ablaze;
  a third US carrier arrives in the region.
- **ULA Vulcan rocket fails**, destroying 40 Amazon internet satellites.
- **Also today:** JPMorgan blames a software bug for Monday's banking
  outage; Western nations urge Israel to open Gaza crossings for aid;
  Estonia to shut its Russia border crossings on 1 December.

Sources: BBC, AP, Al Jazeera, Reuters, Spaceflight Now. The image is
drawn entirely in code (`tools/build_image.py`); `main.py` copies the
vendored PNG byte-for-byte to `/output/entry.png`, so two runs produce
identical bytes.

## Run it

```sh
python3 main.py
# writes /output/entry.png (1024x1024, ~94 KB)
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
