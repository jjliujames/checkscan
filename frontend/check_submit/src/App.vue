<script setup>
import CheckScanner from './views/CheckScanner.vue'
import Logo from './components/Logo.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <div class="container mx-auto px-4 py-4">
        <Logo />
      </div>
    </header>
    
    <main class="flex-1 flex items-center justify-center p-8">
      <div class="w-full max-w-7xl flex justify-center">
        <CheckScanner />
      </div>
    </main>
    
    <footer class="bg-white border-t border-gray-200 py-4">
      <div class="container mx-auto px-4 text-center text-gray-600 text-sm">
        <p>© 2025 TD AMCB AI2 Financial Crime Analystics</p>
      </div>
    </footer>
  </div>
</template>
