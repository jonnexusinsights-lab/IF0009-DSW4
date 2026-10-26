# Subtema 6.5: Seguridad en APIs RESTful: Rate Limiting, Políticas CORS, Cabeceras HTTP y Protección contra DoS

Este módulo se enfoca en el blindaje perimetral y operacional de interfaces de programación de aplicaciones (APIs), protegiéndolas contra ataques de denegación de servicio (DoS), consumo no autorizado y fugas de cabeceras en entornos distribuidos.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar el estándar **OWASP API Security Top 10**, identificando las amenazas específicas que enfrentan los servicios RESTful en la nube.
2. Diseñar e implementar políticas estrictas de intercambio de recursos de origen cruzado (**CORS - Cross-Origin Resource Sharing**) sin comprometer la seguridad ni incurrir en configuraciones permisivas peligrosas.
3. Proteger endpoints de backend contra abusos, ataques de fuerza bruta y saturación mediante algoritmos de limitación de tasa (**Rate Limiting**).
4. Configurar cabeceras de respuesta HTTP defensivas que mitiguen ataques de clickjacking, sniffing de MIME-types y apertura no autorizada de iframes.

---

## 📚 Estructura Temática Planificada

### 6.5.1 El Estándar OWASP API Security Top 10
* Comparativa frente al Top 10 web tradicional:
  * API1: Broken Object Level Authorization (BOLA).
  * API2: Broken Authentication.
  * API3: Broken Object Property Level Authorization (Mass Assignment).
  * API4: Unrestricted Resource Consumption (Falta de cuotas y paginación).
  * API5: Broken Function Level Authorization.

### 6.5.2 Control de Acceso por Origen: CORS Riguroso
* El mecanismo de peticiones pre-vuelo (**Preflight Requests `OPTIONS`**).
* Cabeceras clave: `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`, `Access-Control-Allow-Credentials`.
* El peligro de usar comodines universales (`Access-Control-Allow-Origin: *`) junto con credenciales o cookies (`Allow-Credentials: true`).
* Configuración segura de orígenes permitidos en Spring Boot (`CorsConfigurationSource`).

### 6.5.3 Rate Limiting y Cuotas de Petición
* Algoritmos de limitación de peticiones:
  * *Token Bucket* (balde de tokens para ráfagas controladas).
  * *Leaky Bucket* (salida a tasa constante).
  * *Sliding Window Log / Counter* (ventana deslizante de alta precisión).
* Implementación en Java/Spring Boot con bibliotecas como Bucket4j o a nivel de Proxy Inverso (Nginx `limit_req_zone`).
* Códigos de estado HTTP estandarizados: `429 Too Many Requests` y cabeceras `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`.

### 6.5.4 Cabeceras de Seguridad HTTP Defensivas
* `X-Content-Type-Options: nosniff` (impide la adivinanza de tipo MIME ejecutable).
* `X-Frame-Options: DENY / SAMEORIGIN` (mitigación de Clickjacking).
* `Strict-Transport-Security` (HSTS).
* `Referrer-Policy: strict-origin-when-cross-origin` (previene fugas de parámetros privados en URLs).
* `Permissions-Policy` (deshabilita funciones invasivas del navegador como geolocalización o cámara en páginas incrustadas).

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Prueba de Carga y Rate Limiting:** Simulación de ataque DoS con herramienta de benchmarking (wrk / JMeter) y observación del bloqueo automático a partir de la petición 50 por minuto con código `429`.
* **Configuración CORS en Spring Security:** Configuración selectiva de CORS para permitir únicamente el origen SPA de producción y los esquemas móviles locales.
* **Hardening de Cabeceras:** Inyección y verificación de cabeceras de seguridad en Spring Boot mediante `SecurityFilterChain`.

---

## 📖 Referencias y Estándares Oficiales

* OWASP Foundation. (2023). *OWASP API Security Top 10 2023*. https://owasp.org/www-project-api-security/
* Fielding, R., & Reschke, J. (2014). *Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content* (RFC 7231). IETF.
* Mozilla Developer Network (MDN). (2024). *Cross-Origin Resource Sharing (CORS)*.
