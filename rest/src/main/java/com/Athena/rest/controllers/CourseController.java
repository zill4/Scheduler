package com.Athena.rest.controllers;


import com.Athena.rest.model.Course;
import com.Athena.rest.repositories.CourseRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;



@RestController
@RequestMapping("/courses")
public class CourseController {
    private CourseRepository courseRepository;

    public CourseController(CourseRepository courseRepository){
        this.courseRepository = courseRepository;
    }

    @GetMapping("/all")
    public List<Course> getAll(){
        List<Course> courses = this.courseRepository.findAll();
        return courses;
    }
    @PutMapping
    public void insert(@RequestBody Course _course) {
        this.courseRepository.insert(_course);
    }

    @PostMapping
    public void update(@RequestBody Course _course) {
        this.courseRepository.save(_course);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable("id") String id){
        this.courseRepository.delete(id);
    }
}