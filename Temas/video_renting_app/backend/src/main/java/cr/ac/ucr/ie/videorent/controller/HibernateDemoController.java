package cr.ac.ucr.ie.videorent.controller;

import cr.ac.ucr.ie.videorent.business.DemoHibernateService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/demo-hibernate")
@CrossOrigin(origins = "*")
@Tag(name = "Demo Hibernate", description = "Endpoints demostrativos de Ciclo de Vida y Dirty Checking")
public class HibernateDemoController {

    private final DemoHibernateService demoHibernateService;

    public HibernateDemoController(DemoHibernateService demoHibernateService) {
        this.demoHibernateService = demoHibernateService;
    }

    @PostMapping("/dirty-checking/{id}")
    @Operation(summary = "Demostrar guardado automatico por Dirty Checking")
    public ResponseEntity<String> testDirtyChecking(@PathVariable Integer id, 
                                                    @RequestParam String nuevoTitulo) {
        demoHibernateService.probarCicloVidaYDirtyChecking(id, nuevoTitulo);
        return ResponseEntity.ok("Demostracion ejecutada. Verifique la sentencia UPDATE en consola.");
    }

    @PostMapping("/detached/{id}")
    @Operation(summary = "Demostrar que en estado Detached los cambios no se guardan")
    public ResponseEntity<String> testDetached(@PathVariable Integer id, 
                                               @RequestParam String tituloMemoria) {
        demoHibernateService.probarEstadoDetached(id, tituloMemoria);
        return ResponseEntity.ok("Demostracion ejecutada. El titulo no fue guardado en base de datos.");
    }
}
