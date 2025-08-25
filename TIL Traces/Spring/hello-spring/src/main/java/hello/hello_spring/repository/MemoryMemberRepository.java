package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberReopsitory{
    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
//        Optional로 감싸서 null이어도 반환할 수 있게 해줌 => 반환이후 조작할 수 있음
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
//        람다를 써서 필터링, 이름이 같은 경우에만 필터링됨, 루프를 돌면서 하나라도 찾는 것, 없으면 null로 반환
        return store.values().stream().filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
//        members를 의미
        return new ArrayList<>(store.values());
    }

    public void clearStore(){
        store.clear();
    }
}
