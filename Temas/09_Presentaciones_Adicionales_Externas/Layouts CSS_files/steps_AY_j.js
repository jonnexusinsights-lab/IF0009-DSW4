(function() {
  // Registra cada <steps> como componente: añade data-marpit-fragment
  // a los <step> hijos (excepto el primero) y crea el indicador de progreso.
  // Se ejecuta sincrónicamente aquí para que bespoke.js encuentre los
  // atributos data-marpit-fragment al inicializar su lista de fragmentos.
  document.querySelectorAll('steps').forEach(steps => {
    const stepEls = [...steps.querySelectorAll(':scope > step')];

    // Asignar índices de fragmento a partir del segundo <step>
    stepEls.slice(1).forEach((step, i) => {
      step.setAttribute('data-marpit-fragment', String(i + 1));
    });

    // Crear indicador y añadirlo a la <section> contenedora
    const indicator = document.createElement('div');
    indicator.className = 'step-indicator';
   // const section = steps.closest('section');
    steps.appendChild(indicator);

    const update = () => {
      const total = stepEls.length;
      const lastActive = stepEls.findLastIndex(
        s => s.getAttribute('data-bespoke-marp-fragment') === 'active'
      );
      const current = lastActive === -1 ? 1 : lastActive + 1;
      indicator.textContent = `${current} / ${total}`;
    };

    // Observar cambios de atributo que hace bespoke al navegar
    const observer = new MutationObserver(update);
    stepEls.slice(1).forEach(step => {
      observer.observe(step, { attributes: true, attributeFilter: ['data-bespoke-marp-fragment'] });
    });
    update();
  });
})();