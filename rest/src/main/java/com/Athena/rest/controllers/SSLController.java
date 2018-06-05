package com.Athena.rest.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SSLController {

    @RequestMapping(value="/test/ssl")
    public String testSSL(){
        return "Success";
    }


}
