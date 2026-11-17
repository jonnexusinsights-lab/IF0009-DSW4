![UCR Banner](../../../../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Examen Parcial II: Plataforma de Comercio Electrónico ShopSecure

## Ficha Tecnica del Examen

* **Fecha de Aplicacion:** Miercoles 2 de Diciembre, 2026
* **Horario:** 1:00 PM a 4:30 PM (13:00 a 16:30)
* **Duracion Maxima:** 3 horas y 30 minutos (210 minutos)
* **Ponderacion:** 20% de la nota final del curso
* **Puntaje Total:** 100 puntos
* **Modalidad:** Presencial (Laboratorio de Computo 3) - Estrictamente Individual
* **Entornos de Evaluacion:**
  * **Parte 1 (40 pts):** Cuestionario de Seleccion Unica en Mediacion Virtual (Teoria y Teoria Aplicada).
  * **Parte 2 (60 pts):** Desarrollo Full-Stack y Remediacion Defensiva en Repositorio GitHub.

---

## Instrucciones Generales y Normativa del Examen

1. **Trabajo Estrictamente Individual:** La prueba evalua el desempeno personal y autonomo. No se permite comunicacion entre estudiantes.
2. **Prohibicion Absoluta de Inteligencia Artificial:** Queda totalmente prohibido el uso de herramientas de IA generativa (ChatGPT, GitHub Copilot, Claude, Gemini, DeepSeek o similares). El uso de asistentes de codigo sera calificado con nota cero (0) y remitido a comision disciplinaria.
3. **Parte 1 (Seleccion Unica - 40 Puntos):** Cada pregunta presenta cuatro opciones de respuesta (A, B, C, D) de las cuales **unicamente una es correcta**. Marque o seleccione la opcion correspondiente en la plataforma Mediacion Virtual.
4. **Parte 2 (Desarrollo Practico - 60 Puntos):** Es obligatorio utilizar la plantilla base provista en `web_app_exam`, realizar commits semanticos por cada requerimiento completado y subir el proyecto a su cuenta de GitHub antes de las 16:30.
5. **Distribucion del Tiempo Sugerida:**
   * Parte 1 (Cuestionario Seleccion Unica): 40 minutos.
   * Parte 2 (Codificacion y Remediacion Guiada): 160 minutos.
   * Revision final y entrega: 10 minutos.

---

## Tabla de Ponderacion y Distribucion de Puntos

| Seccion | Componente Evaluado | Formato / Entorno | Puntos |
| :--- | :--- | :--- | :---: |
| **Parte 1** | Teoria y Teoria Aplicada (Movil, OWASP, Despliegue) | Seleccion Unica / Moodle | **40 pts** |
| **Parte 2A** | Backend Spring Boot 3 & Persistencia JPA Segura | Codigo en Vivo / GitHub | **25 pts** |
| **Parte 2B** | Frontend Angular 19 Standalone UI & Interceptor | Codigo en Vivo / GitHub | **20 pts** |
| **Parte 2C** | Remediacion Forense y Hardening Defensivo OWASP | Codigo en Vivo / GitHub | **15 pts** |
| **Total** | **Evaluacion Sumativa del Examen Parcial II** | | **100 pts** |

---

## PARTE 1: Teoria y Teoria Aplicada (40 Puntos)

**Modalidad:** Seleccion Unica en Mediacion Virtual (10 items tecnicos de 4 opciones).  
Seleccione la unica opcion que responde correctamente a cada enunciado.

---

### Modulo Movil: Flutter y Arquitectura Reactiva (15 Puntos)

#### Item 1 (3 puntos): Jerarquia de Arboles y Rendimiento en Flutter
Cual es la funcion que desempena cada uno de los tres arboles (*Widget Tree*, *Element Tree* y *RenderObject Tree*) en Flutter y como se optimiza el rendimiento grafico?

* **A)** Los Widgets son descripciones declarativas e inmutables de la UI; los Elements gestionan el ciclo de vida y el estado; los RenderObjects calculan el tamano y pintan en pantalla. Flutter optimiza el rendimiento reutilizando los RenderObjects existentes cuando unicamente cambian los datos.
* **B)** Los Widgets compilan directamente a codigo C++; los Elements son los hilos de ejecucion del sistema operativo; los RenderObjects son controladores de la GPU.
* **C)** Los tres arboles son copias de respaldo identicas almacenadas en memoria RAM para evitar caidas de la aplicacion en Android y iOS.
* **D)** El Widget Tree se ejecuta en el navegador web; el Element Tree reside en el servidor remoto; y el RenderObject Tree almacena los datos en SQLite.

