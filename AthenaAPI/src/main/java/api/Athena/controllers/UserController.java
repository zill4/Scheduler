package api.Athena.controllers;

import api.Athena.model.User;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;



@RestController
public class UserController {
    private Map<Long, User> users = new HashMap<Long, User>();
    private AtomicLong nextId = new AtomicLong();


    @PostMapping("/user")
    @ResponseStatus(HttpStatus.CREATED)
    public User createUser(@RequestBody User user){
        //Set user to have next id
        user.setId(nextId.incrementAndGet());
        users.put(user.getId(),user);
        return user;
    }

    @GetMapping("/user")
    public Map<Long, User> getAllUsers(){
        return users;
    }

    @GetMapping("/user/{id}")
    public User getUser(@PathVariable("id") long id){

        if(users.get(id) != null){
            return users.get(id);
        } else{
            throw new IllegalArgumentException();

        }
    }

    @PostMapping("/user/{id}")
    public User editUser(@PathVariable("id") Long id,
                         @RequestBody User user){
        if(users.get(id) != null){
            return users.put(id,user);
        } else{
            throw new IllegalArgumentException();

        }

    }

    //ExceptionHandler
    @ResponseStatus(value = HttpStatus.BAD_REQUEST, reason = "Request ID not found")
    @ExceptionHandler(IllegalArgumentException.class)
    public void badIdException(){}


}
