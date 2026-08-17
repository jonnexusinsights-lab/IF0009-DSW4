# Hoja de Referencia: CSS Maquetación y Estilos

Esta guía rápida resume los selectores, unidades, propiedades de variables y los modelos de diseño modernos Flexbox y Grid.

---

## Selectores y Modelo de Caja (Box Model)

CSS asocia estilos a elementos HTML basándose en una jerarquía de especificidad:

```css
/* Selector de Tipo (Etiqueta HTML) */
p {
    color: hsl(210, 40%, 15%);
}

/* Selector de Clase (Reutilizable) */
.card-title {
    font-size: 1.25rem;
}

/* Selector de Identificador (Único) */
#mainForm {
    padding: 20px;
}

/* Restablecimiento del Modelo de Caja Estándar */
* {
    box-sizing: border-box; /* Incluye bordes y rellenos en el ancho */
    margin: 0;
    padding: 0;
}
```

---

## Unidades de Medida Modernas

* **`px`**: Píxeles físicos (unidad estática. Evite su uso para tamaños de fuente).
* **`rem`**: Relativo al tamaño de fuente del elemento raíz (`<html>`). Esencial para accesibilidad.
* **`em`**: Relativo al tamaño de fuente del elemento padre directo.
* **`%`**: Relativo al tamaño del contenedor contenedor padre.
* **`vw` / `vh`**: Relativo al 1% del ancho / alto de la ventana del navegador.

---

## Maquetación Flexbox (Unidimensional)

Flexbox es ideal para alinear elementos en una única dimensión (filas o columnas).

```css
.flex-container {
    display: flex;
    flex-direction: row;        /* Dirección: row | column */
    flex-wrap: wrap;            /* Permitir salto de línea */
    justify-content: center;    /* Alineación horizontal en fila */
    align-items: center;        /* Alineación vertical en fila */
    gap: 15px;                  /* Espaciado interno de elementos */
}

.flex-item {
    flex: 1 1 200px;           /* grow | shrink | basis */
}
```

---

## Maquetación CSS Grid (Bidimensional)

CSS Grid permite diseñar cuadrículas con filas y columnas de forma simultánea.

```css
.grid-container {
    display: grid;
    
    /* Columnas auto-ajustables responsivas sin Media Queries */
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    
    gap: 20px;                 /* Espaciado entre rejillas */
}

.grid-item {
    /* Ocupar 2 columnas de ancho */
    grid-column: span 2;
}
```

---

## Variables CSS y Pseudo-clases de Interacción

```css
:root {
    --primary-color: hsl(220, 90%, 56%);
    --bg-dark: hsl(222, 47%, 11%);
}

/* Pseudo-clase de Foco para accesibilidad */
input:focus {
    border-color: var(--primary-color);
    outline: none;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

/* Pseudo-clases de validación nativas */
input:valid {
    border-color: hsl(142, 70%, 45%);
}
```
