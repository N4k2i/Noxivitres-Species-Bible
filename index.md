---
title: Home
layout: default
accent: cyan
---
<section class="hero"><div class="hero-kicker">BLACKGLASS // CYBER-ORGANIC OPEN SPECIES</div><h1>NOXIVITRES</h1><p>A living species bible for bodies that do not have to stay fixed. Browse BlackGlass biology, Vitrite nanites, anatomy, rarity, culture, design rules, and Generation Zero without digging through one enormous file.</p><div class="hero-actions"><a class="button primary" href="{{ '/atlas/' | relative_url }}">Open the Reference Atlas →</a><a class="button" href="{{ '/parts/identity/' | relative_url }}">Start at Entry 001</a><button class="button" data-search-open>Search all references</button></div></section>
<section class="stats"><div class="stat"><strong>336</strong><span>encyclopedia entries</span></div><div class="stat"><strong>275</strong><span>technical plates</span></div><div class="stat"><strong>18</strong><span>major Parts</span></div><div class="stat"><strong>6</strong><span>rarity tiers</span></div></section>
<div class="callout"><strong>Core rule.</strong> BlackGlass can rewrite the body. Vitrite nanites keep the rewrite functioning. The body can split, duplicate, detach, regrow, and restructure, but the character is still more important than the mutation list.</div>
<div class="section-title"><div><h2>Read by system</h2><p>The fastest routes into the bible.</p></div><a href="{{ '/browse/' | relative_url }}">Browse all →</a></div>
<div class="card-grid">
<a class="card accent-magenta" href="{{ '/parts/blackglass/' | relative_url }}"><small>PART III</small><h3>BlackGlass Biology</h3><p>Glassshifts, duplication, regeneration, mutation memory, rejection, and instability.</p></a>
<a class="card accent-blue" href="{{ '/parts/nanites/' | relative_url }}"><small>PART IV</small><h3>Vitrite Nanites</h3><p>Repair, networking, floating-body control, interfaces, expression, exhaustion, corruption.</p></a>
<a class="card accent-teal" href="{{ '/parts/anatomy/' | relative_url }}"><small>PART II</small><h3>Anatomy</h3><p>Glassheart cores, tissues, skeletons, muscles, sensory structures, limbs and tails.</p></a>
<a class="card accent-gold" href="{{ '/rarity/' | relative_url }}"><small>SIX TIERS</small><h3>Rarity System</h3><p>Common through Mythic are open. Unobtanium is creator-locked.</p></a>
<a class="card accent-orange" href="{{ '/parts/creation/' | relative_url }}"><small>PART XI</small><h3>Create a Noxivitre</h3><p>Build coherent characters without reducing the species to a trait checklist.</p></a>
<a class="card accent-red" href="{{ '/founders/' | relative_url }}"><small>GENERATION ZERO</small><h3>Riven & Blade</h3><p>The first Noxivitres and the reference point for founder-class Unobtanium.</p></a>
</div>
<div class="section-title"><div><h2>All 18 Parts</h2><p>Long-form canon + technical atlas.</p></div></div>
<div class="card-grid">{% for part in site.data.parts %}<a class="card accent-{{ part.accent }}" href="{{ '/parts/' | append: part.slug | append: '/' | relative_url }}"><small>PART {{ part.roman }} · {{ part.range }}</small><h3>{{ part.title }}</h3></a>{% endfor %}</div>
<div class="section-title"><div><h2>Tools & shortcuts</h2><p>Useful ways to work with the canon.</p></div></div><div class="card-grid"><a class="card accent-orange" href="{{ '/tools/character-builder/' | relative_url }}"><small>INTERACTIVE</small><h3>Character Builder</h3><p>Build a structured OC profile and copy it as Markdown.</p></a><a class="card accent-pink" href="{{ '/reading-paths/' | relative_url }}"><small>GUIDED</small><h3>Reading Paths</h3><p>Routes for artists, writers, OC designers, rarity questions, and founder canon.</p></a><a class="card accent-aqua" href="{{ '/glossary/' | relative_url }}"><small>QUICK REFERENCE</small><h3>Glossary</h3><p>Fast definitions and links into the full entries.</p></a></div>
<div class="footer-note">This site is generated from the complete Markdown bible. The untouched source is included under <code>assets/source/</code> for auditing and editing.</div>
