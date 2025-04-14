<template>
  <div class="w-full max-w-2xl">
    <div class="bg-white rounded-xl shadow-md p-8">
      <div class="flex flex-col items-center text-center">
        <h1
          class="text-3xl font-bold mb-2 bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 inline-block text-transparent bg-clip-text">
          Image Analysis</h1>
        <p class="text-gray-600 mb-8 max-w-lg">Upload an image and ask questions about its content</p>

        <div class="w-full mb-8 text-center">
          <input type="file" accept="image/*" @change="handleFileUpload" ref="fileInput" class="hidden" />
          <button @click="triggerFileInput"
            class="bg-green-500 hover:bg-green-600 text-white px-8 py-4 rounded-lg font-medium transition-all duration-300 hover:shadow-lg hover:-translate-y-0.5 flex items-center gap-2 mx-auto">
            <span class="text-xl">📷</span>
            Select Image
          </button>
        </div>

        <div v-if="previewImage" class="w-full">
          <img :src="previewImage" alt="Image Preview"
            class="w-full max-h-[400px] object-contain rounded-lg shadow-md mb-6" />

          <div class="flex gap-4 w-full max-w-lg mx-auto">
            <input v-model="question" type="text" placeholder="Ask a question about the image..."
              class="flex-1 px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-green-500 transition-colors"
              @keyup.enter="askQuestion" />
            <button @click="askQuestion"
              class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-lg font-medium transition-all duration-300 hover:shadow-lg hover:-translate-y-0.5 disabled:bg-gray-400 disabled:cursor-not-allowed min-w-[120px] flex items-center justify-center"
              :disabled="!question || isLoading">
              <span v-if="!isLoading">Ask Question</span>
              <span v-else class="animate-spin">⏳</span>
            </button>
          </div>
        </div>

        <div v-if="answer" class="w-full max-w-lg mt-8 p-6 bg-gray-50 rounded-lg border-l-4 border-green-500">
          <h3 class="text-lg font-semibold text-green-500 mb-3">Analysis Result</h3>
          <p class="text-gray-800 text-lg">{{ answer }}</p>
        </div>

        <div v-if="error"
          class="w-full max-w-lg mt-8 p-4 bg-red-50 text-red-600 rounded-lg border-l-4 border-red-500 text-center">
          {{ error }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const fileInput = ref(null)
const previewImage = ref(null)
const question = ref('')
const answer = ref('')
const isLoading = ref(false)
const error = ref('')

const triggerFileInput = () => {
  fileInput.value.click()
}

const handleFileUpload = async (event) => {
  const file = event.target.files[0]
  if (!file) return

  // Reset states first
  answer.value = ''
  error.value = ''
  question.value = ''
  previewImage.value = null  // Clear existing preview

  // Create preview
  const reader = new FileReader()

  reader.onload = (e) => {
    previewImage.value = e.target.result
  }

  reader.onerror = () => {
    error.value = 'Error loading image preview'
    previewImage.value = null
  }

  try {
    reader.readAsDataURL(file)
  } catch (err) {
    error.value = 'Error loading image preview'
    previewImage.value = null
  }
}

const askQuestion = async () => {
  if (!question.value || !fileInput.value.files[0]) return

  isLoading.value = true
  error.value = ''
  answer.value = ''

  try {
    const formData = new FormData()
    formData.append('file', fileInput.value.files[0])
    formData.append('question', question.value)

    const response = await axios.post('http://localhost:8000/ask', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })

    answer.value = response.data.answer
  } catch (err) {
    error.value = 'Error processing your question. Please try again.'
    console.error(err)
  } finally {
    isLoading.value = false
  }
}
</script>
