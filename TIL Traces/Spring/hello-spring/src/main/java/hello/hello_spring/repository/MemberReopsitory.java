package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberReopsitory {
    Member save(Member member);
//    Optional : 자바 8에서 나온 기능으로 만약 없으면 null처리 해줌
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();

}
