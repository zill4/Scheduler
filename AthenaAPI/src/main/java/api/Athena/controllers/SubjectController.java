package api.Athena.controllers;

import api.Athena.model.Subject;
import api.Athena.repositories.SubjectRepository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/subjects")
public class SubjectController {

    private SubjectRepository subjectRepository;

    public  SubjectController(SubjectRepository subjectRepository){
            this.subjectRepository = subjectRepository;
    }

    @GetMapping("/all")
    public List<Subject> getAll(){
        List<Subject> subjects = this.subjectRepository.findAll();

        return subjects;
    }

}
