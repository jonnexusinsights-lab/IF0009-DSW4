# Plan Integral de Enseñanza — Versión Consolidada
## IF0009 – Desarrollo de Software IV | II Ciclo 2026 | Carrera de Informática Empresarial, Sedes Regionales, UCR

> **Nota de versión:** Este documento fusiona el *Plan Integral de Enseñanza* (usado como estructura base por su fidelidad exacta al cronograma oficial del programa) con las mejoras técnicas y de evaluación del *Plan Maestro de Diseño Instruccional*. Se corrigió la inconsistencia detectada en la versión previa del segundo plan, donde el framework Angular se enseñaba en la semana 11 (después del Examen 1), pese a que el examen declaraba cubrir ese contenido. En esta versión, todo el bloque de front-end —incluyendo Angular— se completa en las semanas 7–9, tal como exige el cronograma oficial del programa (PDF institucional).[^1]

---

## 1. Análisis del Programa Base

IF0009 es un curso teórico-práctico de 4 créditos y 8 horas lectivas semanales (3 teoría, 5 práctica), modalidad Bajo Virtual, dirigido a estudiantes que ya cursaron Desarrollo de Software III o Programación II. Su propósito es que el estudiantado adquiera las competencias para construir aplicaciones web y móviles de pila completa (full-stack), aplicando buenas prácticas de codificación y seguridad en el manejo de sesiones.[^1]

Los siete resultados de aprendizaje oficiales cubren: explicar conceptos de aplicaciones web/móviles, configurar el entorno de desarrollo, extender frameworks actuales, diseñar interfaces de usuario, desarrollar pruebas unitarias, desplegar aplicaciones en un entorno operativo, y codificar con buenas prácticas de seguridad de sesiones.[^1]

El semestre 2026-II se distribuye en 18 semanas (10 agosto – 12 diciembre), con la siguiente ponderación oficial fija: Examen 1 (20%), Examen 2 (20%), Investigación (5%), Proyecto(s) programado(s) (30%), Pruebas cortas/tareas/prácticas/talleres (25%). La bibliografía obligatoria confirma el stack esperado: **Angular** en front-end y **ASP.NET Core / Java Spring Boot** en back-end.[^1]

---

## 2. Desglose por Módulos

| Módulo | Tema del programa | Semanas | % aprox. de horas lectivas |
|---|---|---|---|
| M0 | Inducción, ética y programa del curso | Sem 1 | 3% |
| M1 | Fundamentos de desarrollo Web | Sem 1 | 5% |
| M2 | Configuración del ambiente de desarrollo y control de versiones | Sem 2 | 7% |
| M3 | Desarrollo back-end (datos, negocio, controladores, seguridad de sesión, pruebas) | Sem 3–6 | 27% |
| M4 | Desarrollo front-end (HTML, CSS, ECMAScript, Angular, accesibilidad, i18n) | Sem 7–9 | 20% |
| — | **Examen 1** | Sem 10 | — |
| M5 | Desarrollo móvil | Sem 10–12 | 18% |
| M6 | Seguridad web y móvil (incluye Investigación) | Sem 13–14 | 10% |
| M7 | Despliegue y publicación (incluye contenerización) | Sem 15–16 | 10% |
| — | **Examen 2** | Sem 16 | — |
| M8 | Proyecto final integrador | Sem 17–18 | (evaluado en Proyecto 30%) |

Secuencia lógica: *conocer antes de construir, construir antes de asegurar, asegurar antes de publicar*, respetando exactamente el orden del cronograma oficial.[^1]

---

## 3. Secuencia Pedagógica Recomendada

Enfoque en espiral con **un solo proyecto acumulativo** (aplicación web/móvil con backend real) que crece en complejidad módulo a módulo. Metodología marco: **Aprendizaje Basado en Proyectos (ABP)**, combinada con:

- **Flipped classroom** para contenidos teóricos de menor complejidad (Módulos 1, 2 y 6): lectura o video corto previo, discusión y aplicación en clase.
- **Codificación en vivo guiada (*live coding*)** para los módulos técnicos densos (3, 4, 5, 7), tal como exige la metodología oficial del curso, que prioriza la exposición de código en tiempo real y la vivencia de la secuencia de pasos.[^1]

