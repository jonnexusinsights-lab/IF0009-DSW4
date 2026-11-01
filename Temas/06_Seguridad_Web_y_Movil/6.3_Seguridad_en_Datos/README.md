# Subtema 6.3: Seguridad de Datos: Cifrado en Reposo, Cifrado en Tránsito y Protección contra Inyecciones

Este módulo aborda la confidencialidad, integridad y disponibilidad de la información en todo su ciclo de vida, cubriendo estándares de cifrado criptográfico, canales seguros de comunicación y técnicas avanzadas de aislamiento de datos en aplicaciones distribuidas.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **6.3.1 Cifrado en Tránsito (TLS 1.3 & Pinning)** | [6.3.1_Cifrado_en_Transito_HTTPS_TLS13.md](6.3.1_Cifrado_en_Transito_HTTPS_TLS13.md) | [Slides Markdown](6.3.1_Cifrado_en_Transito_HTTPS_TLS13_Slides.md) | [Presentación HTML Reveal.js](6.3.1_Cifrado_en_Transito_HTTPS_TLS13_Slides.html) |
| **6.3.2 Cifrado en Reposo (JPA & SQLCipher)** | [6.3.2_Cifrado_en_Reposo_BD_Almacenamiento_Movil.md](6.3.2_Cifrado_en_Reposo_BD_Almacenamiento_Movil.md) | [Slides Markdown](6.3.2_Cifrado_en_Reposo_BD_Almacenamiento_Movil_Slides.md) | [Presentación HTML Reveal.js](6.3.2_Cifrado_en_Reposo_BD_Almacenamiento_Movil_Slides.html) |
| **6.3.3 Prevención Integral contra Inyecciones** | [6.3.3_Prevencion_Integral_Inyecciones_Codigo.md](6.3.3_Prevencion_Integral_Inyecciones_Codigo.md) | [Slides Markdown](6.3.3_Prevencion_Integral_Inyecciones_Codigo_Slides.md) | [Presentación HTML Reveal.js](6.3.3_Prevencion_Integral_Inyecciones_Codigo_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Dominar los esquemas de protección de datos en sus tres estados fundamentales: **Datos en Tránsito** (*Data in Transit*), **Datos en Reposo** (*Data at Rest*) y **Datos en Uso** (*Data in Use*).
2. Configurar túneles de comunicación cifrados de alta seguridad utilizando **Transport Layer Security (TLS 1.3)** y anclaje de certificados (*Certificate Pinning*) en clientes móviles.
3. Implementar cifrado simétrico robusto (**AES-256-GCM**) para campos sensibles en bases de datos y motores relacionales embebidos como SQLCipher.
4. Diseñar mecanismos formales para erradicar cualquier posibilidad de inyecciones de código (SQLi, NoSQLi, LDAP Injection y OS Command Injection).

---

## 📖 Referencias y Estándares Oficiales

* Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3* (RFC 8446). IETF.
* National Institute of Standards and Technology. (2001). *Advanced Encryption Standard (AES)* (FIPS PUB 197).
* OWASP Foundation. (2023). *OWASP Injection Prevention Cheat Sheet*.
