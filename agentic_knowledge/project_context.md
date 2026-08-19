# Contexto Integral del Proyecto: IF0009 - Desarrollo de Software IV

Este documento consolidado sirve como la **única fuente de verdad (Single Source of Truth)** para la planificación, estructuración y generación de contenidos del curso **IF0009 - Desarrollo de Software IV (II Ciclo 2026)** en la carrera de Informática Empresarial de la Universidad de Costa Rica (UCR).

---

## 1. Identificación y Descripción del Curso

- **Sigla:** IF0009
- **Nombre:** Desarrollo de Software IV
- **Docente:** Mag. Jonathan Granados C.
- **Ciclo:** II Ciclo 2026 (II-2026)
- **Tipo de Curso:** Teórico-práctico
- **Créditos:** 4 créditos
- **Horas Lectivas:** 8 horas semanales (3 horas de teoría, 5 horas de práctica)
- **Modalidad:** Bajo Virtual / Virtual
- **Requisitos:** IF-0006 Desarrollo de Software III o IF-3000 Programación II
- **Correquisitos:** Ninguno
- **Población Destinataria:** Estudiantes de cuarto nivel del bachillerato en Informática Empresarial.

### Descripción Oficial
Este curso proporciona los conocimientos y habilidades para construir aplicaciones de software complejas y distribuidas mediante diferentes lenguajes de programación, lenguajes de scripting, entornos de desarrollo y frameworks modernos. Se enfoca en el desarrollo full-stack (capas back-end, front-end y móvil), integrando persistencia de datos relacionales/no relacionales, buenas prácticas de desarrollo, arquitecturas desacopladas y seguridad a nivel de sesión y de APIs.

---

## 2. Resultados de Aprendizaje del Curso

Al finalizar el ciclo lectivo, el estudiantado será capaz de:
1. **Explicar** los conceptos fundamentales de arquitectura y tendencias en aplicaciones web y móviles (MPA, SPA, PWA, nativas, multiplataforma).
2. **Configurar** entornos de desarrollo completos para tecnologías full-stack y de control de versiones con Git bajo flujos colaborativos de trabajo.
3. **Desarrollar** aplicaciones web y móviles escalables extendiendo frameworks de software pertinentes (Angular en front-end; ASP.NET Core o Spring Boot en back-end).
4. **Diseñar** interfaces de usuario interactivas, responsivas, internacionalizadas y conformes a estándares de accesibilidad universal (WCAG 2.1 AA / Google Lighthouse).
5. **Desarrollar** pruebas unitarias de software para identificar y mitigar defectos en la lógica de negocio y controladores de red.
6. **Desplegar** aplicaciones contenerizadas en entornos operativos públicos (nube) usando orquestadores básicos.
7. **Codificar** software aplicando directrices y guardrails de seguridad avanzados contra secuestro de sesión y vulnerabilidades comunes (OWASP Top 10).

---

## 3. Contenidos Detallados del Programa

### Tema 1. Fundamentos de desarrollo Web
* **1.1 Aplicaciones web:** Evolución y arquitectura cliente-servidor.
* **1.2 Enfoque de pila completa (Full Stack):**
  * 1.2.1 Back-end (lógica de negocio, persistencia, APIs).
  * 1.2.2 Front-end (UI, interactividad, frameworks cliente).
* **1.3 Tendencias:**
  * 1.3.1 Multi-page applications (MPA).
  * 1.3.2 Single-page applications (SPA).
  * 1.3.3 Progressive web applications (PWA).
  * 1.3.4 Native web applications.
* **1.4 Frameworks:** Criterios de selección de stacks tecnológicos.

### Tema 2. Configuración del ambiente de desarrollo
* **2.1 Instalación y configuración:** SDKs, Node.js, CLI de frameworks, IDEs y bases de datos.
* **2.2 Control de versiones (Git):**
  * 2.2.1 Historia y conceptos fundamentales de Git.
  * 2.2.2 Colaboración y trabajo en equipo (Feature Branching, PRs).
  * 2.2.3 Gestión de versionamiento y resolución de conflictos.
  * 2.2.4 Herramientas y plataformas (GitHub, GitLab o Bitbucket).
  * 2.2.5 Buenas prácticas y solución de problemas en repositorios compartidos.

