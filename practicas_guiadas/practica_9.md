![UCR Banner](../resources/images/UCR_Banner.png)

**UNIVERSIDAD DE COSTA RICA**  
**SEDE DEL ATLÁNTICO - RECINTO PARAÍSO**  
**CARRERA DE INFORMÁTICA EMPRESARIAL**  
**CURSO:** IF0009 - Desarrollo de Software IV  
**PROFESOR:** Mag. Jonathan Granados C.  
**SEMESTRE:** II-2026  

---

# Práctica Guiada 9: Procedimientos Almacenados, Paginación Relacional y Consumo Web en VideoRent

## Resumen

Esta práctica guiada da continuidad directa a la **Práctica Guiada 8**, consolidando los temas avanzados de persistencia del **Tema 8.7.1 (Hibernate Avanzado)** e integrándolos en la plataforma de alquiler de películas **VideoRent**. Usted aprenderá a optimizar el acceso a datos combinando la ejecución de **procedimientos almacenados nativos** (*Stored Procedures*) y la **paginación relacional a nivel de base de datos** (`Pageable`, `Page<T>`) con una interfaz web en **HTML5, CSS3 y JavaScript asíncrono (Fetch API)**.

A lo largo del laboratorio, usted construirá el módulo de consulta y navegación del catálogo de películas de **VideoRent**. Mapeará llamadas a procedimientos almacenados en la base de datos, estructurará consultas paginadas en Spring Boot para evitar la carga masiva en memoria RAM, expondrá endpoints RESTful paginados y consumirá dichos resultados desde una tabla HTML interactiva con controles completos de navegación (`Primera`, `Anterior`, `Página X de Y`, `Siguiente`, `Última`) y selector de tamaño de página.

---

## Metadatos del Laboratorio

*   **Tiempo estimado:** 4 horas.
*   **Herramientas requeridas:** Java 21 (o versión local instalada), Spring Boot 3.x, H2 Database (o SQL Server), Maven, VS Code / IntelliJ IDEA, Navegador Web (Chrome/Firefox).
*   **Metas de Aprendizaje:**

    1.  Configurar y ejecutar procedimientos almacenados nativos en la base de datos de `VideoRent` mediante la anotación `@Procedure` y `EntityManager` de JPA.

    2.  Implementar paginación relacional eficiente utilizando `Pageable`, `PageRequest` y `Page<T>` en Spring Data JPA para el catálogo de películas.

    3.  Construir un controlador RESTful en Spring Boot que retorne payloads JSON paginados estandarizados y filtrados.

    4.  Desarrollar una interfaz cliente web en HTML5 y Vanilla JavaScript que consuma la API paginada con Fetch API y actualice el DOM en tiempo real con controles de navegación (`Primera`, `Anterior`, `Siguiente`, `Última`).

    5.  Diagnosticar y resolver errores comunes como el desajuste de índices de página (base 0 vs base 1) y advertencias de paginación en memoria (`HHH000104`).

---

## Conceptos Clave (El 'Qué')

### 1. Procedimientos Almacenados (`@Procedure`)
Un procedimiento almacenado es una rutina precompilada en el motor de base de datos relacional. Spring Data JPA permite invocar estos procedimientos directamente mediante la anotación `@Procedure` en interfaces `@Repository`, mapeando parámetros de entrada (`IN`) y result sets o salidas (`OUT`).

### 2. Paginación Relacional (`Pageable` y `Page<T>`)
La interfaz `Pageable` transmite el número de página solicitado, el tamaño de lote y los criterios de ordenamiento. Hibernate traduce esto en cláusulas SQL nativas (`LIMIT / OFFSET` en H2/PostgreSQL o `OFFSET ... FETCH NEXT` en SQL Server), procesando únicamente la subpágina requerida y evitando saturar la memoria RAM de la JVM.

### 3. Consumo Asíncrono Web (Fetch API)
El navegador realiza peticiones HTTP asíncronas (ejemplo: `GET /api/v1/videos?page=0&size=5`) sin recargar la página completa, renderizando dinámicamente únicamente las filas de la tabla de películas y recalculando el estado activo de los botones de la barra de paginación.

---

## Parte 1: Práctica Guiada Paso a Paso

### Paso 1: Configuración de la Entidad `Video` y Script SQL con Procedimiento Almacenado

Asegúrese de contar con la entidad `Video.java` en el paquete `com.videorent.model`:

