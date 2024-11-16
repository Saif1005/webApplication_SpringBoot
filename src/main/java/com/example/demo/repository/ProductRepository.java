package com.example.demo.repository;
import com.example.demo.model.Produit;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Produit, Long> {
    // Vous pouvez ajouter des méthodes personnalisées ici si nécessaire
}
