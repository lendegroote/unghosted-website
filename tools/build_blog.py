"""Builds the unghosted blog: blog/index.html and one page per post.

Edit the POSTS list below, then run:  python3 tools/build_blog.py
Body text uses a tiny markup:  blank line = new paragraph, "## " = heading,
"> " = pull quote, "[ritual] Title | text" = ritual card,
"[safety] Title | text" = plain safety box, "- " = list item.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "blog"

POSTS = [
    {
        "slug": "talking-to-your-ghost",
        "title": "How to talk to your ghost (politely)",
        "dek": "Ouija, voice recordings, letters. A few house rules make every conversation calmer, for both of you.",
        "category": "Talk",
        "date": "9 October 2026",
        "read": "5 min",
        "cover": "shop-ouija.jpg",
        "cover_alt": "Hands on a planchette over a Ouija board, night vision",
        "body": """
Sooner or later you will want to ask it something. Who are you. Why the attic. Why always the left cupboard door. Fair questions. Here is how we suggest you ask them, so the conversation stays calm on both sides of the veil.

## The house rules

Every session in the app starts with the same five rules. They are not superstition. They keep you safe, keep the mood low-stress, and stop a quiet evening from turning into a horror film you did not sign up for.

- Introduce yourself. Your ghost has watched you brush your teeth for years. It still deserves a hello.
- Stay respectful. No dares, no "show yourself", no testing.
- Never provoke. If you would not say it to a grumpy neighbour, do not say it to a ghost.
- Set a time limit. Ten to fifteen minutes is plenty.
- Never alone. Do it with someone you trust, or switch on a trusted contact in the app.

> Sessions can't be left open. Always say goodbye.

## Asking out loud

The simplest way to talk is to just talk. Ask one question, then stay quiet for ten seconds. The app records the silence. Afterwards you listen back, slowed down, and mark anything that sounds like an answer.

A small honest note: most of what you will hear is the house. A fridge, a pipe, the neighbour's dog. That is fine. Write down what was nearby, and keep the clips that still make the hair on your arm stand up. Your ghost diary will tell you over time which ones matter.

## The Ouija board

Letter by letter, fingers light on the planchette, never pushing. Use it in a group, never leave the board alone in the middle of a word, and close every session by moving to GOOD BYE together. It is old-fashioned and slow, which is exactly why it works as a ritual: it makes everyone in the room sit still and pay attention.

## Writing a letter

Some things are easier to write than to say. Write to your ghost, read it out once, then let it go. Our app calls it "burn it to send it". Please do that over a sink, or just tear it up. Your ghost does not need a fire in the attic.

## Closing the session

Say goodbye out loud. Then check in with yourself: calm, uneasy, or scared? If you feel uneasy, lay a salt line at the doors and windows, put the lights on, and do something normal for half an hour. If you feel scared after sessions more often than not, take a break from talking and tell someone. That is not losing. That is good care.

[ritual] Try it tonight | One question, ten seconds of silence, one goodbye. That's a whole session. Note how you feel afterwards.
""",
        "sources": [],
    },
    {
        "slug": "the-ghost-diary",
        "title": "The ghost diary: one minute a day",
        "dek": "Vague dread is hard to live with. A pattern is not. Why we ask you to write one line every evening.",
        "category": "Rituals",
        "date": "6 October 2026",
        "read": "4 min",
        "cover": "print-toilet.png",
        "cover_alt": "Found photo: a ghost in a sheet reading comics on the toilet",
        "body": """
The worst part of living with a ghost is often not the ghost. It is not knowing. Was that a knock or the heating? Is it angrier this week, or am I just tired? Vague dread follows you around the house, and it is very hard to do anything with it.

A pattern is different. You can work with a pattern.

## Why writing it down helps

Researchers have found that paranormal experiences and beliefs go up when people feel anxious or out of control (Roe and Bell, 2016; Drinkwater and colleagues, 2024). We are not saying your ghost is "just anxiety". We are saying that taking a minute to write things down gives you some control back, and that alone tends to make a house feel calmer.

## What to log

One line is enough. Five small things:

- Time
- Room
- What you noticed
- How you slept
- How you felt

> "21:40, hallway, cold spot, slept badly, uneasy." That's a perfect entry.

## What you will start to see