```java
package com.videorent.model;

import jakarta.persistence.*;

@Entity
@Table(name = "Video")
public class Video {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String titulo;

    @Column(nullable = false, length = 100)
    private String director;

    @Column(nullable = false, length = 50)
    private String categoria;

    @Column(name = "precio_alquiler", nullable = false)
    private Double precioAlquiler;

    @Column(nullable = false)
    private Boolean disponible;

    public Video() {}

    public Video(String titulo,
                 String director,
                 String categoria,
                 Double precioAlquiler,
                 Boolean disponible) {
        this.titulo = titulo;
        this.director = director;
        this.categoria = categoria;
        this.precioAlquiler = precioAlquiler;
        this.disponible = disponible;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public Double getPrecioAlquiler() {
        return precioAlquiler;
    }

    public void setPrecioAlquiler(Double precioAlquiler) {
        this.precioAlquiler = precioAlquiler;
    }

    public Boolean getDisponible() {
        return disponible;
    }

    public void setDisponible(Boolean disponible) {
        this.disponible = disponible;
    }
}
```

Cree el archivo de inicialización SQL en `src/main/resources/schema.sql` declarando la tabla y el Stored Procedure:

```sql
-- Script de esquema y Stored Procedure para VideoRent
CREATE TABLE IF NOT EXISTS Video (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    director VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio_alquiler DECIMAL(8,2) NOT NULL,
    disponible BOOLEAN NOT NULL
);

-- Stored Procedure nativo compatible con H2 / SQL
CREATE ALIAS IF NOT EXISTS SP_FILTRAR_VIDEOS_DISPONIBLES AS $$
import java.sql.*;
@CODE
ResultSet spFiltrarVideos(Connection conn,
                          Boolean pDisponible)
throws SQLException {
    String sql = "SELECT * FROM Video " +
                 "WHERE disponible = ? " +
                 "ORDER BY titulo ASC";
    PreparedStatement ps =
        conn.prepareStatement(sql);
    ps.setBoolean(1, pDisponible);
    return ps.executeQuery();
}
$$;
```

Cree el archivo de semillas en `src/main/resources/data.sql`:

```sql
INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Inception', 'Christopher Nolan', 'Ciencia Ficcion', 3.99, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('The Matrix', 'Lana & Lilly Wachowski', 'Accion', 2.99, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Interstellar', 'Christopher Nolan', 'Ciencia Ficcion', 4.50, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Pulp Fiction', 'Quentin Tarantino', 'Drama', 3.50, false);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('The Dark Knight', 'Christopher Nolan', 'Accion', 4.00, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Forrest Gump', 'Robert Zemeckis', 'Drama', 2.50, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Avatar', 'James Cameron', 'Ciencia Ficcion', 3.99, false);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Gladiator', 'Ridley Scott', 'Accion', 3.00, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Titanic', 'James Cameron', 'Romance', 2.99, true);

INSERT INTO Video 
(titulo, director, categoria, precio_alquiler, disponible)
VALUES ('Jurassic Park', 'Steven Spielberg', 'Aventura', 3.50, true);
```

---

### Paso 2: Creación del DTO y Repositorio de Spring Data JPA

Cree el DTO `VideoDTO.java` en `src/main/java/com/videorent/dto/VideoDTO.java`:

```java
package com.videorent.dto;

public record VideoDTO(
    Long id,
    String titulo,
    String director,
    String categoria,
    Double precioAlquiler,
    Boolean disponible
) {}
```

Cree la interfaz `VideoRepository.java` en `src/main/java/com/videorent/repository/VideoRepository.java`:

```java
package com.videorent.repository;

import com.videorent.model.Video;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.query.Procedure;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface VideoRepository
        extends JpaRepository<Video, Long> {

    // Invocacion de Stored Procedure nativo
    @Procedure(procedureName = "SP_FILTRAR_VIDEOS_DISPONIBLES")
    List<Video> obtenerPorDisponible(
        @Param("pDisponible") Boolean disponible
    );

    // Consulta paginada por titulo de pelicula
    Page<Video> findByTituloContainingIgnoreCase(
        String titulo,
        Pageable pageable
    );

    // Consulta paginada por categoria
    Page<Video> findByCategoriaIgnoreCase(
        String categoria,
        Pageable pageable
    );
}
```

---

### Paso 3: Capa de Servicio de Negocio (`VideoService.java`)

Cree la clase `VideoService.java` en `src/main/java/com/videorent/service/VideoService.java`:

