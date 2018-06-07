package com.Athena.rest.model;

import com.Athena.rest.repositories.*;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DbSeeder implements CommandLineRunner {

    private SubjectRepository subjectRepository;
    private UserRepository userRepository;
    private CourseRepository courseRepository;


    public DbSeeder (SubjectRepository subjectRepository, UserRepository userRepository, CourseRepository courseRepository){
        this.courseRepository = courseRepository;
        this.subjectRepository = subjectRepository;
        this.userRepository = userRepository;
    }


    public void run(String... strings) throws Exception {
       // Course k = new Course("borks","ROKT","01","FH","5.0","Rocket 101","TR","6pm-8pm","5.0","10","20","30","Doc","1/9 - 03/20","cupertion","forever me ");
        //Lab lab = new Lab("MTWF","24/7","Lee","4/20","hell");
        //k.setLab_time(lab);

        //final List<Course> ak = Arrays.asList(k);
        //final Subject rockets = new Subject("Rockets", "ROKT", ak);

          //  this.subjectRepository.save(rockets);
            //this.courseRepositroy.save(k);

    }


/*

COURSE MATH1A
    CRN": "30202",
    "Crse": "F001A",
    "Sec": "07",
    "Cmp": "FH",
    "Cred": "5.000",
    "Title": "CALCULUS",
               "Days": "TR",
               "Calendar": "06:00 pm-08:15 pm",
               "Cap": "40",
               "Act": "38",
               "WL Cap": "10",
               "WL Act": "0",
               "Instructor": "Yuh,Ni",
               "Date": "01/08-03/30",
               "Location": "FH 4606",
               "Attribute": "Comm and Analytical Thinking",
               "Lab Calendar": []
               "Lab Calendar": [
                  {
                     "Days": "F",
                     "Calendar": "10:00 am-10:50 am",
                     "Instructor": "Young,Hee,Park,Lee",
                     "Date": "01/08-03/30",
                     "Location": "FH 4603"
                  }
               ]
 */

}
