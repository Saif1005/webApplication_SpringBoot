package com.example.demo.config;

import  com.example.demo.service.ProductService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    // Example of creating a ProductService bean manually
    @Bean
    public ProductService productService() {
        return new ProductService(); // You can inject dependencies here if needed
    }
}
