// ============================================================
//  Archivo: src/main/java/com/pokeservice/jjk/model/Personaje.java
// ============================================================
package com.pokeservice.jjk.model;

import jakarta.persistence.*;
import lombok.Data;

@Data                          // Lombok genera getters, setters, toString
@Entity
@Table(name = "jjk_personajes")
public class Personaje {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String nombre;

    @Column(nullable = false)
    private String altura;

    @Column(nullable = false)
    private String peso;

    @Column(nullable = false)
    private String grado;

    @Column(nullable = false)
    private String tecnica;

    @Column(nullable = false)
    private String clan;

    @Column(nullable = false)
    private String imagen;
}