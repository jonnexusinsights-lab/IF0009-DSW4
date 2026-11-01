# Subtema 6.4: Seguridad en el Código Fuente: Validación, Sanitización, Prevención XSS y Políticas CSP

Este módulo aborda la codificación segura (*Secure Coding*) y la defensa contra ataques dirigidos a la capa de presentación y lógica de negocio, incluyendo la neutralización de scripts maliciosos y la validación formal de entradas.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **6.4.1 Validación & Sanitización** | [6.4.1_Validacion_Sanitizacion_Entradas.md](6.4.1_Validacion_Sanitizacion_Entradas.md) | [Slides Markdown](6.4.1_Validacion_Sanitizacion_Entradas_Slides.md) | [Presentación HTML Reveal.js](6.4.1_Validacion_Sanitizacion_Entradas_Slides.html) |
| **6.4.2 Cross-Site Scripting (XSS)** | [6.4.2_Cross_Site_Scripting_XSS_Encoding.md](6.4.2_Cross_Site_Scripting_XSS_Encoding.md) | [Slides Markdown](6.4.2_Cross_Site_Scripting_XSS_Encoding_Slides.md) | [Presentación HTML Reveal.js](6.4.2_Cross_Site_Scripting_XSS_Encoding_Slides.html) |
| **6.4.3 CSP & Mitigación de CSRF** | [6.4.3_Content_Security_Policy_CSP_Mitigacion_CSRF.md](6.4.3_Content_Security_Policy_CSP_Mitigacion_CSRF.md) | [Slides Markdown](6.4.3_Content_Security_Policy_CSP_Mitigacion_CSRF_Slides.md) | [Presentación HTML Reveal.js](6.4.3_Content_Security_Policy_CSP_Mitigacion_CSRF_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Dominar el principio de **Defensa en Profundidad** y la regla de oro: *"Toda entrada de usuario o de red debe considerarse potencialmente hostil"*.
2. Analizar la taxonomía de ataques **Cross-Site Scripting (XSS)**: Almacenado (*Stored/Persistent*), Reflejado (*Reflected*) y Basado en el DOM (*DOM-based*).
3. Diseñar esquemas de validación semántica fuertemente tipada en el backend con **Jakarta Bean Validation** y en el cliente con validadores reactivos.
4. Configurar e interpretar cabeceras de seguridad del navegador, especialmente la directiva **Content Security Policy (CSP)** y protecciones contra **Cross-Site Request Forgery (CSRF)**.

---

## 📖 Referencias y Estándares Oficiales

* W3C. (2024). *Content Security Policy Level 3*. W3C Working Draft.
* OWASP Foundation. (2023). *Cross Site Scripting Prevention Cheat Sheet*.
* Jakarta EE. (2022). *Jakarta Bean Validation Specification 3.0*.
