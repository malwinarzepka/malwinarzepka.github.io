---
title: Visualizing discrepancies
date: 2024-11-11
#external_link: https://github.com/pandas-dev/pandas
tags:
  - Housing bubbles
  - Past research
  - Bubble detection
  - PSY method
---

Interactive charts visualizing the discrepancies between the past housing bubble research in which GSADF test (Philips, Shi and Yu, 2015) was used. Pick country and gradually add each paper for the best understanding of how much results overlap (or not at all!)

For mobile phones, I recommend tilting your device horizontally, or viewing the charts directly in the [Tableau](https://public.tableau.com/shared/6CFY7MWQT?:display_count=n&:origin=viz_share_link).

<div class="tableauPlaceholder" id="viz1735517132628" style="width: 100%; height: auto; max-width: 1200px; min-width: 600px; margin: 0 auto;">
    <noscript>
        <a href="https://public.tableau.com/shared/6CFY7MWQT?:display_count=n&:origin=viz_share_link">
            <img alt="Visualizing detected housing bubbles - United Kingdom" 
                 src="https://public.tableau.com/static/images/HS/HSQ356B5K/1_rss.png" style="border: none;" />
        </a>
    </noscript>
    <object class="tableauViz" style="display: none;">
        <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />
        <param name="embed_code_version" value="3" />
        <param name="path" value="shared/HSQ356B5K" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/HS/HSQ356B5K/1.png" />
        <param name="animate_transition" value="yes" />
        <param name="display_static_image" value="yes" />
        <param name="display_spinner" value="yes" />
        <param name="display_overlay" value="yes" />
        <param name="display_count" value="yes" />
        <param name="language" value="en-US" />
    </object>
</div>
<script type="text/javascript">
    var divElement = document.getElementById('viz1735517132628');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (window.innerWidth <= 600) {
        // Mobile optimization
        vizElement.style.width = '100%';
        vizElement.style.height = '500px';
    } else {
        // Desktop optimization
        vizElement.style.width = '100%';
        vizElement.style.height = (divElement.offsetWidth * 0.6) + 'px'; // Better scaling
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

