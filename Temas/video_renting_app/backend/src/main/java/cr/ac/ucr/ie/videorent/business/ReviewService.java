package cr.ac.ucr.ie.videorent.business;

import cr.ac.ucr.ie.videorent.data.PeliculaRepository;
import cr.ac.ucr.ie.videorent.data.ReviewRepository;
import cr.ac.ucr.ie.videorent.domain.Pelicula;
import cr.ac.ucr.ie.videorent.domain.Review;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class ReviewService {

    private final ReviewRepository reviewRepository;
    private final PeliculaRepository peliculaRepository;

    public ReviewService(ReviewRepository reviewRepository, 
                           PeliculaRepository peliculaRepository) {
        this.reviewRepository = reviewRepository;
        this.peliculaRepository = peliculaRepository;
    }

    @Transactional(readOnly = true)
    public List<Review> obtenerPorPelicula(Integer peliculaId) {
        return reviewRepository.findByPeliculaId(peliculaId);
    }

    @Transactional
    public Review agregarReviewAPelicula(Integer peliculaId, Review review) {
        Pelicula pelicula = peliculaRepository.findById(peliculaId)
                .orElseThrow(() -> new IllegalArgumentException(
                    "Pelicula no encontrada con ID: " + peliculaId));
        pelicula.addReview(review);
        return reviewRepository.save(review);
    }

    @Transactional
    public int archivarResenasConBajaCalificacion(int calificacionMax) {
        return reviewRepository.archivarResenasBajas(calificacionMax);
    }
}
