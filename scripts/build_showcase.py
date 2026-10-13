"""Build the profile's original SVG illustrations. Python standard library only."""
from pathlib import Path
from html import escape
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]


def text(x, y, value, size=24, color="#c0d1df", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(value)}</text>'


def rect(x, y, w, h, fill, radius=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" {extra}/>'


def save(name, body, width, height, title, description, style=""):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>text{{font-family:Arial,sans-serif}}.mono{{font-family:ui-monospace,monospace}}{style}
@media(prefers-reduced-motion:reduce){{.motion{{animation:none!important}}}}</style>
{body}</svg>'''
    digest = hashlib.sha256(svg.encode()).hexdigest()[:12]
    asset = f"assets/{name}-{digest}.svg"
    (ROOT / asset).write_text(svg, encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = re.sub(rf"assets/{name}(?:-[a-f0-9]+)?\.svg", asset, readme)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(asset)


def harbor():
    a = [rect(0, 0, 1200, 390, "#10232f", 8)]
    a.append('<g fill="none" stroke="#26414e" opacity=".65">')
    for y in range(28, 390, 38):
        a.append(f'<path d="M0 {y}Q160 {y-28} 280 {y}T550 {y}"/>')
    a.append('</g>')
    a += [text(42,51,"BROWSER AGENTS",17,"#8eb5ba",'class="mono" letter-spacing="2"'),
          text(38,130,"Harbor",78,"#e7ece3",'font-weight="700" letter-spacing="-3"'),
          text(42,184,"An agent in your browser.",29,"#e7ece3"),
          text(42,224,"Page context. Real browser tools.",24),
          text(42,259,"Watch each step as it works.",24),
          rect(42,299,254,48,"#afd1c2",5),text(62,330,"Explore the source  ↗",22,"#10232f",'font-weight="700"')]
    # A workflow illustration, not an imitation of a real screenshot or measured run.
    a += [rect(552,39,612,312,"#0a161e",9,'stroke="#446273"'),rect(553,40,610,43,"#243b49",8),rect(553,66,610,17,"#243b49"),
          '<g fill="#7294a3"><circle cx="573" cy="61" r="4"/><circle cx="588" cy="61" r="4"/><circle cx="603" cy="61" r="4"/></g>',
          rect(633,50,315,22,"#122733",5),text(650,66,"a page, an agent, your model",13,"#a6bdc9",'class="mono"'),
          rect(572,101,326,230,"#e5e8dc",4),text(590,127,"FIELD NOTES",13,"#49645e",'class="mono" letter-spacing="2"'),
          text(590,160,"A page worth reading.",21,"#183d3c",'font-weight="700"')]
    for i,w in enumerate([260,246,267,170]): a.append(rect(590,180+i*12,w,4,"#aabbb2",2))
    a += [rect(589,242,288,63,"#d4ddd0",3),rect(589,242,288,63,"none",3,'stroke="#437e79" stroke-width="2" class="motion selection"'),
          text(605,266,"A useful detail, right here.",17,"#244b46"),rect(605,278,235,4,"#8ca99a",2),rect(605,289,180,4,"#8ca99a",2),
          text(921,124,"Harbor",22,"#e7ece3",'font-weight="700"'),text(921,151,"Read this page.",16),'<path d="M931 185V276" stroke="#395968" stroke-width="2"/>']
    for i,(label,subtitle) in enumerate([("Read","Visual + DOM"),("Act","Browser tools"),("Report","Streaming progress")]):
        y=193+i*48
        a += [f'<circle cx="931" cy="{y-5}" r="7" fill="#335363"/>',f'<circle cx="931" cy="{y-5}" r="5" fill="#afd1c2" class="motion step step-{i}"/>',
              text(947,y,label,17,"#e7ece3",'font-weight="700"'),text(947,y+19,subtitle,13,"#9bb8c8")]
    a += ['<g class="motion cursor"><path d="M0 0V24L6 18L12 29L18 26L12 15H22Z" fill="#153c42" stroke="#e9f2e9" stroke-width="2"/></g>',
          text(1136,372,"WORKFLOW ILLUSTRATION",11,"#86a6b4",'class="mono" text-anchor="end" letter-spacing="1"')]
    style = '''.cursor{animation:cursor 12s ease-in-out infinite;transform:translate(842px,155px)}
@keyframes cursor{0%,15%,100%{transform:translate(842px,155px)}30%,58%{transform:translate(806px,270px)}72%,86%{transform:translate(1030px,276px)}}
.selection{animation:selection 12s ease-in-out infinite}@keyframes selection{0%,20%,95%,100%{opacity:.15}36%,80%{opacity:1}}
.step{animation:step 12s ease-in-out infinite}.step-1{animation-delay:-8s}.step-2{animation-delay:-4s}
@keyframes step{0%,27%,100%{opacity:1}35%,90%{opacity:.18}}'''
    illustration="".join(a)
    save("harbor-feature",illustration,1200,390,"Harbor — an agent in your browser",
         "Original animated workflow illustration: a cursor highlights a page while an agent uses visual and DOM context, browser tools and streaming progress. This is not a screenshot or a recorded run.",style)
    mobile=rect(0,0,600,665,"#10232f",8)
    mobile+=text(26,44,"BROWSER AGENTS",18,"#8eb5ba",'class="mono" letter-spacing="2"')
    mobile+=text(22,121,"Harbor",76,"#e7ece3",'font-weight="700" letter-spacing="-3"')
    mobile+=text(26,167,"An agent in your browser.",30,"#e7ece3")
    mobile+=text(26,209,"Page context. Real browser tools.",25)
    mobile+=text(26,245,"Watch each step as it works.",25)
    mobile+=f'<svg x="26" y="274" width="548" height="280" viewBox="552 39 612 312">{illustration}</svg>'
    mobile+=rect(26,588,302,49,"#afd1c2",5)+text(47,621,"Explore the source  ↗",25,"#10232f",'font-weight="700"')
    save("harbor-mobile",mobile,600,665,"Harbor — an agent in your browser","A compact version of the animated workflow illustration for smaller screens.",style)


def project_cards():
    shell=lambda bg:rect(0,0,600,264,bg,8)
    serif='style="font-family:Georgia,serif" letter-spacing="-1"'
    sleeve=shell("#201e1c")+text(28,48,"LISTENING HISTORY",15,"#b0a89e",'class="mono" letter-spacing="2"')
    sleeve+=text(26,104,"Sleeve",48,"#f0e7d7",serif)+text(28,140,"Your taste has a history.",23,"#c5bdb1")+text(28,232,"Open your record  ↗",21,"#fca377")
    sleeve+='<g transform="translate(476 192)"><circle r="57" fill="#10100f" stroke="#716457"/>'
    for r in [24,29,36,43,49]: sleeve+=f'<circle r="{r}" fill="none" stroke="#45403b"/>'
    sleeve+='<g class="motion record"><circle r="16" fill="#dc7950"/><path d="M0-16A16 16 0 0 1 16 0H0Z" fill="#f7b486"/><circle r="3" fill="#201e1c"/></g></g>'
    save("sleeve-showcase",sleeve,600,264,"Sleeve — your taste has a history","A rotating record. Explore your listening history in the live Sleeve app.",'.record{animation:spin 24s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}')

    counter=shell("#dfe7e6")+text(28,48,"NUMERICAL EXPERIMENTS",15,"#476c76",'class="mono" letter-spacing="2"')
    counter+=text(26,104,"Counterplot",48,"#123440",serif)+text(28,140,"Change an assumption. See why.",23,"#47616a")+text(28,232,"Explore the experiments  ↗",21,"#123440")
    counter+='<g transform="translate(390 164)" fill="none" stroke="#b0c6c7">'
    for x in range(0,181,30): counter+=f'<path d="M{x} 0V72"/>'
    for y in range(0,73,18): counter+=f'<path d="M0 {y}H180"/>'
    counter+='</g><path d="M390 228C420 228 430 170 460 174S490 235 520 210S546 167 570 169" fill="none" stroke="#3d737e" stroke-width="3"/><circle cx="460" cy="174" r="5" fill="#be754e" class="motion point"/>'
    save("counterplot-showcase",counter,600,264,"Counterplot — change an assumption, see why","A decorative curve on graph paper. Open the real numerical experiments and parameter studies.",'.point{animation:point 5s ease-in-out infinite}@keyframes point{0%,100%{opacity:1}50%{opacity:.4}}')

    rare=shell("#e6decf")+text(28,48,"TEXT-TO-SPEECH EVALUATION",15,"#786458",'class="mono" letter-spacing="1.5"')
    rare+=text(26,104,"RareSpeech",48,"#3e332b",serif)+text(28,140,"Look closer at the uncommon word.",23,"#6d5b4e")+text(28,232,"Inspect the audio evidence  ↗",21,"#8e4938")
    rare+=rect(381,179,177,29,"#d0c1a7",2,'class="motion underline"')+text(388,201,"anaptyxis",23,"#52392d",'class="mono"')+'<path d="M387 216H552M397 221V216M437 221V216M478 221V216M518 221V216" stroke="#957668"/>'
    save("rarespeech-showcase",rare,600,264,"RareSpeech — look closer at the uncommon word","A specialist term highlighted in a lexical notebook. Inspect rare-term target retention beside WER and listen to original recordings.",'.underline{animation:mark 7s ease-in-out infinite}@keyframes mark{0%,100%{opacity:.35}50%{opacity:1}}')

    discord=shell("#172a36")+text(28,48,"LOCAL BOT DEVELOPMENT",15,"#8eb2bc",'class="mono" letter-spacing="2"')
    discord+=text(26,104,"discord-bot-kit",43,"#e6eee8",'font-weight="700" letter-spacing="-1.5"')+text(28,140,"Test the handlers. Inspect the state.",23,"#aec4ca")+text(28,232,"Build a bot you can test  ↗",21,"#afd1c2")
    discord+='<g transform="translate(415 169)"><path d="M10 22H142" stroke="#476779" stroke-width="2"/>'
    for i,label in enumerate(["/","{}","✓"]):
        x=i*61
        discord+=rect(x,0,44,44,"#274654",5)+text(x+22,29,label,20,"#c2dcd0",'class="mono" text-anchor="middle"')
    discord+='<circle r="3" cy="22" fill="#daf0d7" class="motion event"/></g>'
    save("discord-kit-showcase",discord,600,264,"discord-bot-kit — test the handlers, inspect the state","A command flows through a handler to a test. Local bot recipes, executable scenarios, CLI and MCP tools.",'.event{animation:event 6s ease-in-out infinite}@keyframes event{0%,100%{transform:translateX(22px);opacity:0}15%{opacity:1}80%{transform:translateX(145px);opacity:1}90%{transform:translateX(145px);opacity:0}}')

    # GitHub's picture sources keep the project names legible at phone widths.
    variants=[
        ("sleeve-mobile","Sleeve","#201e1c","#f0e7d7","#fca377","LISTENING HISTORY",["Your taste has","a history."],"Open it  ↗",sleeve,"380 130 200 125"),
        ("counterplot-mobile","Counterplot","#dfe7e6","#123440","#3d737e","EXPERIMENTS",["Change an assumption.","See why."],"Try it  ↗",counter,"380 153 200 95"),
        ("rarespeech-mobile","RareSpeech","#e6decf","#3e332b","#8e4938","TTS EVALUATION",["Look closer at the","uncommon word."],"Inspect it  ↗",rare,"375 162 200 70"),
        ("discord-kit-mobile","discord-bot-kit","#172a36","#e6eee8","#afd1c2","BOT DEVELOPMENT",["Test the handlers.","Inspect the state."],"Build it  ↗",discord,"405 158 180 90")]
    for name,title,bg,fg,accent,label,lines,cta,art,view in variants:
        card=rect(0,0,300,284,bg,8)+text(18,32,label,13,fg,'class="mono" letter-spacing="1"')
        size=33 if title=="discord-bot-kit" else 38
        card+=text(16,82,title,size,fg,'font-weight="700" letter-spacing="-1"')
        card+=text(18,119,lines[0],20,fg)+text(18,148,lines[1],20,fg)
        card+=f'<svg x="166" y="178" width="120" height="92" viewBox="{view}">{art}</svg>'
        card+=text(18,249,cta,19,accent)
        save(name,card,300,284,title,f"Compact illustrated {title} panel for smaller screens.")


if __name__=="__main__":
    harbor()
    project_cards()
