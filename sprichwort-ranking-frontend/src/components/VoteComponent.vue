<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import SprichwortComponent from '../components/SprichwortComponent.vue';


onMounted(() => {
    getMatch();
});

const error = ref()

const sprichwortMatch = ref()

const getMatch = async () => {
    try {
        const response = await axios.get(`${import.meta.env.VITE_APP_BASEURL}/match`);
        sprichwortMatch.value = response.data; // Assign the API response
    } catch (err) {
        error.value = (err as Error).message; // Handle the error
        console.error('API Error:', err);
    }
}

const processVote = async (idOfWinner: number, index: number) => {
    const idOfLoser = sprichwortMatch.value[1 - index].id
    try {
        const response = await axios.post(`${import.meta.env.VITE_APP_BASEURL}/processvote`, { idOfWinner: idOfWinner, idOfLoser: idOfLoser });
        //  sprichwortMatch.value = response.data; // Assign the API response
        console.log(response.data)

        getMatch()

    } catch (err) {
        error.value = (err as Error).message; // Handle the error
        console.error('API Error:', err);
        alert(err)
    }
}


</script>

<template>
    <div class="greetings">
        <h2>
            Welches Sprichwort ist cooler?
        </h2>
    </div>

    <div class="vote-container">
        <SprichwortComponent v-for="(item, index) in sprichwortMatch" :key="index" :content="item.content"
            :explanation="item.explanation" :icon="item.icon" :list="false" :rank="0"
            @click="processVote(item.id, index)" />
    </div>
</template>

<style scoped></style>
