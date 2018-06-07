package com.Athena.rest.repositories;

import com.Athena.rest.model.Subject;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface SubjectRepository extends MongoRepository <Subject, String> {
        //Subject findByInitials(String initials);

       // @Query(value = "{ 'userId' : ?0, 'questions.questionID' : ?1 }", fields = "{ 'questions.questionID' : 1 }")
        //List<PracticeQuestion> findByUserIdAndQuestionsQuestionID(int userId, int questionID);


}