After two weeks, most people spot something. It is always around 3 am. It is always near the boiler. It is always after a rough day at work. Each of those tells you what to do next:

- Always 3 am? Read our piece on night visits and try the bedtime ritual.
- Always near the boiler? Check the boiler first. Seriously, today.
- Always after a bad day? Your ghost might be picking up on you. A calm evening ritual helps you both.

## It makes every other conversation easier

When you talk to an expert in the app, the first thing they will ask is what happened and when. With a diary you have the answer in seconds. And if you ever want to talk to a doctor about sleep or stress, two weeks of notes are worth more than any memory.

[ritual] Tonight | Before bed, write one line. Time, room, what you noticed, how you slept, how you feel. Close the app. Say good night.
""",
        "sources": [
            ("Paranormal belief, stress and control (Neuroscience News)", "https://neurosciencenews.com/stress-paranormal-belief-neurotheology-28043"),
            ("How paranormal beliefs help people cope in uncertain times (The Conversation)", "https://theconversation.com/how-paranormal-beliefs-help-people-cope-in-uncertain-times-251648"),
        ],
    },
    {
        "slug": "when-it-feels-like-someone-you-lost",
        "title": "When it feels like someone you lost",
        "dek": "Sensing a loved one after they die is common. For most people it is a comfort, and staying connected can be part of healthy grief.",
        "category": "Grief",
        "date": "2 October 2026",
        "read": "5 min",
        "cover": "shop-candles.jpg",
        "cover_alt": "White candles and flowers on a wooden table in the evening",
        "body": """
Some ghosts arrive with the house. Others arrive after a funeral. A familiar smell in the kitchen. The feeling that someone is sitting in their old chair. A voice saying your name just as you fall asleep.

If that is your ghost, this one is for you, and we will keep the jokes small.

## You are far from alone

Studies of bereaved people find that somewhere between 30 and 60% sense the presence of the person who died. Some reviews put it as high as 70% among widowed spouses. It is one of the most common experiences in grief, and for most people it is comforting. About a quarter find it distressing.

> It is not a sign that something is wrong with you. It is one of the ways people carry someone with them.

## Staying connected is allowed

For a long time, grief advice was about "letting go". Many grief counsellors now work with an idea called continuing bonds: that keeping a connection with someone who died, in your own way, can be a healthy part of grieving rather than a failure to move on.

That is close to how we think about living with a ghost. You do not have to make them leave. You can find a way to live together that feels kind.

## Write to them

One ritual we like for this kind of ghost is a letter. Tell them about your week. Ask the question you never asked. Say the thing you did not get to say. Read it out loud once, in the room where you feel them most.

Writing letters to someone who died is used inside some grief therapy approaches. On its own the evidence is small, so we offer it as a ritual, not as treatment. Many people simply find it helps.

## Small things that help

- Keep their chair, their mug, their song. Use them on purpose, not by accident.
- Light a candle on dates that matter.
- Tell their story to someone new. Ghosts, in our experience, like being remembered out loud.

[safety] If it gets heavy | If the presence frightens you, or grief makes most days hard to get through, please talk to someone: your GP, a grief counsellor, or a helpline. In Belgium you can call Tele-Onthaal on 106. In the Netherlands, 113 Zelfmoordpreventie on 113 or 0800 0113.

[ritual] This week | Write one letter. It can be three lines. Read it out loud once, then keep it or let it go.
""",
        "sources": [
            ("Sensory experiences of a deceased person, review (PMC)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12437889/"),
            ("Prevalence and phenomenology of sensory experiences of a deceased (University of Plymouth)", "https://researchportal.plymouth.ac.uk/en/publications/prevalence-and-phenomenology-of-sensory-experiences-of-a-deceased/"),
            ("Letter writing to the deceased in grief care (Frontiers in Medicine, 2025)", "https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1576298/full"),
            ("Continuing bonds theory in grief counselling (The Loss Foundation)", "https://thelossfoundation.org/continuing-bonds-theory-in-grief-counselling"),
        ],
    },
    {
        "slug": "check-the-boiler-first",
        "title": "Before you call a medium, check the boiler",
        "dek": "Most strange houses are just strange houses. One cause can actually hurt you, and it takes five minutes to rule out.",
        "category": "Safety",
        "date": "25 September 2026",
        "read": "6 min",
        "cover": "blog-yard.jpg",
        "cover_alt": "Night photo of three people in a dark yard, a circled shape between them",
        "body": """
