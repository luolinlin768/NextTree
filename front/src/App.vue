<template>
  <div class="app-container">
    <!-- 左侧边栏 -->
    <Sidebar class="sidebar" />
    
    <!-- 右侧主内容区 -->
    <main class="main-content">
      <div class="content-container">
      <StatsGrid />
      <TaskCard />
      </div>
    </main>
  </div>
</template>




<script>
import Sidebar from './components/Sidebar.vue'
import StatsGrid from './components/StatsGrid.vue'
import TaskCard from './components/TaskCard.vue'

export default {
  name: 'App',
  // 3. 注册组件
  components: {
    Sidebar,
    StatsGrid,
    TaskCard
  },
}
</script>

