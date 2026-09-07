package cr.ac.ucr.ie.videorent.controller;

import cr.ac.ucr.ie.videorent.business.PeliculaService;
import cr.ac.ucr.ie.videorent.domain.Pelicula;
import cr.ac.ucr.ie.videorent.domain.Review;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/peliculas")
@CrossOrigin(origins = "*")
@Tag(name = "Peliculas", description = "Endpoints para la gestion de peliculas")
public class PeliculaController {

    private final PeliculaService peliculaService;

    public PeliculaController(PeliculaService peliculaService) {
        this.peliculaService = peliculaService;
    }

    @GetMapping
    @Operation(summary = "Obtener todas las peliculas")
    public ResponseEntity<List<Pelicula>> getAll() {
        return ResponseEntity.ok(peliculaService.obtenerTodas());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Obtener pelicula por ID")
    public ResponseEntity<Pelicula> getById(@PathVariable Integer id) {
        return peliculaService.obtenerPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/{id}/reviews")
    @Operation(summary = "Obtener pelicula con reviews cargadas de forma optima")
    public ResponseEntity<Pelicula> getByIdConReviews(@PathVariable Integer id) {
        return peliculaService.obtenerPorIdConReviews(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    @Operation(summary = "Crear nueva pelicula")
    public ResponseEntity<Pelicula> create(@RequestBody Pelicula pelicula) {
        Pelicula creada = peliculaService.guardar(pelicula);
        return ResponseEntity.status(HttpStatus.CREATED).body(creada);
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Eliminar pelicula por ID")
    public ResponseEntity<Void> delete(@PathVariable Integer id) {
        peliculaService.eliminar(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/nplusone-demo")
    @Operation(summary = "Demostrar fallo de rendimiento N+1 SELECT")
    public ResponseEntity<List<String>> demoNPlusOne() {
        List<Pelicula> peliculas = peliculaService.obtenerTodas();
        List<String> resultado = new ArrayList<>();
        for (Pelicula p : peliculas) {
            for (Review r : p.getReviews()) {
                resultado.add(p.getTitulo() + " -> " + r.getComentario());
            }
        }
        return ResponseEntity.ok(resultado);
    }

    @GetMapping("/optimized-demo")
    @Operation(summary = "Demostrar solucion N+1 SELECT mediante JOIN FETCH")
    public ResponseEntity<List<String>> demoOptimized() {
        List<Pelicula> peliculas = peliculaService.obtenerTodasOptimizadasConReviews();
        List<String> resultado = new ArrayList<>();
        for (Pelicula p : peliculas) {
            for (Review r : p.getReviews()) {
                resultado.add(p.getTitulo() + " -> " + r.getComentario());
            }
        }
        return ResponseEntity.ok(resultado);
    }
}
