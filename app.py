import streamlit as st

st.set_page_config(page_title="Shorts, on your terms", page_icon="▶", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{--ink:#f5f2ee;--muted:#a5a2ad;--line:#292832;--panel:#17161d;--bg:#101014;--lime:#d7fa68;--pink:#ff7a9d}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;color:var(--ink)}
.stApp{background:radial-gradient(ellipse at 78% 0%,#29242d 0%,#101014 42%);color:var(--ink)}
#MainMenu,footer,header{visibility:hidden}.block-container{max-width:1360px;padding-top:1.4rem;padding-bottom:3rem}
.brand{font-family:'Space Grotesk';font-size:1.32rem;font-weight:700;letter-spacing:-.04em}.brand span{color:var(--lime)}
.eyebrow{color:var(--lime);font-size:.72rem;font-weight:700;letter-spacing:.17em;text-transform:uppercase}
h1,h2,h3{font-family:'Space Grotesk',sans-serif;letter-spacing:-.045em} h1{font-size:3.2rem!important;line-height:1.04!important;margin:.45rem 0 .7rem!important} h2{font-size:1.65rem!important}
.sub{color:var(--muted);font-size:1rem;line-height:1.6}.chip{display:inline-block;border:1px solid #383741;border-radius:100px;padding:7px 13px;margin:4px 5px 4px 0;color:#d1ced7;font-size:.82rem}
.chip.active{border-color:var(--lime);color:var(--lime);background:#d7fa6810}
.video{height:438px;border-radius:24px;background:linear-gradient(145deg,#4e313a,#191c2b 52%,#25253e);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;border:1px solid #3a3744}
.video:before{content:'';position:absolute;width:310px;height:410px;border-radius:50%;background:radial-gradient(ellipse,#ffae8c77,transparent 65%);filter:blur(20px);transform:translate(-15px,20px)}
.play{position:relative;border:1px solid #ffffff55;background:#ffffff25;backdrop-filter:blur(12px);border-radius:50%;width:76px;height:76px;display:grid;place-items:center;font-size:1.8rem}
.v-label{position:absolute;left:22px;top:20px;background:#10101499;border-radius:20px;padding:7px 11px;font-size:.75rem}.v-foot{position:absolute;bottom:18px;left:20px;right:20px;display:flex;justify-content:space-between;color:#fff;font-size:.8rem}
.creator{font-size:1.1rem;font-weight:700}.muted{color:var(--muted);font-size:.86rem}.stat{color:#e8e5ec;font-weight:600}.card{background:linear-gradient(145deg,#1b1a22,#15141a);border:1px solid #2c2b35;border-radius:19px;padding:19px 20px;margin:8px 0}
.mini{height:124px;border-radius:14px;background:linear-gradient(145deg,#c17b5c,#402c55);display:flex;align-items:center;justify-content:center;font-size:2rem;margin-bottom:12px}
.mini.two{background:linear-gradient(145deg,#4c8c8b,#273355)}.mini.three{background:linear-gradient(145deg,#9776ad,#43314f)}.mini.four{background:linear-gradient(145deg,#c5a05c,#554441)}
div[data-testid="stButton"]>button{border-radius:100px;border:1px solid #3a3944;background:#1b1a22;color:#f5f2ee;font-weight:600;min-height:2.55rem} div[data-testid="stButton"]>button:hover{border-color:var(--lime);color:var(--lime)}
button[kind="primary"]{background:var(--lime)!important;color:#14140f!important;border:0!important}
div[data-testid="stSelectbox"]>div,div[data-testid="stTextInput"]>div>div{background:#19181f;border-color:#383741;color:#f5f2ee}
div[role="radiogroup"]{gap:.4rem}div[role="radiogroup"] label{background:#19181f;border:1px solid #363540;border-radius:100px;padding:.45rem .8rem!important}
.divider{border-top:1px solid var(--line);margin:26px 0}.tagline{color:var(--muted);font-size:.84rem}
@media(max-width:800px){h1{font-size:2.2rem!important}.video{height:350px}}
</style>
""", unsafe_allow_html=True)

DATA = [
 {"creator":"Mina Makes","handle":"@minamakes","title":"A tiny garden for your windowsill 🌱","topic":"Creative","views":"2.4M","length":"0:28","glyph":"🌿","tone":"mini"},
 {"creator":"Theo Cooks","handle":"@theocooks","title":"The crispiest chili oil eggs","topic":"Food","views":"890K","length":"0:41","glyph":"🍳","tone":"mini two"},
 {"creator":"Nia Outside","handle":"@niaoutside","title":"A quiet morning in the mountains","topic":"Travel","views":"1.2M","length":"0:34","glyph":"🏔️","tone":"mini three"},
 {"creator":"Soft Science","handle":"@softscience","title":"Why the moon looks bigger at the horizon","topic":"Learning","views":"604K","length":"0:52","glyph":"🌙","tone":"mini four"},
]
if "saved" not in st.session_state: st.session_state.saved = []
if "captions" not in st.session_state: st.session_state.captions = True
if "playing" not in st.session_state: st.session_state.playing = False
if "selected" not in st.session_state: st.session_state.selected = 0

top1, top2 = st.columns([2,3])
with top1: st.markdown('<div class="brand">you<span>●</span>tube <span>SHORTS</span></div>',unsafe_allow_html=True)
with top2:
 page = st.radio("Main navigation",["For you","Explore","Saved","Settings"],horizontal=True,label_visibility="collapsed",key="nav")
st.markdown('<div class="divider"></div>',unsafe_allow_html=True)

if page == "For you":
 left,right=st.columns([1.04,1],gap="large")
 with left:
  st.markdown('<div class="eyebrow">Your feed, your pace</div><h1>Good stuff.<br>On your terms.</h1><div class="sub">A calmer Shorts experience, shaped around what you love and how you like to watch.</div>',unsafe_allow_html=True)
  st.write("")
  st.markdown('<span class="chip active">For you</span><span class="chip">Creative</span><span class="chip">Food</span><span class="chip">Learning</span>',unsafe_allow_html=True)
  st.write("")
  item=DATA[st.session_state.selected]
  st.markdown(f'<div class="creator">{item["creator"]} <span class="muted">{item["handle"]}</span></div><div style="margin-top:7px;font-size:1.08rem">{item["title"]}</div><div class="muted" style="margin-top:8px">{item["views"]} views　·　{item["topic"]}</div>',unsafe_allow_html=True)
  b1,b2,b3=st.columns(3)
  with b1: st.button("＋  Save",use_container_width=True,on_click=lambda: st.session_state.saved.append(st.session_state.selected) if st.session_state.selected not in st.session_state.saved else None,key="save")
  with b2: st.button("↗  Share",use_container_width=True,key="share")
  with b3: st.button("⋯  More",use_container_width=True,key="more")
  st.markdown('<div class="card"><div style="font-weight:700">Make it yours</div><div class="muted" style="margin:5px 0 12px">Tune your feed any time. Your choices stay in your control.</div>',unsafe_allow_html=True)
  st.selectbox("Show me more",["A little more of this","Keep my feed balanced","Less of this creator"],label_visibility="collapsed")
  st.markdown('</div>',unsafe_allow_html=True)
 with right:
  st.markdown(f'<div class="video"><div class="v-label">SHORTS　·　{item["topic"].upper()}</div><div class="play">{"Ⅱ" if st.session_state.playing else "▶"}</div><div class="v-foot"><span>{"CC ON" if st.session_state.captions else "CC OFF"}　•　Audio description available</span><span>{item["length"]}</span></div></div>',unsafe_allow_html=True)
  controls=st.columns([1,1,1,1,1])
  with controls[0]:
   if st.button("▶ / Ⅱ",use_container_width=True): st.session_state.playing=not st.session_state.playing; st.rerun()
  with controls[1]:
   if st.button("CC",use_container_width=True): st.session_state.captions=not st.session_state.captions; st.rerun()
  with controls[2]:
   if st.button("− 10s",use_container_width=True): st.toast("Rewind 10 seconds")
  with controls[3]:
   if st.button("＋ 10s",use_container_width=True): st.toast("Skip ahead 10 seconds")
  with controls[4]:
   if st.button("Next ↓",use_container_width=True): st.session_state.selected=(st.session_state.selected+1)%len(DATA); st.rerun()
  st.markdown('<div class="muted" style="text-align:center;margin-top:8px">Keyboard: ← → change video · Space play / pause · C captions</div>',unsafe_allow_html=True)
 st.markdown('<div class="divider"></div><div class="eyebrow">Picked for your interests</div><h2>A little more like this</h2>',unsafe_allow_html=True)
 cols=st.columns(4)
 for i,(col,item) in enumerate(zip(cols,DATA)):
  with col:
   st.markdown(f'<div class="card"><div class="{item["tone"]}">{item["glyph"]}</div><div style="font-weight:700">{item["title"]}</div><div class="muted" style="margin-top:6px">{item["creator"]} · {item["views"]}</div></div>',unsafe_allow_html=True)
   if st.button("Watch this",key=f"watch{i}",use_container_width=True): st.session_state.selected=i; st.rerun()
elif page == "Explore":
 st.markdown('<div class="eyebrow">Discover something new</div><h1>Find your next<br>little obsession.</h1><div class="sub">Explore by interest, mood, or a quick search.</div>',unsafe_allow_html=True)
 query=st.text_input("Search videos, creators, or topics",placeholder="Try ‘easy recipes’ or ‘slow living’")
 topics=st.columns(4)
 for i,(title,emoji,desc) in enumerate([("Make something","🎨","Art, crafts & ideas"),("Eat well","🍋","Recipes worth saving"),("Go somewhere","🧭","Places to daydream"),("Learn a little","💡","Small things, big ideas")]):
  with topics[i]:
   st.markdown(f'<div class="card"><div style="font-size:2rem">{emoji}</div><h3>{title}</h3><div class="muted">{desc}</div></div>',unsafe_allow_html=True)
 st.markdown('<div class="divider"></div><h2>Popular this week</h2>',unsafe_allow_html=True)
 cols=st.columns(4)
 filtered=[x for x in DATA if not query or query.lower() in (x['title']+x['creator']+x['topic']).lower()]
 for i,x in enumerate(filtered):
  with cols[i%4]: st.markdown(f'<div class="card"><div class="{x["tone"]}">{x["glyph"]}</div><b>{x["title"]}</b><div class="muted">{x["creator"]} · {x["topic"]}</div></div>',unsafe_allow_html=True)
elif page == "Saved":
 st.markdown('<div class="eyebrow">A little library of your own</div><h1>Saved for later.</h1><div class="sub">Keep the Shorts you love, together in one place.</div>',unsafe_allow_html=True)
 c1,c2=st.columns([1,2]);
 with c1: st.markdown('<div class="card"><div class="eyebrow">COLLECTION</div><h2>My favorites</h2><div class="muted">A place for the good ones.</div></div>',unsafe_allow_html=True)
 with c2:
  if st.session_state.saved:
   for i in st.session_state.saved:
    x=DATA[i]; st.markdown(f'<div class="card"><b>{x["glyph"]}　{x["title"]}</b><div class="muted">{x["creator"]} · {x["topic"]}</div></div>',unsafe_allow_html=True)
  else: st.info("Your collection is waiting. Tap ＋ Save on a Short to keep it here.")
 st.button("＋  Create a collection",key="create_collection")
else:
 st.markdown('<div class="eyebrow">Comfort & control</div><h1>Watch your way.</h1><div class="sub">Small adjustments can make a big difference. Set things up just right.</div>',unsafe_allow_html=True)
 st.markdown('<div class="divider"></div>',unsafe_allow_html=True)
 a,b=st.columns(2,gap="large")
 with a:
  st.markdown('<div class="card"><h2>Captions</h2><div class="muted">Choose how captions appear across Shorts.</div>',unsafe_allow_html=True)
  st.toggle("Always show captions",key="captions")
  st.selectbox("Caption size",["Default","Large","Extra large"])
  st.selectbox("Caption style",["High contrast","Classic","Translucent background"])
  st.markdown('</div><div class="card"><h2>Playback</h2><div class="muted">Set the pace and sound that feels right.</div>',unsafe_allow_html=True)
  st.toggle("Autoplay next Short",value=True)
  st.select_slider("Default playback speed",options=["0.5×","0.75×","1×","1.25×","1.5×"],value="1×")
  st.markdown('</div>',unsafe_allow_html=True)
 with b:
  st.markdown('<div class="card"><h2>Your feed</h2><div class="muted">Shape what shows up in your recommendations.</div>',unsafe_allow_html=True)
  st.multiselect("Interests",["Creative","Food","Travel","Learning","Music","Wellness"],default=["Creative","Food","Learning"])
  st.selectbox("Personalization",["Personalized for me","Mix in fresh topics","Show less personalization"])
  st.markdown('</div><div class="card"><h2>Reduce motion</h2><div class="muted">Tone down animation and moving transitions.</div>',unsafe_allow_html=True)
  st.toggle("Reduce motion",value=False)
  st.markdown('</div>',unsafe_allow_html=True)
  st.button("Save preferences",type="primary")
st.markdown('<div class="divider"></div><div class="tagline">A design concept for a more thoughtful Shorts experience · Not affiliated with YouTube</div>',unsafe_allow_html=True)