Real investigators do not start with candles. They start with the house. Not because your ghost is not real, but because a house makes a lot of noise on its own, and you want to know which sounds are your ghost and which are your plumbing.

## The usual suspects

- Knocks and bangs: pipes. "Water hammer" happens when water stops suddenly in a pipe, and it can sound exactly like someone knocking on a wall.
- Cold spots: draughts from windows, doors, chimneys and floorboards.
- Lights flickering, devices switching on: old wiring, loose plugs, a smart speaker with ideas of its own.
- Damp, mould, a musty smell that comes and goes.
- A low hum you feel more than hear: fans, traffic, wind. In one famous case, an engineer named Vic Tandy linked a feeling of unease in his lab to a fan producing low sound around 19 Hz. The evidence since is mixed, but it is worth knowing.

## The one that matters: carbon monoxide

A faulty heater, boiler or stove can leak carbon monoxide. You cannot see it or smell it. It causes headaches, dizziness, tiredness and a heavy sense of dread, and in bad cases people see or hear things that are not there.

In a well-known case from 1921, a family's "haunting" stopped once their furnace was repaired.

> Two clues: everyone in the house feels it, and it fades when you go outside.

[safety] Do this now if it sounds familiar | Headaches or dizziness that get better when you leave the house? Go outside, call your gas emergency number or emergency services, and do not go back in until the appliance has been checked. Test your carbon monoxide alarm today. Have your boiler or heater serviced every year. Open the windows for ten minutes a day.

## Then, and only then

Once the house is safe and the pipes are behaving, and things still happen? Welcome. That one is probably yours. In the app, the "Rule out the usual suspects" checklist walks you through all of this in a couple of minutes, and you only need to do it once a year.

## A weekly ritual: the room walk

Once a week, walk through the house with all the lights on. Stop in every room and name every sound. The fridge. The fan. The old floorboard by the stairs. It sounds silly, and it works: once you know the voice of your house, the sounds that are left stand out, and the rest stops making you jump.

[ritual] This weekend | Test the CO alarm, check the boiler service date, open every window for ten minutes, then do one room walk.
""",
        "sources": [
            ("Environmental factors and haunt experiences, review (Frontiers / PMC)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7304295"),
            ("The 100-year-old haunted house mystery solved (IFLScience)", "https://www.iflscience.com/health-and-medicine/100yearold-haunted-house-mystery-solved-by-professor-and-ophthalmologist/"),
            ("Ghosts, ghouls and faulty furnaces (UL Standards & Engagement)", "https://ulse.org/ul-standards-engagement/carbon-monoxide-safety/ghosts-ghouls-and-faulty-furnaces-these-things-go"),
            ("Infrasound and paranormal activity (HowStuffWorks)", "https://science.howstuffworks.com/science-vs-myth/extrasensory-perceptions/infrasound-paranormal-activity.htm"),
        ],
    },
    {
        "slug": "why-your-ghost-visits-at-3am",
        "title": "Why your ghost visits at 3 am",
        "dek": "You wake up, you can't move, and something is in the room. Here is what is going on, and what helps.",
        "category": "Sleep",
        "date": "18 September 2026",
        "read": "5 min",
        "cover": "blog-nightcam.jpg",
        "cover_alt": "Night vision camera still of a dark living room with a pale shape in the doorway",
        "body": """
It is the most classic visit there is. You wake in the middle of the night. Your eyes are open, but your body will not move. There is a pressure on your chest, and you are certain that someone is standing at the foot of the bed.

## What is happening

This has a name: sleep paralysis. Your mind wakes up while your body is still in the stillness of dream sleep. During those seconds many people feel a presence, see a figure, or feel weight on their chest.

It is common, and it is frightening. In a large 2023 study from Goldsmiths, University of London, with more than 6,800 people who had experienced it, around three in four described strong fear. The same research found that ghost beliefs can make episodes feel longer and scarier.

> We are not going to tell you it isn't your ghost. We are going to tell you your ghost is probably just saying hi.

That small reframe matters. Fear is what makes these moments so bad, and a friendly story about who is in the room takes some of the fear away.

## The bedtime ritual

The things people most often say help prevent episodes are a regular sleep routine and changing the position they sleep in. So our evening ritual is built around exactly that:

