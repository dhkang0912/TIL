package hello.hello_spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model){
        model.addAttribute("data","hello!!");
//        hello라는 템플릿을 찾아서 해당 모델을 반환해라
        return "hello";
    }

//    템플릿에 있는 HTML을 조작해서 보여줌
    @GetMapping("hello-mvc")
//    모델의 키값이 name인 데이터를 매칭하여 전달
    public String helloMvc(@RequestParam("name") String name, Model model){
        model.addAttribute("name",name);
        return "hello-template";
    }

//    데이터를 그대로 보내줌
    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam String name){
        return "hello " + name;
    }

    @GetMapping("hello-api")
//    Jackson이라는 라이브러리를 통해서 ResponseBody가 있으면 자동으로 JSON으로 변환함
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello = new Hello();
        hello.setName(name);
//        키:밸류로 이루어진 JSON
        return hello;
    }
    static class Hello{
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }


}