---

#### Item 2 (4 puntos): Ciclo de Vida y Fuga de Memoria en Flutter
Considere el siguiente fragmento de codigo de un `StatefulWidget` en Flutter:

```dart
class SensorMonitorState
    extends State<SensorMonitor> {
  StreamSubscription? _sub;
  int _lecturas = 0;

  @override
  void initState() {
    super.initState();
    _sub = sensorStream.listen((dato) {
      setState(() {
        _lecturas++;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text("Lecturas: $_lecturas");
  }
}
```

Cual es el defecto critico de ciclo de vida presente en esta clase y cual es su solucion tecnica?

* **A)** Hay una fuga de memoria (*memory leak*) porque no se cancela la suscripcion al destruir la vista. Se soluciona implementando el metodo `dispose()` y ejecutando `_sub?.cancel()`.
* **B)** El error radica en llamar a `super.initState()`; los Streams deben inicializarse unicamente en el constructor de la clase.
* **C)** El recolector de basura de Dart cancela de forma automatica todos los Streams abiertos al salir de la pantalla, por lo que no existe ningun defecto.
* **D)** El defecto se debe a que la variable `_lecturas` debe ser declarada como `final` para que Flutter la actualice sin llamar a `setState()`.

---

#### Item 3 (4 puntos): Persistencia Offline-First y Almacenamiento Seguro
En aplicaciones moviles empresariales con persistencia local en SQLite (mediante `sqflite` en Flutter):
1. Para que se utilizan los metodos `toMap()` y `fromMap()`?
2. Donde deben guardarse los tokens de autenticacion JWT confidenciales?

* **A)** `toMap()` serializa objetos Dart a mapas para guardarlos en SQLite, y `fromMap()` reconstruye objetos Dart desde registros de la base de datos. Los tokens JWT deben guardarse cifrados mediante `flutter_secure_storage` (Keystore en Android / Keychain en iOS).
* **B)** `toMap()` y `fromMap()` se utilizan para ubicar coordenadas GPS en mapas satelitales. Los tokens JWT deben guardarse en un archivo de texto plano `.txt`.
* **C)** Los metodos `toMap()` y `fromMap()` sirven para enviar correos electronicos; los tokens deben guardarse quemados en el codigo fuente.
* **D)** SQLite cifra todas las tablas por defecto con contrasena maestra, por lo que no se requiere ninguna libreria de almacenamiento seguro.

---

#### Item 4 (4 puntos): Pruebas de Widgets (pump vs pumpAndSettle)
Al implementar pruebas automatizadas de interfaz con `WidgetTester` en Flutter, cual es la diferencia tecnica entre `tester.pump()` y `tester.pumpAndSettle()`?

* **A)** `tester.pump()` avanza el reloj simulado un frame unico (o un tiempo fijo); mientras que `tester.pumpAndSettle()` avanza frames continuamente hasta que no queden animaciones o transiciones pendientes en la pantalla.
* **B)** `tester.pump()` funciona solo en telefonos Android; mientras que `tester.pumpAndSettle()` funciona solo en telefonos iPhone.
* **C)** `tester.pump()` reinicia la base de datos; mientras que `tester.pumpAndSettle()` apaga el emulador al terminar las pruebas.
* **D)** Son dos nombres identicos para la misma instruccion, introducidos unicamente por razones de compatibilidad historica.

