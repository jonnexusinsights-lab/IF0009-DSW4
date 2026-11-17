![UCR Banner](../../../../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Examen Parcial II: Solucionario Analitico y Guia de Evaluacion

## Ficha Tecnica

* **Instrumento:** Solucionario Oficial y Criterios Periciales de Calificacion
* **Curso:** IF0009 - Desarrollo de Software IV (Ciclo II-2026)
* **Puntaje Total:** 100 puntos (Escala Sumativa: 20% de la nota final)
* **Poblacion Meta:** Docente y Asistentes Calificadores

---

## Solucionario Detallado: PARTE 1 (40 Puntos)

Modalidad: Seleccion Unica en Mediacion Virtual (10 items tecnicos).

---

### Modulo Movil: Flutter y Arquitectura Reactiva (15 Puntos)

#### Item 1 (3 puntos): Jerarquia de Arboles y Rendimiento en Flutter
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Los Widgets son descripciones declarativas e inmutables de la UI; los Elements gestionan el ciclo de vida y el estado; los RenderObjects calculan el tamano y pintan en pantalla. Flutter optimiza el rendimiento reutilizando los RenderObjects existentes cuando unicamente cambian los datos.*
* **Justificacion Analitica:** La arquitectura reactiva de Flutter separa deliberadamente la configuracion inmutable (`Widget Tree`), la gestion de ciclo de vida e identidad en memoria (`Element Tree`) y el pintado geometrico de bajo nivel (`RenderObject Tree`). Al reconstruir la interfaz tras una llamada a `setState()`, el `Element Tree` compara tipos y llaves para reutilizar los `RenderObjects` previamente asignados, minimizando el impacto en la GPU.
* **Analisis de Distractores:**
  * **B:** Falso. Los widgets no se compilan directamente a C++ ni los elements son hilos del sistema operativo.
  * **C:** Falso. No son copias de respaldo de memoria RAM ante caidas.
  * **D:** Falso. La triada de arboles opera localmente en el runtime de Flutter en el dispositivo movil.

---

#### Item 2 (4 puntos): Ciclo de Vida y Fuga de Memoria en Flutter
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Hay una fuga de memoria (memory leak) porque no se cancela la suscripcion al destruir la vista. Se soluciona implementando el metodo dispose() y ejecutando _sub?.cancel().*
* **Justificacion Analitica:** Una instancia activa de `StreamSubscription` conserva una referencia fuerte al objeto `State`. Si el usuario navega hacia atras y el widget se desmonta sin cancelar la suscripcion, el recolector de basura de Dart no puede liberar el objeto y la llamada a `setState()` sobre un estado desmontado provoca fallas en tiempo de ejecucion.
* **Codigo de Remediacion:**
```dart
@override
void dispose() {
  _sub?.cancel();
  super.dispose();
}
```
* **Analisis de Distractores:**
  * **B:** Falso. `super.initState()` es obligatorio y los Streams no se inicializan en constructores.
  * **C:** Falso. El Garbage Collector no cancela Streams reactivos automaticamente.
  * **D:** Falso. Declarar `final` no resuelve la gestion de eventos asincronos ni el ciclo de vida.

---

#### Item 3 (4 puntos): Persistencia Offline-First y Almacenamiento Seguro
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *toMap() serializa objetos Dart a mapas para guardarlos en SQLite, y fromMap() reconstruye objetos Dart desde registros de la base de datos. Los tokens JWT deben guardarse cifrados mediante flutter_secure_storage (Keystore en Android / Keychain en iOS).*
* **Justificacion Analitica:** SQLite requiere colecciones de pares clave-valor (`Map<String, dynamic>`) para ejecutar inserciones y lecturas estructuradas. Los metodos de serializacion `toMap()` y `fromMap()` desacoplan la persistencia relacional de las entidades Dart. Asimismo, dado que los archivos de SQLite residen en almacenamiento no cifrado por defecto, los tokens confidenciales deben alojarse en almacenamiento cifrado por hardware mediante `flutter_secure_storage`.
* **Analisis de Distractores:**
  * **B:** Falso. No tienen relacion con mapas geograficos ni se deben usar archivos de texto plano.
  * **C:** Falso. No envian correos ni se deben quemar credenciales en el codigo.
  * **D:** Falso. SQLite estandar no cifra las bases de datos por defecto.

---

#### Item 4 (4 puntos): Pruebas de Widgets (pump vs pumpAndSettle)
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *tester.pump() avanza el reloj simulado un frame unico (o un tiempo fijo); mientras que tester.pumpAndSettle() avanza frames continuamente hasta que no queden animaciones o transiciones pendientes en la pantalla.*
* **Justificacion Analitica:** `tester.pump()` avanza un intervalo discreto (un frame), mientras que `tester.pumpAndSettle()` ejecuta frames en bucle hasta que no queden tareas programadas ni animaciones en ejecucion. En flujos asincronos o transiciones de navegacion, `pump()` puede causar fallos de localizacion de widgets si la transicion no ha terminado.
* **Analisis de Distractores:**
  * **B:** Falso. Ambos metodos son multiplataforma en el entorno de pruebas de Flutter.
  * **C:** Falso. No interactuan con bases de datos ni apagan emuladores.
  * **D:** Falso. Poseen comportamientos de ejecucion y sincronizacion claramente distintos.

---

### Modulo Ciberseguridad: OWASP Top 10 Web y Movil (15 Puntos)

#### Item 5 (3 puntos): Categorias de Vulnerabilidades OWASP
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *1: Inyeccion (A03:2021); 2: Control de Acceso Roto / IDOR (A01:2021); 3: Almacenamiento Inseguro / Fallas Criptograficas (M09 / A02).*
* **Justificacion Analitica:**
  1. La concatenacion en consultas es el ejemplo arquetipico de **A03:2021 - Injection**.
  2. Modificar identificadores para ver registros privados ajenos corresponde a **A01:2021 - Broken Access Control** (IDOR).
  3. Secretos quemados en el codigo corresponden a **M09:2024 - Insecure Data Storage** y **A02:2021 - Cryptographic Failures**.
* **Analisis de Distractores:**
  * **B, C, D:** Confunden categorias de configuracion, registro o conceptos no pertinentes.

---

#### Item 6 (4 puntos): Inyeccion SQL (SQLi) y Consultas Seguras
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Un atacante puede inyectar sentencias como ' UNION SELECT ... para robar datos confidenciales de otras tablas. Se soluciona usando @Query con JPQL y parametros nombrados (:termino), que tratan la entrada como dato puro y no como comando ejecutable.*
* **Justificacion Analitica:** Concatenar parametros de entrada en sentencias nativas permite a un atacante inyectar operadores como `' UNION SELECT ...` para extraer datos de la tabla `USUARIOS`. La utilizacion de `@Query` con JPQL parametrizado delega en el motor ORM la preparacion de la consulta con parametros vinculados, neutralizando la inyeccion.
* **Analisis de Distractores:**
  * **B:** Falso. Cambiar a Excel destruye la arquitectura y no es una solucion de seguridad.
  * **C:** Falso. Limitar a 5 letras no previene inyecciones breves (`' OR 1=1--`).
  * **D:** Falso. Un bloque try-catch captura errores pero no detiene la inyeccion exitosa.

---

#### Item 7 (4 puntos): Control de Acceso Roto (IDOR / BOLA)
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Es peligroso porque cualquier usuario con sesion puede ver ordenes ajenas con solo cambiar el numero en la URL (IDOR). Se corrige verificando en el servicio que la orden pertenezca al usuario autenticado (segun su token JWT) o que tenga rol ADMIN, lanzando 403 Forbidden si no coincide.*
* **Justificacion Analitica:** IDOR (Insecure Direct Object Reference) ocurre al asumir que la posesion de un identificador numerico autoriza el acceso al recurso. La remediacion exige comprobar en la capa de negocio que el `usuarioId` del comprobante coincida con la identidad extraida del token o que el usuario sea administrador.
* **Analisis de Distractores:**
  * **B:** Falso. Usar letras (UUID) solo ofusca el problema pero no valida autorizacion.
  * **C:** Falso. Los pedidos y facturas contienen datos personales y financieros privados.
  * **D:** Falso. Cambiar el verbo a DELETE destruye datos y no resuelve la autorizacion.

---

#### Item 8 (4 puntos): Cross-Site Scripting (XSS) y Sanitizacion en Angular
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Se desactiva la proteccion automatica de Angular contra scripts maliciosos, permitiendo que un atacante inyecte codigo JavaScript que se ejecute en el navegador de otros usuarios (Stored XSS). Se remedia quitando el bypass y usando la interpolacion normal {{ orden.notasEntrega }}.*
* **Justificacion Analitica:** `bypassSecurityTrustHtml` instruye a Angular a confiar ciegamente en una cadena HTML sin desinfectarla. Si un usuario malicioso guardo un payload como `<img src=x onerror="alert(1)">`, el navegador lo ejecutara. La remediacion consiste en usar la interpolacion estandar `{{ }}`, que trata la variable como texto plano seguro.
* **Analisis de Distractores:**
  * **B:** Falso. XSS se ejecuta en el navegador del cliente, no borra la base de datos del servidor.
  * **C:** Falso. Renombrar la variable no neutraliza la ejecucion de scripts.
  * **D:** Falso. Los navegadores no desinfectan HTML arbitrario inyectado via innerHTML.

---

### Modulo Despliegue y Publicacion: Web y Movil (10 Puntos)

#### Item 9 (5 puntos): Despliegue Web, Nginx y Certificados SSL/TLS
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *Nginx recibe las peticiones en el puerto 443 con HTTPS, sirve los archivos estaticos de Angular directamente y reenvia las peticiones /api a Spring Boot (8080); Spring Boot corre como un servicio continuo de fondo (systemd); HTTPS cifra los datos en transito entre el navegador y el servidor.*
* **Justificacion Analitica:** Nginx actua como proxy inverso, servidor de archivos estaticos para la SPA de Angular y terminador SSL/TLS en el puerto 443. Redirige el trafico dinamico a Spring Boot en el puerto 8080, el cual se gestiona como servicio del sistema operativo (`systemd`). HTTPS protege la confidencialidad e integridad de la informacion en transito.
* **Analisis de Distractores:**
  * **B:** Falso. Nginx no es una base de datos ni Angular procesa transacciones bancarias directas.
  * **C:** Falso. Nginx no apaga servidores y Angular es TypeScript/JavaScript, no Java.
  * **D:** Falso. Spring Boot corre en el servidor y Angular no es un demonio de base de datos.

---

#### Item 10 (5 puntos): Firma Digital con Keystore y Publicacion AAB
* **Opcion Correcta:** **A**
* **Respuesta Correcta:** *keytool y el keystore permiten crear y guardar la llave criptografica privada para firmar digitalmente la aplicacion y certificar que no ha sido alterada. El formato .aab permite a Google Play entregar paquetes mas livianos adaptados al procesador y pantalla de cada usuario (Dynamic Delivery).*
* **Justificacion Analitica:** `keytool` genera un almacen de llaves criptograficas (`keystore`) que permite firmar los artefactos moviles, autenticando al autor y garantizando la integridad binaria. El formato Android App Bundle (`.aab`) permite a Google Play compilar y servir APKs optimizados para cada arquitectura de hardware (*Dynamic Delivery*), reduciendo el tamano de descarga.
* **Analisis de Distractores:**
  * **B:** Falso. No es una lista de usuarios ni es exclusivo para televisores.
  * **C:** Falso. La firma digital no cambia iconos y el formato APK sigue existiendo internamente.
  * **D:** Falso. `keytool` no es un antivirus ni `.aab` es un archivo de audio.

---

## Solucionario Detallado: PARTE 2 (60 Puntos)

### Requerimiento 1 (10 pts): Autenticacion Criptografica con BCrypt

**Archivo 1:** `backend/.../config/SecurityConfig.java`

```java
package cr.ac.ucr.if0009.insecureshop.config;

import org.springframework.context.
       annotation.Bean;
import org.springframework.context.
       annotation.Configuration;
import org.springframework.security.
       crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.
       crypto.password.PasswordEncoder;

@Configuration
public class SecurityConfig {

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12);
    }
}
```

**Archivo 2:** `backend/.../service/AuthService.java`

```java
// Inyeccion de PasswordEncoder en constructor:
private final PasswordEncoder passwordEncoder;

public AuthService(
    UsuarioRepository usuarioRepository,
    JwtUtil jwtUtil,
    PasswordEncoder passwordEncoder) {
    this.usuarioRepository = usuarioRepository;
    this.jwtUtil = jwtUtil;
    this.passwordEncoder = passwordEncoder;
}

public LoginResponse login(LoginRequest request) {
    Usuario usuario = usuarioRepository
        .findByUsername(request.getUsername())
        .orElseThrow(() ->
            new IllegalArgumentException(
                "Credenciales invalidas"));

    // Validacion criptografica segura con BCrypt:
    if (!passwordEncoder.matches(
            request.getPassword(),
            usuario.getPassword())) {
        throw new IllegalArgumentException(
            "Credenciales invalidas");
    }

    String token = jwtUtil.generarToken(
        usuario.getUsername(),
        usuario.getRol().name(),
        usuario.getId());

    return new LoginResponse(
        token,
        usuario.getUsername(),
        usuario.getNombreCompleto(),
        usuario.getCorreo(),
        usuario.getRol().name(),
        usuario.getId());
}
```

**Criterios de Evaluacion:**
* Instanciacion de `BCryptPasswordEncoder(12)` como `@Bean`: 4 pts.
* Inyeccion de dependencias correcta en `AuthService`: 2 pts.
* Uso de `passwordEncoder.matches(...)` para verificar la clave: 4 pts.

---

### Requerimiento 2 (15 pts): Busqueda Segura con JPQL Parametrizado

**Archivo 1:** `backend/.../repository/ProductoRepository.java`

```java
package cr.ac.ucr.if0009.insecureshop.repository;

import cr.ac.ucr.if0009.insecureshop.model.Producto;
import org.springframework.data.jpa.
       repository.JpaRepository;
import org.springframework.data.jpa.
       repository.Query;
import org.springframework.data.
       repository.query.Param;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface ProductoRepository
    extends JpaRepository<Producto, Long> {

    @Query("SELECT p FROM Producto p WHERE " +
           "LOWER(p.nombre) LIKE " +
           "LOWER(CONCAT('%', :termino, '%')) OR " +
           "LOWER(p.descripcion) LIKE " +
           "LOWER(CONCAT('%', :termino, '%'))")
    List<Producto> buscarPorTermino(
        @Param("termino") String termino);
}
```

**Archivo 2:** `backend/.../service/ProductoService.java`

```java
public List<ProductoDto> buscarPorTermino(
    String termino) {
    return productoRepository
        .buscarPorTermino(termino)
        .stream()
        .map(this::toDto)
        .toList();
}
```

**Archivo 3:** `backend/.../controller/ProductoController.java`

```java
@GetMapping("/buscar")
public ResponseEntity<List<ProductoDto>> buscar(
    @RequestParam(name = "termino",
                  defaultValue = "")
    String termino
) {
    List<ProductoDto> resultado =
        productoService.buscarPorTermino(termino);
    return ResponseEntity.ok(resultado);
}
```

**Criterios de Evaluacion:**
* Consulta JPQL segura con `@Query`, `:termino` y `@Param`: 7 pts.
* Metodo en servicio retornando `List<ProductoDto>`: 4 pts.
* Endpoint REST `@GetMapping("/buscar")` con `List<ProductoDto>`: 4 pts.

---

### Requerimiento 3 (10 pts): Interceptor HTTP Funcional en Angular

> [!NOTE]
> En la plantilla base `web_app_exam`, el interceptor ya se encuentra registrado dentro de `app.config.ts` mediante `withInterceptors([authInterceptor])`. La tarea del estudiante consiste en implementar la logica de inyeccion del token en `auth.interceptor.ts`.

**Archivo:** `frontend/src/app/interceptors/auth.interceptor.ts`

```typescript
import { HttpInterceptorFn }
       from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthService }
       from '../services/auth.service';

export const authInterceptor: HttpInterceptorFn = (
  req, next
) => {
  const authService = inject(AuthService);
  const token = authService.getToken();

  if (token) {
    const authReq = req.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`
      }
    });
    return next(authReq);
  }

  return next(req);
};
```

**Criterios de Evaluacion:**
* Inyeccion de `AuthService` mediante `inject(AuthService)`: 2 pts.
* Obtencion y comprobacion de presencia del token: 2 pts.
* Clonacion inmutable con `req.clone({ setHeaders: { Authorization: ... } })`: 4 pts.
* Continuacion del flujo con `next(authReq)` o `next(req)`: 2 pts.

---

### Requerimiento 4 (10 pts): Checkout y Manejo Reactivo de Senales

**Archivo 1:** `frontend/src/app/pages/checkout/checkout.component.ts`

```typescript
confirmarPedido(): void {
  if (this.tiendaService.carrito().length === 0) {
    this.errorMsg = 'El carrito esta vacio.';
    return;
  }
  if (!this.direccionEntrega.trim()) {
    this.errorMsg = 'La direccion es obligatoria.';
    return;
  }

  this.cargando = true;
  this.tiendaService.crearOrden(
    this.direccionEntrega,
    this.notasEntrega
  ).subscribe({
    next: (orden) => {
      this.cargando = false;
      this.tiendaService.limpiarCarrito();
      this.router.navigate(['/orden', orden.id]);
    },
    error: (err) => {
      this.cargando = false;
      this.errorMsg =
        'Error al procesar la orden de compra.';
    }
  });
}
```

**Archivo 2:** `frontend/src/app/pages/checkout/checkout.component.html`

* Uso de directivas de enlace bidireccional `[(ngModel)]` para capturar `direccionEntrega` y `notasEntrega`.
* Renderizado reactivo de la tabla de articulos leyendo la senal `tiendaService.carrito()`.
* Despliegue de totales reactivos calculados mediante senales computadas.

**Criterios de Evaluacion:**
* Validacion de carrito no vacio y direccion requerida: 3 pts.
* Llamada correcta a `tiendaService.crearOrden(...)`: 3 pts.
* Vaciado de carrito y navegacion al comprobante: 2 pts.
* Gestion reactiva de estado visual (`cargando`, mensajes de error): 2 pts.

---

### Requerimiento 5 (10 pts): Control de Acceso Horizontal contra IDOR

> [!NOTE]
> En `OrdenController.java`, la recepcion del encabezado `Authorization` y la llamada a `jwtUtil.extraerUsuarioId(token)` ya se encuentran pre-configuradas. El estudiante debe programar la regla de control de acceso en `OrdenService.java`.

**Archivo 1:** `backend/.../service/OrdenService.java`

```java
public OrdenDto obtenerPorIdSeguro(
    Long id,
    Long usuarioAutenticadoId,
    String rolAutenticado
) {
    Orden orden = ordenRepository.findById(id)
        .orElseThrow(() ->
            new IllegalArgumentException(
                "Orden " + id + " no encontrada"));

    boolean esAdmin = "ADMIN".equalsIgnoreCase(
        rolAutenticado);
    boolean esPropietario =
        orden.getUsuario().getId()
        .equals(usuarioAutenticadoId);

    // Regla de autorizacion defensiva:
    if (!esAdmin && !esPropietario) {
        throw new AccesoDenegadoException(
            "Acceso denegado: No posee permisos " +
            "para consultar la orden " + id);
    }

    return toDto(orden);
}
```

**Archivo 2:** `backend/.../controller/OrdenController.java` (referencia de conexion)

```java
@GetMapping("/{id}")
public ResponseEntity<OrdenDto> obtenerPorId(
    @PathVariable Long id,
    @RequestHeader(name = "Authorization",
                   required = false)
    String authHeader
) {
    if (authHeader == null ||
        !authHeader.startsWith("Bearer ")) {
        throw new AccesoDenegadoException(
            "Falta token Bearer en Authorization");
    }

    String token = authHeader.substring(7);
    Long usuarioId =
        jwtUtil.extraerUsuarioId(token);
    String rol = jwtUtil.extraerRol(token);

    OrdenDto orden =
        ordenService.obtenerPorIdSeguro(
            id, usuarioId, rol);
    return ResponseEntity.ok(orden);
}
```

**Criterios de Evaluacion:**
* Busqueda y validacion de existencia de la orden: 2 pts.
* Comprobacion de si el usuario posee rol `ADMIN`: 2 pts.
* Comprobacion de si el usuario es el dueno de la orden: 3 pts.
* Lanzamiento de `AccesoDenegadoException` si no es admin ni propietario: 3 pts.

---

### Requerimiento 6 (5 pts): Hardening A05 y Manejo de Errores RFC 7807

**Archivo 1:** `backend/src/main/resources/application.properties`

```properties
server.error.include-stacktrace=never
server.error.include-exception=false
server.error.include-message=always
```

**Archivo 2:** `backend/.../exception/GlobalExceptionHandler.java`

```java
package cr.ac.ucr.if0009.insecureshop.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ProblemDetail;
import org.springframework.web.bind.
       annotation.ExceptionHandler;
