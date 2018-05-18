package com.athena.live.model;


import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;
import org.springframework.data.annotation.TypeAlias;
import org.springframework.data.mongodb.core.index.IndexDirection;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;


@Document(collection = "Subjects")
@TypeAlias("subject")
public class Subject {
    //VARIABLES
    private String name;
    @Id
    private String initials; //JAPN
    private List<Course> courses;
    //CONSTRUCTORS
    public Subject() {
    }

    public Subject(String name, String initials) {
        this.name = name;
        this.initials = initials;
    }

    @PersistenceConstructor
    public Subject(String name, String initials, List<Course> courses) {
        this.name = name;
        this.initials = initials;
        this.courses = courses;
    }
    //MUTATORS/ACCESSORS
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getInitials() {
        return initials;
    }

    public void setInitials(String initials) {
        this.initials = initials;
    }

    public List<Course> getCourses() {
        return courses;
    }

    public void setCourses(List<Course> courses) {
        this.courses = courses;
    }
}


