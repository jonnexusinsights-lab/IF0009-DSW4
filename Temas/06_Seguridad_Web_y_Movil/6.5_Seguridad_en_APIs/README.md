# Subtema 6.5: Seguridad en APIs RESTful: Rate Limiting, Políticas CORS, Cabeceras HTTP y Protección contra DoS

Este módulo se enfoca en el blindaje perimetral y operacional de interfaces de programación de aplicaciones (APIs), protegiéndolas contra ataques de denegación de servicio (DoS), consumo no autorizado y fugas de cabeceras en entornos distribuidos.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **6.5.1 OWASP API Security Top 10** | [6.5.1_Estandar_OWASP_API_Security_Top_10.md](6.5.1_Estandar_OWASP_API_Security_Top_10.md) | [Slides Markdown](6.5.1_Estandar_OWASP_API_Security_Top_10_Slides.md) | [Presentación HTML Reveal.js](6.5.1_Estandar_OWASP_API_Security_Top_10_Slides.html) |
| **6.5.2 Control de Acceso CORS** | [6.5.2_Control_Acceso_Origen_CORS_Riguroso.md](6.5.2_Control_Acceso_Origen_CORS_Riguroso.md) | [Slides Markdown](6.5.2_Control_Acceso_Origen_CORS_Riguroso_Slides.md) | [Presentación HTML Reveal.js](6.5.2_Control_Acceso_Origen_CORS_Riguroso_Slides.html) |
| **6.5.3 Rate Limiting & Cuotas DoS** | [6.5.3_Rate_Limiting_Cuotas_Peticion.md](6.5.3_Rate_Limiting_Cuotas_Peticion.md) | [Slides Markdown](6.5.3_Rate_Limiting_Cuotas_Peticion_Slides.md) | [Presentación HTML Reveal.js](6.5.3_Rate_Limiting_Cuotas_Peticion_Slides.html) |
| **6.5.4 Cabeceras HTTP Defensivas** | [6.5.4_Cabeceras_Seguridad_HTTP_Defensivas.md](6.5.4_Cabeceras_Seguridad_HTTP_Defensivas.md) | [Slides Markdown](6.5.4_Cabeceras_Seguridad_HTTP_Defensivas_Slides.md) | [Presentación HTML Reveal.js](6.5.4_Cabeceras_Seguridad_HTTP_Defensivas_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Dominar el estándar **OWASP API Security Top 10**, identificando las amenazas específicas que enfrentan los servicios RESTful en la nube.
2. Diseñar e implementar políticas estrictas de intercambio de recursos de origen cruzado (**CORS - Cross-Origin Resource Sharing**) sin comprometer la seguridad ni incurrir en configuraciones permisivas peligrosas.
3. Proteger endpoints de backend contra abusos, ataques de fuerza bruta y saturación mediante algoritmos de limitación de tasa (**Rate Limiting**).
4. Configurar cabeceras de respuesta HTTP defensivas que mitiguen ataques de clickjacking, sniffing de MIME-types y apertura no autorizada de iframes.

---

## 📖 Referencias y Estándares Oficiales

* OWASP Foundation. (2023). *OWASP API Security Top 10 2023*. https://owasp.org/www-project-api-security/
* Fielding, R., & Reschke, J. (2014). *Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content* (RFC 7231). IETF.
* Mozilla Developer Network (MDN). (2024). *Cross-Origin Resource Sharing (CORS)*.
