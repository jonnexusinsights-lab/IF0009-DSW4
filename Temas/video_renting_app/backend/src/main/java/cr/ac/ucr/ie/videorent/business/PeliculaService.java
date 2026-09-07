package cr.ac.ucr.ie.videorent.business;

import cr.ac.ucr.ie.videorent.data.PeliculaRepository;
import cr.ac.ucr.ie.videorent.domain.Pelicula;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class PeliculaService {

    private final PeliculaRepository peliculaRepository;

    public PeliculaService(PeliculaRepository peliculaRepository) {
        this.peliculaRepository = peliculaRepository;
    }

    @Transactional(readOnly = true)
    public List<Pelicula> obtenerTodas() {
        return peliculaRepository.findAll();
    }

    @Transactional(readOnly = true)
    public Optional<Pelicula> obtenerPorId(Integer id) {
        return peliculaRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public Optional<Pelicula> obtenerPorIdConReviews(Integer id) {
        return peliculaRepository.findByIdConReviews(id);
    }

    @Transactional(readOnly = true)
    public List<Pelicula> obtenerTodasOptimizadasConReviews() {
        return peliculaRepository.obtenerPeliculasConReviewsOptimizadas();
    }

    @Transactional
    public Pelicula guardar(Pelicula pelicula) {
        return peliculaRepository.save(pelicula);
    }

    @Transactional
    public void eliminar(Integer id) {
        peliculaRepository.deleteById(id);
    }
}
