package api.Athena.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.IndexDirection;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.Map;

@Document(collection = "Subjects")
public class Subject {


    @Indexed(direction = IndexDirection.DESCENDING) //Ordered from A-Z
    private final String name;
    @Id
    private final String initials; //JAPN
    private  Map<String,ArrayList<Course>> courses; // { JAPN01 : [Crs: ... ] }


    Subject(String name, String initials){
        this.name = name;
        this.initials = initials;
    }


    public String getName() {
        return name;
    }

    public String getInitials() {
        return initials;
    }

    //Returns a list of list of courses.
    /*
        AL_Courses{
            MATH1A - 1
            MATH1A - 2
            MATH1A - 3
            }
         AL_Courses{
            MATH1B - 1
            MATH1B - 2
            ...
            }
     */

    public ArrayList<ArrayList<Course>> getCourses(){
            ArrayList<ArrayList<Course>> course = new ArrayList<>();
        for(String courseId: courses.keySet()){
            String key = name.toString();
             ArrayList<Course> _courses = courses.get(name);
             course.add(_courses);
        }
        return course;
    }

    public void addCourse(Course course){
        if( courses.get(course.getCourseCode()) != null){
            //Create a new ArrayList of courses and add to map.
            ArrayList<Course> courseArray = new ArrayList<Course>();
            courseArray.add(course);
            //Puts (course ID, Array List of Courses)
            courses.put(course.getCourseCode(),courseArray);
        } else {
            courses.get(course.getCourseCode()).add(course);
        }
    }

}
