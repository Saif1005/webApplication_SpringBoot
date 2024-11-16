package com.example.demo.controller;

import com.example.demo.model.Produit;
import com.example.demo.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/produits")
@CrossOrigin(origins = "*")  // Permet les requêtes CORS depuis le frontend sur localhost:3000
public class ProductController {

    @Autowired
    private ProductService productService;

    // Obtenir tous les produits
    @GetMapping
    public List<Produit> getAllProducts() {
        return productService.getAllProducts();
    }

    // Obtenir un produit par ID
    @GetMapping("/{id}")
    public ResponseEntity<Produit> getProductById(@PathVariable Long id) {
        Optional<Produit> produits = productService.getProductById(id);
        return produits.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Créer un produit
    @PostMapping
    public Produit createProduct(@RequestBody Produit produits) {
        System.out.println("Produit reçu : " + produits);
        return productService.createProduct(produits);
    }

    // Mettre à jour un produit
    @PutMapping("/{id}")
    public ResponseEntity<Produit> updateProduct(@PathVariable Long id, @RequestBody Produit productDetails) {
        Produit updatedProduct = productService.updateProduct(id, productDetails);
        return updatedProduct != null ? ResponseEntity.ok(updatedProduct) : ResponseEntity.notFound().build();
    }

    // Supprimer un produit
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        return productService.deleteProduct(id) ? ResponseEntity.noContent().build() : ResponseEntity.notFound().build();
    }
}