import org.springframework.web.bind.
       annotation.RestControllerAdvice;

import java.net.URI;
import java.time.Instant;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(AccesoDenegadoException.class)
    public ProblemDetail handleAccessDenied(
        AccesoDenegadoException ex) {
        ProblemDetail problem =
            ProblemDetail.forStatusAndDetail(
                HttpStatus.FORBIDDEN,
                ex.getMessage());
        problem.setTitle("Acceso Prohibido");
        problem.setType(URI.create(
            "https://insecureshop.cr/" +
            "errors/access-denied"));
        problem.setProperty(
            "timestamp", Instant.now());
        return problem;
    }

    @ExceptionHandler(Exception.class)
    public ProblemDetail handleGeneral(
        Exception ex) {
        ProblemDetail problem =
            ProblemDetail.forStatusAndDetail(
                HttpStatus.INTERNAL_SERVER_ERROR,
                "Error interno del servidor. " +
                "Contacte al administrador.");
        problem.setTitle("Error Interno");
        problem.setType(URI.create(
            "https://insecureshop.cr/" +
            "errors/internal-error"));
        problem.setProperty(
            "timestamp", Instant.now());
        return problem;
    }
}
```

**Criterios de Evaluacion:**
* Supresion de stack traces en `application.properties`: 2 pts.
* Respuestas estandarizadas RFC 7807 (`ProblemDetail`) con HTTP 403 y 500: 3 pts.

---

## Tabla Resumen de Calificacion Pericial

| Seccion | Componente | Criterio de Aceptacion | Pts |
| :--- | :--- | :--- | :---: |
| **Parte 1** | Items 1 al 10 | 10 preguntas de seleccion unica en Moodle (100% calibradas) | **40** |
| **Req 1** | Autenticacion | BCryptPasswordEncoder configurado y validado en AuthService | **10** |
| **Req 2** | Busqueda Segura | JPQL parametrizado con `@Query` devolviendo `List<Producto>` | **15** |
| **Req 3** | Interceptor | `authInterceptor` funcional inyectando Bearer token en headers | **10** |
| **Req 4** | Checkout | Componente reactivo con senales y confirmacion de pedido | **10** |
| **Req 5** | IDOR | Validacion estricta en `OrdenService` (esAdmin \|\| esPropietario) | **10** |
| **Req 6** | Hardening A05 | Supresion de trazas y formateo RFC 7807 (`ProblemDetail`) | **5** |
| **Total** | **Evaluacion Sumativa** | **Dominio Teorico-Practico de Desarrollo y Seguridad** | **100** |
