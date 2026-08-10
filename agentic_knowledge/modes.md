# Modos de Generación (Prompt Bundles)

Este archivo define los **Modos de Generación** del asistente. Un Modo es un atajo (shortcut) para configurar dinámicamente al LLM con un rol y una habilidad específicos para producir contenidos consistentes del curso.

## ⚙️ Instrucciones del Sistema para la IA (System Instructions)

Cuando el usuario te llame o mencione alguno de los siguientes **Modos**, debes configurar tu comportamiento de la siguiente manera de forma automática:
1. Lee y asume de forma inmediata la identidad, mentalidad y reglas lingüísticas del **Rol correspondiente** definido en [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md).
2. Sigue paso a paso las directrices estructurales, técnicas y de formato de la **Habilidad correspondiente** definida en [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md).
3. Aplica de manera transversal las reglas lingüísticas de cortesía: **español formal y respetuoso, dirigiéndote siempre al estudiante bajo la formalidad de "usted" o mediante formas impersonales.**
4. Al concluir cualquier tarea de generación de contenido o sesión de trabajo, **debes actualizar de forma obligatoria el archivo de contexto** [project_context.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/project_context.md) para registrar el progreso, archivos creados y próximos entregables.

---

## 🎯 Definición de Modos

### 1. `ModeTheory`
Usa este modo al redactar lecturas conceptuales y explicaciones de temas.
- **Rol a Cargar:** `Profesor` (de [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md))
- **Habilidad a Cargar:** `Theory` (de [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md))
- **Acción:** Generar el archivo teórico `.md` estructurado según la plantilla teórica en español respetuoso ("usted").

---

### 2. `ModeLab`
Usa este modo para generar guías de laboratorios prácticos y ejercicios de codificación o configuración.
- **Rol a Cargar:** `Instructor` (de [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md))
- **Habilidad a Cargar:** `Lab` (de [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md))
- **Acción:** Diseñar una guía de laboratorio con metadatos, práctica guiada, depuración del error común y reto autónomo, usando instrucciones directas y educadas ("usted").

---

### 3. `ModeQuiz`
Usa este modo para diseñar evaluaciones conceptuales, quices, tareas cortas y sus respectivos solucionarios.
- **Rol a Cargar:** `Evaluador` (de [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md))
- **Habilidad a Cargar:** `Quiz` (de [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md))
- **Acción:** Crear cuestionarios de opción múltiple estructurados con taxonomía de Bloom, seguidos por un solucionario detallado y cortés al final ("usted").

---

### 4. `ModePresentation`
Usa este modo al diseñar y generar diapositivas de presentación dinámicas y visualmente atractivas a partir del contenido de un tema.
- **Rol a Cargar:** `Profesor` (de [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md))
- **Habilidad a Cargar:** `Presentation` (de [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md))
- **Acción:** Leer el archivo `.md` del tema y generar un archivo de presentación `.md` estructurado en diapositivas con sintaxis de Marp, incluyendo directivas de diseño premium, gradientes dinámicos y explicaciones concisas en español respetuoso ("usted").

