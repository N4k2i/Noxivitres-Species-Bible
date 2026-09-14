---
title: Reference Atlas
layout: default
accent: cyan
---
<header class="part-hero"><div class="part-number">REFERENCE ATLAS</div><h1>Find the rule you actually need.</h1><p>The bible is enormous on purpose. This page is the shortcut layer: jump by system, rarity, character-building need, or reference type.</p></header>
<div class="section-title"><div><h2>Core systems</h2></div></div><div class="card-grid">
<a class="card accent-teal" href="{{ '/parts/anatomy/' | relative_url }}"><small>BODY</small><h3>Anatomy & Body Plan</h3><p>How structures attach, move, sense, heal, and remain part of the accepted body map.</p></a>
<a class="card accent-magenta" href="{{ '/parts/blackglass/' | relative_url }}"><small>MUTAGENIC SUBSTRATE</small><h3>BlackGlass</h3><p>The living rewrite system underneath Glassshifts, duplication, regeneration, and adaptive anatomy.</p></a>
<a class="card accent-blue" href="{{ '/parts/nanites/' | relative_url }}"><small>INFRASTRUCTURE</small><h3>Vitrite Nanites</h3><p>The distributed maintenance and control layer that keeps impossible-looking bodies operational.</p></a>
<a class="card accent-violet" href="{{ '/parts/morphology/' | relative_url }}"><small>VISIBLE BODY</small><h3>Morphology</h3><p>Arms, legs, floating parts, tails, wings, eyes, horns, mixed-animal builds and extreme silhouettes.</p></a>
<a class="card accent-gold" href="{{ '/rarity/' | relative_url }}"><small>CLASSIFICATION</small><h3>Rarity</h3><p>Six tiers measuring complexity and canon boundaries—not worth, morality, or automatic combat power.</p></a>
<a class="card accent-red" href="{{ '/founders/' | relative_url }}"><small>FOUNDERS</small><h3>Generation Zero</h3><p>Riven and Blade, Origin Glasshearts, founder-class body-map authoring, and Unobtanium restrictions.</p></a>
</div>
<div class="section-title"><div><h2>Technical atlases</h2><p>275 plates built for artists, writers, and system design.</p></div></div>
<div class="card-grid">{% for part in site.data.parts %}{% if part.number >= 14 %}<a class="card accent-{{ part.accent }}" href="{{ '/parts/' | append: part.slug | append: '/' | relative_url }}"><small>PART {{ part.roman }}</small><h3>{{ part.title }}</h3><p>{{ part.range }}</p></a>{% endif %}{% endfor %}</div>
