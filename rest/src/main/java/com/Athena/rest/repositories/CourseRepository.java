package com.Athena.rest.repositories;

import com.Athena.rest.model.Course;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CourseRepository extends MongoRepository<Course, String> {

    Course findByTitle(String title);
}

