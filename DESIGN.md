# Profile design notes

## Direction

Owen chose a blend of an atmospheric blue night scene and a playful retro lab. The README presents machine learning first, gives visitors something real to try, and lets them open the engineering details.

The illustrated room is fictional artwork, not a photograph of Owen's actual workspace. The cassette and animated waveform are decorative. Clicking the panel opens the existing live Inflect demo; the README does not run inference or play audio automatically.

## Inspiration researched

- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme): a broad gallery of personal, illustrated, dynamic, and interactive profiles.
- [Tim Burgan's community chess](https://github.com/timburgan/timburgan): participation can make a profile memorable. Here, participation is trying a difficult sentence with an actual published model.
- [Tw93](https://github.com/tw93/tw93): connect the personal introduction to the work visitors can open.
- [Monica Powell](https://github.com/m0nica): a direct personal introduction and clear interests.
- [WhyProfile](https://github.com/tg-prplx/whyprofile): GitHub-compatible animated SVG scenes. Our SVG assets are original, self-contained files; no code or artwork was copied.
- [GitHub's profile documentation](https://docs.github.com/en/account-and-profile/concepts/personal-profile): profile READMEs combine personal context, work, images, and useful links.

## What makes this work

These are design judgments from the examples, not a universal ranking:

- A recognizable personal scene, with a consistent palette and typography.
- A short introduction in a human voice.
- A clear route to try the work.
- Specific evidence: published models, dataset sizes, runtime exports, and evaluation.
- Useful technical depth in expandable sections.
- Gentle scene animations with a reduced-motion fallback.
- Original files hosted in the repository, avoiding third-party banner widgets.
- Text descriptions and alt text alongside visual assets.

Common problems to avoid: an oversized badge wall, invented job titles, copied motivational slogans, fake live statistics, conflicting visual styles, dense reports, or links that look interactive but do not do what they promise.

## Content sources

- [Inflect source and release details](https://github.com/owenawsong/Inflect)
- [Inflect architecture](https://github.com/owenawsong/Inflect/blob/main/docs/ARCHITECTURE.md)
- [Inflect evaluation](https://github.com/owenawsong/Inflect/blob/main/docs/EVALUATION.md)
- [VoxCPM2 Synthetic English dataset card](https://huggingface.co/datasets/owensong/voxcpm2-synthetic-en-v1)
- [Chatterbox Nano ONNX model card](https://huggingface.co/owensong/chatterbox-nano-ONNX)
- [Harbor](https://github.com/owenawsong/Harbor)
- [Sleeve](https://github.com/owenawsong/liner)

## Artwork

The current banner is a code-authored pixel-art SVG in `assets/night-window.svg`, built with Codex assistance. Its shapes, colors, typography, and scene animations are editable in `scripts/build_banner.py`. Run `python scripts/build_banner.py` to rebuild it. The profile identifies Owen as a student developer. The cassette and waveform animation remain unchanged.

This replaces the earlier image-model illustration. It is not claimed to be artwork made independently by a human artist. All current graphics are self-contained SVG files with no external image services or remote fonts. Motion respects reduced-motion preferences.

### Previous illustration prompt (archived)

Use case: illustration-story.
Asset type: a meticulously art-directed original GitHub profile banner for Owen Song, an independent machine learning developer. Wide landscape composition, approximately 3:1.
Create a beautifully composed editorial illustration, with the finesse of a commissioned independent magazine cover. Blue nocturnal palette, midnight ink, dusty cerulean, pale ivory, one small warm amber lamp. Crisp silhouettes, subtle printed grain, deliberate fine linework, sophisticated light and shadow. It should have personality and be worth looking at closely.

The composition: the left roughly 45% is quiet dark navy negative space carrying the name. The right half depicts a wonderfully detailed small research workspace by a tall window looking into a moonlit blue forest. An empty chair, a compact monitor showing a simple abstract speech waveform without readable numbers, a small speaker, and an open notebook with tiny mathematical scribbles. The warm lamp casts a restrained pool of light. A couple of small plants and orderly books. The room and forest interlock through carefully drawn architectural framing; beautiful branches, atmospheric distance, subtle moon, a few stars. The scene is an illustrated fictional workspace, not a depiction of the user's actual room. No person. Use flat painterly editorial craft, not a glossy 3D render or photorealism. Avoid the stock anime desk-room composition; make this a distinct graphic illustration with interesting negative space and asymmetric composition.

Text verbatim: "Owen Song" on the left, large readable white hand-lettered contemporary serif lettering with a confident, beautiful silhouette, not all caps, not a cursive signature. Beneath it, smaller ivory text verbatim "machine learning & experiments". No other readable text.
This must read exceptionally well at 800px wide on GitHub and at phone size. No fake windows, dashboard cards, badges, network globes, gradient blobs, glowing purple AI brains, robots, logos, watermarks, or artificial-looking motivational taglines. Full-bleed composition, straight edges.

## Preview

The local preview approximates GitHub's Markdown layout. It is not a replacement website or an exact GitHub renderer. README content uses repository images, links, paragraphs, and native details/summary sections.

The repository was public at the last verification. Repository visibility is a separate account setting.

## Motion update

Removed the decorative corner brackets and window mullions. The banner displays just `@owenawsong`. Clouds drift, water shimmers, stars twinkle, fireflies move, coffee steam rises, the monitor waveform animates, and an occasional shooting star crosses the sky. All decorative motion stops when reduced motion is requested. The main text remains stationary. The listening-room animation is unchanged.
