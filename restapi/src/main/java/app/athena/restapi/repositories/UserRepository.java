package app.athena.restapi.repositories;

import app.athena.restapi.model.User;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface  UserRepository extends MongoRepository<User,String> {
}
