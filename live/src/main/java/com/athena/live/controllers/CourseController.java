package com.athena.live.controllers;


import com.athena.live.model.Course;
import com.athena.live.repositories.CourseRepositroy;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static java.lang.String.valueOf;

@RestController
@RequestMapping("/courses")
public class CourseController {
    private CourseRepositroy courseRepositroy;

    public CourseController(CourseRepositroy courseRepositroy){
        this.courseRepositroy = courseRepositroy;
    }

    @GetMapping("/all")
    public List<Course> getAll(){
        List<Course> courses = this.courseRepositroy.findAll();
        return courses;
    }
    @PutMapping
    public void insert(@RequestBody Course _course) {
        this.courseRepositroy.insert(_course);
    }

    @PostMapping
    public void update(@RequestBody Course _course) {
        this.courseRepositroy.save(_course);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable("id") String id){
        this.courseRepositroy.deleteById(id);
    }
}