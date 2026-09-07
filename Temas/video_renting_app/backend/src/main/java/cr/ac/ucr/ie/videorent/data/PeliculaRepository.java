package cr.ac.ucr.ie.videorent.data;

import cr.ac.ucr.ie.videorent.domain.Pelicula;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface PeliculaRepository extends JpaRepository<Pelicula, Integer> {

    List<Pelicula> findByTituloContainingIgnoreCase(String titulo);

    List<Pelicula> findByEstrenoTrue();

    // Consulta JPQL optimizada con JOIN FETCH para prevenir el problema N+1 SELECT
    @Query("SELECT DISTINCT p FROM Pelicula p LEFT JOIN FETCH p.reviews")
    List<Pelicula> obtenerPeliculasConReviewsOptimizadas();

    // Consulta con JOIN FETCH por identificador unico
    @Query("SELECT p FROM Pelicula p LEFT JOIN FETCH p.reviews WHERE p.id = :id")
    Optional<Pelicula> findByIdConReviews(@Param("id") Integer id);
}