### Tema 3. Desarrollo back-end
* **3.1 Capa de datos:**
  * 3.1.1 Acceso a datos a través de un ORM o framework de persistencia.
  * 3.1.2 Consumo y mapeo de procedimientos almacenados en base de datos.
  * 3.1.3 Implementación de operaciones CRUD (crear, leer, actualizar, eliminar).
  * 3.1.4 Paginación y limitación de resultados a nivel de base de datos y API.
* **3.2 Capa de negocios:**
  * 3.2.1 Manejo de validaciones complejas de negocio desacopladas de la persistencia y del controlador.
* **3.3 Capa de controladores:**
  * 3.3.1 Aspectos básicos de HTTP: verbos, códigos de estado (2xx, 3xx, 4xx, 5xx) y encabezados.
  * 3.3.2 Creación de servicios web RESTful (API REST).
  * 3.3.3 Conceptos de microservicios y arquitectura orientada a servicios.
  * 3.3.4 Documentación de APIs (OpenAPI / Swagger) y librerías clave.
* **3.4 Manejo de errores:** Captura centralizada de excepciones y middleware de formateo de errores HTTP.
* **3.5 Autenticación y autorización:** Control de accesos basado en roles.
* **3.6 Seguridad en el manejo de sesiones:** Json Web Tokens (JWT) y prevención de secuestro de sesión.
* **3.7 Pruebas de unidad:** Pruebas unitarias de servicios y controladores con frameworks de testeo (xUnit, JUnit, Mockito).

### Tema 4. Desarrollo en front-end
* **4.1 Introducción al desarrollo front-end:**
  * 4.1.1 ¿Qué es el desarrollo front-end?
  * 4.1.2 Responsabilidades de la ingeniería de software front-end.
* **4.2 Diseño inclusivo y experiencia del usuario (UX):**
  * 4.2.1 Experiencia de usuario y usabilidad.
  * 4.2.2 Usabilidad (U8y).
  * 4.2.3 Internacionalización (I18n).
  * 4.2.4 Accesibilidad web (A11y/A16y).
* **4.3 Lenguaje de Marcado de Hipertexto - HTML:**
  * 4.3.1 ¿Qué es el HTML?
  * 4.3.2 Estructura del DOM.
  * 4.3.3 Elementos y etiquetas semánticas.
  * 4.3.4 La estructura de árbol del DOM.
  * 4.3.5 HTML semántico y accesibilidad.
  * 4.3.6 Creación de formularios accesibles.
  * 4.3.7 El rol del HTML en la accesibilidad.
* **4.4 Hojas de estilo en cascada - CSS:**
  * 4.4.1 ¿Qué es CSS?
  * 4.4.2 Selectores y especificidad.
  * 4.4.3 El modelo de caja (Box Model) y layouts (Flexbox y CSS Grid).
  * 4.4.4 Medidas y unidades relativas (em, rem, %, vh, vw).
  * 4.4.5 Responsividad y Mobile-First.
  * 4.4.6 Conceptos de diseño adaptativo (responsive design).
  * 4.4.7 CSS Flexbox.
  * 4.4.8 CSS Grid Layout.
  * 4.4.9 Media queries.
* **4.5 EcmaScript (Modern JavaScript/TypeScript):**
  * 4.5.1 Introducción a EcmaScript.
  * 4.5.2 Variables, tipos, arrays y métodos de array.
  * 4.5.3 Arrow functions y callbacks.
  * 4.5.4 Promesas, observables y async/await.
  * 4.5.5 Programación modular e importaciones/exportaciones.
  * 4.5.6 Clases y Programación Orientada a Objetos en JS/TS.
  * 4.5.7 Sincronización de datos (data binding) elemental.
* **4.6 Desarrollo en un framework front-end (Angular):**
  * 4.6.1 Marcos de trabajo (frameworks) vs librerías.
  * 4.6.2 Historia de los frameworks JS.
  * 4.6.3 Arquitectura modular de componentes: vista, lógica y estilos.
  * 4.6.4 Estructura modular de componentes: directivas, interpolación y data binding.
  * 4.6.5 Enrutamiento, Lazy Loading y Route Guards (CanActivate).
  * 4.6.6 Pipes personalizados e integrados.
  * 4.6.7 Decoradores y programación reactiva con observables (RxJS).
  * 4.6.8 Consumo de APIs mediante servicios inyectables e HttpClient.
  * 4.6.9 Manejo elemental del estado.
  * 4.6.10 Pruebas unitarias de componentes y servicios en front-end.

