<template>
  <div class="tasks-section">
    <h2>最近任务</h2>
    <div class="tasks-grid">
      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            <div class="task-title">网站重构项目</div>
          </div>
          <span class="badge high">高</span>
        </div>
        <div class="task-content">
          <p class="task-description">完成公司官网的技术重构，包括前端性能优化和后端API重写，确保兼容移动设备和现代浏览器标准。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>65%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator blue" style="width: 65%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2024-01-15</span>
            </div>
            <span class="badge in-progress">进行中</span>
          </div>
          <div class="subtasks">子任务: 5/8</div>
        </div>
      </div>

      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <div class="task-title">季度报告</div>
          </div>
          <span class="badge medium">中</span>
        </div>
        <div class="task-content">
          <p class="task-description">准备并提交第三季度财务和运营报告，包括收入分析、支出报告和下一季度预测。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>100%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator green" style="width: 100%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2023-12-30</span>
            </div>
            <span class="badge completed">已完成</span>
          </div>
          <div class="subtasks">子任务: 7/7</div>
        </div>
      </div>

      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon red" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
              <line x1="12" y1="9" x2="12" y2="13"></line>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
            <div class="task-title">服务器迁移</div>
          </div>
          <span class="badge high">高</span>
        </div>
        <div class="task-content">
          <p class="task-description">将生产服务器从旧数据中心迁移到新的云基础设施，确保零停机时间和数据完整性。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>30%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator red" style="width: 30%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2023-12-15</span>
            </div>
            <span class="badge overdue">已逾期</span>
          </div>
          <div class="subtasks">子任务: 3/10</div>
        </div>
      </div>

      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="9" y1="9" x2="15" y2="15"></line>
              <line x1="15" y1="9" x2="9" y2="15"></line>
            </svg>
            <div class="task-title">UI设计评审</div>
          </div>
          <span class="badge medium">中</span>
        </div>
        <div class="task-content">
          <p class="task-description">评审并批准新产品的UI设计，提供反馈并与设计团队协作进行必要的调整。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>45%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator blue" style="width: 45%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2024-01-05</span>
            </div>
            <span class="badge in-progress">进行中</span>
          </div>
          <div class="subtasks">子任务: 2/5</div>
        </div>
      </div>

      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon blue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 20h9"></path>
              <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
            </svg>
            <div class="task-title">文档更新</div>
          </div>
          <span class="badge low">低</span>
        </div>
        <div class="task-content">
          <p class="task-description">更新API文档以反映最新的端点变更，包括参数说明和示例代码。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>75%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator blue" style="width: 75%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2024-01-10</span>
            </div>
            <span class="badge in-progress">进行中</span>
          </div>
          <div class="subtasks">子任务: 3/4</div>
        </div>
      </div>

      <div class="task-card">
        <div class="task-header">
          <div class="task-title-container">
            <svg class="task-icon green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
              <polyline points="14 2 14 8 20 8"></polyline>
              <line x1="16" y1="13" x2="8" y2="13"></line>
              <line x1="16" y1="17" x2="8" y2="17"></line>
              <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            <div class="task-title">会议纪要</div>
          </div>
          <span class="badge low">低</span>
        </div>
        <div class="task-content">
          <p class="task-description">整理并分发上周战略会议的纪要，突出关键决策和行动项。</p>
          <div class="task-progress">
            <div class="progress-info">
              <span>进度</span>
              <span>100%</span>
            </div>
            <div class="progress-bar">
              <div class="progress-indicator green" style="width: 100%"></div>
            </div>
          </div>
          <div class="task-footer">
            <div class="task-date">
              <svg class="calendar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2v4"></path>
                <path d="M16 2v4"></path>
                <rect width="18" height="18" x="3" y="4" rx="2"></rect>
                <path d="M3 10h18"></path>
              </svg>
              <span>2024-01-03</span>
            </div>
            <span class="badge completed">已完成</span>
          </div>
          <div class="subtasks">子任务: 1/1</div>
        </div>
      </div>
    </div>
  </div>
</template>