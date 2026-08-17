# Hoja de Referencia: Apache Maven

Esta guía rápida resume la estructura de directorios, el ciclo de vida y los comandos principales de Apache Maven.

---

## Estructura Estándar de Directorios

Maven impone una estructura uniforme para organizar los archivos del proyecto:

```text
proyecto/
├── pom.xml                  # Archivo de configuración central
└── src/                     # Código fuente y recursos
    ├── main/                # Recursos de producción
    │   ├── java/            # Clases e interfaces (.java)
    │   └── resources/       # Configuraciones y archivos públicos
    └── test/                # Recursos de pruebas unitarias
        ├── java/            # Clases de prueba (.java)
        └── resources/       # Datos de prueba
```

---

## Ciclo de Vida del Build (Lifecycle Phases)

Cada comando ejecuta la fase indicada y todas las fases predecesoras en orden:

1. **`clean`**: Elimina el directorio `target/` con compilaciones previas.
2. **`validate`**: Verifica que el proyecto esté correcto y la información esté disponible.
3. **`compile`**: Traduce el código fuente `.java` a archivos binarios `.class`.
4. **`test`**: Ejecuta las pruebas unitarias mediante frameworks (ej. JUnit).
5. **`package`**: Empaqueta el código compilado en un formato distribuible (JAR, WAR).
6. **`install`**: Instala el paquete resultante en el repositorio local local.
7. **`deploy`**: Copia el paquete final al repositorio remoto para compartir.

---

## Comandos Comunes en Consola

Ejecute los siguientes comandos en la raíz del proyecto (donde reside el `pom.xml`):

```bash
# Limpiar el proyecto y compilar las clases
mvn clean compile

# Ejecutar las pruebas unitarias
mvn test

# Compilar y empaquetar el proyecto en un archivo JAR
mvn package

# Instalar el JAR en el repositorio local (~/.m2)
mvn clean install

# Analizar e imprimir el árbol de dependencias
mvn dependency:tree
```

---

## Ejecución del Proyecto mediante Plugins

Si configuró el plugin `exec-maven-plugin` o desea lanzar una clase principal:

```bash
# Ejecutar una clase Java específica con Maven
mvn exec:java \
  -Dexec.mainClass="cr.ac.ucr.paraiso.ie.carnet.practica1.AppServer"
```
