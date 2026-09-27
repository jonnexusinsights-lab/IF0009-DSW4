![UCR Banner](../../../../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Guía de Ejecución y Verificación: MedTriage Express (Examen Parcial I)

Esta guía contiene las instrucciones paso a paso para ejecutar y verificar el proyecto del **Examen Parcial I: MedTriage Express**, abarcando tanto la API RESTful back-end en **Spring Boot 3** como el cliente SPA front-end en **Angular 19 Standalone**.

---

## 📋 Requisitos Previos del Entorno

Antes de iniciar la ejecución, verifique que su computadora cuente con las siguientes herramientas instaladas:

* **Java Development Kit (JDK):** Versión 17 o superior.
* **Apache Maven:** Versión 3.8+ (o el wrapper `mvnw` incluido en el proyecto).
* **Node.js:** Versión 18+ o 20+ LTS.
* **Angular CLI:** Versión 19.x (`npm install -g @angular/cli`).
* **Visual Studio Code:** Con el paquete de extensiones *Extension Pack for Java*.

---

## 🚀 Paso 1: Configuración e Inicialización de la Base de Datos

Dependiendo de la modalidad de examen asignada en su laboratorio, siga la opción correspondiente:

### Opción A: Motor SQL Server (Modalidad Estándar)

1. Abra **SQL Server Management Studio (SSMS)** o Azure Data Studio.
2. Ejecute el script DDL y de datos semilla provisto en el enunciado (`schema.sql`):
   ```sql
   CREATE DATABASE MedTriageDB_SuCarnet;
   GO
   ```
3. Verifique que la base de datos `MedTriageDB_SuCarnet` contenga las tablas `Doctor`, `Paciente` y `CitaMedica`.

---

### Opción B: Base de Datos H2 en Memoria (Modalidad Sin DBMS Local)

1. No requiere instalar ni ejecutar ningún motor SQL Server.
2. Verifique que el archivo `src/main/resources/application.properties` en `medtriage-backend` contenga:
   ```properties
   spring.datasource.url=jdbc:h2:mem:medtriagedb;DB_CLOSE_DELAY=-1
   spring.datasource.driverClassName=org.h2.Driver
   spring.datasource.username=sa
   spring.datasource.password=
   spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
   spring.jpa.hibernate.ddl-auto=none
   spring.h2.console.enabled=true
   spring.sql.init.mode=always
   ```
3. Los scripts `schema.sql` y `data.sql` en `src/main/resources/` crearán y poblarán las tablas automáticamente al iniciar Spring Boot.

---

## ☕ Paso 2: Ejecución del Back-End (`medtriage-backend`)

Siga cualquiera de los siguientes dos procedimientos para iniciar el servidor RESTful en el puerto `8080`:

### Método 1: Desde la Terminal Integrada de VS Code (Recomendado)

1. Abra la terminal integrada en VS Code (**Terminal > New Terminal**).
2. Desplácese a la carpeta del backend:
   ```powershell
   cd medtriage-backend
   ```
3. Inicie la aplicación compilando con Maven:
   ```powershell
   mvn spring-boot:run
   ```

---

### Método 2: Desde el Editor de Código de VS Code

- [ ] Abra el archivo `src/main/java/com/medtriage/MedTriageApplication.java`.
- [ ] Presione la tecla `F5` o haga clic en el enlace flotante **`Run`** ubicado sobre la firma del método `main()`.

---

### 🔍 Verificación del Servidor Back-End

- **Prueba de API REST:** Abra su navegador e ingrese a [http://localhost:8080/api/v1/citas](http://localhost:8080/api/v1/citas). Deberá visualizar la lista de citas en formato JSON.
- **Consola H2 (Sólo Modalidad H2):** Ingrese a [http://localhost:8080/h2-console](http://localhost:8080/h2-console) con la URL JDBC `jdbc:h2:mem:medtriagedb` y usuario `sa`.

---

## 🅰️ Paso 3: Ejecución del Front-End (`medtriage-frontend`)

1. Abra una **nueva pestaña de terminal** en VS Code (haga clic en el ícono `+` del panel de la terminal).
2. Navegue a la carpeta del proyecto Angular:
   ```powershell
   cd medtriage-frontend
   ```

---

### ⚠️ Solución a Errores de Permisos en PowerShell Windows

Si al ejecutar comandos `npm` recibe el mensaje *"No se puede cargar el archivo npm.ps1 porque la ejecución de scripts está deshabilitada"*, aplique cualquiera de estas dos soluciones:

- **Solución A (Recomendada):** Habilite permisos temporales en la terminal actual de PowerShell ejecutando:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
- **Solución B:** Use directamente la extensión `.cmd`:
  ```powershell
  npm.cmd install
  npm.cmd start
  ```

---

### 🛠️ Instalación y Arranque del Cliente SPA

1. Instale los paquetes y dependencias necesarias:
   ```powershell
   npm install
   ```
2. Inicie el servidor de desarrollo de Angular:
   ```powershell
   ng serve
   ```
   *(O alternativamente: `npm start`)*.

3. Abra su navegador web en la dirección: [http://localhost:4200/citas](http://localhost:4200/citas).

---

## 🧪 Paso 4: Ejecución de Pruebas Unitarias

Para validar las pruebas unitarias creadas con JUnit 5 y Mockito en la capa de servicios del backend, ejecute el siguiente comando en la carpeta `medtriage-backend`:

```powershell
mvn test
```

Verifique en la salida de la consola que todas las pruebas en `CitaMedicaServiceTest` se hayan ejecutado con estado **BUILD SUCCESS** y 0 fallos.

---

## 📌 Checklist de Verificación Final del Examen

Antes de dar por concluida la prueba, revise el siguiente checklist:

- [ ] El backend responde correctamente en `http://localhost:8080/api/v1/citas`.
- [ ] La política CORS permite solicitudes provenientes de `http://localhost:4200`.
- [ ] El dashboard en `/citas` muestra la tabla de pacientes y doctores.
- [ ] El filtro de reactividad con Angular Signals (`TODAS`, `ALTA`, `MEDIA`, `BAJA`) actualiza la tabla dinámicamente.
- [ ] El formulario en `/nueva-cita` permite registrar citas y redirige automáticamente al dashboard.
- [ ] Se han realizado al menos 5 commits semánticos en el repositorio personal de GitHub.