---

### Modulo Ciberseguridad: OWASP Top 10 Web y Movil (15 Puntos)

#### Item 5 (3 puntos): Categorias de Vulnerabilidades OWASP
Empareje las siguientes situaciones con su categoria oficial de OWASP:
1. Concatenar entradas de texto del usuario directamente en sentencias SQL.
2. Permitir que un usuario vea pedidos de otros cambiando el ID en la URL.
3. Dejar contrasenas maestras o llaves de API escritas dentro del codigo de la app.

* **A)** 1: Inyeccion (A03:2021); 2: Control de Acceso Roto / IDOR (A01:2021); 3: Almacenamiento Inseguro / Fallas Criptograficas (M09 / A02).
* **B)** 1: Configuracion Insegura (A05); 2: Inyeccion (A03); 3: Ataque de Red (M01).
* **C)** 1: Control de Acceso (A01); 2: Falla Criptografica (A02); 3: Registro Insuficiente (A09).
* **D)** 1: Desbordamiento de Memoria; 2: Suplantacion de Identidad; 3: Fallo de Hardware.

---

#### Item 6 (4 puntos): Inyeccion SQL (SQLi) y Consultas Seguras
Dado el siguiente codigo vulnerable en un servicio Spring Boot:

```java
String sql = "SELECT * FROM PRODUCTOS " +
             "WHERE NOMBRE LIKE '%" +
             filtro + "%'";
Query q = em.createNativeQuery(sql);
```

Cual es el riesgo de seguridad de este diseno y como se soluciona en Spring Data JPA?

* **A)** Un atacante puede inyectar sentencias como `' UNION SELECT ...` para robar datos confidenciales de otras tablas. Se soluciona usando `@Query` con JPQL y parametros nombrados (`:termino`), que tratan la entrada como dato puro y no como comando ejecutable.
* **B)** El servidor se apaga por sobrecalentamiento. Se soluciona cambiando la base de datos a formato de hoja de calculo Excel.
* **C)** No existe riesgo si el usuario escribe nombres cortos. Se soluciona limitando el campo de busqueda a 5 letras.
* **D)** El riesgo es que los productos se borren solos. Se soluciona agregando un `try-catch` que capture excepciones generales.

---

#### Item 7 (4 puntos): Control de Acceso Roto (IDOR / BOLA)
El endpoint `GET /api/ordenes/{id}` devuelve los datos del pedido buscando unicamente por ID numerico en la base de datos:
Por que es peligroso y como debe corregirse en el servicio?

* **A)** Es peligroso porque cualquier usuario con sesion puede ver ordenes ajenas con solo cambiar el numero en la URL (IDOR). Se corrige verificando en el servicio que la orden pertenezca al usuario autenticado (segun su token JWT) o que tenga rol ADMIN, lanzando 403 Forbidden si no coincide.
* **B)** Es peligroso porque los numeros consumen mas ancho de banda que las letras. Se corrige usando letras aleatorias en la ruta.
* **C)** No es peligroso porque los pedidos son informacion publica en todas las aplicaciones web comerciales.
* **D)** Se corrige cambiando el metodo de GET a DELETE para que los usuarios no puedan leer informacion.

---

#### Item 8 (4 puntos): Cross-Site Scripting (XSS) y Sanitizacion en Angular
En un componente Angular, el programador escribio:

```typescript
this.notasHtml = this.sanitizer
  .bypassSecurityTrustHtml(orden.notasEntrega);
```

y en la vista HTML coloco: `<div [innerHTML]="notasHtml"></div>`.
Cual es la vulnerabilidad generada y como se remedia?

