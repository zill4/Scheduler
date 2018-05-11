package api.Athena.model;

import api.Athena.repositories.SubjectRepository;
import api.Athena.repositories.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.List;


@Component
public class DbSeeder implements CommandLineRunner {

    private SubjectRepository subjectRepository;
    private UserRepository userRepository;

    public DbSeeder (SubjectRepository subjectRepository,UserRepository userRepository ){
        this.subjectRepository = subjectRepository;
        this.userRepository = userRepository;
    }

    @Override
    public void run(String... strings) throws Exception{
        User me = new User("zill4", "p1ep1ep1e","justcrisp@outlook.com");

        Subject japanese = new Subject("Japanese","JAPN");
        japanese.addCourse(new Course("12345","JAPN01","1","DA",
                6,"Intro to Japanese","MTWTHF","3:30-4:20",30,
                10,"Kato, Kanako","01/12-03/12","L42","Learn basic Japanese"));
        System.out.println(japanese.getName());

        //Drop all Subjects
        this.subjectRepository.deleteAll();
        this.userRepository.deleteAll();
        //add our subjects to DB
        List<Subject> subjects = Arrays.asList(japanese);
        this.subjectRepository.saveAll(subjects);
        this.userRepository.save(me);
        //this.subjectRepository.save(japanese);

    }



}
