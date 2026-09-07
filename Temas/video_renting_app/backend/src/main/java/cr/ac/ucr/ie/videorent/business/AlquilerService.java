package cr.ac.ucr.ie.videorent.business;

import cr.ac.ucr.ie.videorent.data.AlquilerRepository;
import cr.ac.ucr.ie.videorent.data.PeliculaRepository;
import cr.ac.ucr.ie.videorent.domain.Alquiler;
import cr.ac.ucr.ie.videorent.domain.Pelicula;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class AlquilerService {

    private final AlquilerRepository alquilerRepository;
    private final PeliculaRepository peliculaRepository;

    public AlquilerService(AlquilerRepository alquilerRepository, 
                           PeliculaRepository peliculaRepository) {
        this.alquilerRepository = alquilerRepository;
        this.peliculaRepository = peliculaRepository;
    }

    @Transactional(readOnly = true)
    public List<Alquiler> obtenerAlquileresActivos() {
        return alquilerRepository.findByEstadoConPelicula("ACTIVO");
    }

    @Transactional(readOnly = true)
    public List<Alquiler> obtenerTodos() {
        return alquilerRepository.findAll();
    }

    @Transactional
    public Alquiler registrarAlquiler(Alquiler nuevo) {
        Integer peliculaId = nuevo.getPelicula().getId();
        Pelicula pelicula = peliculaRepository.findById(peliculaId)
                .orElseThrow(() -> new IllegalArgumentException(
                    "Pelicula no encontrada con ID: " + peliculaId));

        nuevo.setPelicula(pelicula);
        nuevo.setEstado("ACTIVO");
        if (nuevo.getFechaAlquiler() == null) {
            nuevo.setFechaAlquiler(LocalDateTime.now());
        }
        return alquilerRepository.save(nuevo);
    }

    @Transactional
    public Alquiler procesarDevolucion(Integer alquilerId) {
        Alquiler alquiler = alquilerRepository.findById(alquilerId)
                .orElseThrow(() -> new IllegalArgumentException(
                    "Alquiler no encontrado con ID: " + alquilerId));

        alquiler.setEstado("DEVUELTO");
        alquiler.setFechaDevolucion(LocalDateTime.now());
        return alquiler; // Guardado automatico por Dirty Checking en contexto @Transactional
    }
}