- Same bedtime every night, give or take half an hour.
- Screens off, lights low.
- Sleep on your side rather than your back.
- Say good night to your ghost. Out loud is best.

## The wiggle

If it happens anyway, try this. It is one of the most reported ways people break an episode:

- Wiggle one finger. Just one.
- Then your toes.
- Breathe out slowly. Make a small sound if you can.
- Remind yourself: it's just a visit. It will pass in a moment.

[safety] When to see someone | If this happens often, or you have been sleeping badly for weeks, talk to your GP. Sleep problems are common and very treatable, and a doctor will not laugh at your ghost.

[ritual] Tonight | Phone away 30 minutes before bed, lights low, lie on your side, and say good night to your ghost.
""",
        "sources": [
            ("Sleep paralysis coping strategies, Goldsmiths 2023 (Sleep Medicine)", "https://eprints-gro.gold.ac.uk/33215/14/1-s2.0-S1389945723000709-main.pdf"),
        ],
    },
    {
        "slug": "you-are-not-the-only-one",
        "title": "1 in 6 homes. You are not the only one.",
        "dek": "Most people who live with a ghost never tell anyone. The numbers say they should.",
        "category": "Living with a ghost",
        "date": "4 September 2026",
        "read": "4 min",
        "cover": "blog-cart.jpg",
        "cover_alt": "Found photo: a ghost in a sheet and white heels pushing a shopping cart",
        "body": """
You hear the knock again. Three times, always from the attic. You do not mention it at dinner. You do not mention it to your friends, because the last time you did, someone hummed the Ghostbusters theme for a week.

So you keep quiet. And you assume you are the only one.

## You are really not

About 1 in 6 Americans say their home is haunted, and more than 2 in 5 say something they could not explain has happened at home. That is from a 2023 survey by All Star Home of just over a thousand people. In another poll, 35% said they had felt an unexplained presence in their house. (A wine brand paid for that one, so take it with a glass.)

> That's a few people on your street. Maybe a few in your building.

## Most people stay

Here is the part we find most interesting. According to Realtor.com, 56% of people who believe their home is haunted have never considered moving out.

They don't want it gone. They want to get along.

## So why does it feel so lonely?

Because almost nothing out there is made for people who stay. Friends laugh, family worries. Online it is exorcisms, horror films, and people with night vision cameras shouting "is anybody there". Very little of it helps you live a calm, normal life with someone in the attic.

## What we do differently

unghosted starts from one simple idea: we believe you. No proof needed. You tell us who you live with, and we help you take care of them, the way you would care for a cat or a plant.

- A daily check-in on how your ghost is doing.
- Small rituals: a candle, a song, ten quiet minutes together.
- A map of people nearby who understand, and experts when you need advice.
- A safety net, for the moments when it is not a ghost and you need real help.

[ritual] Tonight | Say good night to your ghost, out loud. It costs nothing, and you might sleep better for it.
""",
        "sources": [
            ("At least 1 in 6 Americans believe their home is haunted (WOWT, on the All Star Home survey)", "https://www.wowt.com/2023/10/09/least-1-6-americans-believe-their-home-is-haunted-survey-says"),
            ("Survey: 63% of people believe in the paranormal (Higgypop)", "https://higgypop.com/news/survey-reveals-63-of-people-believe-in-the-paranormal"),
        ],
    },
]

CATS = ["All", "Living with a ghost", "Sleep", "Safety", "Grief", "Rituals", "Talk"]

LOGO_PATH = (ROOT / "assets" / "logomark.svg").read_text()
LOGO_D = re.search(r'd="([^"]+)"', LOGO_PATH).group(1)
MARK = f'<svg class="logo__mark" viewBox="0 0 24 30" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="{LOGO_D}"/></svg>'
WORD = '<span class="logo__word"><span class="logo__un">un</span>ghosted</span>'

SOUND_BTN = """<button class="sound-toggle" type="button" aria-pressed="true" aria-label="Sound on">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11 5 6 9H3v6h3l5 4V5Z"/><path class="wave" d="M15.5 8.5a5 5 0 0 1 0 7"/><path class="wave" d="M18.5 5.5a9 9 0 0 1 0 13"/><path class="mute" d="m16 9 6 6m0-6-6 6"/></svg>
          <span class="sound-toggle__label">Sound on</span>
        </button>"""


def head(title, desc, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Special+Elite&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{up}styles.css">
</head>
<body class="is-blog">
  <div class="progress" aria-hidden="true"></div>
  <div class="veil" aria-hidden="true"></div>
  <div class="grain" aria-hidden="true"></div>
  <header class="nav">
    <div class="wrap nav__inner">
      <a href="{up}index.html" class="logo" data-sound="boo-short">{MARK}{WORD}</a>
      <nav class="nav__links" aria-label="Main">
        <a href="{up}index.html#features">Features</a>
        <a href="{up}index.html#shop">Spirit shop</a>
        <a href="{up}blog/index.html" aria-current="page">Blog</a>
        <a href="{up}index.html#faq">FAQ</a>
      </nav>
      <div class="nav__actions">
        {SOUND_BTN}
        <a href="{up}index.html#download" class="btn btn--rust" data-sound="boo">Download</a>
      </div>
    </div>
  </header>
"""


