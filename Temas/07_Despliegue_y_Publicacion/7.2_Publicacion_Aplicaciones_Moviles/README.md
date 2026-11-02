# Subtema 7.2: Publicación de Aplicaciones Móviles: Firma Digital, Binarios (.aab/.ipa), Flavors y Tiendas Oficiales

Este módulo aborda la fase final de ingeniería de software móvil: la preparación, firma criptográfica, empaquetado binario y distribución de aplicaciones Flutter en las tiendas oficiales **Google Play Store** y **Apple App Store**.

---

## 📚 Estructura de Subtemas y Contenidos Generados

| Subtema | Lectura Teórica (ModeTheory) | Presentación Marp | Presentación Interactiva |
| :--- | :--- | :--- | :--- |
| **7.2.1 Firma Digital & Keystores Android** | [7.2.1_Firma_Digital_Gestion_Claves_Android.md](7.2.1_Firma_Digital_Gestion_Claves_Android.md) | [Slides Markdown](7.2.1_Firma_Digital_Gestion_Claves_Android_Slides.md) | [Presentación HTML Reveal.js](7.2.1_Firma_Digital_Gestion_Claves_Android_Slides.html) |
| **7.2.2 APK vs Android App Bundle (AAB)** | [7.2.2_Formatos_Distribucion_APK_vs_AAB.md](7.2.2_Formatos_Distribucion_APK_vs_AAB.md) | [Slides Markdown](7.2.2_Formatos_Distribucion_APK_vs_AAB_Slides.md) | [Presentación HTML Reveal.js](7.2.2_Formatos_Distribucion_APK_vs_AAB_Slides.html) |
| **7.2.3 Ecosistema Apple & TestFlight** | [7.2.3_Ecosistema_Apple_Certificados_TestFlight.md](7.2.3_Ecosistema_Apple_Certificados_TestFlight.md) | [Slides Markdown](7.2.3_Ecosistema_Apple_Certificados_TestFlight_Slides.md) | [Presentación HTML Reveal.js](7.2.3_Ecosistema_Apple_Certificados_TestFlight_Slides.html) |
| **7.2.4 Flavors Esenciales en Flutter (Dev/Prod)** | [7.2.4_Arquitectura_Entornos_Flavors_Esenciales.md](7.2.4_Arquitectura_Entornos_Flavors_Esenciales.md) | [Slides Markdown](7.2.4_Arquitectura_Entornos_Flavors_Esenciales_Slides.md) | [Presentación HTML Reveal.js](7.2.4_Arquitectura_Entornos_Flavors_Esenciales_Slides.html) |
| **7.2.5 Directrices de Tiendas (Data Safety)** | [7.2.5_Directrices_Aprobacion_Tiendas_Store_Guidelines.md](7.2.5_Directrices_Aprobacion_Tiendas_Store_Guidelines.md) | [Slides Markdown](7.2.5_Directrices_Aprobacion_Tiendas_Store_Guidelines_Slides.md) | [Presentación HTML Reveal.js](7.2.5_Directrices_Aprobacion_Tiendas_Store_Guidelines_Slides.html) |

---

## 🎯 Objetivos de Aprendizaje

1. Comprender el rol de la **Firma Digital Criptográfica** en la distribución móvil, garantizando la identidad del desarrollador y la integridad del paquete binario.
2. Generar y administrar almacenes de claves privadas (**Keystores**) en Android mediante la herramienta de línea de comandos `keytool`.
3. Compilar paquetes optimizados de distribución moderna: **Android App Bundle (`.aab`)** con Google Play Feature Delivery y paquetes de archivo **`.ipa`** para iOS.
4. Diseñar e implementar entornos de compilación múltiples (**Flavors en Android / Schemes en iOS**) para segregar configuraciones de desarrollo y producción (`dev` y `prod`).
5. Conocer los flujos de revisión, pruebas cerradas (**Google Play Internal Testing** / **Apple TestFlight**) y directrices de conformidad para la aprobación en tiendas.

---

## 📖 Referencias y Estándares Oficiales

* Google Developers. (2024). *About Android App Bundles & Play App Signing*. https://developer.android.com/distribute/play-services/app-signing
* Apple Developer. (2024). *App Distribution and TestFlight Overview*. https://developer.apple.com/testflight/
* Flutter Documentation. (2024). *Build and release an Android app & Build and release an iOS app*. https://docs.flutter.dev/deployment
