// ============================================================
//  Archivo: src/main/java/com/pokeservice/jjk/repository/PersonajeRepository.java
// ============================================================
package com.pokeservice.jjk.repository;

import com.pokeservice.jjk.model.Personaje;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface PersonajeRepository extends JpaRepository<Personaje, Long> {

    // Buscar por nombre exacto (insensible a mayúsculas)
    Optional<Personaje> findByNombreIgnoreCase(String nombre);
}