### Política de uso de Inteligencia Artificial Generativa *(incorporada)*

Dado que el programa oficial sanciona el uso indebido de IA no autorizada como falta disciplinaria,[^1] se recomienda una regulación **transparente y no prohibicionista**:

- Se autoriza el uso de IA generativa exclusivamente para explicar errores sintácticos, sugerir algoritmos o acelerar tareas repetitivas (boilerplate).
- Todo fragmento de código asistido por IA debe documentarse con un comentario indicando su origen y el prompt utilizado.
- La verificación de autoría real se realiza mediante la **defensa oral individual** del proyecto integrador, donde cada estudiante debe modificar código en tiempo real ante el docente.
- Cualquier uso no declarado que constituya copia o plagio se gestiona conforme al Reglamento de Orden y Disciplina Estudiantil.[^1]

---

## 4. Plan Detallado por Módulo

### Módulo 0 — Inducción y ética institucional (Semana 1, 1 sesión)

- **Objetivo:** Comprender el programa, la política de evaluación y el marco de convivencia institucional.
- **Estrategia:** Sesión sincrónica expositiva + discusión guiada del video institucional sobre hostigamiento sexual (CIEM, UCR, 2023).[^1]
- **Material a crear:** Presentación del programa; guía de convivencia; foro de bienvenida en Mediación Virtual.
- **Nivel de profundidad:** Informativo, sin evaluación sumativa.

### Módulo 1 — Fundamentos de desarrollo Web (Semana 1)

**1.1 Aplicaciones web · 1.2 Full Stack Development · 1.3 Tendencias (MPA/SPA/PWA/nativa) · 1.4 Frameworks**

- **Objetivo:** Explicar el modelo cliente-servidor, diferenciar arquitecturas MPA/SPA/PWA y justificar la elección de un framework según el caso de uso.
- **Estrategia:** Lección magistral interactiva + análisis comparativo en grupos pequeños (estudio de caso: comparar 3 apps reales).
- **Duración:** 3h teoría + 2h práctica.
- **Material a crear:** Presentación con diagramas de arquitectura cliente-servidor; matriz comparativa de frameworks (Angular, React, Vue); video corto (10 min) de tendencias.
- **Recursos sugeridos:** Cybellium (2023); documentación oficial de Angular.[^1]
- **Actividad práctica:** Taller de identificación de arquitectura en 3 sitios web reales (grupal, 45 min).

### Módulo 2 — Configuración del ambiente de desarrollo (Semana 2)

**2.1 Instalación y configuración de herramientas · 2.2 Control de versiones**

- **Objetivo:** Configurar un entorno de desarrollo completo y gestionar un repositorio Git colaborativo aplicando Feature Branching, resolución de conflictos y Pull Requests.
- **Estrategia:** Laboratorio guiado paso a paso (coding en vivo) + trabajo colaborativo en parejas.
- **Duración:** 2h teoría + 6h práctica.
- **Material a crear:** Guía de instalación con capturas; video tutorial de configuración; cheat-sheet de comandos Git; repositorio plantilla con políticas de rama predefinidas *(mejora: estandariza el punto de partida entre las 9 sedes)*.
- **Laboratorio 1 — "Setup del entorno full-stack":** Instalar SDK back-end, Node.js, Angular CLI, IDE y crear repositorio remoto. Checklist de verificación entregable.
- **Laboratorio 2 — "Flujo de trabajo colaborativo con Git":** Simulación de divergencia en pareja (Rol A crea feature branch, Rol B modifica el mismo archivo); ambos resuelven el conflicto y documentan el proceso.

### Módulo 3 — Desarrollo back-end (Semanas 3–6, bloque más extenso)

**3.1 Capa de datos → 3.2 Capa de negocios → 3.3 Capa de controladores → 3.4 Manejo de errores → 3.5 Autenticación y autorización → 3.6 Seguridad de sesiones → 3.7 Pruebas de unidad**

