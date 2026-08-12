![UCR Banner](resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Laboratorio 1: Estructuras Web Semánticas y Diseño Responsivo con CSS Grid y Flexbox

## Metadatos
* **Tiempo Estimado:** 4 horas
* **Herramientas Requeridas:**
  * VS Code (o editor de texto preferido).
  * Extensión "Live Server" de VS Code (recomendada para previsualización dinámica).
  * Navegador web moderno con herramientas de desarrollador (DevTools).
* **Metas de Aprendizaje:**
  1. Diseñar una estructura de navegación multipágina utilizando elementos semánticos de HTML5.
  2. Implementar un diseño de grilla fluido y responsivo utilizando CSS Grid y Flexbox combinado con Media Queries.
  3. Crear formularios HTML5 con validaciones nativas y estilos visuales personalizados para los estados de foco, éxito y error.

---

## Introducción
El desarrollo moderno de interfaces web exige una separación clara entre el contenido (HTML) y la presentación (CSS). El uso correcto de etiquetas semánticas no solo mejora el posicionamiento SEO y la accesibilidad para lectores de pantalla, sino que también facilita la mantenibilidad del código.

En este laboratorio, usted construirá de manera semi-guiada un **Catálogo de Arquitecturas de Software Web**. La aplicación contará con tres secciones interconectadas: una página principal con tarjetas de tecnologías (usando CSS Grid), una página de detalle con contenidos técnicos estructurados, y una página de registro/contacto con un formulario validado.

---

## Parte 1: Práctica Guiada (Paso a Paso)

### Paso 1: Configuración de la Estructura del Proyecto
Cree un directorio de trabajo y estructure los siguientes archivos:
```text
laboratorio-1/
├── index.html
├── detalle.html
├── contacto.html
└── styles.css
```

### Paso 2: Página de Inicio (`index.html`) - Retícula de Tarjetas
Implemente el siguiente código para la página de inicio. Esta página utilizará etiquetas semánticas y un contenedor de clase `grid-container` que estilizaremos en el siguiente paso.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Arquitecturas Web</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header class="main-header">
        <div class="logo">ArchitecWeb</div>
        <nav class="main-nav">
            <ul>
                <li><a href="index.html" class="active">Inicio</a></li>
                <li><a href="detalle.html">Detalle</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main class="container">
        <section class="intro">
            <h2>Arquitecturas y Enfoques Web</h2>
            <p>Explore los diferentes paradigmas de desarrollo web modernos.</p>
        </section>

        <!-- Contenedor Grid -->
        <div class="tech-grid">
            <article class="tech-card">
                <h3>Multi-Page Applications (MPA)</h3>
                <p>El modelo clásico donde cada interacción del usuario solicita
                   una página completa nueva desde el servidor.</p>
                <a href="detalle.html" class="btn">Leer más</a>
            </article>

            <article class="tech-card">
                <h3>Single-Page Applications (SPA)</h3>
                <p>Aplicaciones fluidas que cargan una sola página HTML y
                   actualizan dinámicamente el DOM usando JavaScript.</p>
                <a href="detalle.html" class="btn">Leer más</a>
            </article>

            <article class="tech-card">
                <h3>Progressive Web Apps (PWA)</h3>
                <p>Sitios web optimizados que pueden instalarse y funcionar
                   offline asemejando la experiencia de apps nativas.</p>
                <a href="detalle.html" class="btn">Leer más</a>
            </article>
        </div>
    </main>

    <footer class="main-footer">
        <p>© 2026 ArchitecWeb - Universidad de Costa Rica</p>
    </footer>

</body>
</html>
```

### Paso 3: Diseño de la Retícula Responsiva con CSS Grid
Abra el archivo `styles.css` y escriba las reglas de diseño base. Utilizaremos la potencia de `grid-template-columns` combinado con `repeat` y `auto-fit` para crear una grilla que se adapte al tamaño de cualquier pantalla automáticamente.

```css
/* Variables del Sistema de Diseño */
:root {
  --primary-color: #1e3a8a;
  --secondary-color: #3b82f6;
  --bg-dark: #0f172a;
  --bg-card: #1e293b;
  --text-light: #f8fafc;
  --text-muted: #94a3b8;
  --border-color: #334155;
  --max-width: 1200px;
}

/* Reset Estándar */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-dark);
  color: var(--text-light);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.container {
  width: 90%;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 40px 0;
}

/* Navegación y Cabecera */
.main-header {
  background-color: var(--bg-card);
  border-bottom: 1px solid var(--border-color);
  padding: 20px 5%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--secondary-color);
}

.main-nav ul {
  display: flex;
  list-style: none;
  gap: 20px;
}

.main-nav a {
  color: var(--text-light);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.main-nav a:hover, .main-nav a.active {
  color: var(--secondary-color);
}

/* Sección de Grilla (CSS Grid) */
.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 30px;
}

/* Tarjetas */
.tech-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.tech-card h3 {
  color: var(--secondary-color);
  margin-bottom: 15px;
}

.tech-card p {
  color: var(--text-muted);
  margin-bottom: 20px;
}

