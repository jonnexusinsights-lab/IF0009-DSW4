# Subtema 6.2: Autenticación Robusta, Protocolos de Autorización y Gestión de Identidad (OAuth2, OIDC y JWT Hardening)

Este módulo aborda la ingeniería de la identidad digital en sistemas modernos, profundizando en el diseño de arquitecturas de autenticación seguras, el ciclo de vida de tokens criptográficos y los estándares abiertos de autorización delegada.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar la distinción conceptual entre **Autenticación** (verificación irrefutable de identidad) y **Autorización** (determinación de permisos sobre recursos).
2. Analizar el funcionamiento interno de **OAuth 2.0** y **OpenID Connect (OIDC)**, comprendiendo los flujos de concesión modernos (*Authorization Code Flow with PKCE*).
3. Implementar esquemas de control de acceso basados en roles (**RBAC**) y atributos (**ABAC**) en Spring Boot 3 con Spring Security y en aplicaciones móviles con Flutter.
4. Aplicar técnicas avanzadas de robustecimiento (*Hardening*) en tokens **JSON Web Tokens (JWT)**: rotación de llaves, Refresh Tokens seguros y revocación de sesiones distribuidas.

---

## 📚 Estructura Temática Planificada

### 6.2.1 Arquitectura de Autenticación Moderna
* Sesiones tradicionales con estado (*Stateful Session Cookies*) vs. Autenticación sin estado (*Stateless Token-Based*).
* Factores de Autenticación (MFA/2FA): Códigos de un solo uso basados en tiempo (TOTP), llaves de seguridad WebAuthn / FIDO2 y biometría móvil.
* Almacenamiento y verificación de contraseñas de alta entropía con **Argon2id** y **BCrypt** (cost factor adaptativo).

### 6.2.2 Protocolos Estándar: OAuth 2.0 y OpenID Connect (OIDC)
* Roles fundamentales en OAuth 2.0: *Resource Owner*, *Client*, *Authorization Server*, *Resource Server*.
* El flujo obligatorio para clientes públicos (SPA y Apps Móviles): **Authorization Code Flow con PKCE** (*Proof Key for Code Exchange*).
* Capa de identidad OIDC: Estructura del `id_token` vs `access_token` y endpoints de usuario (`/userinfo`).

### 6.2.3 Endurecimiento de JWT (JWT Hardening)
* Especificación RFC 7519: Anatomía del Header, Payload y Signature.
* Vulnerabilidades recurrentes en implementaciones caseras de JWT:
  * Ataque de algoritmo nulo (`alg: none`).
  * Confusión de algoritmos simétricos/asimétricos (HMAC vs RSA).
  * Fuga de información sensible en Claims sin cifrar.
* Patrón de Doble Token (*Access Token* de corta duración + *Refresh Token* de rotación con detección de reutilización).

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Integración Spring Boot 3:** Configuración de un Resource Server con validación de tokens JWT mediante Spring Security 6 y filtros personalizados.
* **Flujo PKCE Móvil:** Demostración de intercambio de código con desafío criptográfico (`code_verifier` y `code_challenge`) en Flutter.
* **Control RBAC granular:** Uso de anotaciones `@PreAuthorize("hasRole('ADMIN') or hasAuthority('INCIDENCIA_WRITE')")` en controladores REST.

---

## 📖 Referencias y Estándares Oficiales

* Hardt, D. (2012). *The OAuth 2.0 Authorization Framework* (RFC 6749). IETF.
* Jones, M., Bradley, J., & Sakimura, N. (2015). *JSON Web Token (JWT)* (RFC 7519). IETF.
* Sakimura, N., et al. (2014). *OpenID Connect Core 1.0 incorporating errata set 1*. OpenID Foundation.
