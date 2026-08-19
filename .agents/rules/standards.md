# Reglas y Estándares para Planificación de Lecciones y Prácticas Guiadas

Este documento define las reglas de diseño, formato y programación que se deben seguir obligatoriamente en todas las futuras sesiones para evitar errores estéticos de formato en la generación de PDF, incompatibilidades en consolas de Windows y no conformidades con el estándar del curso.

---

## 1. Reglas de Formateo de Código en Documentos Markdown

*   **Límite de caracteres en bloques de código:** Ninguna línea dentro de un bloque de código markdown (de lenguajes como Java, XML/Maven, JavaScript, HTML, CSS o comandos Bash) debe superar los **80 caracteres**. Si una línea de código o comentario supera este límite, debe segmentarse con saltos de línea estratégicos para evitar que se recorte en el margen derecho del PDF impreso.
*   **Numeración de pasos secuenciales:**
    *   **NO** utilice listas numeradas nativas de markdown (`1.`, `2.`, etc.) si los pasos están intercalados por bloques de código, citas o párrafos independientes. El compilador de PDF (`xhtml2pdf`) cierra la lista y la reinicia en `1.` en cada interrupción.
    *   **SÍ** utilice párrafos de texto plano numerados en negrita (ej: `**1.**`, `**2.**`, `**3.**`).
    *   **Espaciado obligatorio:** Siempre deje una línea en blanco (doble salto de línea) entre cada paso numerado en negrita para evitar que el renderizador de PDF los una en una única línea de texto.

---

## 2. Compatibilidad con Terminales de Windows (PowerShell/CMD)

*   **Evitar flag `-p` en mkdir:** Al indicar comandos de creación de directorios para los estudiantes, nunca use `mkdir -p`. Este flag no existe en el comando nativo de Windows PowerShell y genera errores. Use simplemente `mkdir` ya que crea los directorios intermedios de forma automática en Windows.
*   **Separadores de ruta:** Use barras normales (`/`) para las rutas en los comandos; son compatibles tanto en terminales de Windows como de Unix.

---

## 3. Estándar de Programación y Arquitectura Backend

*   **Estructura Multicapa Obligatoria:** Todos los proyectos backend en Java creados deben estructurarse bajo los siguientes paquetes de manera mandatoria:
    1.  `domain`: Modelos, entidades u objetos de negocio.
    2.  `controller`: Controladores REST.
    3.  `business`: Servicios o lógica de negocio.
    4.  `data`: Acceso a datos, persistencia o repositorios.
*   **Versión de Java:** Configurar los proyectos por defecto con **Java 21** en el `pom.xml`, incorporando siempre un comentario aclaratorio indicando al estudiante que debe sustituir esta versión por la que tenga instalada localmente en su computadora.

---

## 4. Control de Versiones con Git y GitHub

*   **Asegurar Rama `main`:** Siempre guíe al estudiante a verificar si la inicialización de Git se realizó sobre la rama `master`. De ser así, instruya la conversión a `main` ejecutando `git branch -M main` antes del primer *push* remoto para prevenir conflictos con GitHub.
