![UCR Banner](../../../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Quiz 9: Auditoría Forense de Vulnerabilidades Web (OWASP Top 10) en InsecureCare

**Puntuación Total:** 25 Puntos (5 Puntos por pregunta)  
**Tiempo Límite Estimado:** 35 - 45 minutos  
**Modalidad:** Evaluación Individual Práctica y Formativa / Sumativa  
**Escenario de Trabajo:** Aplicación Web `InsecureCare` ubicada en `web_apps/unsecure_web_app/`  
**Instrucciones:** Ejecute localmente el entorno de desarrollo multiraíz de la aplicación web médica `InsecureCare` (Backend Spring Boot en el puerto 8080 y Frontend Angular en el puerto 4200). Utilizando las herramientas de desarrollador del navegador (DevTools), comandos cURL o la interfaz de usuario, analice el código fuente y audite el comportamiento del sistema para responder a cada uno de los siguientes reactivos. Al concluir, complete la hoja de hallazgos (*Pentest Findings Sheet*) adjunta con las evidencias de explotación y propuestas de mitigación para su respectiva entrega y calificación.

---

## Cuestionario de Evaluación

### 1. Inventario y Cuantificación de Vulnerabilidades OWASP (5 Puntos)

Tras auditar exhaustivamente la arquitectura Full-Stack de la aplicación `InsecureCare` (revisando endpoints REST, persistencia JPA, configuración de Spring Boot y componentes Standalone en Angular), ¿cuál es la cantidad exacta de vulnerabilidades críticas del estándar **OWASP Top 10** deliberadamente implementadas en el sistema y cuál es su clasificación correspondiente?

- [ ] A) Existen exactamente **3** vulnerabilidades: Inyección SQL (A03), Desbordamiento de Búfer (A04) y Fallo de Cifrado en Disco (A02).
- [ ] B) Existen exactamente **5** vulnerabilidades: Broken Access Control / IDOR (A01), Fallos Criptográficos / Contraseñas en Texto Plano (A02), Inyección SQL (A03), Cross-Site Scripting Almacenado (A03) y Configuración de Seguridad Incorrecta / Fuga de Trazas (A05).
- [ ] C) Existen exactamente **2** vulnerabilidades: Cross-Site Scripting (XSS) y Denegación de Servicio Distribuida (DDoS) por falta de balanceador Nginx.
- [ ] D) Existen exactamente **7** vulnerabilidades: Ataque de Hombre en el Medio (MitM), Falsificación de Solicitudes del Servidor (SSRF), XML External Entity (XXE), Clickjacking, Broken Object Level Authorization, Memory Leak y Buffer Overflow.

---

### 2. Inyección SQL (SQLi) y Exfiltración de Registros Confidenciales (5 Puntos)

En la barra de búsqueda de diagnósticos clínicos del componente `ExpedienteListComponent`, un auditor de seguridad prueba evadir el filtro ingresando cadenas de control SQL en la URL:  
`GET /api/expedientes/buscar?termino=' OR '1'='1`

¿Por qué este vector de ataque tiene éxito en el servidor y cuál es la solución técnica estándar en Spring Data JPA para neutralizarlo definitivamente?

- [ ] A) El ataque tiene éxito porque H2 Database no admite claves foráneas; se soluciona migrando el backend a Oracle Database sin tocar el código Java.
- [ ] B) El ataque tiene éxito porque el servicio `ExpedienteService` concatena dinámicamente el parámetro del usuario en una consulta SQL nativa (`createNativeQuery`); se soluciona utilizando consultas parametrizadas con marcadores de posición (`:termino`) o métodos derivados de `JpaRepository`.
- [ ] C) El ataque tiene éxito porque el navegador envía los parámetros en texto claro mediante HTTP; se soluciona instalando un certificado SSL autofirmado en el puerto 4200 de Angular.
- [ ] D) El ataque tiene éxito debido a que la base de datos corre en memoria RAM; se neutraliza configurando `spring.datasource.username=root`.

---

### 3. Broken Access Control / Insecure Direct Object Reference (IDOR / BOLA) (5 Puntos)

