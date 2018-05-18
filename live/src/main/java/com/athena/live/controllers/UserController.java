package com.athena.live.controllers;


import com.athena.live.model.User;
import com.athena.live.repositories.UserRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/users")
public class UserController {

    private UserRepository userRepository;

    public UserController (UserRepository userRepository){
        this.userRepository = userRepository;
    }

    @GetMapping("/all")
    public List<User> getAll(){
        List<User> users = this.userRepository.findAll();
        return users;
    }


    @PutMapping
    public void insert(@RequestBody User user) {
        this.userRepository.insert(user);
    }


    @PostMapping
    public void update(@RequestBody User user) {
        this.userRepository.save(user);
    }

}