# Subtema 5.2.3: Desarrollo de UI y Componentes Móviles Avanzados

Este módulo aborda la ingeniería avanzada de interfaces de usuario en Flutter, profundizando en sistemas de diseño multiplataforma, maquetación responsiva de alto rendimiento, optimización de ciclo de vida visual y dibujo a bajo nivel sobre la GPU.

---

## 📚 Estructura de Subtemas y Contenidos

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **5.2.3.1 Sistemas de Diseño** | [5.2.3.1_Sistemas_Diseno_Material3_Cupertino.md](5.2.3.1_Sistemas_Diseno_Material3_Cupertino.md) | [Slides Markdown](5.2.3.1_Sistemas_Diseno_Material3_Cupertino_Slides.md) | [Presentación HTML Reveal.js](5.2.3.1_Sistemas_Diseno_Material3_Cupertino_Slides.html) |
| **5.2.3.2 Layouts y Slivers** | [5.2.3.2_Layouts_Responsivos_Adaptativos_Slivers.md](5.2.3.2_Layouts_Responsivos_Adaptativos_Slivers.md) | [Slides Markdown](5.2.3.2_Layouts_Responsivos_Adaptativos_Slivers_Slides.md) | [Presentación HTML Reveal.js](5.2.3.2_Layouts_Responsivos_Adaptativos_Slivers_Slides.html) |
| **5.2.3.3 Custom Widgets y Animaciones** | [5.2.3.3_Widgets_Personalizados_Animaciones.md](5.2.3.3_Widgets_Personalizados_Animaciones.md) | [Slides Markdown](5.2.3.3_Widgets_Personalizados_Animaciones_Slides.md) | [Presentación HTML Reveal.js](5.2.3.3_Widgets_Personalizados_Animaciones_Slides.html) |
| **5.2.3.4 CustomPainter y Canvas** | [5.2.3.4_Pintado_Personalizado_CustomPainter_Canvas.md](5.2.3.4_Pintado_Personalizado_CustomPainter_Canvas.md) | [Slides Markdown](5.2.3.4_Pintado_Personalizado_CustomPainter_Canvas_Slides.md) | [Presentación HTML Reveal.js](5.2.3.4_Pintado_Personalizado_CustomPainter_Canvas_Slides.html) |

---

## 🎯 Competencias de Aprendizaje

1. **Diseño Multiplataforma:** Dominio de Material Design 3 (paletas tonales HCT, `ColorScheme.fromSeed`), Cupertino (Apple HIG) e interfaces adaptativas contextuales.
2. **Arquitectura de Maquetación:** Implementación del algoritmo de una sola pasada (*Constraints go down, sizes go up, parent sets position*), discriminación técnica entre `MediaQuery` y `LayoutBuilder`, y virtualización con `CustomScrollView`, `SliverAppBar`, `SliverList` y `SliverGrid`.
3. **Optimización Gráfica:** Aplicación del principio de composición sobre herencia, canonicalización de memoria mediante `const`, aislamiento de capas en GPU con `RepaintBoundary` y orquestación de animaciones a 60/120 FPS.
4. **Dibujo Vectorial a Bajo Nivel:** Manejo directo del sistema cartesiano 2D, primitivas de `Canvas`, curvas de Bézier cuadráticas/cúbicas con `Path` y optimización condicional con `shouldRepaint`.
