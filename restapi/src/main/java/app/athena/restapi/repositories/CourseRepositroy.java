package app.athena.restapi.repositories;

import app.athena.restapi.model.Course;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CourseRepositroy extends MongoRepository<Course, String> {
}

