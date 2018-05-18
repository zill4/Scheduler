package com.athena.live.repositories;

import com.athena.live.model.Subject;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SubjectRepository extends MongoRepository <Subject, String> {
        Subject findByInitials(String initials);

       // @Query(value = "{ 'userId' : ?0, 'questions.questionID' : ?1 }", fields = "{ 'questions.questionID' : 1 }")
        //List<PracticeQuestion> findByUserIdAndQuestionsQuestionID(int userId, int questionID);


}