| Subtema | Objetivo específico | Semana | Estrategia |
|---|---|---|---|
| 3.1 Capa de datos | CRUD con paginación usando ORM/framework de persistencia | 3 | Codificación en vivo + laboratorio individual |
| 3.2 Capa de negocios | Validaciones de reglas de negocio desacopladas del controlador | 4 | Práctica guiada |
| 3.3 Capa de controladores | API REST documentada (OpenAPI/Swagger) + microservicio básico | 4–5 | Taller práctico + codificación en vivo |
| 3.4 Manejo de errores | Manejo centralizado de excepciones y códigos HTTP correctos | 5 | Demostración + ejercicio guiado |
| 3.5 Autenticación/autorización | Login, roles y protección de endpoints | 6 | Laboratorio guiado |
| 3.6 Seguridad de sesiones | Tokens JWT y buenas prácticas contra secuestro de sesión | 6 | Demostración técnica + discusión de riesgos |
| 3.7 Pruebas de unidad | Pruebas unitarias de la capa de negocios y controladores | 6 | Taller práctico |

- **Nivel de profundidad:** Alto — núcleo técnico del curso, requiere dominio funcional.
- **Recursos sugeridos:** De Sanctis (2024); Green (2023); Meric (2024).[^1]
- **Laboratorio 3 — "API REST completa con autenticación":** Backend con CRUD paginado, validaciones, manejo de errores, JWT y pruebas unitarias sobre una entidad de negocio real (ej. inventario, matrícula). Entrega incremental por sprint semanal con retroalimentación.
- **Tarea integradora:** Documentar la API (OpenAPI/Swagger) y presentar informe técnico de decisiones de arquitectura.

### Módulo 4 — Desarrollo front-end, incluye Angular (Semanas 7–9)

> **Corrección de secuencia:** todo el bloque 4, incluyendo el framework Angular (4.6), se completa en las semanas 7–9, **antes** del Examen 1 (semana 10), tal como indica el cronograma oficial. No se traslada contenido a semanas posteriores.[^1]

**4.1 Introducción · 4.2 Diseño inclusivo y UX (usabilidad, i18n, accesibilidad) · 4.3 HTML · 4.4 CSS · 4.5 ECMAScript · 4.6 Framework front-end (Angular)**

- **Objetivo general:** Construir una interfaz de usuario accesible, responsiva, internacionalizada y conectada a la API REST del Módulo 3 usando Angular.
- **Secuencia por subtema:**
  1. UX/accesibilidad (2h) → 2. HTML semántico (4h) → 3. CSS y responsive design (6h) → 4. ECMAScript moderno, incl. promesas/async-await (6h) → 5. Angular: componentes y módulos (6h) → 6. Enrutamiento, guards, pipes (5h) → 7. Consumo de servicios (HttpClient, interceptores JWT) y manejo de estado con RxJS (6h) → 8. Pruebas de software front-end (3h).
- **Estándares técnicos concretos** *(mejora incorporada)*:
  - Auditar cada interfaz con **Google Lighthouse**, corrigiendo hasta alcanzar un puntaje de accesibilidad ≥ 90.
  - Verificar contraste cromático y atributos **WAI-ARIA** conforme a **WCAG 2.1 AA**.
  - Configurar internacionalización (i18n) para alternar dinámicamente contenido en español/inglés.
- **Material a crear:** Presentaciones por subtema; repositorio base Angular; guía de estilos CSS responsivo; video de RxJS y manejo de estado; checklist de accesibilidad (WCAG).
- **Recursos sugeridos:** Callaghan (2024); Freeman (2024).[^1]
- **Laboratorio 4 — "SPA modular conectada a la API"**: Estructura modular (AuthModule, DashboardModule, SharedModule); servicios inyectables con HttpClient; interceptor HTTP para adjuntar el token JWT; rutas con lazy loading y CanActivate Guard; suscripción a flujos asíncronos con el operador `async`. Sprint de 3 semanas con entregas parciales (estructura → enrutamiento → integración de API).
- **Lectura en inglés obligatoria #1:** Fragmento de Freeman (2024) sobre arquitectura de componentes, con reporte de comprensión en español.[^1]

