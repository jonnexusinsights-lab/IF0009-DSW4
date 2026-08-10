# Guía Técnica: ¿Cómo Gestionar y Compilar los Contenidos del Curso?

Esta guía técnica explica cómo utilizar las herramientas de compilación y estructuración de este repositorio para generar nuevas diapositivas, lecturas teóricas y evaluaciones.

---

## 📋 Requisitos Previos

Solo necesita contar con **Python 3.x** instalado localmente en su sistema. No se requieren instalaciones de Node.js, npm, ni de Marp CLI global. Toda la compilación se realiza de forma directa en Python mediante CDNs externas embebidas en la plantilla HTML resultante.

---

## 🚀 Compilación de Diapositivas

Las presentaciones se escriben en archivos Markdown (`.md`) utilizando la sintaxis de Marp y se compilan a archivos interactivos HTML con Reveal.js utilizando nuestro script compilador.

### Comando de Compilación
Abra una consola de comandos (PowerShell o CMD) en la raíz del proyecto y ejecute:

```powershell
python src/python_utils_src/marp_to_reveal.py Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa/1.2_Pila_Completa_Slides.md
```

Esto generará automáticamente el archivo:
`Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa/1.2_Pila_Completa_Slides.html`

---

## ✍️ Sintaxis y Reglas para Crear Diapositivas (`_Slides.md`)

Para que el script `marp_to_reveal.py` compile la presentación correctamente, siga las siguientes convenciones estructurales:

### 1. Cabecera (YAML Frontmatter)
Toda presentación debe iniciar con la configuración del motor de renderizado y el diseño visual premium. Copie y pegue esta cabecera en el primer slide:

```markdown
---
marp: true
theme: default
paginate: true
_class: lead
style: |
  section {
    font-family: 'Outfit', 'Inter', sans-serif;
    background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #1e1b4b 100%);
    color: #f8fafc;
    padding: 50px 70px;
    font-size: 22px;
  }
  h1 {
    color: #38bdf8;
    font-size: 1.7em;
    font-weight: 800;
    margin-bottom: 12px;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 10px;
  }
... (estilos css)
---
```

### 2. Separador de Diapositivas
Utilice exactamente la secuencia `\n---\n` en una sola línea para delimitar las diapositivas:

```markdown
# Slide anterior
Contenido...

---

# Siguiente Slide
Contenido...
```

### 3. Títulos y Subtítulos
*   **Título Principal (H1)**: `# Título de Diapositiva` (solo use uno por diapositiva).
*   **Subtítulo (H2)**: `## Subtítulo o Sección`.

### 4. Formateo de Listas e Indentación (Regla de Oro)
Para asegurar la legibilidad, escriba siempre los elementos de una lista en líneas separadas. Nuestro compilador soporta anidación:
*   **Listas Desordenadas (Viñetas)**:
    ```markdown
    * Componente Principal
      * Sub-componente o detalle A
      * Sub-componente o detalle B
    ```
*   **Listas Ordenadas (Numeración)**:
    ```markdown
    1. Primer paso operativo.
    2. Segundo paso operativo.
    ```

### 5. Bloques de Código
Escriba bloques de código con triple backtick e indique el lenguaje. El compilador protege estos bloques automáticamente y resalta su sintaxis con Tokyo Night:
```java
// Código Java
System.out.println("Seguro");
```

---

## 🧩 Crear un Nuevo Subtema (Paso a Paso)

Cuando deba planificar una nueva sesión de clases (ejemplo: **1.3 Tendencias**):

1.  **Crear Directorio**: Cree la carpeta correspondiente `Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias/`.
2.  **Lectura Teórica**: Redacte el archivo `1.3_Tendencias.md` en lenguaje educado en español ("usted"), explicando los conceptos clave y agregando ejemplos prácticos y preguntas de reflexión.
3.  **Diapositivas**: Cree el archivo `1.3_Tendencias_Slides.md`, inserte la cabecera YAML e ilustre de manera concisa y expandida el contenido del tema.
4.  **Compilar**: Ejecute el script `marp_to_reveal.py` sobre las diapositivas para generar el HTML.
5.  **Actualizar Contexto**: Abra [project_context.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/project_context.md) y registre los nuevos entregables en la **Tabla de Seguimiento de Entregables Generados**, actualizando las próximas tareas recomendadas.
