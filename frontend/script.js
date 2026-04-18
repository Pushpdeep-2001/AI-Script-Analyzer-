const API_URL = '/api/analyze';
let currentAnalysis = null;

async function analyzeText() {
    const scriptInput = document.getElementById('script-input');
    const analyzeBtn = document.getElementById('analyze-button');
    const resultsSection = document.getElementById('results-section');
    const errorMsg = document.getElementById('error-message');
    const text = scriptInput.value.trim();

    // Reset UI state
    hideError();
    resultsSection.classList.add('hidden');

    if (!text) {
        showError('Please paste some text to analyze.');
        return;
    }

    // UI state: Loading
    analyzeBtn.classList.add('loading');
    analyzeBtn.disabled = true;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ script: text }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        currentAnalysis = data;

        // Show results section and switch to first tab
        resultsSection.classList.remove('hidden');
        switchTab('summary');
        resultsSection.scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Failed to analyze text. Please ensure the backend is running.');
    } finally {
        analyzeBtn.classList.remove('loading');
        analyzeBtn.disabled = false;
    }
}

function showError(msg) {
    const errorMsg = document.getElementById('error-message');
    errorMsg.textContent = msg;
    errorMsg.classList.remove('hidden');
}

function hideError() {
    const errorMsg = document.getElementById('error-message');
    errorMsg.textContent = '';
    errorMsg.classList.add('hidden');
}

function switchTab(tabId) {
    if (!currentAnalysis) return;

    // Update Tab Buttons
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.tab === tabId);
    });

    // Update Content
    const contentArea = document.getElementById('tab-content');
    contentArea.innerHTML = renderTabContent(tabId);
}

function renderTabContent(tabId) {
    const res = currentAnalysis;

    switch (tabId) {
        case 'summary':
            return `
                <div class="analysis-card">
                    <span class="analysis-label">Summary</span>
                    <p class="analysis-text">${res.summary || 'N/A'}</p>
                </div>
            `;
        case 'emotions':
            return `
                <div class="analysis-card">
                    <span class="analysis-label">Dominant Emotions</span>
                    <div class="tag-container">
                        ${(res.emotions?.dominant_emotions || []).map(e => `<span class="tag">${e}</span>`).join('')}
                    </div>
                    <div style="margin-top: 2rem;">
                        <span class="analysis-label">Emotional Arc</span>
                        <p class="analysis-text">${res.emotions?.emotional_arc || 'N/A'}</p>
                    </div>
                </div>
            `;
        case 'engagement':
            return `
                <div class="analysis-card">
                    <span class="analysis-label">Engagement Score</span>
                    <span class="score-badge">${res.engagement?.score || 0}/10</span>
                    <span class="analysis-label">Key Factors</span>
                    <div class="tag-container">
                        ${(res.engagement?.factors || []).map(f => `<span class="tag">${f}</span>`).join('')}
                    </div>
                </div>
            `;
        case 'cliffhanger':
            return `
                <div class="analysis-card">
                    <span class="analysis-label">Cliffhanger Moment</span>
                    <p class="analysis-text" style="font-weight: 600; margin-bottom: 1.5rem;">${res.cliffhanger?.moment || 'N/A'}</p>
                    <span class="analysis-label">Reasoning</span>
                    <p class="analysis-text">${res.cliffhanger?.reason || 'N/A'}</p>
                </div>
            `;
        case 'improvements':
            return `
                <div class="analysis-card">
                    <span class="analysis-label">Suggested Improvements</span>
                    <div style="margin-top: 1rem;">
                        ${(res.improvements || []).map(imp => `<li class="list-item">${imp}</li>`).join('')}
                    </div>
                </div>
            `;
        default:
            return '';
    }
}

// Global Event Listeners for Tabs
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('tab-btn')) {
        switchTab(e.target.dataset.tab);
    }
});

function clearResults() {
    document.getElementById('script-input').value = '';
    document.getElementById('results-section').classList.add('hidden');
    hideError();
    currentAnalysis = null;
}
