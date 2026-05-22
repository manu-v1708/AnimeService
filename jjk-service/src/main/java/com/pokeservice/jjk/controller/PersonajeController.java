// ============================================================
//  Archivo: src/main/java/com/pokeservice/jjk/controller/PersonajeController.java
// ============================================================
package com.pokeservice.jjk.controller;

import com.pokeservice.jjk.model.Personaje;
import com.pokeservice.jjk.repository.PersonajeRepository;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.Optional;

@RestController
@CrossOrigin(origins = "*")   // Permite peticiones desde GitHub Pages
@Tag(name = "Jujutsu Kaisen", description = "Consulta personajes de JJK")
public class PersonajeController {

    private final PersonajeRepository repo;

    public PersonajeController(PersonajeRepository repo) {
        this.repo = repo;
    }

    // ── Health-check ──────────────────────────────────────
    @GetMapping("/")
    @Operation(summary = "Health-check", description = "Verifica que el servidor esté activo")
    public ResponseEntity<Map<String, String>> healthCheck() {
        return ResponseEntity.ok(Map.of(
            "message", "🚀 JJK Service en línea",
            "version", "1.0.0 – Spring Boot + Supabase"
        ));
    }

    // ── GET /personaje/{nombre} ───────────────────────────
    @GetMapping("/personaje/{nombre}")
    @Operation(
        summary = "Consultar personaje por nombre",
        description = "Devuelve los datos completos de un personaje de Jujutsu Kaisen"
    )
    public ResponseEntity<?> getPersonaje(
        @Parameter(description = "Nombre del personaje (ej: satoru gojo)", example = "satoru gojo")
        @PathVariable String nombre
    ) {
        Optional<Personaje> resultado = repo.findByNombreIgnoreCase(nombre.trim());

        if (resultado.isEmpty()) {
            return ResponseEntity.status(404).body(
                Map.of("error", "Personaje \"" + nombre.toLowerCase() + "\" no encontrado")
            );
        }

        return ResponseEntity.ok(resultado.get());
    }
}