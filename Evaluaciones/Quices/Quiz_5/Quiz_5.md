# Quiz 5: Integración Rápida Back-End (Spring Boot) y Front-End Estático (HTML/CSS/JS)

**Curso:** IF0009 - Desarrollo de Software IV  
**Docente:** Mag. Jonathan Granados C.  
**Modalidad:** Trabajo Práctico Autónomo Individual  
**Tiempo Estimado de Ejecución:** 30 minutos  
**Entregable:** Un archivo `.zip` con el proyecto completo a través de Mediación Virtual.

---

## 📋 Enunciado General de la Evaluación Práctica

El objetivo de esta evaluación corta es comprobar la capacidad del estudiantado para integrar rápidamente un **Back-End en Spring Boot** básico con un **Front-End construido puramente en HTML, CSS y JavaScript Vanilla** (sin frameworks como Angular).

Deberá construir una pequeña aplicación de principio a fin, verificar su funcionamiento y subir el proyecto empaquetado a Mediación Virtual antes de que finalicen los 30 minutos.

---

## 🗳️ Caso de Estudio: Sistema de Votación Rápida "FastVote"

La asociación de estudiantes requiere un sistema exprés para realizar sondeos rápidos. Usted deberá construir un MVP (Minimum Viable Product) que permita registrar votos y visualizar los resultados en tiempo real.

---

## 🎯 Especificaciones Técnicas

### 1. Desarrollo Back-End (Spring Boot - 15 minutos)

Cree un proyecto Spring Boot con soporte para Web, JPA y H2 Database.

*   **Dominio:** Cree una entidad JPA `Voto` con los atributos:
    *   `id` (Long, PK, Autogenerado)
    *   `opcionVotada` (String, no nulo) - Puede ser por ejemplo "Opcion A", "Opcion B".
*   **Persistencia:** Cree una interfaz `VotoRepository` que herede de `JpaRepository`.
*   **Controlador:** Cree un `@RestController` (`VotoController`) expuesto en `/api/votos` con dos endpoints:
    *   `POST /api/votos`: Recibe un JSON con la `opcionVotada` y guarda el voto en la base de datos H2.
    *   `GET /api/votos`: Retorna la lista de todos los votos registrados.
*   **CORS:** Recuerde habilitar `@CrossOrigin` en el controlador para permitir peticiones desde el Front-End local.

### 2. Desarrollo Front-End (HTML/CSS/JS Vanilla - 10 minutos)

Cree una carpeta llamada `frontend` (fuera o dentro del proyecto Spring Boot, según prefiera) que contenga un archivo `index.html` y un archivo de estilos `style.css`.

*   **Estructura HTML:**
    *   Un título atractivo para la aplicación "FastVote".
    *   Dos botones de votación (ej. "Votar por Opción A", "Votar por Opción B").
    *   Una sección (ej. `<ul id="lista-votos">`) donde se mostrarán los votos registrados.
*   **Estilos CSS:**
    *   Utilice **Flexbox** o **CSS Grid** para centrar el contenido en la pantalla.
    *   Aplique colores, padding y bordes redondeados a los botones para darles un aspecto moderno y responsivo.
*   **Lógica JavaScript (Fetch API):**
    *   Agregue un script en el HTML que asigne eventos `click` a los botones.
    *   Al hacer clic, debe realizar un `fetch()` con método `POST` hacia su API en Spring Boot para registrar el voto.
    *   Inmediatamente después, debe realizar un `fetch()` con método `GET` para obtener la lista actualizada de votos y renderizarlos dinámicamente en el DOM (manipulando el `innerHTML` o creando nodos de la lista).

### 3. Empaquetado y Entrega (5 minutos)

*   Asegúrese de que el código compile y de que la inserción de datos funcione correctamente desde la interfaz web.
*   Elimine las carpetas de binarios compilados (`/target` del backend) para reducir el tamaño del archivo.
*   Comprima la carpeta raíz que contiene tanto el backend como el frontend en un archivo `.zip`.
*   Suba el archivo `.zip` al buzón habilitado en **Mediación Virtual** antes de que finalice el tiempo.

---

## 📊 Rúbrica de Evaluación (100 Puntos)

| Criterio | Puntos | Descripción |
|---|:---:|---|
| **API REST (Back-End)** | **40 pts** | Entidad JPA bien definida, repositorio y endpoints `GET` y `POST` funcionales y expuestos correctamente con soporte CORS. |
| **Interfaz y Estilos (Front-End)** | **30 pts** | Uso correcto de etiquetas semánticas HTML5. Diseño moderno empleando Flexbox o CSS Grid, con estilos visualmente atractivos. |
| **Integración JS (Fetch API)** | **30 pts** | Consumo exitoso de los endpoints de la API mediante `fetch()`. Actualización dinámica del DOM con los datos provenientes del servidor. |
