# Subtema 7.2: Publicación de Aplicaciones Móviles: Firma Digital, Binarios (.aab/.ipa), Flavors y Tiendas Oficiales

Este módulo aborda la fase final de ingeniería de software móvil: la preparación, firma criptográfica, empaquetado binario y distribución de aplicaciones Flutter en las tiendas oficiales **Google Play Store** y **Apple App Store**.

---

## 🎯 Objetivos de Aprendizaje

1. Comprender el rol de la **Firma Digital Criptográfica** en la distribución móvil, garantizando la identidad del desarrollador y la integridad del paquete binario.
2. Generar y administrar almacenes de claves privadas (**Keystores**) en Android mediante la herramienta de línea de comandos `keytool`.
3. Compilar paquetes optimizados de distribución moderna: **Android App Bundle (`.aab`)** con Google Play Feature Delivery y paquetes de archivo **`.ipa`** para iOS.
4. Diseñar e implementar entornos de compilación múltiples (**Flavors en Android / Schemes en iOS**) para segregar configuraciones de desarrollo, pruebas y producción (`dev`, `staging`, `prod`).
5. Conocer los flujos de revisión, pruebas cerradas (**Google Play Internal Testing** / **Apple TestFlight**) y directrices de conformidad para la aprobación en tiendas.

---

## 📚 Estructura Temática Planificada

### 7.2.1 Firma Digital y Gestión de Claves en Android
* Principio de confianza: Por qué el sistema operativo móvil rechaza cualquier binario no firmado con certificado válido.
* Generación del almacén de claves con Java `keytool`:
  ```bash
  keytool -genkey -v -keystore upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
  ```
* Configuración segura de credenciales en `android/key.properties` y su referencia en `android/app/build.gradle` sin exponer contraseñas en Git.
* El servicio **Google Play App Signing**: Separación entre la clave de subida (*Upload Key*) y la clave de firmado del usuario final (*App Signing Key*).

### 7.2.2 Formatos de Distribución: APK vs Android App Bundle (AAB)
* Desventajas del APK tradicional universal (pesado, incluye recursos para todas las densidades de pantalla y arquitecturas de procesador).
* Arquitectura del **Android App Bundle (`.aab`)**:
  * Empaquetado de publicación obligatorio por Google Play desde agosto de 2021.
  * Generación dinámica de APKs divididos (*Split APKs*) en los servidores de Google: el usuario descarga únicamente los binarios correspondientes a su arquitectura específica (arm64-v8a, armeabi-v7a, x86_64) y resolución gráfica (hdpi, xxhdpi), reduciendo el tamaño de descarga hasta en un 50%.
* Comando de compilación optimizada:
  ```bash
  flutter build appbundle --release --obfuscate --split-debug-info=/<symbols-path>
  ```

### 7.2.3 Ecosistema Apple: Certificados, Perfiles y TestFlight
* El programa de desarrolladores de Apple (*Apple Developer Program*).
* Certificados de distribución (*Apple Distribution Certificate*), Identificadores de aplicación (*App ID*) y Perfiles de aprovisionamiento (*Provisioning Profiles*).
* Compilación en macOS con Xcode: creación del paquete Archive y exportación del archivo binario `.ipa`.
* Distribución beta con **TestFlight**: Pruebas internas (hasta 100 usuarios del equipo) y pruebas externas (hasta 10.000 evaluadores mediante enlace público).

### 7.2.4 Arquitectura de Entornos y Variantes (Flavors y Schemes)
* Por qué es un antipatrón cambiar manualmente las URLs de API antes de compilar para producción.
* Implementación de **Flavors en Flutter**:
  * Flavor `dev`: Icono con cinta "DEV", base de datos local / mock, `applicationIdSuffix: ".dev"`.
  * Flavor `staging`: Conexión a servidores de control de calidad (QA).
  * Flavor `prod`: Entorno productivo real con endpoint HTTPS oficial.
* Ejecución por línea de comandos: `flutter run --flavor dev -t lib/main_dev.dart`.

### 7.2.5 Directrices de Aprobación en Tiendas (Store Guidelines)
* Requisitos de privacidad y divulgación de datos (*Google Play Data Safety* y *Apple App Privacy Nutrition Labels*).
* Auditoría de políticas de consentimiento de usuario, supresión de cuentas y directrices de diseño (Google Play Policy y Apple App Store Review Guidelines).

---

## 🛠️ Casos Prácticos y Demostraciones Planificadas

* **Generación y Firma de un App Bundle Real:** Proceso paso a paso desde la creación del keystore hasta la generación del archivo `.aab` en la carpeta `build/app/outputs/bundle/release/`.
* **Configuración de Flavors Multi-Entorno:** Configuración de `build.gradle` en Android con `flavorDimensions` y tres puntos de entrada en Dart (`main_dev.dart`, `main_prod.dart`).
* **Ofuscación de Código en Flutter:** Compilación con `--obfuscate` para proteger el código Dart contra ingeniería inversa y lectura de símbolos.

---

## 📖 Referencias y Estándares Oficiales

* Google Developers. (2024). *About Android App Bundles & Play App Signing*.
* Apple Developer. (2024). *App Distribution and TestFlight Overview*.
* Flutter Documentation. (2024). *Build and release an Android app & Build and release an iOS app*.
