# Subtema 5.2.4: Consumo de APIs RESTful (Spring Boot / JWT), Persistencia Local y Hardware

Este módulo aborda la comunicación cliente-servidor robusta, el almacenamiento persistente en disco del dispositivo y la interacción directa con los sensores físicos de hardware, garantizando arquitecturas móviles empresariales de alta disponibilidad.

---

## 📚 Estructura de Subtemas y Contenidos

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **5.2.4.1 Consumo APIs & JWT** | [5.2.4.1_Consumo_APIs_Spring_Boot_JWT.md](5.2.4.1_Consumo_APIs_Spring_Boot_JWT.md) | [Slides Markdown](5.2.4.1_Consumo_APIs_Spring_Boot_JWT_Slides.md) | [Presentación HTML Reveal.js](5.2.4.1_Consumo_APIs_Spring_Boot_JWT_Slides.html) |
| **5.2.4.2 Persistencia SQLite & Offline-First** | [5.2.4.2_Persistencia_Local_SQLite_Offline_First.md](5.2.4.2_Persistencia_Local_SQLite_Offline_First.md) | [Slides Markdown](5.2.4.2_Persistencia_Local_SQLite_Offline_First_Slides.md) | [Presentación HTML Reveal.js](5.2.4.2_Persistencia_Local_SQLite_Offline_First_Slides.html) |
| **5.2.4.3 Hardware: GPS, Cámara y Permisos** | [5.2.4.3_Integracion_Hardware_GPS_Camara_Permisos.md](5.2.4.3_Integracion_Hardware_GPS_Camara_Permisos.md) | [Slides Markdown](5.2.4.3_Integracion_Hardware_GPS_Camara_Permisos_Slides.md) | [Presentación HTML Reveal.js](5.2.4.3_Integracion_Hardware_GPS_Camara_Permisos_Slides.html) |

---

## 🎯 Competencias de Aprendizaje

1. **Integración Cliente-Servidor:** Consumo asíncrono de APIs RESTful en Spring Boot 3 mediante el paquete `http`, modelado de DTOs fuertemente tipados en Dart 3 y manejo resiliente de errores HTTP y timeouts.
2. **Seguridad Móvil con JWT:** Almacenamiento criptográfico de credenciales y tokens JWT en hardware nativo utilizando `flutter_secure_storage` (Android Keystore y Apple Keychain).
3. **Persistencia Local Relacional:** Manejo de bases de datos embebidas SQLite mediante `sqflite`, transacciones ACID, Singleton helpers y almacenamiento de preferencias con `shared_preferences`.
4. **Arquitectura Offline-First:** Implementación de sincronización bidireccional de datos con resolución de conflictos, colas de procesamiento y base de datos local como fuente de verdad.
5. **Acceso a Sensores Físicos:** Gestión de permisos en tiempo de ejecución en Android e iOS, captura de coordenadas satelitales con `geolocator`, fotografía digital con `image_picker` y transmisión multipart hacia el backend.
