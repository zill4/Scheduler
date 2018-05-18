package com.athena.live.model;


import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;

import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@Document(collection="users")
public  class User {
    //Critical for account creation
    private  String userName;
    private  String email;
    private  String password;
    //User customization
    private String firstName;
    private String lastName;
    //User class information
    private Schedule schedule;
    private List<Course> courses;
    @Id
    private String id;

    public User(){}

    @PersistenceConstructor
    public User(String userName, String password, String email) {
        this.userName = userName;
        this.email = email;
        this.password = password;
    }

    public User(String userName, String password, String email, String firstName, String lastName){
        this.userName = userName;
        this.email = email;
        this.password =password;
        this.firstName =firstName;
        this.lastName = lastName;
    }




    public String getUserName() {
        return userName;
    }



    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }


    public String getPassword() {
        return password;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }



}