### Tema 5. Desarrollo móvil
* **5.1 Introducción al desarrollo móvil:**
  * 5.1.1 Ecosistemas móviles (Android, iOS).
  * 5.1.2 Ecosistemas y entornos multiplataforma vs desarrollo nativo.
  * 5.1.3 Desarrollo nativo y multiplataforma.
  * 5.1.4 Lenguajes modernos en tendencia (TypeScript, Dart, Kotlin, Swift).
* **5.2 Desarrollo de aplicaciones móviles (multiplataforma):**
  * 5.2.1 Introducción al diseño de apps móviles.
  * 5.2.2 Configuración del SDK de desarrollo e IDEs.
  * 5.2.3 Marcos de trabajo modernos (React Native, Flutter, MAUI).
  * 5.2.4 Desarrollo de UI y componentes nativos móviles.
  * 5.2.5 Navegación móvil (stack, tabs).
  * 5.2.6 Gestión de datos y persistencia local (SQLite, Async Storage).
  * 5.2.7 Integración y consumo de hardware de dispositivos (GPS, cámara).

### Tema 6. Seguridad web y móvil
* **6.1 Vulnerabilidades comunes:** Mitigación frente al OWASP Top 10.
* **6.2 Autenticación y autorización:** Protocolos estándar (OAuth2, JWT).
* **6.3 Seguridad de datos:** Cifrado en reposo, tránsito e inyecciones de código.
* **6.4 Seguridad en el código:** Validación, sanitización de inputs y prevención XSS.
* **6.5 Seguridad en APIs:** Rate limiting, CORS y headers de seguridad.
* **6.6 Seguridad en el despliegue:** Gestión segura de variables de entorno y secretos.
* **6.7 Herramientas de análisis:** Escaneos automatizados de vulnerabilidades (OWASP ZAP).

### Tema 7. Despliegue y publicación
* **7.1 Despliegue de aplicaciones web:**
  * 7.1.1 Empaquetado y construcción de bundles para entornos productivos.
  * 7.1.2 Servidores de hosting estático y dinámico.
  * 7.1.3 Servidores y Proxies inversos (Nginx, Apache).
  * 7.1.4 Dominios, DNS y configuración de certificados SSL/TLS (HTTPS).
  * 7.1.5 Despliegue contenerizado de la aplicación (Dockerfile, Docker Compose).
* **7.2 Publicación de aplicaciones móviles:** Generación de archivos binarios firmados (.apk, .aab, .ipa) y publicación en tiendas oficiales.

---

## 4. Cronograma Oficial Consolidado (18 Semanas)

El cronograma consolida el orden lógico de impartición eliminando el desfase detectado originalmente para asegurar que Angular se imparte en su totalidad antes del Examen 1:

