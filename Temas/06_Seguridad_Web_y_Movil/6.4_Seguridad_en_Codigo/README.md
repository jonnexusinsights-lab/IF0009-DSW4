# Subtema 6.4: Seguridad en el Código Fuente: Validación, Sanitización, Prevención XSS y Políticas CSP

Este módulo aborda la codificación segura (*Secure Coding*) y la defensa contra ataques dirigidos a la capa de presentación y lógica de negocio, incluyendo la neutralización de scripts maliciosos y la validación formal de entradas.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar el principio de **Defensa en Profundidad** y la regla de oro: *"Toda entrada de usuario o de red debe considerarse potencialmente hostil"*.
2. Analizar la taxonomía de ataques **Cross-Site Scripting (XSS)**: Almacenado (*Stored/Persistent*), Reflejado (*Reflected*) y Basado en el DOM (*DOM-based*).
3. Diseñar esquemas de validación semántica fuertemente tipada en el backend con **Jakarta Bean Validation** y en el cliente con validadores reactivos.
4. Configurar e interpretar cabeceras de seguridad del navegador, especialmente la directiva **Content Security Policy (CSP)** y protecciones contra **Cross-Site Request Forgery (CSRF)**.

---

## 📚 Estructura Temática Planificada

### 6.4.1 Validación y Sanitización de Entradas (Input Validation)
* Diferencia fundamental entre validación sintáctica (expresiones regulares, rangos numéricos) y sanitización (limpieza o neutralización de etiquetas HTML).
* Lista blanca (*Whitelisting / Allowlisting*) vs. Lista negra (*Blocklisting*): por qué el bloqueo de palabras clave siempre es eludible.
* Validación declarativa en Spring Boot 3 con anotaciones `@NotNull`, `@Size`, `@Pattern`, `@Email` y `@Valid`.

### 6.4.2 Cross-Site Scripting (XSS) y Context-Aware Encoding
* Cómo un atacante inyecta JavaScript malicioso para robar cookies de sesión, tokens o interceptar pulsaciones de teclado (*Keylogger*).
* Codificación contextual de caracteres (*Context-Aware Output Encoding*):
  * Contexto HTML Body (`&lt;`, `&gt;`, `&amp;`).
  * Contexto Atributos HTML (`&quot;`, `&#x27;`).
  * Contexto JavaScript literal y URLs (`encodeURIComponent`).
* Mecanismos automáticos de escape en frameworks modernos (Angular interpolación `{{ }}` y DomSanitizer, Flutter Text widgets) y cómo no deshabilitarlos imprudentemente (`bypassSecurityTrustHtml`).

### 6.4.3 Content Security Policy (CSP) y Mitigación de CSRF
* **Content Security Policy (CSP Nivel 3):**
  * Restricción de orígenes de carga de scripts, estilos, fuentes e imágenes (`default-src 'self'`).
  * Eliminación de scripts en línea (`unsafe-inline`) y funciones `eval()` mediante *nonces* y hashes criptográficos.
* **Cross-Site Request Forgery (CSRF):**
  * Por qué las aplicaciones móviles y APIs stateless con cabecera `Authorization: Bearer` no son vulnerables a CSRF tradicional.
  * Protección en SPAs con cookies mediante atributos `SameSite=Strict` y patrón *Double-Submit Cookie*.

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Explotación y Remediación XSS:** Demostración controlada de robo de sesión mediante inyección en un campo de comentarios y su neutralización con codificación contextual.
* **Configuración CSP en Nginx y Spring Security:** Implementación de cabeceras CSP estrictas y análisis de violaciones mediante directivas `report-uri`.
* **Bean Validation Personalizada:** Creación de un validador `@CedulaCostarricense` con algoritmo de dígito verificador y manejo de errores RFC 7807.

---

## 📖 Referencias y Estándares Oficiales

* W3C. (2024). *Content Security Policy Level 3*. W3C Working Draft.
* OWASP Foundation. (2023). *Cross Site Scripting Prevention Cheat Sheet*.
* Jakarta EE. (2022). *Jakarta Bean Validation Specification 3.0*.