* **A)** Se desactiva la proteccion automatica de Angular contra scripts maliciosos, permitiendo que un atacante inyecte codigo JavaScript que se ejecute en el navegador de otros usuarios (Stored XSS). Se remedia quitando el bypass y usando la interpolacion normal `{{ orden.notasEntrega }}`.
* **B)** Provoca que la base de datos Spring Boot borre la tabla de clientes. Se remedia reiniciando el servidor web.
* **C)** Angular no compila si se usa `bypassSecurityTrustHtml`. Se remedia renombrando la variable a `notasSeguras`.
* **D)** Los navegadores bloquean todos los ataques XSS automaticamente, por lo que este codigo es 100% seguro y recomendado.

---

### Modulo Despliegue y Publicacion: Web y Movil (10 Puntos)

#### Item 9 (5 puntos): Despliegue Web, Nginx y Certificados SSL/TLS
Al poner en produccion una aplicacion con Frontend en Angular y Backend en Spring Boot:
1. Cual es la funcion principal de Nginx como proxy inverso?
2. Cual es la diferencia entre el bundle de Angular y el servicio Spring Boot?
3. Para que sirve el protocolo HTTPS (TLS)?

* **A)** Nginx recibe las peticiones en el puerto 443 con HTTPS, sirve los archivos estaticos de Angular directamente y reenvia las peticiones `/api` a Spring Boot (8080); Spring Boot corre como un servicio continuo de fondo (`systemd`); HTTPS cifra los datos en transito entre el navegador y el servidor.
* **B)** Nginx es la base de datos relacional del sistema; Angular procesa las transacciones bancarias; y HTTPS solo sirve para conectar impresoras en red.
* **C)** Nginx apaga los servidores por las noches; Angular se ejecuta en Java 21; y TLS solo protege mensajes de WhatsApp.
* **D)** Spring Boot debe compilarse dentro del navegador web de cada cliente; y Angular corre en la terminal de Linux como demonio de base de datos.

---

#### Item 10 (5 puntos): Firma Digital con Keystore y Publicacion AAB
En la preparacion de una app movil para publicarla en Google Play Store:
1. Que es el archivo `keystore` y la herramienta `keytool`?
2. Por que se utiliza el formato Android App Bundle (`.aab`) en lugar del `.apk` tradicional?

* **A)** `keytool` y el `keystore` permiten crear y guardar la llave criptografica privada para firmar digitalmente la aplicacion y certificar que no ha sido alterada. El formato `.aab` permite a Google Play entregar paquetes mas livianos adaptados al procesador y pantalla de cada usuario (*Dynamic Delivery*).
* **B)** El archivo `keystore` es la lista de usuarios y contrasenas de la app. El formato `.aab` sirve exclusivamente para televisores inteligentes.
* **C)** La firma digital sirve para cambiar el icono de la aplicacion en el menu. El formato `.apk` ya no existe en ningun sistema operativo.
* **D)** `keytool` es un antivirus para celulares; y `.aab` es un archivo de audio para musica de fondo en la aplicacion.

---

## PARTE 2: Desarrollo Full-Stack y Remediacion Defensiva (60 Puntos)

### Caso de Estudio: ShopSecure E-Commerce

La empresa **ShopSecure** requiere completar y asegurar su plataforma web de pedidos de suministros tecnologicos:
* **Backend:** Spring Boot 3.3.4, Java 21, JPA, H2 en memoria (`jdbc:h2:mem:insecureshop_db`).
* **Frontend:** Angular 19 Standalone Components, Router, Signals y HttpClient.

Usted trabajara sobre la plantilla base provista en la carpeta `web_app_exam`. Su labor es completar los requerimientos guiados identificados con comentarios `// TODO: [Examen II - Ítem X]`.

---

### Informacion de Acceso y Credenciales Pre-sembradas

* **Backend API Base:** `http://localhost:8080/api`
* **Consola H2:** `http://localhost:8080/h2-console` (JDBC URL: `jdbc:h2:mem:insecureshop_db`, Usuario: `sa`, Clave: en blanco)
* **Frontend Angular:** `http://localhost:4200/`