def foot(depth):
    up = "../" * depth
    return f"""
  <section class="section">
    <div class="wrap">
      <div class="cta reveal">
        <h2 class="display display--cta flicker">Your ghost is waiting.</h2>
        <p class="sub">Download unghosted. Free to start.</p>
        <div class="store-buttons store-buttons--center">
          <a href="{up}index.html#download" class="btn btn--rust" data-sound="boo">App Store</a>
          <a href="{up}index.html#download" class="btn btn--ghost" data-sound="boo">Google Play</a>
        </div>
      </div>
    </div>
  </section>
  <footer class="footer">
    <div class="wrap footer__inner">
      <div>
        <a href="{up}index.html" class="logo logo--footer" data-sound="boo-short">{MARK}{WORD}</a>
        <p class="footer__tag">Don't ghost your ghost. Made in Brussels.</p>
      </div>
      <div class="footer__cols">
        <div><h4>Product</h4><a href="{up}index.html#features">Features</a><a href="{up}index.html#shop">Spirit shop</a><a href="{up}index.html#faq">FAQ</a></div>
        <div><h4>Company</h4><a href="{up}blog/index.html">Blog</a><a href="#">About</a><a href="#">Contact</a></div>
        <div><h4>Follow</h4><a href="#">Instagram</a><a href="#">TikTok</a><a href="#">LinkedIn</a></div>
      </div>
    </div>
  </footer>
  <div class="toast" role="status" aria-live="polite">Click anywhere to wake the house. <span>Sound on</span></div>
  <script src="{up}main.js"></script>
</body>
</html>
"""


def inline(text):
    return html.escape(text, quote=False)


def render_body(src):
    out, items = [], []

    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    first_p = True
    for block in [b.strip() for b in src.strip().split("\n\n")]:
        lines = block.split("\n")
        if all(l.startswith("- ") for l in lines):
            items.extend(l[2:] for l in lines)
            flush()
            continue
        flush()
        if block.startswith("## "):
            out.append(f'<h2 class="reveal">{inline(block[3:])}</h2>')
        elif block.startswith("> "):
            out.append(f'<blockquote class="pull reveal"><p>{inline(block[2:])}</p></blockquote>')
        elif block.startswith("[ritual] ") or block.startswith("[safety] "):
            kind = "ritual" if block.startswith("[ritual]") else "safety"
            t, body = block.split("] ", 1)[1].split(" | ", 1)
            label = "Ritual" if kind == "ritual" else "Safety first"
            out.append(f'<aside class="callout callout--{kind} reveal"><p class="callout__label">{label}</p><h3>{inline(t)}</h3><p>{inline(body)}</p></aside>')
        else:
            cls = ' class="lede"' if first_p else ""
            first_p = False
            out.append(f"<p{cls}>{inline(block)}</p>")
    flush()
    return "\n".join(out)


def card(p, depth, big=False):
    up = "../" * depth
    href = f"{p['slug']}.html" if depth == 1 else f"blog/{p['slug']}.html"
    cls = "post-card post-card--big" if big else "post-card"
    return f"""<a class="{cls} reveal" href="{href}" data-cat="{html.escape(p['category'])}" data-sound="whisper">
  <span class="post-card__img"><img src="{up}assets/{p['cover']}" alt="{html.escape(p['cover_alt'])}" loading="lazy"></span>
  <span class="post-card__body">
    <span class="post-card__meta">{html.escape(p['category'])} · {p['read']}</span>
    <span class="post-card__title">{html.escape(p['title'])}</span>
    <span class="post-card__dek">{html.escape(p['dek'])}</span>
    <span class="link">Read <span aria-hidden="true">→</span></span>
  </span>
</a>"""


