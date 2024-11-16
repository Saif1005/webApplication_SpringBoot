package com.example.demo.service;

import com.example.demo.model.Produit;
import com.example.demo.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    public List<Produit> getAllProducts() {
        return productRepository.findAll();
    }

    public Optional<Produit> getProductById(Long id) {
        return productRepository.findById(id);
    }

    public Produit createProduct(Produit produits) {
        System.out.println("Nom: " + produits.getNom() + ", Prix: " + produits.getPrix());
        return productRepository.save(produits);
    }

    public Produit updateProduct(Long id, Produit productDetails) {
        Optional<Produit> produits = productRepository.findById(id);
        if (produits.isPresent()) {
            Produit existingProduct = produits.get();
            existingProduct.setNom(productDetails.getNom());
            existingProduct.setPrix(productDetails.getPrix());
            return productRepository.save(existingProduct);
        }
        return null;
    }

    public boolean deleteProduct(Long id) {
        Optional<Produit> produits = productRepository.findById(id);
        if (produits.isPresent()) {
            productRepository.deleteById(id);
            return true;
        }
        return false;
    }
}