| Usuario | Contrasena en Claro | Rol | ID |
| :--- | :--- | :--- | :---: |
| `carlos.mora` | `ClaveSegura2026!` | `CLIENTE` | 1 |
| `maria.solano` | `MariaPass2026*` | `CLIENTE` | 2 |
| `alejandro.vega` | `Alejandro2026#` | `CLIENTE` | 3 |
| `lucia.ramirez` | `LuciaKey2026$` | `CLIENTE` | 4 |
| `admin.tienda` | `AdminRoot2026#` | `ADMIN` | 5 |

---

### Requerimientos Tecnicos de la Parte 2

#### Requerimiento 1 (10 pts): Autenticacion Criptografica con BCrypt
* **Ubicacion:** `SecurityConfig.java` y `AuthService.java`
* **Tarea 1.1:** En `SecurityConfig.java`, declare e instancie el bean `PasswordEncoder` retornando `new BCryptPasswordEncoder(12)`.
* **Tarea 1.2:** En `AuthService.java`, sustituya la validacion en texto plano por `passwordEncoder.matches(request.getPassword(), usuario.getPassword())`.
* **Criterio de Exito:** El login debe autenticar exitosamente a los usuarios utilizando las claves pre-sembradas en `data.sql` hasheadas con BCrypt.

#### Requerimiento 2 (15 pts): Busqueda Segura con JPQL Parametrizado (Inmunidad SQLi)
* **Ubicacion:** `ProductoRepository.java`, `ProductoService.java` y `ProductoController.java`
* **Tarea 2.1:** En `ProductoRepository`, declare el metodo seguro con `@Query`:
  ```java
  @Query("SELECT p FROM Producto p WHERE " +
         "LOWER(p.nombre) " +
         "LIKE LOWER(CONCAT('%', :termino, '%')) " +
         "OR LOWER(p.descripcion) " +
         "LIKE LOWER(CONCAT('%', :termino, '%'))")
  List<Producto> buscarPorTermino(
      @Param("termino") String termino);
  ```
* **Tarea 2.2:** En `ProductoService`, invoque el repositorio y mapee la lista de resultados a DTO:
  ```java
  return productoRepository
      .buscarPorTermino(termino)
      .stream()
      .map(this::toDto)
      .collect(Collectors.toList());
  ```
* **Criterio de Exito:** Al buscar terminos que incluyan comillas o vectores como `' OR '1'='1`, el sistema busca el texto literal sin alterar la semantica de la base de datos.