```java
package com.videorent.service;

import com.videorent.dto.VideoDTO;
import com.videorent.model.Video;
import com.videorent.repository.VideoRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class VideoService {

    private final VideoRepository videoRepository;

    public VideoService(VideoRepository videoRepository) {
        this.videoRepository = videoRepository;
    }

    @Transactional(readOnly = true)
    public Page<VideoDTO> listarPaginado(int page,
                                           int size,
                                           String sortBy,
                                           String dir,
                                           String titulo,
                                           String categoria) {
        Sort.Direction direction =
            dir.equalsIgnoreCase("DESC") ?
            Sort.Direction.DESC : Sort.Direction.ASC;

        Pageable pageable =
            PageRequest.of(page, size,
                           Sort.by(direction, sortBy));

        Page<Video> videosPage;
        if (titulo != null && !titulo.trim().isEmpty()) {
            videosPage = videoRepository
                .findByTituloContainingIgnoreCase(
                    titulo, pageable
                );
        } else if (categoria != null && !categoria.trim().isEmpty()) {
            videosPage = videoRepository
                .findByCategoriaIgnoreCase(
                    categoria, pageable
                );
        } else {
            videosPage =
                videoRepository.findAll(pageable);
        }

        return videosPage.map(v -> new VideoDTO(
            v.getId(), v.getTitulo(),
            v.getDirector(), v.getCategoria(),
            v.getPrecioAlquiler(), v.getDisponible()
        ));
    }

    @Transactional(readOnly = true)
    public List<VideoDTO> listarViaStoredProcedure(Boolean disp) {
        List<Video> lista =
            videoRepository.obtenerPorDisponible(disp);

        return lista.stream()
            .map(v -> new VideoDTO(
                v.getId(), v.getTitulo(),
                v.getDirector(), v.getCategoria(),
                v.getPrecioAlquiler(), v.getDisponible()
            ))
            .toList();
    }
}
```

---

### Paso 4: Controlador RESTful (`VideoController.java`)

Cree la clase `VideoController.java` en `src/main/java/com/videorent/controller/VideoController.java`:

```java
package com.videorent.controller;

import com.videorent.dto.VideoDTO;
import com.videorent.service.VideoService;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/videos")
@CrossOrigin(origins = "*")
public class VideoController {

    private final VideoService videoService;

    public VideoController(VideoService videoService) {
        this.videoService = videoService;
    }

    @GetMapping
    public ResponseEntity<Page<VideoDTO>> listar(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "5") int size,
            @RequestParam(defaultValue = "titulo") String sortBy,
            @RequestParam(defaultValue = "ASC") String direction,
            @RequestParam(required = false) String titulo,
            @RequestParam(required = false) String categoria) {

        Page<VideoDTO> resultado =
            videoService.listarPaginado(
                page, size, sortBy, direction, titulo, categoria
            );
        return ResponseEntity.ok(resultado);
    }

    @GetMapping("/procedimiento/{disponible}")
    public ResponseEntity<List<VideoDTO>> listarSP(
            @PathVariable Boolean disponible) {

        List<VideoDTO> resultado =
            videoService.listarViaStoredProcedure(disponible);
        return ResponseEntity.ok(resultado);
    }
}
```

---

### Paso 5: Interfaz de Usuario Cliente (HTML5 + CSS3 + Vanilla JavaScript)