El estudiante inicia sesión con las credenciales del paciente `carlos_mora` (Usuario ID: 3, asignado al Expediente #1). Al navegar a la vista de detalle, la URL del navegador muestra `/expediente/1`. Si el estudiante reemplaza manualmente la ruta por `/expediente/2`, ¿qué ocurre técnica y conceptualmente en la aplicación?

- [ ] A) El sistema lanza inmediatamente un error HTTP 403 Forbidden y bloquea la IP del cliente durante 24 horas por violación de políticas de seguridad.
- [ ] B) Se produce una vulnerabilidad de Broken Access Control (IDOR / BOLA) donde el paciente accede al expediente psiquiátrico confidencial de `maria_rojas`, debido a que `ExpedienteService.obtenerPorId()` busca directamente por clave primaria sin verificar que el `usuarioId` del recurso coincida con el usuario autenticado en la sesión.
- [ ] C) El servidor Angular redirige al usuario a la página de inicio porque el componente Standalone detecta la discrepancia en el árbol de enrutamiento mediante un `CanActivateFn`.
- [ ] D) La base de datos H2 se corrompe automáticamente al recibir una petición de lectura fuera del ámbito transaccional `@Transactional`.

---

### 4. Cross-Site Scripting (XSS Almacenado) y Bypass en Angular (5 Puntos)

En el registro de un nuevo expediente médico, un atacante ingresa el siguiente contenido en el campo de observaciones clínicas:
```html
<img src="invalido" 
     onerror="alert('XSS Detectado')">
```
Al visualizar dicho registro en `ExpedienteDetailComponent`, la ventana modal de alerta de JavaScript se ejecuta exitosamente en el navegador. ¿Cuál fue el fallo cometido en el código del Front-End que provocó la ejecución del payload?

- [ ] A) El desarrollador utilizó la directiva `[innerHTML]` invocando explícitamente `sanitizer.bypassSecurityTrustHtml()`, desactivando voluntariamente el motor de sanitización contextual nativo de Angular.
- [ ] B) Angular carece de defensas nativas contra XSS y requiere obligatoriamente instalar la librería externa jQuery para filtrar etiquetas peligrosas.
- [ ] C) El navegador web tiene deshabilitado el motor V8, provocando que las etiquetas `<img>` ejecuten scripts en el hilo de renderizado visual.
- [ ] D) El fallo ocurrió porque el archivo `index.html` no tiene configurado el atributo `lang="es"`.

---

### 5. Fallos Criptográficos y Fuga de Información Técnica (5 Puntos)

Durante la inspección de la base de datos mediante la consola `/h2-console` y al forzar un error de sintaxis SQL en la API, el equipo auditor observa dos violaciones críticas a la confidencialidad. ¿Cuáles son estas dos debilidades y qué directivas de configuración corrigen la fuga de información?

- [ ] A) El puerto 8080 está bloqueado por el firewall de Windows y la memoria JVM es insuficiente para procesar el garbage collector.
- [ ] B) Las contraseñas de los usuarios se almacenan en texto plano en la tabla `USUARIOS`, y el servidor tiene configurado `server.error.include-stacktrace=always`, lo cual expone la arquitectura interna y consultas SQL; se remedia implementando `BCryptPasswordEncoder` y configurando `server.error.include-stacktrace=never`.
- [ ] C) El servidor utiliza algoritmos cuánticos no estandarizados; se soluciona deshabilitando el protocolo HTTP 1.1 en `pom.xml`.
- [ ] D) La consola de H2 requiere autenticación biométrica y el backend rechaza peticiones JSON de Angular.

---

## Plantilla de Reporte de Hallazgos (Pentest Findings Sheet)

*Espacio para ser completado por el estudiante durante la sesión práctica de auditoría:*

| No. | Nombre del Hallazgo / Vulnerabilidad | Categoría OWASP Top 10 | Endpoint o Archivo Vulnerable | Evidencia / Payload de Explotación | Propuesta de Remediación |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | | | | | |
| **2** | | | | | |
| **3** | | | | | |
| **4** | | | | | |
| **5** | | | | | |
