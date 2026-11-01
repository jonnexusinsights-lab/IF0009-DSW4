# Subtema 6.6: Seguridad en el Despliegue: Gestión de Secretos, Contenedores Seguros y Hardening de Entornos Productivos

Este módulo aborda la seguridad en la fase operacional y de infraestructura (DevSecOps), cubriendo la administración de credenciales sensibles, la reducción de superficies de ataque en contenedores Docker y la inmutabilidad de entornos productivos.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **6.6.1 Gestión de Secretos (12-Factor & GitLeaks)** | [6.6.1_Gestion_Secretos_Configuracion_Externa.md](6.6.1_Gestion_Secretos_Configuracion_Externa.md) | [Slides Markdown](6.6.1_Gestion_Secretos_Configuracion_Externa_Slides.md) | [Presentación HTML Reveal.js](6.6.1_Gestion_Secretos_Configuracion_Externa_Slides.html) |
| **6.6.2 Hardening de Docker & Distroless** | [6.6.2_Hardening_Imagenes_Contenedores_Docker.md](6.6.2_Hardening_Imagenes_Contenedores_Docker.md) | [Slides Markdown](6.6.2_Hardening_Imagenes_Contenedores_Docker_Slides.md) | [Presentación HTML Reveal.js](6.6.2_Hardening_Imagenes_Contenedores_Docker_Slides.html) |
| **6.6.3 Seguridad en la Cadena de Suministro** | [6.6.3_Seguridad_Cadena_Suministro_Supply_Chain.md](6.6.3_Seguridad_Cadena_Suministro_Supply_Chain.md) | [Slides Markdown](6.6.3_Seguridad_Cadena_Suministro_Supply_Chain_Slides.md) | [Presentación HTML Reveal.js](6.6.3_Seguridad_Cadena_Suministro_Supply_Chain_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Erradicar la práctica de almacenar secretos en código duro (*Hardcoded Credentials*) en repositorios de control de versiones Git.
2. Diseñar estrategias seguras de inyección de configuración mediante variables de entorno, almacenes de secretos (**Docker Secrets**, HashiCorp Vault, AWS Secrets Manager) y archivos `.env` excluidos.
3. Aplicar directrices de **Hardening en Contenedores Docker**: ejecución sin privilegios de root (*Non-Root Containers*), imágenes base mínimas (Alpine / Distroless) y escaneo de vulnerabilidades en imágenes.
4. Diseñar pipelines de Integración y Entrega Continua (CI/CD) con escaneos automatizados de dependencias (*Software Supply Chain Security*).

---

## 📖 Referencias y Estándares Oficiales

* Center for Internet Security (CIS). (2024). *CIS Docker Benchmark v1.6.0*.
* National Institute of Standards and Technology. (2017). *Application Container Security Guide* (SP 800-190).
* Wiggins, A. (2017). *The Twelve-Factor App*. https://12factor.net/