Cree el archivo de vista en `src/main/resources/static/index.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">
    <title>VideoRent - Catalogo Paginado</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent-color: #38bdf8;
            --text-color: #f8fafc;
            --border-color: #334155;
            --badge-success: #22c55e;
            --badge-danger: #ef4444;
        }

        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 950px;
            margin: 0 auto;
            background-color: var(--card-bg);
            padding: 24px;
            border-radius: 10px;
        }

        h1 {
            color: var(--accent-color);
            font-size: 22px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
        }

        .filter-bar {
            display: flex;
            gap: 10px;
            margin-bottom: 18px;
            flex-wrap: wrap;
        }

        input, select, button {
            padding: 8px 12px;
            border-radius: 5px;
            border: 1px solid var(--border-color);
            background-color: #0f172a;
            color: var(--text-color);
            font-size: 13px;
        }

        button {
            background-color: #0284c7;
            color: white;
            cursor: pointer;
            border: none;
        }

        button:disabled {
            opacity: 0.4;
            cursor: not-allowed;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 18px;
        }

        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            font-size: 13px;
        }

        th {
            background-color: #0f172a;
            color: var(--accent-color);
        }

        .badge {
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: bold;
        }

        .badge-disponible {
            background-color: rgba(34, 197, 94, 0.2);
            color: var(--badge-success);
        }

        .badge-alquilado {
            background-color: rgba(239, 68, 68, 0.2);
            color: var(--badge-danger);
        }

        .pagination-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>VideoRent - Catalogo de Peliculas</h1>

    <div class="filter-bar">
        <input type="text" id="inputTitulo"
               placeholder="Buscar por titulo...">
        <button onclick="buscarTitulo()">Buscar</button>

        <select id="selectSP"
                onchange="ejecutarSP()">
            <option value="">-- Probar SP Nativo --</option>
            <option value="true">SP: Solo Disponibles</option>
            <option value="false">SP: Solo Alquilados</option>
        </select>

        <select id="selectSize"
                onchange="cambiarTamano()">
            <option value="5" selected>5 por pagina</option>
            <option value="10">10 por pagina</option>
        </select>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Titulo</th>
                <th>Director</th>
                <th>Categoria</th>
                <th>Precio</th>
                <th>Estado</th>
            </tr>
        </thead>
        <tbody id="tablaBody"></tbody>
    </table>

    <div class="pagination-controls">
        <div id="infoPagina">Cargando...</div>
        <div>
            <button id="btnPrimera"
                    onclick="primeraPagina()">&lt;&lt; Primera</button>
            <button id="btnAnterior"
                    onclick="paginaAnterior()">&lt; Ant</button>
            <button id="btnSiguiente"
                    onclick="paginaSiguiente()">Sig &gt;</button>
            <button id="btnUltima"
                    onclick="ultimaPagina()">Ultima &gt;&gt;</button>
        </div>
    </div>
</div>

<script>
    let currentPage = 0;
    let pageSize = 5;
    let totalPages = 0;
    let filtroTitulo = "";

    document.addEventListener("DOMContentLoaded", () => {
        cargar();
    });

    async function cargar() {
        let url = `/api/v1/videos?page=${currentPage}` +
                  `&size=${pageSize}`;
        if (filtroTitulo) {
            url += `&titulo=${encodeURIComponent(filtroTitulo)}`;
        }
        const resp = await fetch(url);
        const data = await resp.json();
        renderTabla(data.content);
        renderPaginador(data);
    }

    function renderTabla(lista) {
        const body = document.getElementById("tablaBody");
        body.innerHTML = "";
        lista.forEach(v => {
            const tr = document.createElement("tr");
            const badgeClass = v.disponible ?
                "badge-disponible" : "badge-alquilado";
            const estadoTexto = v.disponible ?
                "DISPONIBLE" : "ALQUILADO";
            tr.innerHTML = `
                <td>${v.id}</td>
                <td><strong>${v.titulo}</strong></td>
                <td>${v.director}</td>
                <td>${v.categoria}</td>
                <td>$${v.precioAlquiler.toFixed(2)}</td>
                <td><span class="badge ${badgeClass}">${estadoTexto}</span></td>
            `;
            body.appendChild(tr);
        });
    }

    function renderPaginador(data) {
        totalPages = data.totalPages;
        const info = `Pagina ${data.number + 1} ` +
                     `de ${data.totalPages} ` +
                     `(Total: ${data.totalElements} peliculas)`;
        document.getElementById("infoPagina").innerText = info;
        document.getElementById("btnPrimera").disabled = data.first;
        document.getElementById("btnAnterior").disabled = data.first;
        document.getElementById("btnSiguiente").disabled = data.last;
        document.getElementById("btnUltima").disabled = data.last;
    }

    function primeraPagina() {
        currentPage = 0;
        cargar();
    }

    function paginaAnterior() {
        if (currentPage > 0) {
            currentPage--;
            cargar();
        }
    }

    function paginaSiguiente() {
        if (currentPage < totalPages - 1) {
            currentPage++;
            cargar();
        }
    }

    function ultimaPagina() {
        if (totalPages > 0) {
            currentPage = totalPages - 1;
            cargar();
        }
    }

    function cambiarTamano() {
        pageSize =
            parseInt(document.getElementById("selectSize").value);
        currentPage = 0;
        cargar();
    }

    function buscarTitulo() {
        filtroTitulo =
            document.getElementById("inputTitulo").value;
        currentPage = 0;
        cargar();
    }

    async function ejecutarSP() {
        const val = document.getElementById("selectSP").value;
        if (val === "") { cargar(); return; }
        const disp = val === "true";
        const resp =
            await fetch(`/api/v1/videos/procedimiento/${disp}`);
        const data = await resp.json();
        renderTabla(data);
        document.getElementById("infoPagina").innerText =
            `Resultados SP Nativo: ${data.length} registros`;
        document.getElementById("btnPrimera").disabled = true;
        document.getElementById("btnAnterior").disabled = true;
        document.getElementById("btnSiguiente").disabled = true;
        document.getElementById("btnUltima").disabled = true;
    }
</script>
</body>
</html>
```

---

### Paso 6: Integración con Git Flow en IDE y Prompts de IA

