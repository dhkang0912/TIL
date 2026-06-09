package com.example.demo.repository;

import org.springframework.data.repository.CrudRepository;
import com.example.demo.entity.Article;

import java.util.ArrayList;

public interface ArticleRepository extends CrudRepository<Article, Long> {
    @Override
    ArrayList<Article> findAll(); // Iterable → ArrayList 수정
}
