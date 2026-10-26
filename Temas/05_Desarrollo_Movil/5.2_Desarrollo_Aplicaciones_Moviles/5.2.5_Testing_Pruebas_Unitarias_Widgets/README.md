# Subtema 5.2.5: Pruebas Unitarias y Widget Testing en Aplicaciones Móviles

Este módulo aborda la pirámide de aseguramiento de calidad de software móvil en Flutter, profundizando en pruebas unitarias deterministas, técnicas de simulación de dependencias (Mocking), pruebas de componentes gráficos (Widget Testing) y métricas cuantitativas de cobertura de código.

---

## 📚 Estructura de Subtemas y Contenidos

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **5.2.5.1 Pruebas Unitarias & Mocking** | [5.2.5.1_Pruebas_Unitarias_Logica_Servicios_Mocking.md](5.2.5.1_Pruebas_Unitarias_Logica_Servicios_Mocking.md) | [Slides Markdown](5.2.5.1_Pruebas_Unitarias_Logica_Servicios_Mocking_Slides.md) | [Presentación HTML Reveal.js](5.2.5.1_Pruebas_Unitarias_Logica_Servicios_Mocking_Slides.html) |
| **5.2.5.2 Widget Testing & Coverage** | [5.2.5.2_Widget_Testing_Integracion_Code_Coverage.md](5.2.5.2_Widget_Testing_Integracion_Code_Coverage.md) | [Slides Markdown](5.2.5.2_Widget_Testing_Integracion_Code_Coverage_Slides.md) | [Presentación HTML Reveal.js](5.2.5.2_Widget_Testing_Integracion_Code_Coverage_Slides.html) |

---

## 🎯 Competencias de Aprendizaje

1. **Alineación con la Pirámide de Pruebas:** Comprensión de los diferentes niveles de testeo de software (Unitario, Widget, Integración E2E) y su impacto en la velocidad de desarrollo y el costo de mantenimiento.
2. **Pruebas Unitarias Puras:** Uso del paquete `flutter_test` para evaluar modelos DTO, funciones de cálculo y validaciones de negocio en la máquina virtual de Dart.
3. **Simulación de Clientes HTTP:** Creación de dobles de prueba con `mocktail` para aislar servicios cliente RESTful, validando respuestas 200 OK, códigos de error y timeouts sin depender de servidores activos.
4. **Pruebas de Componentes UI (Widget Testing):** Renderizado virtual headless con `WidgetTester`, gestión de frames con `pump` y `pumpAndSettle`, localización por claves con `find.byKey` y simulación de toques y texto.
5. **Auditoría de Cobertura de Código:** Generación automatizada de reportes LCOV con `flutter test --coverage` y análisis de ramas lógicas no ejecutadas.
