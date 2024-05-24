<template>
    <div class="password-card" v-if="!isConfirmed">
        <div class="password-title">
            <h2>비밀번호 확인</h2>
        </div>
        <form @submit.prevent="passwordCheck">
            <div class="review-submit">
                <label for="password">비밀번호 확인 :</label>&ThickSpace;
                <input type="password" name="password" id="password" v-model.trim="password" style="margin-right: 10px;">
                <input type="submit" value="submit" style=" border-radius: 10px; background-color: #828282; color: aliceblue;">
            </div>
        </form>
    </div>
    <div class="infoEdit" v-else>
        <MyPageUserEditDetail />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import MyPageUserEditDetail from './MyPageUserEditDetail.vue';
import { useAccountStore } from '@/stores/account';

const AccountStore = useAccountStore()

const isConfirmed = ref(false)
const password = ref(null)

const passwordCheck = function () {
    axios({
        method: 'POST',
        url: `${AccountStore.url}/accounts/password_check/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {
            password: password.value
        }
    }).then((res) => {
        isConfirmed.value = true
        alert('검증 완료!')
    }).catch((err) => {
        console.log(err)
        alert('비밀번호가 일치하지 않습니다.')
    })
}
</script>

<style scoped>
.review-submit {
    display: flex;
    justify-content: center;
    height: 30px;
    width: 100%;
}

.password-card {
    width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 40px;
    padding: 0 20px;
    height: 600px;
    box-sizing: border-box;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center; /* 중앙 정렬 */
    justify-content: center;
    position: relative;
}

.password-title{
    position: absolute; /* 자식 요소를 절대적으로 위치시킴 */
    top: 25%; /* 부모 요소의 상단에 고정 */
    left: 0;
    width: 100%;

}

#review-text{
    width: 450px;
}

.infoEdit{
width: 100%;
min-height: 620px;
}
</style>