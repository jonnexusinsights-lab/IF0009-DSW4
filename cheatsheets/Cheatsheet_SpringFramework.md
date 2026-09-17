# 🍃 Hoja de Referencia Rápida: Spring Framework (IoC & Inyección)

---

## 📌 1. Anotaciones de Componentes e Inyección (IoC)

Spring Framework se basa en **Inversión de Control (IoC)** e **Inyección de Dependencias (DI)** para conectar Beans dentro del `ApplicationContext`.

| Anotación | Propósito | Ejemplo |
| :--- | :--- | :--- |
| **`@Component`** | Anotación genérica para registrar un Bean. | `@Component` |
| **`@Service`** | Especialización para lógica de negocio. | `@Service` |
| **`@Repository`** | Capa de acceso a datos y traducción de SQL. | `@Repository` |
| **`@Controller`** | Controlador Web MVC para vistas HTML. | `@Controller` |
| **`@RestController`**| Controlador REST con `@ResponseBody`. | `@RestController` |
| **`@Configuration`**| Clase contenedora de definiciones `@Bean`. | `@Configuration` |
| **`@Bean`** | Define un Bean sobre métodos de fábrica. | `@Bean` |
| **`@Autowired`** | Inyecta dependencia automáticamente por tipo. | `@Autowired` |
| **`@Qualifier`** | Desambigua entre múltiples Beans. | `@Qualifier("sms")` |
| **`@Primary`** | Establece el Bean preferido por defecto. | `@Primary` |
| **`@Value`** | Inyecta propiedades o expresiones SpEL. | `@Value("${app.desc}")`|
| **`@Lazy`** | Retarda la inicialización del Bean. | `@Lazy` |

---

## 🏗️ 2. Estilos de Inyección de Dependencias

### A. Inyección por Constructor (Estándar Recomendado)

```java
@Service
public class ClienteService {

    private final ClienteRepository clienteRepository;
    private final NotificadorService notificadorService;

    // En Spring 4.3+, @Autowired es implícito
    public ClienteService(ClienteRepository repo, 
                          NotificadorService notificador) {
        this.clienteRepository = repo;
        this.notificadorService = notificador;
    }
}
```

### B. Inyección por Campo (No Recomendada)

```java
@Service
public class PedidoService {
    @Autowired // Inyeccion directa por campo
    private PedidoRepository pedidoRepository;
}
```

---

## 🔄 3. Ciclo de Vida del Bean y Alcances (Scopes)

| Alcance (Scope) | Descripción | Anotación |
| :--- | :--- | :--- |
| **`singleton`** | *(Por defecto)* Instancia única global. | `@Scope("singleton")` |
| **`prototype`** | Nueva instancia en cada petición. | `@Scope("prototype")` |
| **`request`** | Instancia por cada petición HTTP. | `@RequestScope` |
| **`session`** | Instancia por cada sesión HTTP. | `@SessionScope` |

```java
@Component
public class ConexionExternaService {

    @PostConstruct
    public void inicializar() {
        System.out.println("Conexion inicializada.");
    }

    @PreDestroy
    public void limpiar() {
        System.out.println("Conexion cerrada.");
    }
}
```

---

## 🌐 4. Expresiones SpEL (Spring Expression Language)

```java
@Component
public class CalculadoraDescuento {

    @Value("#{systemProperties['user.language']}")
    private String idiomaSistema;

    @Value("#{tasaService.obtenerTasa() * 1.13}")
    private double tasaCalculada;

    @Value("#{pedido.monto > 50000 ? 0.10 : 0.05}")
    private double porcentajeDescuento;
}
```

---

## 📂 5. Perfiles de Entorno (`@Profile`)

```java
@Configuration
@Profile("dev")
public class DevDatabaseConfig {

    @Bean
    public DataSource dataSource() {
        return new EmbeddedDatabaseBuilder()
            .setType(EmbeddedDatabaseType.H2)
            .build();
    }
}
```
