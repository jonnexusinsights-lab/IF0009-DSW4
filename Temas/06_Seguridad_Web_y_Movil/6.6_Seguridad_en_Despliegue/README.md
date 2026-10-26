# Subtema 6.6: Seguridad en el Despliegue: Gestión de Secretos, Contenedores Seguros y Hardening de Entornos Productivos

Este módulo aborda la seguridad en la fase operacional y de infraestructura (DevSecOps), cubriendo la administración de credenciales sensibles, la reducción de superficies de ataque en contenedores Docker y la inmutabilidad de entornos productivos.

---

## 🎯 Objetivos de Aprendizaje

1. Erradicar la práctica de almacenar secretos en código duro (*Hardcoded Credentials*) en repositorios de control de versiones Git.
2. Diseñar estrategias seguras de inyección de configuración mediante variables de entorno, almacenes de secretos (**Docker Secrets**, HashiCorp Vault, AWS Secrets Manager) y archivos `.env` excluidos.
3. Aplicar directrices de **Hardening en Contenedores Docker**: ejecución sin privilegios de root (*Non-Root Containers*), imágenes base mínimas (Alpine / Distroless) y escaneo de vulnerabilidades en imágenes.
4. Diseñar pipelines de Integración y Entrega Continua (CI/CD) con escaneos automatizados de dependencias (*Software Supply Chain Security*).

---

## 📚 Estructura Temática Planificada

### 6.6.1 Gestión de Secretos y Configuración Externa
* Los 12 Factores de las Aplicaciones Modernas (Factor III: Configuración almacenada en el entorno).
* Riesgos críticos de exponer llaves privadas, cadenas de conexión y tokens en GitHub/GitLab:
  * Herramientas de detección de secretos en commits: `git-secrets`, `trufflehog` y `gitleaks`.
  * Procedimiento de rotación inmediata de credenciales comprometidas.
* Almacenamiento seguro en la nube: Azure Key Vault, AWS Secrets Manager y Parameter Store.

### 6.6.2 Hardening de Imágenes y Contenedores Docker
* El peligro de ejecutar contenedores como usuario `root`:
  * Riesgo de escape de contenedor (*Container Breakout*) hacia el kernel anfitrión.
  * Directiva obligatoria en Dockerfile: creación y conmutación a usuario sin privilegios (`USER appuser`).
* Selección de imágenes base seguras:
  * De imágenes pesadas y vulnerables (`ubuntu:latest`) hacia imágenes mínimas depuradas (**Eclipse Temurin Alpine** o **GoogleContainerTools Distroless**).
* Principio de solo lectura (*Read-Only Root Filesystem*): `--read-only` con montajes temporales `tmpfs`.

### 6.6.3 Seguridad en la Cadena de Suministro (Supply Chain Security)
* Análisis de dependencias de terceros: Identificación de CVEs (*Common Vulnerabilities and Exposures*) en bibliotecas Maven y paquetes NPM.
* Herramientas de auditoría automatizada en compilación:
  * `mvn dependency-check:check` (OWASP Dependency-Check).
  * `npm audit` y Snyk.
  * Escaneo de capas de imagen con **Trivy** o **Docker Scout**.

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Detección y Limpieza de Secretos con GitLeaks:** Escaneo de un repositorio simulado con claves expuestas y eliminación del historial con `git-filter-repo`.
* **Dockerfile Multi-Stage Hardened para Spring Boot:** Construcción de un contenedor Java 21 que corre bajo usuario `appuser`, sin shell (`distroless`), con memoria acotada y validación de salud (*HEALTHCHECK*).
* **Escaneo de Vulnerabilidades con Trivy:** Análisis de un contenedor vulnerable y remediación de paquetes del sistema operativo hasta alcanzar cero vulnerabilidades críticas.

---

## 📖 Referencias y Estándares Oficiales

* Center for Internet Security (CIS). (2024). *CIS Docker Benchmark v1.6.0*.
* National Institute of Standards and Technology. (2017). *Application Container Security Guide* (SP 800-190).
* Wiggins, A. (2017). *The Twelve-Factor App*. https://12factor.net/