En Visual Studio Code, usted puede gestionar el control de versiones de forma visual utilizando la pestaña **Source Control** (`Ctrl+Shift+G` / `Cmd+Shift+G`):

**1.** Haga clic en el ícono de **Source Control** en la barra lateral izquierda.

**2.** Revise los archivos modificados e introduzca su mensaje de commit siguiendo la convención de Commits Semánticos:

```bash
feat(backend): add paginated video catalog endpoint and stored procedure
```

**3.** Presione el botón **Commit** y posteriormente **Sync Changes** para enviar los cambios a su repositorio en GitHub.

#### Prompts Sugeridos para Google Antigravity / Copilot:

*   *Generar Gitignore:* `"Genera un archivo .gitignore completo para un proyecto Spring Boot 3 con Maven, Java 21 e H2/SQL Server."`
*   *Redactar Commit Semántico:* `"Sugerime un mensaje de commit semantico en espanol para la implementacion de la paginacion relacional en VideoService."`
*   *Depuración de Consola:* `"Analiza este stacktrace de Spring Data JPA sobre un error en @Procedure y explica paso a paso como solucionarlo."`

---

## Parte 2: Sección de Depuración de Errores Comunes

### Error 1: Desajuste de Índice Base 0 en Spring Data (`IndexOutOfBoundsException`)

#### Guía de Depuración:

- [ ] Verifique la URL emitida en la pestaña **Network** (F12) del navegador al cambiar de página.

- [ ] Observe que Spring Data JPA interpreta `page = 0` como la primera página de la colección.

- [ ] Inspeccione el controlador Java y asegúrese de que `@RequestParam(defaultValue = "0")` coincida con el script cliente.

- [ ] En JavaScript, presente al usuario `data.number + 1` en el texto UI mientras envía `currentPage` (base 0) a la API.

---

### Error 2: Advertencia de Paginación en Memoria (`HHH000104`)

#### Guía de Depuración:

- [ ] Revise sus consultas JPQL personalizadas en `VideoRepository.java`.

- [ ] Confirme que no está utilizando `JOIN FETCH` sobre colecciones `@OneToMany` junto con un parámetro `Pageable`.

- [ ] Para solucionar este aviso y evitar desbordamientos de memoria RAM, sustituya el `JOIN FETCH` por la anotación `@EntityGraph(attributePaths = {"alquileres"})` sobre el método del repositorio.

---

## Parte 3: Reto Autónomo (Evaluado)

Para completar esta práctica guiada, extienda el módulo de **VideoRent** resolviendo los siguientes requerimientos técnicos:

- [ ] **Tarea 1: Nuevo Stored Procedure con Mapeo JPA**  
  Diseñe en `schema.sql` el procedimiento almacenado `SP_OBTENER_VIDEOS_POR_CATEGORIA` que reciba el parámetro `pCategoria` (VARCHAR) y devuelva las películas pertenecientes a dicha categoría ordenadas por precio descendente. Mapee este método en `VideoRepository` utilizando la anotación `@Procedure`.

- [ ] **Tarea 2: Endpoint de Consulta por Categoría**  
  Exponga en `VideoController` el endpoint `GET /api/v1/videos/categoria-sp/{categoria}` que invoque el procedimiento almacenado mediante `VideoService` y retorne un payload JSON con la lista de objetos DTO correspondientes.

- [ ] **Tarea 3: Componente de Tarjetas de Métricas en HTML5/CSS3**  
  Modifique `src/main/resources/static/index.html` para incorporar un desplegable de selección de categoría y una sección superior de métricas (*Metrics Cards*) en CSS Grid. Al seleccionar una categoría, consuma el nuevo endpoint del Stored Procedure y renderice dinámicamente las películas resultantes junto con la cantidad total hallada.

---

## Lista de Chequeo Final

Antes de dar por concluida la práctica, asegúrese de haber verificado los siguientes puntos:

- [ ] El esquema y Stored Procedure `SP_FILTRAR_VIDEOS_DISPONIBLES` se ejecutan sin errores en la base de datos de `VideoRent`.

- [ ] El endpoint `GET /api/v1/videos` responde con la estructura paginada nativa de Spring Data (`content`, `totalPages`, `totalElements`, `first`, `last`).

- [ ] La interfaz HTML5 (`index.html`) navega entre páginas correctamente mediante la Fetch API sin recargar la página.

- [ ] Los botones `Primera`, `Anterior`, `Siguiente` y `Última` se deshabilitan adecuadamente según los bordes del catálogo.

- [ ] El código de la solución ha sido subido a su repositorio remoto en GitHub mediante un commit semántico documentado.
