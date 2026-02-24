(function () {
  'use strict';

  var header = document.querySelector('header');
  var scrollThreshold = 50;

  // ----- 1. Nav background on scroll (opaque white + shadow after 50px) -----
  function updateNavStyle() {
    if (!header) return;
    if (window.scrollY > scrollThreshold) {
      header.style.backgroundColor = 'rgba(255, 255, 255, 0.92)';
      header.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.08)';
    } else {
      header.style.backgroundColor = '';
      header.style.boxShadow = '';
    }
  }

  window.addEventListener('scroll', updateNavStyle, { passive: true });
  updateNavStyle();

  // ----- 2. Smooth scroll to anchor (offset by header height) -----
  document.querySelectorAll('nav a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (href === '#') return;

      var id = href.slice(1);
      var target = document.getElementById(id);
      if (!target) return;

      e.preventDefault();
      var headerHeight = header ? header.offsetHeight : 0;
      var top = target.getBoundingClientRect().top + window.scrollY - headerHeight;
      window.scrollTo({ top: top, behavior: 'smooth' });
      if (history.replaceState) history.replaceState(null, '', href);
    });
  });

  // ----- 3. Load and render publications (clickable title: DOI > arXiv > url) -----
  var publicationsContainer = document.querySelector('.publications-cards');
  if (publicationsContainer) {
    fetch('data/publications.json')
      .then(function (res) { return res.ok ? res.json() : Promise.reject(res); })
      .then(function (list) {
        publicationsContainer.innerHTML = '';
        if (!list || list.length === 0) {
          publicationsContainer.innerHTML = '<p class="publications-empty">No publications loaded. Run <code>python scripts/fetch_publications.py</code> or check data/publications.json.</p>';
          return;
        }
        list.forEach(function (pub) {
          var linkUrl = '';
          if (pub.doi) linkUrl = 'https://doi.org/' + String(pub.doi).replace(/^https?:\/\/doi\.org\/?/i, '');
          else if (pub.arxiv_id) linkUrl = 'https://arxiv.org/abs/' + String(pub.arxiv_id).trim();
          else if (pub.url) linkUrl = pub.url;

          var venueYear = [pub.venue, pub.year].filter(Boolean).join(', ');
          if (pub.volume || pub.pages) venueYear += ' ' + (pub.volume || '') + (pub.pages ? ':' + pub.pages : '');
          var titleHtml = linkUrl
            ? '<a href="' + escapeAttr(linkUrl) + '" target="_blank" rel="noopener">' + escapeHtml(pub.title || '') + '</a>'
            : escapeHtml(pub.title || '');

          var card = document.createElement('article');
          card.className = 'publication-card';
          card.innerHTML =
            '<h3 class="publication-title">' + titleHtml + '</h3>' +
            '<p class="publication-meta">' + escapeHtml(pub.authors || '') + '</p>' +
            '<p class="publication-venue">' + escapeHtml(venueYear.trim()) + '</p>';
          publicationsContainer.appendChild(card);
        });
      })
      .catch(function () {
        publicationsContainer.innerHTML = '<p class="publications-empty">Could not load publications. <a href="https://scholar.google.com/citations?user=LZcqZqYAAAAJ&hl=en" target="_blank" rel="noopener">View on Google Scholar</a>.</p>';
      });
  }

  function escapeHtml(s) {
    var div = document.createElement('div');
    div.textContent = s;
    return div.innerHTML;
  }
  function escapeAttr(s) {
    return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
})();
