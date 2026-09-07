package cr.ac.ucr.ie.videorent.data;

import cr.ac.ucr.ie.videorent.domain.Alquiler;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface AlquilerRepository extends JpaRepository<Alquiler, Integer> {

    @Query("SELECT a FROM Alquiler a JOIN FETCH a.pelicula p JOIN FETCH p.genero " +
           "WHERE a.estado = :estado")
    List<Alquiler> findByEstadoConPelicula(@Param("estado") String estado);

    @Query("SELECT a FROM Alquiler a JOIN FETCH a.pelicula p " +
           "WHERE p.id = :peliculaId AND a.estado = 'ACTIVO'")
    Optional<Alquiler> findActivoByPeliculaId(@Param("peliculaId") Integer peliculaId);
}
