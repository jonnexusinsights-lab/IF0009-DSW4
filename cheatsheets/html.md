# Hoja de Referencia: HTML5 Semántico y Estructuras

Esta guía rápida detalla los elementos semánticos estructurados y la sintaxis de formularios accesibles recomendados para el desarrollo web en el curso.

---

## Estructura Básica de un Documento HTML5

Todo documento HTML5 debe iniciar con la declaración de tipo de documento y contener las secciones principales cabecera (`head`) y cuerpo (`body`):

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estructura Estándar HTML5</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <h1>Mi Aplicación Web</h1>
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Servicios</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Sección de Contenido</h2>
            <article>
                <h3>Artículo 1</h3>
                <p>Descripción detallada del contenido semántico.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>© 2026 Universidad de Costa Rica</p>
    </footer>

</body>
</html>
```

---

## Principales Elementos Semánticos Estructurales

El HTML5 semántico describe el significado de los elementos tanto al desarrollador como a los navegadores y lectores de pantalla:

* **`<header>`**: Define la cabecera para un documento o una sección (suele contener logos, títulos o barras de búsqueda).
* **`<nav>`**: Define un conjunto de enlaces de navegación principal.
* **`<main>`**: Define el contenido dominante y único del cuerpo (`body`). Solo debe existir uno por página.
* **`<section>`**: Define una sección temática lógica y genérica en un documento.
* **`<article>`**: Define una unidad de contenido autónoma e independiente que puede distribuirse de forma aislada (ej. un post, una tarjeta de producto).
* **`<aside>`**: Define contenido indirectamente relacionado con el contenido principal (barra lateral de widgets, glosarios).
* **`<footer>`**: Define el pie de página para un documento o sección (suele contener derechos de autor, políticas, etc.).

---

## Formularios Accesibles e Interacción (Fetch)

Para garantizar la accesibilidad y permitir el envío asíncrono al Backend, relacione siempre los elementos de entrada con sus etiquetas:

```html
<form id="registroForm">
    <!-- Grupo de Entrada -->
    <div class="form-group">
        <label for="userEmail">Correo Electrónico:</label>
        <input type="email" id="userEmail" required 
               placeholder="ejemplo@correo.com">
    </div>

    <!-- Selección Única -->
    <div class="form-group">
        <label for="userRole">Rol:</label>
        <select id="userRole" required>
            <option value="">Seleccione...</option>
            <option value="estudiante">Estudiante</option>
            <option value="profesor">Profesor</option>
        </select>
    </div>

    <!-- Botón de Envío -->
    <button type="submit">Registrar Datos</button>
</form>
```
