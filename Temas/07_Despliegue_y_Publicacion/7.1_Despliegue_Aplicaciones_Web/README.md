# Subtema 7.1: Despliegue de Aplicaciones Web: Empaquetado de Producción, Hosting, Proxies Inversos (Nginx), SSL/TLS y Docker

Este módulo estructura el ciclo de puesta en producción de sistemas web full-stack, abordando la optimización de activos para la web, la configuración de servidores y proxies inversos, la automatización de certificados HTTPS con Let's Encrypt y la orquestación contenerizada con Docker Compose.

---

## 🎯 Objetivos de Aprendizaje

1. Dominar los procesos de empaquetado y optimización para producción en aplicaciones Single Page Application (**Angular**) y servidores backend (**Spring Boot 3**).
2. Comprender la función arquitectónica de los **Servidores Web y Proxies Inversos** (Nginx / Apache), aplicando terminación SSL, balanceo de carga y reescritura de URLs para SPAs.
3. Configurar la resolución de dominios en el Sistema de Nombres de Dominio (**DNS**) y automatizar la emisión y renovación de certificados criptográficos **SSL/TLS con Let's Encrypt y Certbot**.
4. Diseñar e implementar arquitecturas de despliegue contenerizadas multi-contenedor mediante **Dockerfile Multi-Stage** y **Docker Compose** (Front-end Nginx + API Spring Boot + Base de Datos).

---

## 📚 Estructura Temática Planificada

### 7.1.1 Empaquetado y Optimización de Bundles para Producción
* **Front-End (Angular / Vite):**
  * Compilación AOT (*Ahead-Of-Time*) y eliminación de código muerto (*Tree Shaking*).
  * Minificación, ofuscación y compresión de activos estáticos (Gzip y Brotli).
  * Estrategias de división de código (*Code Splitting*) y carga diferida (*Lazy Loading* de rutas).
  * Cache busting mediante nombres de archivo basados en hashes (`main.[hash].js`).
* **Back-End (Spring Boot 3):**
  * Empaquetado en JAR ejecutable optimizado (`mvn clean package -DskipTests`).
  * Perfiles de Spring para producción (`spring.profiles.active=prod`).
  * Ajuste de parámetros de memoria de la JVM (`-Xms`, `-Xmx`, Garbage Collector G1).

### 7.1.2 Servidores Web y Proxies Inversos (Nginx)
* Diferencia fundamental entre Servidor Web de archivos estáticos y Proxy Inverso (*Reverse Proxy*).
* Arquitectura basada en eventos y alto rendimiento de Nginx.
* Configuración de enrutamiento SPA (`try_files $uri $uri/ /index.html =404`).
* Directiva `proxy_pass` hacia el servidor backend Spring Boot en puerto 8080.
* Bloques de balanceo de carga (*Load Balancing*: round-robin, least_conn, ip_hash).

### 7.1.3 Dominios, DNS y Certificados SSL/TLS (HTTPS)
* Registros DNS fundamentales: `A` (dirección IPv4), `AAAA` (IPv6), `CNAME` (alias de dominio) y `TXT` (validación de propiedad SPF/DKIM).
* La Autoridad Certificadora libre **Let's Encrypt** y el protocolo ACME.
* Automatización de certificados con **Certbot** (desafíos HTTP-01 y DNS-01, crontab para renovación automática).
* Configuración de cifrados modernos y redirección forzada de HTTP (puerto 80) a HTTPS (puerto 443).

### 7.1.4 Despliegue Contenerizado con Docker y Docker Compose
* **Dockerfile Multi-Stage:**
  * Etapa 1 (*Builder*): Node.js / Maven para compilar código fuente y generar bundles.
  * Etapa 2 (*Runner / Production*): Imagen mínima Nginx Alpine / Temurin JRE Alpine copiando únicamente los artefactos compilados.
  * Ventaja: Reducción del tamaño de la imagen final de 1.5 GB a menos de 50 MB y eliminación de herramientas de compilación en producción.
* **Orquestación con Docker Compose (`docker-compose.yml`):**
  * Definición de redes privadas internas (`bridge network`).
  * Persistencia de base de datos con volúmenes montados (`volumes`).
  * Secuencia ordenada de inicio y comprobación de salud (`depends_on` con `condition: service_healthy`).

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Stack Completo en Docker Compose:** Despliegue en un solo comando (`docker compose up -d`) de Angular 19 servido por Nginx, Spring Boot 3 conectado a base de datos y proxy reverso con SSL.
* **Configuración de Nginx desde Cero:** Redacción del archivo `nginx.conf` con compresión gzip, cabeceras de caché para archivos estáticos y proxy reverso para `/api/`.
* **Emisión de Certificado HTTPS Real:** Configuración de Certbot en un servidor en la nube con dominio público para alcanzar calificación A+ en SSL Labs.

---

## 📖 Referencias y Estándares Oficiales

* Docker Inc. (2024). *Docker Documentation: Multi-stage builds & Compose specification*.
* Nginx, Inc. (2024). *NGINX Reverse Proxy and Load Balancing Administration Guide*.
* Electronic Frontier Foundation (EFF). (2024). *Certbot: Automated SSL/TLS Certificates*.
