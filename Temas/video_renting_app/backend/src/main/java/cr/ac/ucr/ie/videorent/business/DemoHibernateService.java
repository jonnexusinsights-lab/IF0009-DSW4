package cr.ac.ucr.ie.videorent.business;

import cr.ac.ucr.ie.videorent.data.PeliculaRepository;
import cr.ac.ucr.ie.videorent.domain.Pelicula;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class DemoHibernateService {

    @PersistenceContext
    private EntityManager entityManager;

    private final PeliculaRepository repository;

    public DemoHibernateService(PeliculaRepository repository) {
        this.repository = repository;
    }

    @Transactional
    public void probarCicloVidaYDirtyChecking(Integer id, String nuevoTitulo) {
        // A. ESTADO TRANSITORIO (Transient)
        Pelicula nueva = new Pelicula();
        nueva.setTitulo("Pelicula Demo Transitoria");

        // B. ESTADO PERSISTENTE (Managed)
        entityManager.persist(nueva);

        // C. DIRTY CHECKING (Guardado automatico sin llamar a .save())
        Pelicula existente = repository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException(
                    "Pelicula no encontrada con ID: " + id));
        
        existente.setTitulo(nuevoTitulo);
        // Al finalizar el metodo transaccional, Hibernate detectara la modificacion
        // en memoria y sincronizara la base de datos ejecutando UPDATE automaticamente.
    }

    @Transactional
    public void probarEstadoDetached(Integer id, String tituloMemoria) {
        Pelicula p = repository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException(
                    "Pelicula no encontrada con ID: " + id));

        // Desasociar del contexto de persistencia (L1 Cache)
        entityManager.detach(p); // Estado DETACHED

        p.setTitulo(tituloMemoria);
        // Al terminar la transaccion, la modificacion NO se guardara en la base de datos
    }
}
