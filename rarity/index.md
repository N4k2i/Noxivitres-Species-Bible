---
title: Rarity System
layout: default
accent: gold
---
<header class="part-hero"><div class="part-number">CLASSIFICATION</div><h1>Six rarity tiers.</h1><p>Rarity measures how much structural complexity and special BlackGlass behavior a complete build requires. It is not an automatic power scale and it does not rank a character's importance.</p></header>
<div class="rarity-grid">{% for rarity in site.data.rarities %}<div class="rarity-card" style="--rarity:{{ rarity.color }}"><h3>{{ rarity.name }}</h3><small>{{ rarity.status }}</small><p>{{ rarity.note }}</p></div>{% endfor %}</div>
<div class="callout"><strong>Open boundary:</strong> Common, Uncommon, Rare, Legendary, and Mythic are open. Mythic is deliberately the extreme open tier. <strong>Unobtanium is creator-locked</strong> and is reserved for specifically permitted founder-class or canon-authority concepts.</div>
<div class="section-title"><div><h2>Rarity entries</h2></div><a href="{{ '/parts/rarity/' | relative_url }}">Full Part VI →</a></div>
<div class="directory-grid">{% assign rarity_entries = site.entries | where_exp:'e','e.number >= "126" and e.number <= "150"' | sort:'number' %}{% for e in rarity_entries %}<a class="directory-item" href="{{ e.url | relative_url }}"><span class="num">ENTRY {{ e.number }}</span><strong>{{ e.title }}</strong><small>→</small></a>{% endfor %}</div>