### Examen 1 (Semana 10)

Cubre Módulos 1 a 4 completos (fundamentos, entorno, back-end, front-end **incluyendo Angular**), formato teórico-práctico. Al enseñarse todo el Módulo 4 antes de esta semana, no existe desfase entre lo evaluado y lo impartido.

### Módulo 5 — Desarrollo móvil (Semanas 10–12)

**5.1 Introducción (ecosistemas, nativo vs. multiplataforma) · 5.2 Desarrollo de aplicaciones móviles**

- **Objetivo:** Diseñar y desarrollar una app móvil básica con framework multiplataforma, integrando navegación, persistencia local y acceso a hardware.
- **Duración:** 6h teoría + 18h práctica (3 semanas).
- **Material a crear:** Comparativa nativo vs. multiplataforma; guía de instalación de entorno móvil (emuladores); repositorio base de app móvil.
- **Laboratorio 5 — "App móvil con persistencia y sensores"**: mínimo 3 pantallas navegables; base de datos local (SQLite/Async Storage) para operación offline; permisos y consumo de un componente de hardware (cámara o GPS); renderizado reactivo de los datos obtenidos. Entrega en 2 sprints con demo en vivo.
- **Investigación sugerida del módulo (no evaluada formalmente):** Comparar 2 ecosistemas móviles (ej. Flutter vs. React Native) en rendimiento, curva de aprendizaje y comunidad — entregable de 3-5 páginas.

### Módulo 6 — Seguridad web y móvil (Semanas 13–14, incluye Investigación formal 5%)

**6.1 Vulnerabilidades comunes · 6.2 Autenticación y autorización · 6.3 Seguridad de datos · 6.4 Seguridad en el código · 6.5 Seguridad en APIs · 6.6 Seguridad en el despliegue · 6.7 Herramientas**

- **Objetivo:** Identificar vulnerabilidades del OWASP Top 10 y aplicar mitigaciones en código, API y despliegue.
- **Duración:** 6h teoría + 8h práctica.
- **Material a crear:** Presentación OWASP Top 10 (código vulnerable vs. seguro); checklist de auditoría; demostración controlada de un ataque XSS.
- **Laboratorio 6 — "Auditoría de seguridad del proyecto propio":** Aplicar checklist OWASP (con OWASP ZAP o similar) al proyecto integrador y corregir al menos 3 vulnerabilidades detectadas.

**Investigación formal (5% de la nota) — temas predefinidos** *(mejora: se fijan 3 temas concretos para asegurar equidad entre las 9 sedes en lugar de un tema libre)*:

1. *Modern Front-End Architectures & Micro-Frontends: Scalability and Patterns.*
2. *OWASP API Security Top 10: Vulnerabilities, Hardening and Mitigation in Enterprise Systems.*
3. *State Management and Reactive Programming Patterns in Cross-Platform Mobile Applications.*

- **Modalidad:** individual o en parejas.
- **Entregable:** informe técnico en español (máx. 5 páginas) que analice el problema, los patrones propuestos, resultados y una reflexión crítica de aplicabilidad, más presentación de 10 minutos, con al menos una fuente en inglés.[^1]

### Módulo 7 — Despliegue y publicación (Semanas 15–16)

**7.1 Despliegue de aplicaciones web (empaquetado, hospedaje, servidores, dominios) · 7.2 Publicación de aplicaciones móviles**

- **Objetivo:** Empaquetar y desplegar la aplicación web en producción, y preparar la app móvil para publicación.
- **Duración:** 4h teoría + 10h práctica.
- **Especificación técnica concreta** *(mejora incorporada, reemplaza el enunciado genérico "servicio cloud según stack")*:
  - Redactar un **Dockerfile multi-stage** para back-end y front-end.
  - Orquestar API, base de datos y proxy inverso **Nginx** mediante **docker-compose.yml**.
  - Desplegar la imagen contenerizada en una plataforma **PaaS** (Render, Azure Web Apps o AWS) con acceso público vía HTTPS.
  - Generar el empaquetado/firma de la app móvil para su publicación.