| Semana | Tema / Módulo | Detalle Técnico | Entregables y Evaluaciones |
|---|---|---|---|
| **Sem 1** | M0/M1: Fundamentos Web | Arquitecturas MPA, SPA, PWA, e inducción ética | Inicio de lecturas teóricas |
| **Sem 2** | M2: Setup & Git | Feature Branching, resolución de conflictos | **Entrega Laboratorio 1 y 2 (Setup y Git)** |
| **Sem 3** | M3.1: Capa de Datos | Persistencia relacional, ORM, operaciones CRUD | Inicio de Laboratorio 3 (Backend API) |
| **Sem 4** | M3.2-3.3: Lógica y REST | Controladores, validaciones, OpenAPI | Avance de Laboratorio 3 |
| **Sem 5** | M3.3-3.4: Errores & API | Middleware centralizado de errores | Avance de Laboratorio 3 |
| **Sem 6** | M3.5-3.7: Sesiones & Tests | JWT, sesiones seguras, pruebas unitarias | **Entrega Laboratorio 3 (Backend Completo)** |
| **Sem 7** | M4.1-4.3: HTML & UX | HTML semántico, diseño inclusivo y accesibilidad | Inicio de Laboratorio 4 (Front-end Angular) |
| **Sem 8** | M4.4-4.5: CSS & JS/TS | CSS Flexbox/Grid, responsivo, promesas, async | **Avance 1 del Proyecto Integrador (10%)** |
| **Sem 9** | M4.6: Angular | Modulos, componentes, RxJS, HttpClient, Guards | **Entrega Laboratorio 4 (SPA Angular)** |
| **Sem 10** | **Evaluación 1** / M5 | **Examen 1 (20% - Módulos 1 a 4)** + Intro Móvil | Examen 1 |
| **Sem 11** | M5: Desarrollo Móvil | Layouts móviles, enrutamiento, vistas | Avance Laboratorio 5 (App Móvil) |
| **Sem 12** | M5: Desarrollo Móvil | Persistencia local y acceso a hardware | **Entrega Laboratorio 5 (App Móvil)** |
| **Sem 13** | M6: Seguridad | OWASP Top 10, sanitización, JWT Hardening | Asignación de Investigación |
| **Sem 14** | M6: Seguridad (Cont.) | Checklist de seguridad | **Entrega Investigación (5%)** + **Laboratorio 6** |
| **Sem 15** | M7: Despliegue | Dockerfile multi-stage, docker-compose, Nginx | Avance Laboratorio 7 (Despliegue) |
| **Sem 16** | **Evaluación 2** / M7 | **Examen 2 (20% - Módulos 5 a 7)** | Examen 2 + **Entrega Laboratorio 7** |
| **Sem 17** | M8: Proyecto Final | Integración del sistema full-stack | Avance y consultas del proyecto final |
| **Sem 18** | M8: Evaluación Final | **Defensa Oral y Entrega Final (20%)** | Rúbrica final, codificación en vivo individual |

---

## 5. Ponderaciones de Evaluación y Políticas

La distribución oficial fija de los porcentajes es la siguiente:
* **Examen 1 (Módulos 1-4 completo):** 20%
* **Examen 2 (Módulos 5-7):** 20%
* **Investigación formal:** 5%
* **Proyecto Programado (Acumulativo):** 30%
  * *Avance 1 (Backend funcional, JWT y base de datos en Sem 8):* 10%
  * *Entrega final y defensa oral (Sem 18):* 20%
* **Pruebas cortas, tareas, prácticas guiadas, laboratorios:** 25%

### Políticas Importantes:
- **Metodología de Codificación en Vivo (Live Coding):** Las lecciones técnicas densas se basarán en programación interactiva guiada por el docente, asegurando la vivencia práctica.
- **Auditoría de Accesibilidad (WCAG 2.1 AA):** Todos los desarrollos de interfaces web deben auditarse con Google Lighthouse y alcanzar una puntuación mínima de accesibilidad de **90**.
- **Internacionalización (i18n):** Todo front-end debe soportar traducción dinámica español/inglés.
- **Dockerización Multi-Stage:** El despliegue exige estructurar Dockerfiles multi-stage y orquestar API + DB + Nginx a través de Docker Compose.
- **Política de IA Generativa:** Se permite como asistente sintáctico e instrumental. Todo código asistido por IA debe documentarse con el prompt y origen. La validez de autoría se verificará en la **defensa oral individual**, donde cada estudiante debe modificar secciones del código del proyecto en tiempo real frente al docente.

---

## 6. Rúbrica Detallada del Proyecto Integrador (30% de la Nota)

