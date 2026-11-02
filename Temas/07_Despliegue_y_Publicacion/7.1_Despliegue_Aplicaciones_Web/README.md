# Subtema 7.1: Despliegue de Aplicaciones Web: Empaquetado de Producción, Hosting Estático/Dinámico, DNS/SSL y Servicios Cloud

Este módulo estructura el ciclo de puesta en producción de sistemas web full-stack, abordando la optimización de activos para la web, la configuración de servidores y hosting desacoplado, la automatización de certificados HTTPS con Let's Encrypt y la gestión de servicios productivos resilientes con systemd y plataformas Cloud PaaS.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **7.1.1 Empaquetado & Optimización** | [7.1.1_Empaquetado_Optimizacion_Bundles_Produccion.md](7.1.1_Empaquetado_Optimizacion_Bundles_Produccion.md) | [Slides Markdown](7.1.1_Empaquetado_Optimizacion_Bundles_Produccion_Slides.md) | [Presentación HTML Reveal.js](7.1.1_Empaquetado_Optimizacion_Bundles_Produccion_Slides.html) |
| **7.1.2 Hosting Estático & Dinámico** | [7.1.2_Servidores_Hosting_Estatico_Dinamico.md](7.1.2_Servidores_Hosting_Estatico_Dinamico.md) | [Slides Markdown](7.1.2_Servidores_Hosting_Estatico_Dinamico_Slides.md) | [Presentación HTML Reveal.js](7.1.2_Servidores_Hosting_Estatico_Dinamico_Slides.html) |
| **7.1.3 Dominios, DNS y Certificados SSL/TLS** | [7.1.3_Dominios_DNS_Certificados_SSL_TLS.md](7.1.3_Dominios_DNS_Certificados_SSL_TLS.md) | [Slides Markdown](7.1.3_Dominios_DNS_Certificados_SSL_TLS_Slides.md) | [Presentación HTML Reveal.js](7.1.3_Dominios_DNS_Certificados_SSL_TLS_Slides.html) |
| **7.1.4 Despliegue en Producción & Cloud PaaS** | [7.1.4_Despliegue_Produccion_Servicios_Cloud.md](7.1.4_Despliegue_Produccion_Servicios_Cloud.md) | [Slides Markdown](7.1.4_Despliegue_Produccion_Servicios_Cloud_Slides.md) | [Presentación HTML Reveal.js](7.1.4_Despliegue_Produccion_Servicios_Cloud_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Dominar los procesos de empaquetado y optimización para producción en aplicaciones Single Page Application (**Angular**) y servidores backend (**Spring Boot 3 con Java 25**).
2. Comprender la función arquitectónica de los **Servidores de Hosting Estático y Dinámico**, resolviendo el problema del error 404 en enrutamiento SPA y aplicando políticas defensivas de caché HTTP.
3. Configurar la resolución de dominios en el Sistema de Nombres de Dominio (**DNS**) y automatizar la emisión y renovación de certificados criptográficos **SSL/TLS con Let's Encrypt y Certbot**.
4. Diseñar e implementar servicios continuos y resilientes del sistema operativo con **`systemd`** y evaluar plataformas de despliegue administradas en la nube (**Cloud PaaS**).

---

## 📖 Referencias y Estándares Oficiales

* Angular Team. (2024). *Deployment Guide & Production Builds*. https://angular.dev/
* Spring Boot Team. (2024). *Production-ready Features & Systemd Service Deployment*. https://spring.io/projects/spring-boot
* Electronic Frontier Foundation (EFF). (2024). *Certbot: Automated SSL/TLS Certificates*. https://certbot.eff.org/