- **Material a crear:** Guía paso a paso de despliegue (checklist); video de despliegue en vivo; plantilla de configuración de dominio y SSL.
- **Laboratorio 7 — "Despliegue end-to-end":** entrega de URL funcional + evidencia de build móvil.

### Examen 2 (Semana 16)

Cubre Módulos 5, 6 y 7 (móvil, seguridad, despliegue), formato teórico-práctico.

### Módulo 8 — Proyecto final integrador (Semanas 8, 17–18 — 30% de la nota)

- **Descripción:** Aplicación web y móvil completa que integra las 7 capas trabajadas en el semestre: back-end en capas, front-end Angular (accesible e internacionalizado), app móvil, seguridad OWASP y despliegue contenerizado funcional.
- **Enfoque:** Grupal (2-3 personas), con rúbrica de coevaluación de aporte individual y defensa oral individualizada.
- **Hitos de entrega** *(mejora incorporada: se agrega un avance temprano formativo, dividiendo el 30% sin mover contenido del cronograma)*:

| Hito | Semana | % | Contenido evaluado |
|---|---|---|---|
| **Avance 1** | 8 | 10% | Script de base de datos, API back-end funcional desplegada con Swagger, autenticación JWT operativa y pruebas unitarias de servicios |
| **Entrega final y defensa oral** | 17–18 | 20% | Sistema full-stack totalmente integrado (web + móvil + seguridad + despliegue), con defensa oral individual donde cada estudiante modifica código en tiempo real |

> Nota: el Avance 1 se ubica en la semana 8 porque en esa fecha el Módulo 3 (back-end) ya está cerrado y el Módulo 4 (front-end) está en curso, por lo que solo se exige la capa de back-end del proyecto — no genera adelantos de contenido no impartido.

---

## 5. Rúbrica de Evaluación del Proyecto Integrador (30%) *(incorporada del segundo plan)*

| Criterio | Ponderación (sobre el 30%) | Excelente | Aceptable | Deficiente |
|---|---|---|---|---|
| Arquitectura back-end y persistencia | 25% | Separación limpia de capas, ORM optimizado, SPs correctos, paginación y cobertura de pruebas | Estructura aceptable, ORM con fallas menores o cobertura de pruebas incompleta | Código acoplado, sin ORM ni pruebas, o con errores graves de ejecución |
| Front-end SPA (UX/Accesibilidad/i18n) | 25% | SPA modular en Angular, responsiva, accesible (Lighthouse ≥ 90), i18n funcional, RxJS eficiente | SPA funcional con errores menores de maquetación, accesibilidad 70-89% o i18n incompleto | No es SPA, inadaptable a móviles, accesibilidad < 70% y sin i18n |
| Integración app móvil | 20% | Consume la API correctamente, persistencia local offline operativa, uso correcto del hardware | Consume la API pero sin almacenamiento local o falla el sensor | Aplicación inestable, no conecta a la API ni usa hardware |
| Seguridad OWASP y despliegue | 15% | Sanitización completa, JWT robusto, contenerización funcional, URL pública activa | JWT funcional con vulnerabilidades menores; Docker solo local | Sin seguridad, expuesto a inyecciones, sin despliegue |
| Defensa oral y dominio de código | 15% | Domina individualmente el código y la arquitectura ante preguntas del docente | Explicación imprecisa en secciones desarrolladas por otros | Incapaz de explicar el código o justificar decisiones |

Cada criterio debe publicarse en Mediación Virtual antes de la aplicación del hito correspondiente, conforme exige el programa oficial.[^1]

---

## 6. Estrategia Pedagógica General