| Criterio de Evaluación | Ponderación | Nivel Excelente (100-90) | Nivel Aceptable (89-70) | Nivel Deficiente (<70) |
|---|---|---|---|---|
| **Arquitectura Back-end y Persistencia** | **25%** | Separación limpia en capas, uso de ORM eficiente, paginación optimizada a nivel de base de datos y cobertura de pruebas unitarias robusta. | Separación de capas aceptable, fallas menores en optimización de consultas, pruebas unitarias incompletas. | Código acoplado en un único controlador, sin ORM ni pruebas de código, o con fallas críticas de compilación. |
| **Front-end SPA (Angular, UX, Accesibilidad)** | **25%** | SPA modular en Angular, estructurado y dinámico, responsive, accesibilidad Lighthouse ≥ 90, atributos WAI-ARIA, i18n español/inglés funcional, y RxJS implementado de manera limpia. | SPA funcional pero con errores de diseño responsivo menores, accesibilidad entre 70-89%, o internacionalización incompleta. | No es una Single-Page Application, inaccesible a lectores de pantalla (Lighthouse < 70), o sin i18n. |
| **Integración de Aplicación Móvil** | **20%** | Conexión correcta a la API back-end, persistencia local para operación offline y consumo adecuado de hardware del dispositivo (GPS/Cámara). | Conexión funcional con la API pero sin soporte offline o fallos menores en la respuesta del hardware. | Aplicación móvil inestable, incapaz de comunicarse con el servidor o sin consumir APIs ni hardware local. |
| **Seguridad OWASP y Despliegue Nube** | **15%** | Protección robusta de endpoints con tokens JWT, sanitización de inputs completa, Dockerfile multi-stage limpio, compose y URL pública HTTPS funcional. | Autenticación JWT funcional pero con debilidades de encriptación menores, Dockerfile no optimizado o despliegue únicamente local. | Sin seguridad contra inyecciones, token expuesto o sin despliegue contenerizado en la nube. |
| **Defensa Oral y Dominio de Código** | **15%** | Explicación clara del funcionamiento del código por el estudiante, justificando la arquitectura y modificando código de forma autónoma en vivo. | Explicación imprecisa en secciones del código que fueron desarrolladas en conjunto o por terceros. | Incapacidad absoluta de explicar la arquitectura, lógica del código o de hacer modificaciones simples propuestas en tiempo real. |

---

## 7. Temas Predefinidos de Investigación (5%)

Para garantizar la uniformidad en las evaluaciones, se establecen los siguientes temas específicos:
1. **Arquitecturas modernas de Front-End y Micro-Frontends:** Escalabilidad, orquestación y patrones de diseño en frontend.
2. **OWASP API Security Top 10:** Análisis exhaustivo de vulnerabilidades y hardening de seguridad a nivel de servidores y APIs empresariales.
3. **Manejo de Estados y Patrones Reactivos en Desarrollo Móvil Multiplataforma:** Arquitectura de flujos de datos asíncronos y reactivos en dispositivos móviles.

*Requisitos:* Formato individual o parejas. Informe técnico máximo de 5 páginas con al menos una referencia en inglés y defensa de 10 minutos.

---

## 8. Progreso Actual de Planificación y Generación

Este bloque mantiene el control de qué carpetas y archivos se han creado o modificado en la sesión de trabajo.

* **Actualización Reciente (Tema 3.0: Desarrollo en Capas):** Se analizó la presentación antigua del curso y se generó el nuevo material conceptual del Tema 3.0: Desarrollo en Capas (`3.0_Desarrollo_en_Capas.md`, versión PDF, diapositivas Marp `.md` y su versión interactiva Reveal.js `.html`) estructurado bajo los estándares del curso II-2026, con diseño de diapositivas oscuro premium.
* **Actualización Reciente (Tema 3.1: Capa de Datos y Presentaciones):** Se completó la lectura conceptual del Tema 3.1: Capa de Datos (`3.1_Capa_de_Datos.md` y su versión PDF) junto con sus diapositivas en formato Marp (`3.1_Capa_de_Datos_Slides.md`) y su versión interactiva compilada en HTML (`3.1_Capa_de_Datos_Slides.html`). El contenido cubre ORM (JPA/Hibernate), CRUD, procedimientos almacenados y paginación física. El compilador PDF fue optimizado para resolver rutas de imágenes relativas sin fallas.
* **Actualización Reciente (Estandarización y Práctica Guiada 2):** Se finalizó la Práctica Guiada 2 (Markdown y PDF). Se reestructuró para iniciar desde cero con DSW4_workspace, se cambió a Java 21 con nota local, y se organizaron las capas en 'data, business, controller, domain'. Para evitar problemas de alineación y numeración en la compilación PDF (xhtml2pdf), se transformaron las listas a párrafos en negrita (`**1.**`) separados por líneas en blanco obligatorias. Se eliminó el uso del flag `-p` en `mkdir` para compatibilidad en terminales de PowerShell de Windows, y se añadió la verificación de rama `master` a `main` al iniciar Git.
* **Actualización Reciente (Estandarización de Estilos y Portadas):** Se unificaron los estilos CSS del compilador `marp_to_reveal.py` y se simplificó la cabecera frontmatter de todos los archivos de presentación, garantizando un look and feel visualmente idéntico para todo el curso.
* **Actualización Reciente (Taller 2 y Reglas de Formato PDF):** Se completó la generación del Taller 2 (Markdown y PDF). Se corrigieron errores de colapso de código y listas en el generador PDF revirtiendo el estilo `pre-wrap` en `md_to_pdf.py` e insertando líneas en blanco obligatorias en `Taller_2.md`. Se integraron estas directrices (ancho de código < 75 chars, sangría de 4 espacios, líneas en blanco pre-lista, y uso guiado de Git en VS Code e IA Google Antigravity) como estándar formal para futuros laboratorios y talleres dentro de `skills.md`.

