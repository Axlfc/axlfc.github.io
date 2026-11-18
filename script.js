(() => {
  'use strict';
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  let saved = null;
  try { saved = localStorage.getItem('axlfc-theme'); } catch (_) {}
  const preferred = window.matchMedia && window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
  const apply = (theme) => {
    root.dataset.theme = theme;
    const statusBar = document.querySelector('meta[name="theme-color"]');
    if (statusBar) statusBar.setAttribute('content', theme === 'dark' ? '#142025' : '#faf9f6');
    button.setAttribute('aria-pressed', String(theme === 'dark'));
    button.setAttribute('aria-label', theme === 'dark' ? 'Activar modo claro' : 'Activar modo oscuro');
  };
  apply(saved === 'dark' || saved === 'light' ? saved : preferred);
  button.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    apply(next);
    try { localStorage.setItem('axlfc-theme', next); } catch (_) {}
  });
  // The original FormSubmit _next mistakenly used #contact?success=true.
  // A query parameter before the fragment lets this callback detect a redirect.
  const success = document.getElementById('contact-success');
  const params = new URLSearchParams(window.location.search);
  if (params.get('success') === 'true' && success) {
    success.hidden = false;
    window.history.replaceState({}, document.title, window.location.pathname + '#contacto');
  }
  // Deep links into archived items must reveal the containing disclosure.
  // Without this, original #EditMovie and #GetWinget URLs target hidden content.
  const revealHashTarget = () => {
    if (!window.location.hash) return;
    let id;
    try { id = decodeURIComponent(window.location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (!target) return;
    let parent = target.closest('details');
    let wasHidden = false;
    while (parent) {
      if (!parent.open) { parent.open = true; wasHidden = true; }
      parent = parent.parentElement?.closest('details');
    }
    if (wasHidden) {
      window.requestAnimationFrame(() => target.scrollIntoView({block: 'start', behavior: 'instant'}));
    }
  };
  window.addEventListener('hashchange', revealHashTarget);
  revealHashTarget();

  // Close the compact navigation after selection or Escape.
  const mobileNav = document.getElementById('mobile-nav');
  mobileNav?.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => { mobileNav.open = false; });
  });
  mobileNav?.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mobileNav.open) {
      mobileNav.open = false;
      mobileNav.querySelector('summary')?.focus();
    }
  });

  // Maintain the original clone/copy functionality as an optional disclosure.
  const clipboardStatus = document.getElementById('clone-copy-status');
  document.querySelectorAll('.clone-copy').forEach(copyBtn => {
    copyBtn.addEventListener('click', async () => {
      const command = `git clone ${copyBtn.dataset.repo}`;
      try {
        if (navigator.clipboard?.writeText) {
          await navigator.clipboard.writeText(command);
        } else {
          const field = document.createElement('textarea');
          field.value = command;
          field.style.position = 'fixed';
          field.style.left = '-9999px';
          document.body.appendChild(field);
          field.select();
          const ok = document.execCommand('copy');
          field.remove();
          if (!ok) throw new Error('La copia no está disponible');
        }
        if (clipboardStatus) clipboardStatus.textContent = `Comando copiado: ${copyBtn.dataset.repo.split('/').pop()}`;
      } catch (_) {
        if (clipboardStatus) clipboardStatus.textContent = 'No se pudo copiar. Selecciona el comando mostrado y cópialo manualmente.';
      }
    });
  });
})();

