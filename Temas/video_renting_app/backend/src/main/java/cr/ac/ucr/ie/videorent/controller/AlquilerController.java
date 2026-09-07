package cr.ac.ucr.ie.videorent.controller;

import cr.ac.ucr.ie.videorent.business.AlquilerService;
import cr.ac.ucr.ie.videorent.domain.Alquiler;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/alquileres")
@CrossOrigin(origins = "*")
@Tag(name = "Alquileres", description = "Endpoints para la gestion de alquileres de peliculas")
public class AlquilerController {

    private final AlquilerService alquilerService;

    public AlquilerController(AlquilerService alquilerService) {
        this.alquilerService = alquilerService;
    }

    @GetMapping
    @Operation(summary = "Obtener todos los alquileres")
    public ResponseEntity<List<Alquiler>> getAll() {
        return ResponseEntity.ok(alquilerService.obtenerTodos());
    }

    @GetMapping("/activos")
    @Operation(summary = "Obtener alquileres activos")
    public ResponseEntity<List<Alquiler>> getActivos() {
        return ResponseEntity.ok(alquilerService.obtenerAlquileresActivos());
    }

    @PostMapping
    @Operation(summary = "Registrar nuevo alquiler")
    public ResponseEntity<Alquiler> create(@RequestBody Alquiler nuevo) {
        Alquiler creado = alquilerService.registrarAlquiler(nuevo);
        return ResponseEntity.status(HttpStatus.CREATED).body(creado);
    }

    @PatchMapping("/{id}/devolucion")
    @Operation(summary = "Procesar devolucion de pelicula alquilada")
    public ResponseEntity<Alquiler> procesarDevolucion(@PathVariable Integer id) {
        Alquiler actualizado = alquilerService.procesarDevolucion(id);
        return ResponseEntity.ok(actualizado);
    }
}
