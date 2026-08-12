(function () {
  const IMAGE_EXTS = /\.(png|jpe?g|webp|gif|svg)(\?.*)?$/i;

  /* ── Styles ────────────────────────────────────────────────────── */
  const style = document.createElement('style');
  style.textContent = `
    #img-modal-overlay {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: rgba(0, 0, 0, 0.85);
      align-items: center;
      justify-content: center;
      cursor: zoom-out;
    }
    #img-modal-overlay.open {
      display: flex;
    }
    #img-modal-overlay img {
      max-width: 90vw;
      max-height: 90vh;
      object-fit: contain;
      border-radius: 4px;
      box-shadow: 0 8px 40px #000a;
      cursor: default;
    }
    #img-modal-close {
      position: fixed;
      top: 1rem;
      right: 1.25rem;
      font-size: 2rem;
      line-height: 1;
      color: #fff;
      background: none;
      border: none;
      cursor: pointer;
      opacity: 0.7;
      z-index: 10000;
    }
    #img-modal-close:hover { opacity: 1; }
  `;
  document.head.appendChild(style);

  /* ── DOM ───────────────────────────────────────────────────────── */
  const overlay = document.createElement('div');
  overlay.id = 'img-modal-overlay';

  const closeBtn = document.createElement('button');
  closeBtn.id = 'img-modal-close';
  closeBtn.textContent = '✕';
  closeBtn.setAttribute('aria-label', 'Cerrar imagen');

  const img = document.createElement('img');
  img.alt = '';

  overlay.appendChild(closeBtn);
  overlay.appendChild(img);
  document.body.appendChild(overlay);

  /* ── Helpers ───────────────────────────────────────────────────── */
  const open = (src) => {
    img.src = src;
    overlay.classList.add('open');
  };

  const close = () => {
    overlay.classList.remove('open');
    img.src = '';
  };

  /* ── Events ────────────────────────────────────────────────────── */
  closeBtn.addEventListener('click', (e) => { e.stopPropagation(); close(); });
  overlay.addEventListener('click', close);
  img.addEventListener('click', (e) => e.stopPropagation()); // don't close when clicking image

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') close();
  });

  // Delegate: catch image-links added at any time (Marp fragments, etc.)
  document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a[href]');
    if (!anchor) return;
    if (!IMAGE_EXTS.test(anchor.getAttribute('href'))) return;
    e.preventDefault();
    open(anchor.getAttribute('href'));
  });
})();
