package cr.ac.ucr.ie.videorent.controller;

import cr.ac.ucr.ie.videorent.business.ReviewService;
import cr.ac.ucr.ie.videorent.domain.Review;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/reviews")
@CrossOrigin(origins = "*")
@Tag(name = "Reviews", description = "Endpoints para la gestion de reseñas de peliculas")
public class ReviewController {

    private final ReviewService reviewService;

    public ReviewController(ReviewService reviewService) {
        this.reviewService = reviewService;
    }

    @GetMapping("/pelicula/{peliculaId}")
    @Operation(summary = "Obtener reseñas de una pelicula especifica")
    public ResponseEntity<List<Review>> getByPelicula(@PathVariable Integer peliculaId) {
        return ResponseEntity.ok(reviewService.obtenerPorPelicula(peliculaId));
    }

    @PostMapping("/pelicula/{peliculaId}")
    @Operation(summary = "Agregar nueva reseña a una pelicula")
    public ResponseEntity<Review> create(@PathVariable Integer peliculaId, 
                                         @RequestBody Review review) {
        Review creada = reviewService.agregarReviewAPelicula(peliculaId, review);
        return ResponseEntity.status(HttpStatus.CREATED).body(creada);
    }

    @PutMapping("/archivar-bajas/{calificacionMax}")
    @Operation(summary = "Archivar reseñas masivas con calificacion menor o igual")
    public ResponseEntity<String> archivarBajas(@PathVariable int calificacionMax) {
        int afectadas = reviewService.archivarResenasConBajaCalificacion(calificacionMax);
        return ResponseEntity.ok("Se archivaron " + afectadas + " reseña(s) correctamente.");
    }
}
