# Subtema 6.3: Seguridad de Datos: Cifrado en Reposo, Cifrado en Tránsito y Protección contra Inyecciones

Este módulo aborda la confidencialidad, integridad y disponibilidad de la información en todo su ciclo de vida, cubriendo estándares de cifrado criptográfico, canales seguros de comunicación y técnicas avanzadas de aislamiento de datos en aplicaciones distribuidas.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar los esquemas de protección de datos en sus tres estados fundamentales: **Datos en Tránsito** (*Data in Transit*), **Datos en Reposo** (*Data at Rest*) y **Datos en Uso** (*Data in Use*).
2. Configurar túneles de comunicación cifrados de alta seguridad utilizando **Transport Layer Security (TLS 1.3)** y anclaje de certificados (*Certificate Pinning*) en clientes móviles.
3. Implementar cifrado simétrico robusto (**AES-256-GCM**) para campos sensibles en bases de datos y motores relacionales embebidos como SQLCipher.
4. Diseñar mecanismos formales para erradicar cualquier posibilidad de inyecciones de código (SQLi, NoSQLi, LDAP Injection y OS Command Injection).

---

## 📚 Estructura Temática Planificada

### 6.3.1 Cifrado en Tránsito: De HTTPS a TLS 1.3
* Negociación criptográfica de claves efímeras (*Ephemeral Diffie-Hellman* / ECDHE) y secreto perfecto hacia adelante (*Forward Secrecy*).
* Cabeceras de transporte estricto: **HTTP Strict Transport Security (HSTS)** y mitigación de ataques de degradación (*SSL Stripping*).
* **Certificate Pinning en Flutter:** Validación del hash SHA-256 de la clave pública (SPKI) del certificado del servidor backend para impedir ataques Man-in-the-Middle (MitM) en redes Wi-Fi públicas o con certificados corporativos instalados.

### 6.3.2 Cifrado en Reposo: Bases de Datos y Almacenamiento Móvil
* Cifrado transparente de bases de datos (**Transparent Data Encryption - TDE**) a nivel de almacenamiento físico.
* Cifrado a nivel de aplicación (Field-Level Encryption) mediante convertidores JPA (`@Convert(converter = CifradoAtributoConverter.class)`).
* Motores SQLite cifrados para clientes móviles: **SQLCipher** y derivación de llaves con PBKDF2.

### 6.3.3 Prevención Integral contra Inyecciones de Código
* Fundamento teórico del principio de equivalencia de datos y código de Von Neumann.
* Inyecciones SQL ciegas (*Blind SQLi* basadas en tiempo o booleanos) y su mitigación mediante mapeo objeto-relacional riguroso.
* Prevención de inyecciones NoSQL (en MongoDB / documentos JSON) mediante validación estricta de esquemas.

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Simulación de Ataque MitM:** Intercepción de tráfico HTTP con proxy de depuración (Charles / Burp Suite) y cómo el Certificate Pinning en Flutter rechaza la conexión instantáneamente.
* **Convertidor Criptográfico JPA en Spring Boot:** Implementación de un `AttributeConverter` con AES-GCM para almacenar números de cédula y teléfonos cifrados en la base de datos H2 / SQL Server.
* **Auditoría de Certificados SSL/TLS:** Análisis automatizado de parámetros de cifrado de servidores con herramientas como SSL Labs.

---

## 📖 Referencias y Estándares Oficiales

* Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3* (RFC 8446). IETF.
* National Institute of Standards and Technology. (2001). *Advanced Encryption Standard (AES)* (FIPS PUB 197).
* OWASP Foundation. (2023). *OWASP Injection Prevention Cheat Sheet*.