.btn {
  background-color: var(--secondary-color);
  color: var(--text-light);
  padding: 10px 20px;
  text-decoration: none;
  text-align: center;
  border-radius: 4px;
  font-weight: 600;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #2563eb;
}

/* Pie de Página */
.main-footer {
  background-color: var(--bg-card);
  border-top: 1px solid var(--border-color);
  padding: 20px;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.9rem;
}
```

---

## Parte 2: Depuración (Gotchas y Diagnósticos)

### Escenario de Error: Layout Quebrado y Desborde de Elementos
Uno de los problemas más usuales ocurre cuando se utilizan propiedades de Flexbox o Grid de manera incorrecta, causando que las tarjetas no colapsen en pantallas pequeñas y desborden la ventana horizontalmente (aparece scrollbar horizontal).

#### Pasos de Simulación:
1. En su archivo `styles.css`, busque la regla `.tech-grid` y modifique temporalmente el valor de columnas para fijarlo estáticamente:
   ```css
   .tech-grid {
     display: grid;
     grid-template-columns: repeat(3, 350px); /* Valor incorrecto */
     gap: 30px;
   }
   ```
2. Reduzca la ventana del navegador a un tamaño simulado de dispositivo móvil (menos de 600px de ancho).
3. Notará que la retícula de tarjetas no se ajusta en columnas verticales, sino que permanece en tres columnas desbordando la pantalla.

#### Resolución del Problema:
- [ ] Presione **F12** y active el modo de emulación de dispositivo móvil (icono de celular/tablet en la esquina superior izquierda de DevTools).
- [ ] Seleccione el elemento contenedor `<div class="tech-grid">` en la pestaña **Elements**.
- [ ] En la pestaña lateral **Styles**, observe cómo el navegador procesa la propiedad `grid-template-columns`.
- [ ] Modifique el valor directamente en el navegador por `repeat(auto-fit, minmax(280px, 1fr))` y observe cómo el navegador recalcula automáticamente las columnas según el espacio disponible sin necesidad de recargar el archivo original.
- [ ] Copie la solución definitiva en su archivo `styles.css`.

---

## Parte 3: Trabajo Autónomo y Construcción

Para completar el laboratorio de forma exitosa, usted debe diseñar las vistas `detalle.html` y `contacto.html` aplicando las siguientes directrices técnicas:

### 1. Vista de Detalle (`detalle.html`)
* **Navegación:** Debe incluir el mismo encabezado (`header`) y pie de página (`footer`) de `index.html`. Asegúrese de marcar el enlace "Detalle" con la clase `active`.
* **Estructura Semántica:**
  * Use una sección principal que contenga un artículo descriptivo detallado sobre la arquitectura de tres capas (Cliente, Servidor, Datos).
  * Incorpore una tabla comparativa (`<table>`) que confronte las diferencias de rendimiento, SEO y velocidad de carga entre **SPA** y **MPA**.
  * Use etiquetas `<code>` e imágenes simuladas o diagramas para dar formato técnico al artículo.

### 2. Vista de Formulario (`contacto.html`)
* **Formulario de Registro de Suscriptores:**
  * Cree un formulario con los siguientes campos obligatorios:
    1. *Nombre Completo* (input de texto).
    2. *Correo Electrónico* (input de tipo `email`).
    3. *Rol Académico* (elemento select con opciones: Estudiante, Profesor, Graduado, Otro).
    4. *Mensaje o Comentarios* (textarea con un límite mínimo de 10 caracteres).
  * **Estilización CSS Requerida:**
    * Los inputs deben ocupar el 100% del contenedor y poseer bordes suaves con transiciones de color.
    * Al enfocar un campo (`:focus`), el borde debe cambiar a color azul celeste (`--secondary-color`) con un leve resplandor (`box-shadow`).
    * Use selectores de validación CSS como `:invalid` para marcar en rojo y `:valid` en verde de manera visual los campos correctos/incorrectos durante la escritura.

---

## Rúbrica de Evaluación

La calificación del laboratorio se calculará según la escala estipulada en la siguiente tabla:

| Criterio | Porcentaje | Descripción Detallada |
| :--- | :---: | :--- |
| **Estructuración Semántica (HTML5)** | **20%** | Uso correcto de etiquetas estructurales (`header`, `nav`, `main`, `section`, `article`, `footer`) en los tres documentos. |
| **Maquetación CSS Grid (Inicio)** | **20%** | Implementación correcta de una rejilla dinámica con columnas autoajustables y adaptables a dispositivos móviles sin desborde. |
| **Página de Detalle e Información** | **20%** | Maquetación interna con tablas estructuradas limpias, listas, formatos de código y flujo textual legible. |
| **Diseño y Estilo de Formulario** | **25%** | Formulario responsivo bien maquetado con estados visuales activos (`:focus`), y validación nativa funcional (`:invalid` / `:valid`). |
| **Calidad de Código y Entrega** | **15%** | Limpieza en el código fuente, correcto anidamiento de selectores, uso adecuado de variables y entrega puntual de los archivos. |
| **Total** | **100%** | **Nota final del Laboratorio 1** |
