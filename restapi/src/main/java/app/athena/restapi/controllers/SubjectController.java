package app.athena.restapi.controllers;

import app.athena.restapi.model.Subject;
import app.athena.restapi.repositories.SubjectRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/subjects")
public class SubjectController {

        private SubjectRepository subjectRepository;

        public SubjectController (SubjectRepository subjectRepository){
            this.subjectRepository= subjectRepository;
        }

        @GetMapping("/all")
        public List<Subject> getAll(){
            List<Subject> subjects = this.subjectRepository.findAll();
            return subjects;
        }


        @PutMapping
        public void insert(@RequestBody Subject subject) {
            this.subjectRepository.insert(subject);
        }

        @PostMapping
        public void update(@RequestBody Subject subject) {
            this.subjectRepository.save(subject);
        }



}