### Estado General de la Estructura de Directorios

```
Planificacion Lecciones/
├── agentic_knowledge/
│   ├── modes.md (Modos de Generación)
│   ├── roles.md (Identidades del Asistente)
│   ├── skills.md (SOP de Generación)
│   └── project_context.md (Contexto Consolidad de Verdad - ESTE ARCHIVO)
├── resources/
│   ├── IF0009_Desarrollo_de_Software_IV_II_2026.pdf
│   └── Plan_Consolidado_IF0009_Desarrollo_de_Software_IV.md
├── Temas/
│   ├── 01_Fundamentos_Desarrollo_Web/
│   ├── 02_Configuracion_Ambiente_y_Git/
│   ├── 03_Desarrollo_Backend/
│   ├── 04_Desarrollo_Frontend/
│   ├── 05_Desarrollo_Movil/
│   ├── 06_Seguridad_Web_y_Movil/
│   ├── 07_Despliegue_y_Publicacion/
│   └── 08_Temas_Adicionales/
└── Evaluaciones/
    ├── Examenes/
    ├── Laboratorios/
    ├── Quices/
    ├── Tareas/
    ├── Talleres/
    ├── Investigaciones/
    └── Proyectos/
```

### Tabla de Seguimiento de Entregables Generados

| Directorio de Destino | Archivo Generado | Tipo de Contenido | Modo Utilizado | Estado |
|---|---|---|---|---|
| [agentic_knowledge](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge) | [modes.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/modes.md) | Configuración | Sistema / Modos | [x] Completado |
| [agentic_knowledge](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge) | [roles.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/roles.md) | Configuración | Sistema / Roles | [x] Completado |
| [agentic_knowledge](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge) | [skills.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/skills.md) | Configuración | Sistema / Habilidades | [x] Completado |
| [agentic_knowledge](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge) | [project_context.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/agentic_knowledge/project_context.md) | Contexto de Verdad | Contexto del Asistente | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web) | [1.1_Aplicaciones_Web.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web/1.1_Aplicaciones_Web.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web) | [1.1_Aplicaciones_Web_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web/1.1_Aplicaciones_Web_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web) | [1.1_Aplicaciones_Web_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.1_Aplicaciones_Web/1.1_Aplicaciones_Web_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [src/python_utils_src](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/src/python_utils_src) | [marp_to_reveal.py](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/src/python_utils_src/marp_to_reveal.py) | Compilador de Presentaciones | Script Útil | [x] Completado |
| [src/python_utils_src](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/src/python_utils_src) | [md_to_pdf.py](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/src/python_utils_src/md_to_pdf.py) | Conversor de Markdown a PDF | Script Útil | [x] Completado |
| [/](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones) | [README.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/README.md) | Documentación General | Estructura / Inicio | [x] Completado |
| [/](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones) | [HOWTO.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/HOWTO.md) | Guía Técnica de Compilación | Instrucción / Código | [x] Completado |
| [/](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones) | [USER_GUIDE.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/USER_GUIDE.md) | Guía Académica y Pedagógica | Metodología / Uso | [x] Completado |
| [/](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones) | [index.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/index.html) | Portal Dashboard de Presentaciones | HTML / Frontend | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa) | [1.2_Pila_Completa.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa/1.2_Pila_Completa.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa) | [1.2_Pila_Completa_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa/1.2_Pila_Completa_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa) | [1.2_Pila_Completa_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.2_Pila_Completa/1.2_Pila_Completa_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias) | [1.3_Tendencias.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias/1.3_Tendencias.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias) | [1.3_Tendencias_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias/1.3_Tendencias_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias) | [1.3_Tendencias_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.3_Tendencias/1.3_Tendencias_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks) | [1.4_Frameworks.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks/1.4_Frameworks.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks) | [1.4_Frameworks_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks/1.4_Frameworks_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks) | [1.4_Frameworks_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/01_Fundamentos_Desarrollo_Web/1.4_Frameworks/1.4_Frameworks_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot) | [3.0_Desarrollo_en_Capas.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot/3.0_Desarrollo_en_Capas.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot) | [3.0_Desarrollo_en_Capas.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot/3.0_Desarrollo_en_Capas.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot) | [3.0_Desarrollo_en_Capas_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot/3.0_Desarrollo_en_Capas_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot) | [3.0_Desarrollo_en_Capas_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.0_Introduccion_SpringBoot/3.0_Desarrollo_en_Capas_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos) | [3.1_Capa_de_Datos.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos/3.1_Capa_de_Datos.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos) | [3.1_Capa_de_Datos.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos/3.1_Capa_de_Datos.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos) | [3.1_Capa_de_Datos_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos/3.1_Capa_de_Datos_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos) | [3.1_Capa_de_Datos_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/03_Desarrollo_Backend/3.1_Capa_de_Datos/3.1_Capa_de_Datos_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Evaluaciones/Laboratorios/warmup](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/warmup) | [Laboratorio_Warmup.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/warmup/Laboratorio_Warmup.md) | Guía de Laboratorio | ModeLab | [x] Completado |
| [Evaluaciones/Laboratorios/warmup](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/warmup) | [Laboratorio_Warmup.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/warmup/Laboratorio_Warmup.pdf) | Guía de Laboratorio PDF | Conversor Python | [x] Completado |
| [Evaluaciones/Talleres/Taller_1](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Taller_1) | [Taller_1.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Taller_1/Taller_1.md) | Guía de Taller | ModeLab | [x] Completado |
| [Evaluaciones/Talleres/Taller_1](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Taller_1) | [Taller_1.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Taller_1/Taller_1.pdf) | Guía de Taller PDF | Conversor Python | [x] Completado |
| [Evaluaciones/Talleres/Tema I/Taller_2](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Tema%20I/Taller_2) | [Taller_2.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Tema%20I/Taller_2/Taller_2.md) | Guía de Taller | ModeLab | [x] Completado |
| [Evaluaciones/Talleres/Tema I/Taller_2](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Tema%20I/Taller_2) | [Taller_2.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Talleres/Tema%20I/Taller_2/Taller_2.pdf) | Guía de Taller PDF | Conversor Python | [x] Completado |
| [Evaluaciones/Laboratorios/Laboratorio_1](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/Laboratorio_1) | [Laboratorio_1.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/Laboratorio_1/Laboratorio_1.md) | Guía de Laboratorio | ModeLab | [x] Completado |
| [Evaluaciones/Laboratorios/Laboratorio_1](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/Laboratorio_1) | [Laboratorio_1.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Evaluaciones/Laboratorios/Laboratorio_1/Laboratorio_1.pdf) | Guía de Laboratorio PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.1_Maven](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven) | [8.1_Maven.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven/8.1_Maven.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/08_Temas_Adicionales/8.1_Maven](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven) | [8.1_Maven.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven/8.1_Maven.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.1_Maven](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven) | [8.1_Maven_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven/8.1_Maven_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/08_Temas_Adicionales/8.1_Maven](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven) | [8.1_Maven_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.1_Maven/8.1_Maven_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.2_GitHub](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub) | [8.2_GitHub.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub/8.2_GitHub.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/08_Temas_Adicionales/8.2_GitHub](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub) | [8.2_GitHub.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub/8.2_GitHub.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.2_GitHub](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub) | [8.2_GitHub_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub/8.2_GitHub_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/08_Temas_Adicionales/8.2_GitHub](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub) | [8.2_GitHub_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.2_GitHub/8.2_GitHub_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.3_HTML](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML) | [8.3_HTML.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML/8.3_HTML.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/08_Temas_Adicionales/8.3_HTML](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML) | [8.3_HTML.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML/8.3_HTML.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.3_HTML](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML) | [8.3_HTML_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML/8.3_HTML_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/08_Temas_Adicionales/8.3_HTML](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML) | [8.3_HTML_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.3_HTML/8.3_HTML_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.4_CSS](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS) | [8.4_CSS.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS/8.4_CSS.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/08_Temas_Adicionales/8.4_CSS](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS) | [8.4_CSS.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS/8.4_CSS.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.4_CSS](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS) | [8.4_CSS_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS/8.4_CSS_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/08_Temas_Adicionales/8.4_CSS](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS) | [8.4_CSS_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.4_CSS/8.4_CSS_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.5_Debugging](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging) | [8.5_Debugging.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging/8.5_Debugging.md) | Lectura Conceptual | ModeTheory | [x] Completado |
| [Temas/08_Temas_Adicionales/8.5_Debugging](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging) | [8.5_Debugging.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging/8.5_Debugging.pdf) | Lectura en PDF | Conversor Python | [x] Completado |
| [Temas/08_Temas_Adicionales/8.5_Debugging](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging) | [8.5_Debugging_Slides.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging/8.5_Debugging_Slides.md) | Diapositivas Marp | ModePresentation | [x] Completado |
| [Temas/08_Temas_Adicionales/8.5_Debugging](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging) | [8.5_Debugging_Slides.html](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/Temas/08_Temas_Adicionales/8.5_Debugging/8.5_Debugging_Slides.html) | Presentación Interactiva HTML | Compilador Python | [x] Completado |
| [practicas_guiadas](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas) | [practica_1.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas/practica_1.md) | Guía de Práctica 1 | ModeTheory | [x] Completado |
| [practicas_guiadas](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas) | [practica_1.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas/practica_1.pdf) | Guía de Práctica 1 PDF | Conversor Python | [x] Completado |
| [practicas_guiadas](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas) | [practica_2.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas/practica_2.md) | Guía de Práctica 2 | ModeTheory | [x] Completado |
| [practicas_guiadas](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas) | [practica_2.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/practicas_guiadas/practica_2.pdf) | Guía de Práctica 2 PDF | Conversor Python | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [git_github.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/git_github.md) | Hoja de Referencia: Git & GitHub | ModeTheory | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [git_github.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/git_github.pdf) | Hoja de Referencia: Git & GitHub PDF | Conversor Python | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [maven.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/maven.md) | Hoja de Referencia: Maven | ModeTheory | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [maven.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/maven.pdf) | Hoja de Referencia: Maven PDF | Conversor Python | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [html.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/html.md) | Hoja de Referencia: HTML5 | ModeTheory | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [html.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/html.pdf) | Hoja de Referencia: HTML5 PDF | Conversor Python | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [css.md](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/css.md) | Hoja de Referencia: CSS | ModeTheory | [x] Completado |
| [cheatsheets](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets) | [css.pdf](file:///c:/Users/jonat/OneDrive/Documentos/UCR-2026/IF0009/Planificacion%20Lecciones/cheatsheets/css.pdf) | Hoja de Referencia: CSS PDF | Conversor Python | [x] Completado |

---

## 🚀 Planificación de Próximas Tareas

1. **Próxima Tarea Prioritaria:**
   - Iniciar la generación de contenidos conceptuales (lecturas teóricas) y diapositivas (Marp) para el subtema **2.1 Configuración de Entornos** bajo `02_Configuracion_Ambiente_y_Git/2.1_Configuracion/` utilizando `ModeTheory` y `ModePresentation`.
2. **Tareas Pendientes (Próximas Sesiones):**
   - Continuar con el subtema 2.2 de Control de Versiones con Git.
   - Redacción de los laboratorios prácticos subsiguientes utilizando `ModeLab`.
   - Formulación de cuestionarios/quices utilizando `ModeQuiz`.

---

## ⚠️ Reglas para la Actualización de la Fuente de Verdad

Al final de cada interacción o sesión en la que se agreguen, modifiquen o estructuren carpetas o archivos de este curso, la IA debe **actualizar de forma obligatoria este archivo `project_context.md`** reflejando las tareas completadas, los cambios en el estado de los módulos y las prioridades de la siguiente sesión.
