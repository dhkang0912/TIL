package com.example.demo.dto;

import com.example.demo.entity.Article;

public class ArticleForm {
    private String title;
    private String content;
    private Long id;

    public ArticleForm(String content, String title) {
        this.content = content;
        this.title = title;
    }

    @Override
    public String toString() {
        return "ArticleForm{" +
                "title='" + title + '\'' +
                ", content='" + content + '\'' +
                '}';
    }

    public Article toEntity() {
        return new Article(null, title, content);
    }
}
