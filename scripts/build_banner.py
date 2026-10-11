"""Build the profile's editable, code-authored pixel-art banner. No image model."""
from pathlib import Path
from html import escape
import math
import random

root = Path(__file__).resolve().parents[1]
rng = random.Random(37)
out = []
def rect(x, y, w, h, fill, extra=""):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>')
def path(d, fill, extra=""):
    out.append(f'<path d="{d}" fill="{fill}" {extra}/>')
def tree(x, ground, height, color):
    rect(x-1, ground-height+6, 2, height-6, color)
    for level in range(5):
        yy=ground-height+level*(height//6)
        half=3+level*2
        rect(x-half,yy,half*2+1,3,color)
        rect(x-half+2,yy-2,max(1,half*2-3),2,color)
    rect(x-7,ground-6,15,4,color)

# Right-hand illustration uses a compact pixel grid, scaled with sharp edges.
rect(0,0,304,192,"#152b45")
# Sparse stars, spaced with a fixed seed.
for _ in range(58):
    x=rng.randrange(8,287); y=rng.randrange(5,79)
    rect(x,y,1,1,rng.choice(["#6285a9","#a3becb","#345570"]))
# A stepped pixel moon.
for x,y,w,h in [(168,24,8,16),(164,28,16,8),(166,26,12,12)]:
    rect(x,y,w,h,"#d6d5bb")
rect(175,29,3,3,"#bcbfae");rect(168,35,2,2,"#c4c6b0")
# Distant layered ridgelines and lake.
path("M0 119V102H16V96H24V88H31V92H39V102H57V93H68V85H76V81H85V91H98V98H116V91H128V83H137V91H149V97H164V92H177V83H185V90H200V97H219V103H237V94H255V103H275V111H304V119Z","#254463")
path("M0 131V116H22V108H34V112H56V119H74V106H89V113H101V118H122V108H139V116H154V126H176V112H193V121H206V113H227V122H247V117H268V126H288V120H304V131Z","#1d3854")
rect(0,129,304,33,"#294a64")
for y,w in [(133,14),(137,25),(142,35),(148,43),(155,51)]:
    rect(171-w//2,y,w,1,"#8da9b5")
    rect(176-w//3,y+2,max(5,w//2),1,"#527894")
for _ in range(35):
    rect(rng.randrange(5,280),rng.randrange(131,161),rng.randrange(2,10),1,"#355871")
# Trees seen through the window.
for x,h in [(6,58),(23,35),(39,42),(60,31),(79,49),(109,30),(129,44),(206,65),(229,38),(247,49),(271,71),(292,42)]:
    tree(x,158,h,"#102a3e")
for x,h in [(4,76),(35,58),(92,64),(244,87),(284,95)]:
    tree(x,175,h,"#0b2233")
# Architectural window: a frame, not an arbitrary floating dashboard.
rect(0,0,7,175,"#081724");rect(0,172,304,9,"#354757")
rect(117,0,5,174,"#081724");rect(122,0,2,172,"#2c4150")
rect(297,0,7,192,"#081724")
rect(0,181,304,11,"#101f2b")
# Desk and amber lamp.
rect(133,165,164,7,"#877354");rect(133,172,164,3,"#594d3b")
rect(142,175,5,17,"#514639");rect(284,175,5,17,"#514639")
path("M258 119L294 157H221Z","#bda064", 'opacity=".15"')
rect(275,130,2,30,"#d7b77c");rect(266,159,19,3,"#a38c60")
path("M265 114H280V119H286V125H261V120H265Z","#d0b27c")
rect(261,125,25,2,"#eed4a2")
# Small monitor. The waveform is decorative, not a fabricated reading.
rect(194,118,64,43,"#0b151e");rect(197,121,58,36,"#193044")
rect(218,161,5,4,"#526373");rect(210,164,23,2,"#71808a")
for i in range(23):
    hh=2+int(abs(math.sin(i*.74)*math.sin(i*.22))*18)
    rect(202+i*2,139-hh//2,1,hh,"#a3bfcb")
# Notebook, books, keyboard and speaker.
rect(225,165,31,2,"#d4c7a6");rect(231,163,23,2,"#b7b6a0")
rect(152,156,28,5,"#486479");rect(155,152,23,4,"#b9a98b");rect(150,149,25,3,"#6c725e")
rect(200,167,22,2,"#8d9da3")
rect(263,143,9,20,"#0b1822");rect(265,147,5,5,"#3b5160");rect(266,148,3,3,"#81928f")
# Mug and a small plant.
rect(183,159,7,6,"#ae9574");rect(190,160,2,3,"#ae9574");rect(184,158,5,1,"#dbc09a")
rect(141,159,7,6,"#8d8061")
rect(143,146,2,13,"#536f64");rect(140,151,3,3,"#68867b");rect(145,147,4,3,"#597567")
# Chair with a folded scarf: deliberately geometric, small details.
rect(169,163,18,18,"#172b3b");rect(166,166,3,15,"#263b49");rect(169,180,23,5,"#1b3343")
rect(183,184,3,8,"#111d27");rect(172,170,3,13,"#66808a");rect(175,171,2,12,"#4c6571")
# Foreground frame makes the right edge intentional.
rect(297,4,7,188,"#091722")

scene = "".join(out)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
<title id="title">Owen Song — student developer</title>
<desc id="desc">An editable pixel-art night scene: a moonlit forest, a small desk and gently drifting fireflies. Machine learning and experiments.</desc>
<defs><clipPath id="edge"><rect width="1200" height="400" rx="8"/></clipPath><linearGradient id="fade"><stop stop-color="#091827"/><stop offset="1" stop-color="#091827" stop-opacity="0"/></linearGradient></defs>
<style>.firefly{{animation:drift 8s ease-in-out infinite alternate}}.firefly.slow{{animation-duration:11s;animation-delay:-4s}}@keyframes drift{{0%{{transform:translate(0,0);opacity:.35}}60%{{opacity:.85}}100%{{transform:translate(5px,-6px);opacity:.45}}}}@media(prefers-reduced-motion:reduce){{.firefly{{animation:none}}}}</style>
<g clip-path="url(#edge)">
<rect width="1200" height="400" fill="#091827"/>
<g transform="translate(592 8) scale(2)" shape-rendering="crispEdges">{scene}</g>
<rect x="550" width="95" height="400" fill="url(#fade)"/>
<path d="M36 46H72 M36 46V82 M1164 354H1128 M1164 354V318" fill="none" stroke="#657d90" opacity=".5"/>
<text x="48" y="106" fill="#8fa9bb" font-family="ui-monospace,monospace" font-size="17" letter-spacing="1.5">STUDENT DEVELOPER</text>
<text x="44" y="196" fill="#eadbc0" font-family="Georgia,serif" font-size="80" letter-spacing="-2">Owen Song</text>
<text x="48" y="242" fill="#a9becf" font-family="Arial,sans-serif" font-size="24">Machine learning &amp; experiments.</text>
<path d="M48 276H280" stroke="#365168"/>
<text x="48" y="308" fill="#829cad" font-family="ui-monospace,monospace" font-size="16">owenawsong / owensong</text>
<g fill="#e8d19c" shape-rendering="crispEdges">
<rect class="firefly" x="683" y="277" width="4" height="4"/><rect class="firefly slow" x="1068" y="191" width="3" height="3"/><rect class="firefly slow" x="849" y="96" width="3" height="3"/>
</g></g></svg>'''
(root/"assets"/"night-window.svg").write_text(svg,encoding="utf-8")
print("Built assets/night-window.svg")
