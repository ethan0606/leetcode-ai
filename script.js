// AI工具数据
const aiTools = [
    {
        id: 1,
        name: "文本生成",
        description: "使用AI生成各种类型的文本内容",
        details: "该工具可以生成文章、故事、诗歌等各种文本内容，支持多种语言和风格。通过简单的提示，AI就能生成高质量的文本。"
    },
    {
        id: 2,
        name: "图像生成",
        description: "根据描述生成逼真的图像",
        details: "输入文字描述，AI将生成与之匹配的图像。支持多种风格和场景，可用于设计、创意和艺术创作。"
    },
    {
        id: 3,
        name: "语音识别",
        description: "将语音转换为文本",
        details: "实时将语音输入转换为文本，支持多种语言和口音，适用于会议记录、字幕生成等场景。"
    },
    {
        id: 4,
        name: "机器翻译",
        description: "高质量的多语言翻译",
        details: "支持多种语言之间的互译，提供准确、流畅的翻译结果，适用于文档翻译、跨国交流等场景。"
    },
    {
        id: 5,
        name: "代码生成",
        description: "根据需求生成代码",
        details: "输入功能描述，AI将生成相应的代码。支持多种编程语言，可帮助开发者快速实现功能。"
    },
    {
        id: 6,
        name: "数据分析",
        description: "智能分析数据并生成报告",
        details: "上传数据，AI将进行分析并生成可视化报告，帮助用户快速理解数据趋势和洞察。"
    }
];

// 渲染工具卡片
function renderToolCards() {
    const toolGrid = document.querySelector('.tool-grid');
    toolGrid.innerHTML = '';
    
    aiTools.forEach(tool => {
        const card = document.createElement('div');
        card.className = 'tool-card';
        card.dataset.id = tool.id;
        card.innerHTML = `
            <h3>${tool.name}</h3>
            <p>${tool.description}</p>
        `;
        
        card.addEventListener('click', () => selectTool(tool.id));
        toolGrid.appendChild(card);
    });
}

// 选择工具
function selectTool(toolId) {
    // 移除所有卡片的active类
    document.querySelectorAll('.tool-card').forEach(card => {
        card.classList.remove('active');
    });
    
    // 添加当前卡片的active类
    document.querySelector(`.tool-card[data-id="${toolId}"]`).classList.add('active');
    
    // 显示工具详情
    const tool = aiTools.find(t => t.id === toolId);
    const detailsContent = document.getElementById('tool-details-content');
    detailsContent.innerHTML = `
        <h3>${tool.name}</h3>
        <p>${tool.details}</p>
    `;
}

// 初始化
function init() {
    renderToolCards();
}

// 页面加载完成后初始化
window.addEventListener('DOMContentLoaded', init);