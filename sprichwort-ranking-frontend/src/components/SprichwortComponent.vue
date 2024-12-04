<script setup lang="ts">
import {
    computed
} from 'vue';



const customStyle = computed(() => ({
    cursor: props.list ? 'default' : 'pointer',
    transition: props.list ? 'none' : 'transform 0.1s ease-out',
    transform: 'scale(1)',
    ':active': props.list ? {} : {
        transform: 'scale(0.98)'
    }
}))

const props = defineProps<{
    content: string,
    explanation: string,
    icon: string,
    rank: number,
    list: boolean
}>()
</script>

<template>
    <div class="sprichwort-container" :style="customStyle">
        <p class="sprichwort" v-if="props.list">#{{ rank }}</p>
        <p class="sprichwort" v-else>„</p>
        <p class="sprichwort"> {{ props.content }}</p>
        <p class="erklaerung"> {{ props.explanation }}</p>
        <i class="material-icons">{{ icon }}</i>
    </div>
</template>

<style scoped>
.sprichwort {
    font-weight: bold;
    font-family: 'Georgia', Times, serif;
    font-size: 1.25em;
    /* color: var(--vt-c-text-dark-1) */

}

.erklaerung {
    font-family: 'Georgia', Times, serif;
    font-style: italic;
    /* color: var(--vt-c-text-dark-2) */
}

.sprichwort-container {
    cursor: pointer;
    /* background-color: var(--vt-c-text-dark-1); */
    margin: 1em 0 1em 0;
    outline: 1px var(--color-text) solid;
    outline-offset: -0.5em;
    border-radius: 1em;
    display: flex;
    padding: 2em;
    flex-direction: column;
    align-items: left;
    justify-content: center;
}
</style>