#### Requerimiento 3 (10 pts): Interceptor HTTP en Angular (Inyeccion Bearer)
* **Ubicacion:** `frontend/src/app/interceptors/auth.interceptor.ts` (ya pre-registrado en `app.config.ts`)
* **Tarea:** Complete la logica funcional en `auth.interceptor.ts`:
  ```typescript
  export const authInterceptor: HttpInterceptorFn =
      (req, next) => {
    const authService = inject(AuthService);
    const token = authService.getToken();

    if (token) {
      req = req.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`
        }
      });
    }
    return next(req);
  };
  ```
* **Criterio de Exito:** Las peticiones salientes hacia `/api/ordenes` incluyen el encabezado `Authorization: Bearer <token>`.

#### Requerimiento 4 (10 pts): Componente Reactivo y Formularios en Angular
* **Ubicacion:** `frontend/src/app/components/catalogo/` y `checkout/`
* **Tarea 4.1:** Verifique que agregar productos desde el catalogo actualice el estado del carrito reactivo en `CheckoutComponent`.
* **Tarea 4.2:** Asegure que el boton de confirmacion de orden se deshabilite si el carrito esta vacio o si la direccion de despacho esta en blanco.
* **Criterio de Exito:** Al hacer clic en "Confirmar y Pagar", se invoca la API y se redirige al comprobante de compra.

#### Requerimiento 5 (10 pts): Control de Acceso Horizontal (Mitigacion IDOR / BOLA)
* **Ubicacion:** `service/OrdenService.java` (`OrdenController.java` ya extrae el `usuarioId` y `rol` del token)
* **Tarea:** En `OrdenService.obtenerPorIdSeguro(id, usuarioAutenticadoId, rolAutenticado)` implemente la regla defensiva:
  ```java
  boolean esAdmin = "ADMIN".equalsIgnoreCase(
      rolAutenticado);
  boolean esPropietario =
      orden.getUsuario().getId()
      .equals(usuarioAutenticadoId);

  if (!esAdmin && !esPropietario) {
      throw new AccesoDenegadoException(
          "Acceso denegado: orden ajena");
  }
  ```
* **Criterio de Exito:** Un usuario autenticado unicamente puede ver sus propias ordenes. Al consultar el ID de un pedido ajeno, el backend deniega el acceso con HTTP 403 Forbidden.

#### Requerimiento 6 (5 pts): Hardening A05 y Manejo Global RFC 7807
* **Ubicacion:** `application.properties` y `GlobalExceptionHandler.java`
* **Tarea 6.1:** En `application.properties`, configure `server.error.include-stacktrace=never` y `server.error.include-exception=false`.
* **Tarea 6.2:** En `GlobalExceptionHandler.java`, configure el manejador para `AccesoDenegadoException` retornando `ProblemDetail` con `HttpStatus.FORBIDDEN`.
* **Criterio de Exito:** Al recibir un error de autorizacion o interno, la respuesta JSON cumple el estandar RFC 7807 sin mostrar trazas de error de la JVM.

---

## Rubrica Analitica de Calificacion (100 Puntos)

| Seccion | Criterio de Evaluacion | Puntaje |
| :--- | :--- | :---: |
| **Parte 1** | **Teoria y Teoria Aplicada en Mediacion Virtual (Seleccion Unica)** | **40 pts** |
| 1.1 | Dominio conceptual y analisis en Flutter (Items 1 al 4) | 15 pts |
| 1.2 | Analisis forense y defensivo OWASP Web y Movil (Items 5 al 8) | 15 pts |
| 1.3 | Arquitectura de despliegue, Nginx, TLS y publicacion AAB (Items 9 y 10) | 10 pts |
| **Parte 2** | **Desarrollo Practico Full-Stack y Remediacion Guiada** | **60 pts** |
| 2.1 | Requerimiento 1: Bean PasswordEncoder y verificacion BCrypt en AuthService | 10 pts |
| 2.2 | Requerimiento 2: Consulta JPQL segura con @Query, parametros y DTOs | 15 pts |
| 2.3 | Requerimiento 3: Interceptor HTTP funcional con inyeccion de token Bearer | 10 pts |
| 2.4 | Requerimiento 4: Componente reactivo, validaciones de formulario y checkout | 10 pts |
| 2.5 | Requerimiento 5: Validacion estricta de titularidad contra IDOR/BOLA (403) | 10 pts |
| 2.6 | Requerimiento 6: Supresion de stacktrace y manejo RFC 7807 (ProblemDetail) | 5 pts |
| **Total** | **Calificacion Final Sumativa del Examen** | **100 pts** |

---

## Procedimiento de Entrega

1. **Parte 1 (Mediacion Virtual):** Complete el cuestionario oficial de seleccion unica antes de finalizar los primeros 40 minutos.
2. **Parte 2 (Repositorio GitHub):**
   * Realice el commit final con el mensaje: `build: entrega examen parcial II - <Nombre_Estudiante>`.
   * Realice `git push origin main` a su repositorio personal de GitHub.
   * Pegue el enlace publico a su repositorio en el buzon de entrega de Mediacion Virtual antes de las 16:30.
