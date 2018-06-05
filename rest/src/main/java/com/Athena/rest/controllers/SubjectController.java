package com.Athena.rest.controllers;

import com.Athena.rest.model.Subject;
import com.Athena.rest.repositories.SubjectRepository;
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
