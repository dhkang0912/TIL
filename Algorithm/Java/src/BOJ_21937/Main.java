package BOJ_21937;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    // 런타임 시 제네릭 배열 금지 규칙으로 인해 graph가 먼저 선언됨
    // 배열 기반 시 속도가 더 빠름
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static void dfs(int node){
        visited[node] = true;
        for (int next : graph[node] ){
            if(!visited[next]){
                dfs(next);
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 작업 개수
        int m = Integer.parseInt(st.nextToken()); // 작업 순서의 개수

        // 그래프 초기화
        // 선언된 그래프의 크기를 선언
        graph = new ArrayList[n + 1];
        // 이차원 배열 하당
        for (int i = 0; i <=n; i++){
            graph[i] = new ArrayList<>();
        }

        // 그래프 입력 B->A
        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine().trim());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[y].add(x);
        }

        visited = new boolean[n+1];

        int target = Integer.parseInt(br.readLine().trim());

        // DFS 탐색
        dfs(target);

        // 방문 노드 개수 출력 (자기 자신 제외)
        int result = -1;
        for (int i = 1; i<=n; i++){
            if (visited[i]){
                result++;
            }
        }

        System.out.println(result);

    }
}
