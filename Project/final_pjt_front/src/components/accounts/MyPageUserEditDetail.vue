<template>
    <div class="password-change">
        <div class="password-title">
            <h2>비밀번호 변경</h2>
        </div>
        <form @submit.prevent="editPassword">
            <div class="password-submit">
                <label for="password1">새 비밀번호 :</label>&ThickSpace;
                <input type="password" name="password1" id="password1" v-model.trim="password1" style="margin-right: 10px;">&ThickSpace;
                <label for="password1">  비밀번호 확인 :</label>&ThickSpace;
                <input type="password" name="password2" id="password2" v-model.trim="password2" style="margin-right: 10px;">
                <input type="submit" value="submit" style=" border-radius: 10px; background-color: #828282; color: aliceblue;">
            </div>
        </form>
    </div>
    <div class="password-change">
        <div class="password-title">
            <h2>닉네임 변경</h2>
        </div>
        <form @submit.prevent="editNickname">
            <div class="password-submit">
                <input type="text" name="nickname" v-model.trim="nickname" style="margin-right: 10px;">
                <input type="submit" value="submit" style=" border-radius: 10px; background-color: #828282; color: aliceblue;">
            </div>
        </form>
    </div>
    <div class="password-change">
        <div class="password-title">
            <h2>회원탈퇴</h2>
            <p><i class="fa-solid fa-exclamation"></i><i class="fa-solid fa-exclamation"></i>회원 탈퇴 시 추천 서비스를 제공 받지 못합니다.</p>
            <p>정말 탈퇴하시겠습니까?</p>
        </div>
        <form @submit.prevent="signOut">
            <div class="password-submit">
                <label for="signOut">동의하면 클릭!</label>&ThinSpace;
                <input type="checkbox" id="signOut" v-model="signOutBool" style="margin-right: 10px;">
                <input type="submit" value="submit" style=" border-radius: 10px; background-color: #828282; color: aliceblue;">
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useAccountStore } from '@/stores/account';
import router from '@/router';

const AccountStore = useAccountStore()

const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const signOutBool = ref(false)

const editPassword = function () {
    axios({
        method: 'POST',
        url: `${AccountStore.url}/dj_rest_auth/password/change/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {
            new_password1: password1.value,
            new_password2: password2.value,
        }
    }).then((res) => {
        console.log(res)
        password1.value = ''
        password2.value = ''
        alert('비밀번호가 변경되었습니다.')
    }).catch((err) => {
        console.log(err)
    })
}

const editNickname = function () {
    axios({
        method: 'PUT',
        url: `${AccountStore.url}/accounts/nickname/`,
        headers: {
            Authorization: `Token ${AccountStore.token}`
        },
        data: {
            nickname: nickname.value,
        }
    }).then((res) => {
        AccountStore.user.nickname = nickname.value
        alert(`닉네임이 "${nickname.value}"(으)로 변경되었습니다.`)
        nickname.value = ''
    }).catch((err) => {
        alert(`${nickname.value}은/는 중복된 닉네임입니다.`)
    })
}

const signOut = function () {
    if (signOutBool.value) {
        if (confirm('진짜로? 정말로?')) {
            axios({
                method: 'DELETE',
                url: `${AccountStore.url}/accounts/signout/`,
                headers: {
                    Authorization: `Token ${AccountStore.token}`
                },
            }).then((res) => {
                console.log(res)
                AccountStore.token = ''
                localStorage.removeItem('token'); // Remove the token from local storage
                AccountStore.isLogin = false

                router.push({ name: 'HomeView' }).then(() => {
                    // Refresh the page after navigating
                    alert('또 만나요~')
                    window.location.reload()
                })
            })
        }
    } else {
        alert('동의에 체크해 주세요!')
    }
}
</script>

<style scoped>
.password-submit {
    display: flex;
    justify-content: center;
    height: 30px;
    width: 100%;
}

h2 {
    margin-top: 0;
    margin-bottom: 10;
}

.password-change {
    width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 40px;
    padding: 20px;
    height: fit-content;
    box-sizing: border-box;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* 중앙 정렬 */
}

.fa-exclamation {
    color: red;
}

input[type=checkbox] {
    zoom: 1.5;
}
</style>