def build_index():
    chips = "".join(
        f'<button class="chip{" is-on" if c == "All" else ""}" type="button" data-filter="{html.escape(c)}">{html.escape(c)}</button>'
        for c in CATS
    )
    featured, rest = POSTS[0], POSTS[1:]
    page = head("Blog · unghosted", "Care tips, research and rituals for people who live with a ghost.", 1)
    page += f"""
  <main>
    <section class="blog-hero">
      <div class="wrap">
        <p class="eyebrow reveal">The journal</p>
        <h1 class="display flicker reveal">Notes from<br>the haunted.</h1>
        <p class="lead reveal" style="--d:.1s">Care tips, research and rituals for people who live with a ghost. We believe you.</p>
        <div class="chips reveal" style="--d:.2s" role="group" aria-label="Filter posts">{chips}</div>
      </div>
    </section>
    <section class="section section--tight">
      <div class="wrap">
        {card(featured, 1, big=True)}
        <div class="post-grid">
          {"".join(card(p, 1) for p in rest)}
        </div>
      </div>
    </section>
  </main>
"""
    page += foot(1)
    (OUT / "index.html").write_text(page)


def build_post(i, p):
    related = [POSTS[(i + 1) % len(POSTS)], POSTS[(i + 2) % len(POSTS)]]
    sources = ""
    if p["sources"]:
        lis = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a></li>' for t, u in p["sources"])
        sources = f'<section class="sources reveal"><p class="eyebrow">Sources</p><ol>{lis}</ol></section>'
    page = head(f"{p['title']} · unghosted", p["dek"], 1)
    page += f"""
  <main>
    <article class="article">
      <header class="article__head wrap">
        <a class="back link" href="index.html"><span aria-hidden="true">←</span> All posts</a>
        <p class="eyebrow reveal">{html.escape(p['category'])} · {p['date']} · {p['read']} read</p>
        <h1 class="article__title flicker reveal">{html.escape(p['title'])}</h1>
        <p class="article__dek reveal" style="--d:.1s">{html.escape(p['dek'])}</p>
      </header>
      <figure class="article__cover wrap reveal" style="--d:.15s">
        <div class="print-frame float" data-sound="whisper"><img src="../assets/{p['cover']}" alt="{html.escape(p['cover_alt'])}"></div>
      </figure>
      <div class="prose">
        {render_body(p['body'])}
        {sources}
        <p class="byline reveal">Written by the unghosted team. We are not doctors or mediums. When something feels unsafe, we point you to people who are.</p>
      </div>
    </article>
    <section class="section section--tight">
      <div class="wrap">
        <p class="eyebrow">Keep reading</p>
        <div class="post-grid post-grid--2">{card(related[0], 1)}{card(related[1], 1)}</div>
      </div>
    </section>
  </main>
"""
    page += foot(1)
    (OUT / f"{p['slug']}.html").write_text(page)


def build_home_strip():
    home = ROOT / "index.html"
    h = home.read_text()
    start, end = "<!-- journal:start -->", "<!-- journal:end -->"
    strip = f"""{start}
    <section class="section section--alt journal-strip" id="journal">
      <div class="wrap">
        <header class="section__head reveal">
          <p class="eyebrow">From the journal</p>
          <h2 class="h2">Notes from the haunted.</h2>
          <p class="sub">Care tips, research and rituals for living together.</p>
        </header>
        <div class="post-grid">{"".join(card(p, 0) for p in POSTS[:3])}</div>
        <div class="center reveal"><a class="btn btn--ghost" href="blog/index.html" data-sound="creak">Read the blog</a></div>
      </div>
    </section>
    {end}"""
    a, b = h.index(start), h.index(end) + len(end)
    home.write_text(h[:a] + strip + h[b:])


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build_home_strip()
    build_index()
    for i, p in enumerate(POSTS):
        build_post(i, p)
    print(f"Built blog index + {len(POSTS)} posts in {OUT}")
