package cr.ac.ucr.ie.videorent.data;

import cr.ac.ucr.ie.videorent.domain.Review;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ReviewRepository extends JpaRepository<Review, Integer> {

    List<Review> findByPeliculaId(Integer peliculaId);

    // Consulta de modificacion masiva con anotacion @Modifying y limpieza de L1 Cache
    @Modifying(clearAutomatically = true)
    @Query("UPDATE Review r SET r.comentario = CONCAT('[ARCHIVADA] ', r.comentario) " +
           "WHERE r.calificacion <= :calificacionMax")
    int archivarResenasBajas(@Param("calificacionMax") int calificacionMax);
}
