package com.athena.live.repositories;

import com.athena.live.model.Course;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CourseRepositroy extends MongoRepository<Course, String> {
}

