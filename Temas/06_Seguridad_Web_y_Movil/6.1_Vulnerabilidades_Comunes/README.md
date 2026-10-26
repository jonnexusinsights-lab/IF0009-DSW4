# Subtema 6.1: Vulnerabilidades Comunes y Mitigación del OWASP Top 10 en Aplicaciones Web y Móviles

Este módulo de planificación pedagógica estructura los fundamentos de seguridad ofensiva y defensiva, analizando los principales vectores de ataque que amenazan los sistemas de software modernos según el estándar internacional **OWASP (Open Web Application Security Project)**.

---

## 🎯 Objetivos de Aprendizaje

1. Comprender la metodología de evaluación de riesgos del **OWASP Top 10 (Web)** y del **OWASP Mobile Top 10**, identificando los vectores de mayor impacto en arquitecturas distribuidas.
2. Analizar la anatomía de fallas críticas: inyecciones (SQLi, NoSQLi, Command Injection), pérdida de control de acceso (*Broken Access Control*), fallos criptográficos (*Cryptographic Failures*) y desconfiguración de seguridad (*Security Misconfiguration*).
3. Evaluar los riesgos específicos del ecosistema móvil: almacenamiento inseguro de credenciales, comunicaciones no cifradas y ejecución en dispositivos modificados (*root* y *jailbreak*).
4. Diseñar estrategias proactivas de remediación y buenas prácticas arquitectónicas para mitigar defectos desde las etapas tempranas del diseño de software (*Security by Design*).

---

## 📚 Estructura Temática Planificada

### 6.1.1 El Estándar OWASP Top 10 (Edición Web y Móvil)
* Historia, evolución y metodología de puntuación del riesgo (Probabilidad vs. Impacto).
* Comparativa entre los 10 riesgos web y los vectores críticos en dispositivos móviles:
  * M1: Uso Inseguro de Credenciales y Autenticación Móvil.
  * M2: Almacenamiento Inadecuado en el Dispositivo (Keystore vs. SharedPreferences).
  * M3: Comunicaciones de Red Inseguras y MitM (*Man-in-the-Middle*).
  * M4: Validación Insuficiente de Entradas y Entornos Vulnerables.

### 6.1.2 Vectores de Inyección y Pérdida de Control de Acceso
* **Inyección SQL (SQLi):**
  * Mecanismo de explotación mediante concatenación de cadenas en sentencias SQL.
  * Remediación en el backend: Consultas parametrizadas con JPA, Spring Data y PreparedStatement.
* **Control de Acceso Deficiente (Broken Access Control):**
  * Referencias directas a objetos inseguras (IDOR - *Insecure Direct Object References*).
  * Evasión de controles de privilegios verticales (Usuario regular a Administrador) y horizontales (Acceso a registros de otro usuario).
  * Implementación de filtros de autorización contextuales a nivel de servicio.

### 6.1.3 Fallos Criptográficos y Exposición de Datos Sensibles
* Diferenciación técnica entre funciones hash (BCrypt, Argon2), cifrado simétrico (AES-256-GCM) y asimétrico (RSA, Curvas Elípticas).
* Deprecación de algoritmos inseguros (MD5, SHA-1, DES).
* Protección de secretos en tránsito (TLS 1.3) y en reposo (cifrado a nivel de base de datos y SQLite móvil).

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Laboratorio Demostrativo:** Análisis forense de una petición vulnerable a IDOR en un endpoint de usuarios y su mitigación en Spring Boot con `@PreAuthorize`.
* **Práctica de Inyección:** Comparativa en vivo entre una consulta nativa vulnerable concatenada y una consulta derivada segura en Spring Data JPA.
* **Inspección Móvil:** Extracción de datos en texto plano desde una aplicación con base de datos no cifrada frente a una protegida con `flutter_secure_storage`.

---

## 📖 Referencias y Estándares Oficiales

* OWASP Foundation. (2021). *OWASP Top 10: The Ten Most Critical Web Application Security Risks*. https://owasp.org/Top10/
* OWASP Foundation. (2024). *OWASP Mobile Top 10 Security Risks*. https://owasp.org/www-project-mobile-top-10/
* NIST Special Publication 800-63B. *Digital Identity Guidelines: Authentication and Lifecycle Management*.