| Elemento | Recomendación |
|---|---|
| Metodología marco | ABP, con el proyecto integrador como columna vertebral desde el Módulo 2 |
| Contenido teórico | Flipped classroom en Módulos 1, 2 y 6 |
| Contenido técnico | Codificación en vivo guiada (exigencia oficial de metodología) |
| Dinámica de clase | Exposición corta (20-30 min) + práctica guiada inmediata; foros de discusión y resolución de casos |
| Trabajo colaborativo | Pair programming en laboratorios de back-end/front-end; proyecto final en equipos de 2-3 |
| Idioma técnico | Mínimo 2 lecturas en inglés con reporte en español (Módulos 4 y 6, temas predefinidos) |
| Uso de IA generativa | Regulado y transparente, verificado mediante defensa oral (ver sección 3) |
| Accesibilidad técnica | Estándar WCAG 2.1 AA + auditoría Lighthouse en todo material y proyecto de front-end |
| Plataforma | Mediación Virtual UCR como repositorio central; Teams/Zoom para sesiones sincrónicas |

---

## 7. Cronograma Consolidado (18 semanas)

| Semana | Fechas (2026) | Módulo/Actividad | Evaluación asociada |
|---|---|---|---|
| 1 | 10-15 ago | M0 Inducción + M1 Fundamentos web | — |
| 2 | 17-22 ago | M2 Configuración de ambiente y Git | Entrega Laboratorio 1-2 |
| 3 | 24-29 ago | M3.1 Capa de datos | Inicio Laboratorio 3 |
| 4 | 31 ago-05 set | M3.2-3.3 Capa de negocio y controladores | Avance de laboratorio |
| 5 | 07-12 set | M3.3-3.4 API REST y manejo de errores | Avance de laboratorio |
| 6 | 14-19 set | M3.5-3.7 Autenticación, sesiones, pruebas | Entrega Laboratorio 3 |
| 7 | 21-26 set | M4.1-4.3 UX, accesibilidad, HTML | Inicio Laboratorio 4 |
| 8 | 28 set-03 oct | M4.4-4.5 CSS, ECMAScript | Avance Laboratorio 4 + **Avance 1 de Proyecto (10%)** |
| 9 | 05-10 oct | M4.6 Framework Angular (completo) | Entrega Laboratorio 4 + Lectura en inglés #1 |
| 10 | 12-17 oct | **Examen 1 (20%)** — cubre M1-M4 completos | Examen 1 |
| 11 | 19-24 oct | M5 Desarrollo móvil | Avance Laboratorio 5 |
| 12 | 26-31 oct | M5 Desarrollo móvil | Entrega Laboratorio 5 |
| 13 | 02-07 nov | M6 Seguridad web y móvil | Asignación de Investigación (temas predefinidos) |
| 14 | 09-14 nov | M6 Seguridad (cont.) | Entrega Investigación (5%) + Entrega Laboratorio 6 |
| 15 | 16-21 nov | M7 Despliegue (Docker, Nginx, PaaS) | Avance Laboratorio 7 |
| 16 | 23-28 nov | M7 Despliegue (cont.) | **Examen 2 (20%)** |
| 17 | 30 nov-05 dic | M8 Proyecto final: integración y ajustes | Avance de proyecto |
| 18 | 07-12 dic | M8 Defensa oral y ampliación | **Entrega final y defensa (20%)** |

Esta distribución respeta el cronograma oficial del programa y ubica todo el contenido de Angular antes del Examen 1, corrigiendo el desfase detectado.[^1]

---

## 8. Evaluaciones: Instrumentos y Ponderación

| Instrumento | Peso | Momento | Cobertura |
|---|---|---|---|
| Examen 1 | 20% | Semana 10 | Módulos 1-4 (incluye Angular completo) |
| Examen 2 | 20% | Semana 16 | Módulos 5-7 |
| Investigación (temas predefinidos) | 5% | Semana 14 | Módulo 6 (seguridad) |
| Proyecto programado — Avance 1 | 10% | Semana 8 | Back-end (Módulo 3) |
| Proyecto programado — Entrega final y defensa | 20% | Semanas 17-18 | Integrador (todos los módulos) |
| Pruebas cortas, tareas, prácticas guiadas, talleres | 25% | Continuo | Todos los módulos |
| **Total** | **100%** | | |

La suma del proyecto (10% + 20% = 30%) respeta exactamente el peso oficial fijado en el programa; solo se distribuye en dos hitos para dar retroalimentación formativa temprana.[^1] Toda evaluación debe comunicarse con al menos 5 días hábiles de antelación (excepto quices), y cada actividad debe contar con rúbrica publicada previamente en Mediación Virtual.[^1]

