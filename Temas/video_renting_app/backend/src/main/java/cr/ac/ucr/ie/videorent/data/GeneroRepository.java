package cr.ac.ucr.ie.videorent.data;

import cr.ac.ucr.ie.videorent.domain.Genero;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface GeneroRepository extends JpaRepository<Genero, Integer> {
    Optional<Genero> findByNombreIgnoreCase(String nombre);
}
