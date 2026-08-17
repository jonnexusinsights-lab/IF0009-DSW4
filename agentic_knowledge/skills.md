# Habilidades Generativas (AI Skills)

Este archivo define los Procedimientos Estándares de Operación (SOP) y las estructuras de formato que debes seguir al ejecutar una tarea generativa específica para el curso.

**⚠️ Obligación de Contexto:** Al finalizar cualquier sesión o tarea de generación de contenido, debes actualizar el archivo de estado [project_context.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/project_context.md) para registrar el progreso, archivos creados y siguientes pasos.

## 🛠️ Definición de Habilidades

### 1. `Theory`
Usa este procedimiento para crear contenido de guías y explicaciones teóricas.
- **Estructura Requerida:**
  1. **Título (`H1`):** Título claro e identificativo del tema.
  2. **Resumen:** Breve resumen de 2 a 3 oraciones con los objetivos del tema.
  3. **Concepto Principal (El 'Qué'):** Definición rigurosa y académica apoyada en la documentación oficial, destacando términos clave en negrita y cursiva.
  4. **Analogía (La Intuición):** Asociación didáctica con un concepto de la vida cotidiana para asentar la teoría.
  5. **Ejemplo de Código e Implementación (El 'Cómo'):** Bloque de código completo, limpio y funcional en la tecnología objetivo, seguido de una explicación línea por línea de las instrucciones clave.
  6. **Trampas Comunes:** Detalle técnico de los errores más recurrentes al implementar el concepto y cómo prevenirlos.
  7. **Pregunta de Reflexión:** Reto lógico corto para que el estudiante evalúe lo aprendido en la lectura.
- **Reglas de Formato:** Markdown estándar limpio, separadores horizontales (`---`) entre secciones y uso del trato formal de **"usted"** en español.

---

### 2. `Lab`
Usa este procedimiento para diseñar laboratorios prácticos paso a paso.
- **Estructura Requerida:**
  1. **Título (`H1`):** Título descriptivo del laboratorio.
  2. **Metadatos:** Tiempo estimado de desarrollo, versiones de herramientas requeridas (Node.js, SDKs, Docker, etc.) y tres metas medibles.
  3. **Parte 1 (Práctica Guiada):** Planteamiento paso a paso de un problema real, código base completo con todas sus dependencias declaradas y captura/output de consola esperado.
  4. **Parte 2 (Depuración):** Código con un error intencional y común, guía instruccional para analizar el error en consola y procedimiento exacto para resolverlo.
  5. **Parte 3 (Reto Autónomo):** Requerimiento técnico adicional sin solución explícita, indicando únicamente las especificaciones a cumplir y cómo verificar el éxito.
- **Reglas de Formato y Estructura Técnica:**
  * **Trato Formal:** Uso estricto del pronombre formal **"usted"** en todas las directivas de acción.
  * **Checkboxes de Markdown:** Uso de `- [ ]` para pasos de depuración y tareas completadas.
  * **Separación Obligatoria de Listas (Líneas en Blanco):** Siempre coloque una **línea en blanco** entre un párrafo explicativo y el inicio de cualquier lista (viñetas `*`, numeraciones `1.` o checklists `- [ ]`). De lo contrario, los parsers de PDF/Markdown colapsarán la lista dentro del párrafo en una única línea continua en el PDF.
  * **Ajuste de Ancho de Código (Límite de 75 caracteres):** Todos los bloques de código (HTML, CSS, Java, Bash, etc.) deben tener líneas que no superen los **75 caracteres** de longitud, aplicando saltos de línea y formateo manual (ej. `\` para continuación de comandos). Esto evita que el código sea recortado lateralmente al exportarse a PDF.
  * **Sangría de Código Estructurado:** En bloques de código jerárquico (como HTML), aplique una indentación rigurosa de **4 espacios** por nivel de anidamiento para garantizar legibilidad.
  * **Flujo de Git integrado en IDE e IA:** En talleres o laboratorios de control de versiones, incluya guías visuales para operar el panel **Source Control** de Visual Studio Code y ejemplos prácticos de cómo interactuar con **Google Antigravity** como copiloto de IA (prompts sugeridos para redactar commits semánticos, generar archivos `.gitignore` y depurar fallas de consola).

---

### 3. `Quiz`
Usa este procedimiento para formular evaluaciones y cuestionarios.
- **Estructura Requerida:**
  1. **Metadata:** Título del cuestionario, total de puntos y tiempo límite recomendado.
  2. **Preguntas (`H3` numeradas):** Cuestionarios de opción múltiple (A, B, C, D) con casillas de verificación de Markdown (`- [ ]`), incluyendo al menos un ejercicio de rastreo de código (Tracing) donde el estudiante deba deducir la salida o el comportamiento de un script.
  3. **Solucionario:** Regla horizontal al final de la página (`---`) seguida de la explicación analítica e indiscutible de cada respuesta correcta y el análisis pedagógico de los distractores.
- **Reglas de Formato:** Lenguaje neutral de evaluación en español utilizando la conjugación de **"usted"** y bloques de código libres de ambigüedades lógicas.

---

### 4. `Presentation`
Usa este procedimiento para crear presentaciones de diapositivas atractivas utilizando la sintaxis de **Marp (Markdown Presentation Ecosystem)**.
- **Estructura Requerida:**
  1. **Directivas Marp (Frontmatter):** Define `marp: true`, `theme: default`, `paginate: true`, y un bloque `<style>` de CSS personalizado con un diseño premium, dinámico y de alto contraste (ej. gradientes de fondo modernos, tipografía Inter/Outfit, fuentes limpias y colores balanceados).
  2. **Diapositiva de Portada:** Título del tema (`H1`), subtítulo descriptivo corto y detalles del curso en una slide con alineación centrada (usando `_class: lead` o directiva de centrado).
  3. **Diapositivas de Contenido (Separadas por `---`):**
     - Distribuye el contenido conceptual en viñetas cortas, directas y legibles.
     - Utiliza palabras clave destacadas y evita el exceso de texto (máximo 4-5 viñetas por diapositiva).
     - Incorpora diagramas conceptuales textuales o esquemas rápidos cuando aplique.
  4. **Diapositivas de Código:** Bloques de código de sintaxis resaltada (` ```typescript `, etc.) ocupando un espacio visible y bien formateado.
  5. **Diapositivas de Discusión/Preguntas:** Slides específicas para plantear retos prácticos rápidos o preguntas de reflexión para captar la atención del estudiantado.
- **Reglas de Formato y Estética:**
  - Emplea un diseño moderno (ej. fondos oscuros con gradientes, tipografías elegantes, y un contraste de color impecable).
  - Mantén un tono formal y educado utilizando la conjugación de **"usted"** al dirigirse a la audiencia.