---

## 9. Riesgos Docentes y Recomendaciones (fusión de ambos planes)

### Riesgos identificados

- **Subestimar el Módulo 3 (back-end):** es el bloque más extenso y técnicamente denso; no debe comprimirse pese a presión de cronograma.
- **Saltar a Angular sin reforzar ECMAScript moderno:** genera confusión en estudiantes con bases débiles; por eso 4.5 (ECMAScript) precede a 4.6 (Angular) en la secuencia.
- **Tratar la seguridad como anexo aislado:** debilita la comprensión real de vulnerabilidades; se recomienda introducir JWT y sesiones seguras desde el Módulo 3, no solo en el Módulo 6.
- **Heterogeneidad de base del estudiantado:** al provenir de dos requisitos alternativos (DS III o Programación II), hay brechas en POO, SQL o fundamentos web.
- **Sobrecarga cognitiva por dispersión tecnológica:** el aprendizaje simultáneo de back-end, front-end, móvil, seguridad y contenerización puede fragmentar la comprensión si no se ancla en un solo proyecto conductor.
- **Proyectos grupales sin coevaluación individual:** generan *free-riding* y calificaciones injustas.
- **Variabilidad entre las 9 sedes/docentes:** sin estándares técnicos explícitos (herramientas, umbrales de accesibilidad, plataforma de despliegue), la dificultad y calidad del curso puede variar mucho entre grupos.

### Mitigaciones y sugerencias

- Usar el **mismo proyecto acumulativo** desde el Módulo 2 hasta el Módulo 8, de modo que cada tema se perciba como una capa añadida, no contenido aislado.
- Grabar las sesiones de codificación en vivo para consulta asincrónica (modalidad virtual).
- Implementar **retroalimentación formativa semanal** mediante quices cortos de bajo riesgo, no solo en los dos exámenes.
- Fomentar foros técnicos donde el estudiantado resuelva dudas de compañeros antes de escalar al docente.
- Ofrecer **guías de nivelación asincrónica** (videos cortos de HTTP, POO, SQL) antes del Módulo 3, para estudiantes con brechas de base.
- Proveer **repositorios plantilla / starter kits** preconfigurados (estructura de carpetas, middleware base) para que el esfuerzo se concentre en la lógica de negocio, no en configuración repetitiva.
- Ofrecer retos opcionales de extensión (microservicios adicionales, testing avanzado) para estudiantes con base sólida, evitando desmotivación.
- Priorizar materiales descargables (PDF, video offline) para sedes con conectividad limitada (ej. Caribe).
- Garantizar accesibilidad de todo material publicado (transcripciones, lectores de pantalla) y coordinar adecuaciones con el CAID cuando corresponda.[^1]
- Mantener el ambiente de clase dentro de los protocolos institucionales de prevención del hostigamiento y respeto, conforme a la política oficial del curso.[^1]

---

## Referencias

**Obligatorias**
- Callaghan, M. D. (2024). *Angular for business: Awaken the advocate within and become the angular expert at work.* Apress.
- De Sanctis, V. (2024). *ASP.NET Core 8 and Angular: Full-stack web development with ASP.NET Core 8 and Angular* (6th ed.). Packt Publishing Ltd.
- Freeman, A. (2024). *Pro angular 16* (6th ed.). Manning Publications.
- Green, D. (2023). *Java spring boot: 3 books in 1.* Self-Published.
- Meric, A. (2024). *Mastering spring boot 3.0.* Packt Publishing Ltd.

**Secundarias**
- Centro de Investigación de Estudios de la Mujer, UCR. (2023). *Hostigamiento sexual en la UCR. ¿Qué hacer para enfrentarlo?*
- Cybellium. (2023). *Mastering front-end development: A comprehensive guide to learn front-end development.*

[^1]: IF0009_Desarrollo_de_Software_IV_II_2026.pdf — Programa oficial del curso, UCR, SR-CIE, II Ciclo 2026.
