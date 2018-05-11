package api.Athena.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;
import org.springframework.data.annotation.TypeAlias;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Document(collection="users")
@TypeAlias("user")
public final class User {
    @Field("username")
    @Indexed(name="username", unique=true)
    private final String userName;
    private String firstName;
    private String lastName;
    private final String email;
    private String password;
    @Id
    private long id;

    @PersistenceConstructor
    public User(String userName, String password, String email) {
        this.userName = userName;
        this.email = email;
        this.password = password;
    }

    public User(String userName, String firstName, String lastName, String password, String email) {
        this.userName = userName;
        this.email = email;
        this.password = password;
    }


    public String getUserName() {
        return userName;
    }


    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setPassword(String passwod) {
        this.password = password;
    }

    public String getPassword() {
        return password;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }



}
