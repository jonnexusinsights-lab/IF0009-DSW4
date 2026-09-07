package cr.ac.ucr.ie.videorent.data;

import cr.ac.ucr.ie.videorent.domain.Actor;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ActorRepository extends JpaRepository<Actor, Integer> {
    List<Actor> findByApellidosContainingIgnoreCase(String apellidos);
}
