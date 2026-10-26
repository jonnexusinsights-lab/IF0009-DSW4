# Subtema 6.7: Herramientas de Análisis de Seguridad: SAST, DAST, Auditorías Móviles y OWASP ZAP

Este módulo aborda el ecosistema de herramientas de aseguramiento y pruebas de seguridad automatizadas, dotando al estudiante de los instrumentos para auditar código fuente y aplicaciones en ejecución antes de su paso a producción.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar las diferencias operativas y metodológicas entre pruebas estáticas de seguridad (**SAST**) y pruebas dinámicas de seguridad (**DAST**).
2. Configurar y operar escáneres de seguridad dinámicos como **OWASP ZAP (Zed Attack Proxy)** para detectar vulnerabilidades en tiempo de ejecución en APIs y sitios web.
3. Conocer herramientas de auditoría y análisis de binarios móviles como **MobSF (Mobile Security Framework)**.
4. Integrar compuertas de calidad de seguridad (*Security Quality Gates*) en entornos de desarrollo mediante **SonarQube** y linters de seguridad.

---

## 📚 Estructura Temática Planificada

### 6.7.1 Análisis Estático de Seguridad (SAST - Static Application Security Testing)
* Fundamentos: Análisis del código fuente y del árbol de sintaxis abstracta (AST) sin compilar ni ejecutar el programa.
* Detección temprana de patrones inseguros: concatenaciones SQL, manejo deficiente de excepciones, secretos en código y deserializaciones inseguras.
* Herramientas SAST en el flujo de trabajo: **SonarQube / SonarLint**, Semgrep y SpotBugs con Find Security Bugs.

### 6.7.2 Análisis Dinámico de Seguridad (DAST - Dynamic Application Security Testing)
* Fundamentos: Análisis de caja negra (*Black-Box Testing*) interactuando contra la aplicación desplegada y activa en un servidor.
* **OWASP ZAP (Zed Attack Proxy):**
  * Modos de escaneo: Pasivo (inspección de tráfico y cabeceras sin generar peticiones intrusivas) y Activo (inyección controlada de payloads para descubrir XSS, SQLi y fallas de enrutamiento).
  * Escaneo de APIs REST mediante especificaciones OpenAPI / Swagger (`zap-api-scan.py`).
  * Análisis e interpretación del reporte de hallazgos (Falsos Positivos vs. Riesgos Reales).

### 6.7.3 Análisis y Auditoría de Seguridad Móvil (MASVS y MobSF)
* Estándar **OWASP MASVS** (*Mobile Application Security Verification Standard*).
* **Mobile Security Framework (MobSF):**
  * Análisis estático de binarios Android (`.apk` / `.aab`) e iOS (`.ipa`).
  * Descompilación automatizada, análisis de permisos declarados en manifiestos, certificados de firmado y detección de URLs embebidas o librerías desactualizadas.

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Escaneo Automatizado de API con OWASP ZAP:** Ejecución del escáner ZAP en contenedor Docker apuntando al backend Spring Boot documentado con OpenAPI y remediación de alertas medias y altas.
* **Inspección de APK con MobSF:** Carga de un binario compilado de Flutter en MobSF y revisión del reporte de seguridad (permisos excesivos y configuraciones de red inseguras).
* **Configuración de SonarQube Quality Gate:** Definición de una regla que bloquee la integración si se detecta una vulnerabilidad de severidad alta (*Vulnerability / Security Hotspot*).

---

## 📖 Referencias y Estándares Oficiales

* OWASP Foundation. (2024). *OWASP Zed Attack Proxy (ZAP) Official Documentation*. https://www.zaproxy.org/
* OWASP Foundation. (2024). *OWASP Mobile Application Security (MASVS & MASTG)*. https://mas.owasp.org/
* SonarSource. (2024). *SonarQube Security Rules and Guidelines*.
