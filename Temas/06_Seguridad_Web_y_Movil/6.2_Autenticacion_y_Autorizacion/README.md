# Subtema 6.2: Autenticación Robusta, Protocolos de Autorización y Gestión de Identidad (OAuth2, OIDC y JWT Hardening)

Este módulo aborda la ingeniería de la identidad digital en sistemas modernos, profundizando en el diseño de arquitecturas de autenticación seguras, el ciclo de vida de tokens criptográficos y los estándares abiertos de autorización delegada.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **6.2.1 Autenticación Moderna & Biometría** | [6.2.1_Arquitectura_Autenticacion_Moderna.md](6.2.1_Arquitectura_Autenticacion_Moderna.md) | [Slides Markdown](6.2.1_Arquitectura_Autenticacion_Moderna_Slides.md) | [Presentación HTML Reveal.js](6.2.1_Arquitectura_Autenticacion_Moderna_Slides.html) |
| **6.2.2 Protocolos OAuth 2.0, OIDC & PKCE** | [6.2.2_Protocolos_OAuth2_OpenID_Connect.md](6.2.2_Protocolos_OAuth2_OpenID_Connect.md) | [Slides Markdown](6.2.2_Protocolos_OAuth2_OpenID_Connect_Slides.md) | [Presentación HTML Reveal.js](6.2.2_Protocolos_OAuth2_OpenID_Connect_Slides.html) |
| **6.2.3 Endurecimiento de JWT (Hardening)** | [6.2.3_Endurecimiento_JWT_Hardening.md](6.2.3_Endurecimiento_JWT_Hardening.md) | [Slides Markdown](6.2.3_Endurecimiento_JWT_Hardening_Slides.md) | [Presentación HTML Reveal.js](6.2.3_Endurecimiento_JWT_Hardening_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Dominar la distinción conceptual entre **Autenticación** (verificación irrefutable de identidad) y **Autorización** (determinación de permisos sobre recursos).
2. Analizar el funcionamiento interno de **OAuth 2.0** y **OpenID Connect (OIDC)**, comprendiendo los flujos de concesión modernos (*Authorization Code Flow with PKCE*).
3. Implementar esquemas de control de acceso basados en roles (**RBAC**) y atributos (**ABAC**) en Spring Boot 3 con Spring Security y en aplicaciones móviles con Flutter.
4. Aplicar técnicas avanzadas de robustecimiento (*Hardening*) en tokens **JSON Web Tokens (JWT)**: rotación de llaves, Refresh Tokens seguros y revocación de sesiones distribuidas.

---

## 📖 Referencias y Estándares Oficiales

* Hardt, D. (2012). *The OAuth 2.0 Authorization Framework* (RFC 6749). IETF.
* Jones, M., Bradley, J., & Sakimura, N. (2015). *JSON Web Token (JWT)* (RFC 7519). IETF.
* Sakimura, N., et al. (2014). *OpenID Connect Core 1.0 incorporating errata set 1*. OpenID Foundation.
